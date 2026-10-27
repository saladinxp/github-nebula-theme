# Nebula for GitHub

GitHub 蓝紫日夜主题：白天使用柔和雾紫，夜晚使用深蓝，搭配细网格、渐变和漂浮几何背景。

**[通过 Stylus 安装](https://raw.githubusercontent.com/saladinxp/github-nebula-theme/main/dist/nebula-github.user.css)** · **[下载完整 ZIP](https://github.com/saladinxp/github-nebula-theme/releases/download/v1.2.1/nebula-github-1.2.1.zip)** · [English](README.md) · [更新日志](CHANGELOG.md) · [Gitea 版](https://github.com/saladinxp/gitea-nebula-theme)

## 下载、安装和更新入口

| 需要做什么 | 入口 / 操作 |
| --- | --- |
| 下载当前完整包（v1.2.1） | **[下载 nebula-github-1.2.1.zip](https://github.com/saladinxp/github-nebula-theme/releases/download/v1.2.1/nebula-github-1.2.1.zip)** |
| 查找后续版本 | [最新发布](https://github.com/saladinxp/github-nebula-theme/releases/latest) · [全部版本](https://github.com/saladinxp/github-nebula-theme/releases) |
| 校验压缩包和单独文件 | [SHA-256 校验清单](https://github.com/saladinxp/github-nebula-theme/releases/download/v1.2.1/release-SHA256SUMS.txt) |
| 首次安装到浏览器 | **[通过 Stylus 安装主题](https://raw.githubusercontent.com/saladinxp/github-nebula-theme/main/dist/nebula-github.user.css)** · [安装步骤](#安装) |
| 更新已安装的主题 | Stylus 管理页 → 检查更新；[详细说明](#更新或移除) |

完整 ZIP 包含安装说明、字体、离线预览、源码和许可证，下载后先解压。发布页自动生成的 **Source code** 是仓库快照；需要整理好的发行包时，请下载上面有版本号的 ZIP。

## 外观

| 浅色 | 深色 |
| --- | --- |
| ![浅色主题](preview/nebula-github-geometry-light.png) | ![深色主题](preview/nebula-github-geometry-dark.png) |

预览使用虚构仓库和独立示例页面。

## 安装

1. 安装 **Stylus**：[Chrome / Edge](https://chromewebstore.google.com/detail/stylus/clngdbkpkpeebahjckkjfobafhncgmne) · [Firefox](https://addons.mozilla.org/firefox/addon/styl-us/)。
2. 打开 **[主题安装文件](https://raw.githubusercontent.com/saladinxp/github-nebula-theme/main/dist/nebula-github.user.css)**，在 Stylus 页面点击 **Install style / 安装样式**。
3. 刷新 GitHub。

在 GitHub **Settings → Appearance** 选择浅色、深色或跟随系统，Nebula 会跟随该选择。

主题只在安装它的浏览器中影响 `https://github.com/`，不会修改仓库文件，也不会改变其他访客看到的页面。

### 配色在哪里切换？

打开 **[GitHub 设置 → 外观](https://github.com/settings/appearance)**，选择 **Light（浅色）**、**Dark（深色）** 或 **Sync with system（跟随系统）**。Nebula 跟随 GitHub 的选择。Stylus 里的选项控制网格、几何背景和动效，GitHub 顶栏不会新增独立的配色按钮。

离线演示顶部的 Light / Dark 按钮是**预览专用控件**。演示使用示例页面结构和内嵌字体，因此顶栏布局、字形可能与实时网站不同。需要相同字体时，可安装下文列出的可选本地字体。

### 更新或移除

通过上面的 Raw 链接安装后，Stylus 可以从固定地址检查更新。如果此前通过本地文件或粘贴 CSS 安装，请打开该链接一次并替换原 Nebula 样式。只保留一份启用的 Nebula。

之后可在 Stylus 管理页使用“检查更新”。手动管理的版本也可替换完整 UserCSS 后保存。关闭或卸载主题时，在 Stylus 中操作该样式即可。

[Stylus 官方安装说明](https://github.com/openstyles/stylus/wiki/Writing-UserCSS#installation)

## 配置

在 Stylus 管理页点击主题旁边的齿轮。

| 选项 | 默认 | 作用 |
| --- | --- | --- |
| 细网格背景 | 开启 | 显示或隐藏背景网格。 |
| 漂浮几何背景 | 开启 | 显示或隐藏方块、三角形和六边形。 |
| 背景与顶栏动效 | 开启 | 播放或暂停几何漂移及顶栏光效。 |

网格和大面积光晕保持静止。两层图形在桌面端分别以 18 秒、22 秒为一轮，窄屏为 32 秒一轮。图形不会拦截点击或改变页面尺寸。系统启用“减少动态效果”时动画停止，打印时隐藏图形。

## 页面适配

- 顶部导航、仓库文件列表、README、首页和搜索使用统一配色。
- 阅读卡片、侧栏保持不透明，背景图形不会穿过文字。
- 保留 GitHub 状态、警告、错误、语法和差异对比的语义颜色。
- 安装的主题只有 CSS，不增加 JavaScript、远程字体或远程图片请求。
- 尊重系统减少动态效果和强制颜色模式。

GitHub 页面结构会更新，不同账号也可能使用不同版本。若某页异常，可在 [Issues](https://github.com/saladinxp/github-nebula-theme/issues) 反馈页面类型、配色模式及浏览器版本。关闭样式即可恢复原始外观。

## 可选字体

主题优先使用本机已安装的 **Sora、Oxanium、JetBrains Mono**，未安装时使用系统字体。可选字体位于 [`fonts/`](fonts/)；Windows 用户可双击三个 `.ttf` 文件安装。中文等字符使用系统字体。

离线预览内嵌 WOFF2 字体，实际安装的 UserCSS 不下载或内嵌字体。

## 更多预览

| 首页 | 搜索 |
| --- | --- |
| ![首页预览](preview/nebula-github-dashboard-light.png) | ![搜索预览](preview/nebula-github-search-light.png) |

下载 HTML 后在本地打开，可以切换日夜配色、网格、几何和动效：

- [仓库预览](preview/nebula-github-preview.html)
- [首页预览](preview/nebula-github-dashboard-preview.html)
- [搜索预览](preview/nebula-github-search-preview.html)

这些是独立示例，不连接真实 GitHub 业务功能。

## 从源码构建

需要 Python 3，无需额外构建依赖：

```sh
python3 build-theme.py
```

生成两种 CSS 和三个离线 HTML 预览，几何 SVG 在构建时内嵌到 CSS。

打包并生成校验文件：

```sh
python3 package-theme.py
```

输出为 `release/nebula-github-1.2.1.zip`。

## 署名与许可

本项目是独立浏览器主题，不是 GitHub 官方产品。Gitea 服务器请使用独立的 [Gitea 版](https://github.com/saladinxp/gitea-nebula-theme)。

见 [LICENSING.md](LICENSING.md)、[NOTICE.txt](NOTICE.txt) 和字体目录中的许可证。字体许可仅适用于相应字体，不代表整个主题采用同一种许可证。

