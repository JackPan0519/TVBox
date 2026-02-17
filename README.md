<div align="center">
  <img src=".github/assets/logo.png" alt="TVBox" width="180" height="180">

  # TVBox

  基于 [takagen99/Box](https://github.com/takagen99/Box) 的自动化构建版本

[![Release](https://img.shields.io/github/v/release/JackPan0519/TVBox)](https://github.com/JackPan0519/TVBox/releases) [![Actions](https://img.shields.io/github/actions/workflow/status/JackPan0519/TVBox/build-release.yml)](https://github.com/JackPan0519/TVBox/actions) [![License](https://img.shields.io/github/license/JackPan0519/TVBox)](https://github.com/JackPan0519/TVBox/blob/main/LICENSE)
</div>

---

## 什么是 TVBox？

TVBox 是一款开源的安卓端视频播放器，采用 **「壳与源分离」** 设计：

| 组件　　　　　　 | 说明　　　　　　　　　　　　　　　　|
| ------------------| -------------------------------------|
| **壳（播放器）** | 开源免费，仅提供播放功能　　　　　　|
| **源（数据源）** | 网友维护的影视/直播接口（JSON/M3U） |

> TVBox 本身是"空壳播放器"，需要配置数据源才能观看。

#### 主要特性

- 无广告、开源免费
- 支持多种视频解码
- 适配电视遥控操作

---

## 本项目功能

上游仓库 [takagen99/Box](https://github.com/takagen99/Box) 更新时，自动添加修改、构建并发布 APK。

#### 当前修改

| 修改 | 说明 |
|------|------|
| M3U Logo 支持 | 从 `tvg-logo` 字段解析并显示频道 Logo |

---

## 下载安装

前往 [Releases](https://github.com/JackPan0519/TVBox/releases) 下载：

| 文件名 | 架构 |
|--------|------|
| `TVBox_Patch_arm64_*.apk` | ARM64（推荐）|
| `TVBox_Patch_armeabi_*.apk` | ARM32 |

---

## 自动构建

| 触发方式 | 说明 |
|----------|------|
| 定时任务 | 每天自动检查更新 |
| 手动触发 | GitHub Actions 页面运行 |
| 上游发布 | [takagen99/Box](https://github.com/takagen99/Box) 发版时自动触发 |

---

## 常见问题

**Q: 没有频道 Logo？**
> 确认数据源 M3U 包含 `tvg-logo` 字段，Logo URL 可访问。

**Q: 如何更新？**
> 已安装其他版本：下载最新 APK → 卸载旧版 → 安装新版
> 安装了较旧版本：下载最新 APK → 安装新版

---

## 致谢

- [takagen99/Box](https://github.com/takagen99/Box) - 上游项目
- [CatVodTVOfficial/TVBoxOSC](https://github.com/CatVodTVOfficial/TVBoxOSC) - 原始项目
- 所有数据源维护者

---

## 声明

1. 本项目仅供学习交流使用
2. 本软件开源免费，不收取任何费用
3. 影视资源版权归属原作者，切勿侵权