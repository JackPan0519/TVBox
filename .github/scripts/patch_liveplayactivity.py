#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用M3U Logo替代方案：优先使用M3U中的logo，回退到EPG logo
"""

with open('app/src/main/java/com/github/tvbox/osc/ui/activity/LivePlayActivity.java', 'r', encoding='utf-8') as f:
    content = f.read()

# 替换 getTvLogo 调用，使用 M3U logo 优先级
old_code = '''String[] epgInfo = EpgUtil.getEpgInfo(channelName);
        String epgTagName = channelName;
        getTvLogo(channelName, epgInfo == null ? null : epgInfo[0]);'''

new_code = '''String[] epgInfo = EpgUtil.getEpgInfo(channelName);
        String epgTagName = channelName;
        // 优先使用M3U中的logo，如果没有则使用EPG的logo
        String m3uLogo = TxtSubscribe.getChannelLogo(channelName);
        String logoUrl = (m3uLogo != null && !m3uLogo.isEmpty()) ? m3uLogo : (epgInfo == null ? null : epgInfo[0]);
        getTvLogo(channelName, logoUrl);'''

content = content.replace(old_code, new_code)

with open('app/src/main/java/com/github/tvbox/osc/ui/activity/LivePlayActivity.java', 'w', encoding='utf-8') as f:
    f.write(content)

print("LivePlayActivity.java modified (M3U logo priority)")
