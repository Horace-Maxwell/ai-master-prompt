# 图标 / 字体 / 配色 / 主题

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="ui-assets"></a>

## 图标、字体、配色、主题生成

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Fontshare](https://www.fontshare.com) | 免费高质量字体（Clash、General Sans、Satoshi…），比 Inter 更有个性 |  |  | 免费 |
| ⭐ [Iconify](https://iconify.design) | 200+ 图标集、20 万+ 图标；公开免 key API |  | `claude mcp add iconify -- npx -y iconify-mcp-server@latest`（社区） | 免费 |
| ⭐ [Lucide](https://lucide.dev) | shadcn 和多数 AI 工具的默认图标集 |  | llms.txt: https://lucide.dev/llms.txt<br>`npx lucide-mcp`（社区） | 免费 |
| ⭐ [Realtime Colors](https://www.realtimecolors.com) | 在真实页面上预览配色和字体，导出 CSS/Tailwind |  |  | 免费 |
| ⭐ [tweakcn](https://tweakcn.com) | shadcn/Tailwind 可视化主题编辑器，有预设和 AI 主题生成，导出后一行命令装入 |  | `npx shadcn@latest add https://tweakcn.com/r/themes/<preset>.json`（预设主题，例如 amber-minimal） | 免费 |
| [Coolors](https://coolors.co) | 配色生成器 |  |  | 免费+付费 |
| [Fontjoy](https://fontjoy.com) | AI 生成字体搭配 |  |  | 免费 |
| [Fontpair](https://www.fontpair.co) | Google Fonts 搭配 |  |  | 免费 |
| [Google Fonts](https://fonts.google.com) | 字体目录 + Developer API |  | `uvx google-fonts-mcp`（社区） | 免费 |
| [Happy Hues](https://www.happyhues.co) | 在真实页面语境里展示的配色 |  |  | 免费 |
| [Heroicons](https://heroicons.com) | Tailwind 官方图标 |  |  | 免费 |
| [Huemint](https://huemint.com) | AI 生成配色 |  |  | 免费 |
| [lucide-animated](https://lucide-animated.com) | 468 个带动画的 Lucide 图标 | React, Tailwind | `npx shadcn@latest add @lucide-animated/<icon>` | 免费 |
| [Phosphor Icons](https://phosphoricons.com) | 6 种字重的图标家族 |  |  | 免费 |
| [Radix Colors](https://www.radix-ui.com/colors) | 可访问性友好的色阶系统 |  |  | 免费 |
| [Simple Icons](https://simpleicons.org) | 品牌图标 |  |  | 免费 |
| [SVGL](https://svgl.app) | 品牌 Logo SVG，有公开 API | React, Tailwind | `npx shadcn@latest add @svgl/<logo>` | 免费 |
| [Typewolf](https://www.typewolf.com) | 字体搭配与真实用例 |  |  | 免费 |
| [UI Colors](https://uicolors.app) | 生成 Tailwind 50–950 色阶 |  |  | 免费+付费 |
