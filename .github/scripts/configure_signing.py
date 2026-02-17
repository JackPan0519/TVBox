#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('app/build.gradle', 'r', encoding='utf-8') as f:
    content = f.read()

# 在 buildTypes.release 中添加 signingConfig
content = content.replace(
    'minifyEnabled true',
    'minifyEnabled true\n            signingConfig signingConfigs.debug'
)

# 添加 signingConfigs 块
signing_config = '''    signingConfigs {
        debug {
            storeFile file(System.getenv("HOME") + "/.android/debug.keystore")
            storePassword "android"
            keyAlias "androiddebugkey"
            keyPassword "android"
        }
    }
'''

content = content.replace(
    'buildTypes {',
    signing_config + 'buildTypes {'
)

with open('app/build.gradle', 'w', encoding='utf-8') as f:
    f.write(content)

print("build.gradle signing configured")
