#!/usr/bin/env python3

with open('app/src/main/java/com/github/tvbox/osc/ui/activity/LivePlayActivity.java', 'r', encoding='utf-8') as f:
    content = f.read()

old_code_1 = '''String[] epgInfo = EpgUtil.getEpgInfo(channelName);
        String epgTagName = channelName;
        getTvLogo(channelName, epgInfo == null ? null : epgInfo[0]);
        if (epgInfo != null && !epgInfo[1].isEmpty()) {
            epgTagName = epgInfo[1];
        }'''

new_code_1 = '''String m3uLogo = TxtSubscribe.getChannelLogo(channelName);
        String logoUrl = null;
        String epgTagName = channelName;
        if (m3uLogo != null && !m3uLogo.isEmpty()) {
            logoUrl = m3uLogo;
        } else {
            String[] epgInfo = EpgUtil.getEpgInfo(channelName);
            logoUrl = (epgInfo == null ? null : epgInfo[0]);
            if (epgInfo != null && !epgInfo[1].isEmpty()) {
                epgTagName = epgInfo[1];
            }
        }
        getTvLogo(channelName, logoUrl);'''

content = content.replace(old_code_1, new_code_1)

old_code_2 = '''if (hsEpg.containsKey(savedEpgKey)) {
                String[] epgInfo = EpgUtil.getEpgInfo(channel_Name.getChannelName());
                getTvLogo(channel_Name.getChannelName(), epgInfo == null ? null : epgInfo[0]);'''

new_code_2 = '''if (hsEpg.containsKey(savedEpgKey)) {
                String m3uLogo2 = TxtSubscribe.getChannelLogo(channel_Name.getChannelName());
                String logoUrl2 = null;
                if (m3uLogo2 != null && !m3uLogo2.isEmpty()) {
                    logoUrl2 = m3uLogo2;
                } else {
                    String[] epgInfo = EpgUtil.getEpgInfo(channel_Name.getChannelName());
                    logoUrl2 = (epgInfo == null ? null : epgInfo[0]);
                }
                getTvLogo(channel_Name.getChannelName(), logoUrl2);'''

content = content.replace(old_code_2, new_code_2)

with open('app/src/main/java/com/github/tvbox/osc/ui/activity/LivePlayActivity.java', 'w', encoding='utf-8') as f:
    f.write(content)

print("[002] M3U logo priority done")
