#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
M3U Logo提取 - 简化方案
保持原数据结构不变，额外维护 channelName -> logoUrl 映射
"""

import re

# 修改 TxtSubscribe.java - 添加 Logo 相关字段和方法
with open('app/src/main/java/com/github/tvbox/osc/util/live/TxtSubscribe.java', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 添加 LOGO_PATTERN
if 'LOGO_PATTERN' not in content:
    content = content.replace(
        'private static final Pattern GROUP_PATTERN = Pattern.compile("group-title=\\"(.*?)\\"");',
        'private static final Pattern GROUP_PATTERN = Pattern.compile("group-title=\\"(.*?)\\"");\n    private static final Pattern LOGO_PATTERN = Pattern.compile("tvg-logo=\\"(.*?)\\"");'
    )

# 2. 添加 logoMap 静态字段和访问方法
logo_methods = '''
    // M3U Logo 支持: 频道名 -> Logo地址的映射
    private static final LinkedHashMap<String, String> logoMap = new LinkedHashMap<>();

    public static String getChannelLogo(String channelName) {
        return logoMap.get(channelName);
    }

    public static void clearLogoMap() {
        logoMap.clear();
    }
'''

# 在类定义后添加方法
content = content.replace(
    'public static void parse(',
    logo_methods + '\n    public static void parse('
)

# 3. 在 parseM3u 中解析并存储 logo
old_parse_m3u_body = '''if (line.startsWith("#EXTINF")) {
                    String name = getStrByRegex(NAME_PATTERN, line);
                    String group = getStrByRegex(GROUP_PATTERN, line);'''

new_parse_m3u_body = '''if (line.startsWith("#EXTINF")) {
                    String name = getStrByRegex(NAME_PATTERN, line);
                    String group = getStrByRegex(GROUP_PATTERN, line);
                    String logo = getStrByRegex(LOGO_PATTERN, line);
                    if (logo != null && !logo.isEmpty()) {
                        logoMap.put(name, logo);
                    }'''

content = content.replace(old_parse_m3u_body, new_parse_m3u_body)

with open('app/src/main/java/com/github/tvbox/osc/util/live/TxtSubscribe.java', 'w', encoding='utf-8') as f:
    f.write(content)

print("TxtSubscribe.java logo support added (simplified approach)")
