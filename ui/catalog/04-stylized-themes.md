# 风格化主题组件库

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="ui-stylized"></a>

## 风格化主题（手绘 / 复古 / 像素 / 新粗野 / 玻璃）

想要一眼有记忆点的视觉风格时用。

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Looseleaf](https://kevintngo.github.io/looseleaf/) | 「手绘版 shadcn/ui」：123 个可访问组件，纸张纹理 + 钢笔墨线 + 胶带贴纸印章；保留 shadcn 的 props 和 data-slot，直接替换不改 JSX | React, Tailwind v4, Radix | `npx shadcn@latest add https://kevintngo.github.io/looseleaf/r/button.json`<br>或在 components.json 的 registries 里加 @looseleaf 后用 @looseleaf/button（写法见 ui/SKILL.md 第 3 步） | 免费 |
| ⭐ [Neobrutalism components](https://www.neobrutalism.dev) | 新粗野主义 shadcn 组件 | React, Tailwind | `npx shadcn@latest add https://neobrutalism.dev/r/<item>.json`（官方文档写法，例如 button.json）<br>或 `npx shadcn@latest add @neobrutalism/<item>` | 免费 |
| ⭐ [Sketchbook UI](https://sarthakrawat-1.github.io/sketchbook-ui/) | 手绘笔记本风：20 个带抖动 SVG 边框和纸张纹理的组件，零运行时依赖，<70KB | React, TS | `npm i sketchbook-ui` | 免费 |
| [8bitcn](https://www.8bitcn.com) | 8-bit 复古 shadcn 组件、区块、游戏 UI | React, Tailwind | `npx shadcn@latest add @8bitcn/<item>` | 免费 |
| [98.css / XP.css / 7.css](https://jdan.github.io/98.css/) | 还原 Windows 98/XP/7 界面（XP: botoxparty.github.io/XP.css，7: khang-nd.github.io/7.css） | CSS |  | 免费 |
| [augmented-ui](https://augmented-ui.com) | 纯 CSS 赛博朋克切角边框 | CSS |  | 免费 |
| [BoldKit](https://boldkit.dev) | 新粗野主义组件库（43 个组件 + 42 个 SVG 形状，粗边框硬阴影，带 MCP 与自有 CLI）；做大胆撞色的 neubrutalism 界面时选 | React, shadcn, Tailwind | `npx shadcn@latest add @boldkit/button`<br>`npx -y @boldkit/mcp` | 开源 |
| [css.glass](https://css.glass) | 玻璃拟态 CSS 生成器 |  |  | 免费 |
| [DoodleCSS](https://chr15m.github.io/DoodleCSS/) | 手绘风 CSS 主题 | CSS |  | 免费 |
| [Ein UI](https://ui.eindev.ir) | 磨砂玻璃风的 shadcn 组件集（响应式、完整暗色模式）；要 glassmorphism 风格的表单、卡片、导航时选 | React, shadcn, Tailwind | `npx shadcn@latest add @einui/<item>` | 开源 |
| [GameKit UI](https://www.gamekitui.com) | 可直接嵌入的主题化小游戏（贪吃蛇、2048、扫雷） | React, Tailwind | `npx shadcn@latest add @gamekitui/<item>` | 免费 |
| [Glass UI](https://glass-ui.crenspire.com) | Apple 风格的玻璃拟态 shadcn 组件（40+ 个，带模糊、高光等增强视觉效果）；想快速得到毛玻璃质感界面时用 | React, shadcn, Tailwind | `pnpm dlx shadcn@latest add @glass-ui/button` | 免费 |
| [glasscn](https://glasscn-components.vercel.app) | Apple 风「液态玻璃」shadcn 组件 | React, Tailwind | `npx shadcn@latest add @glasscn/<item>` | 免费 |
| [Glassy UI](https://glassyui.com) | 38 个玻璃拟态组件，含 React Native/Expo 版 | React, Tailwind, React Native | `npx shadcn@latest add @glassyui/<item>`<br>`npx shadcn@latest add @glassyui-native/<item>`（React Native 版） | 免费 |
| [liquid-glass-react](https://github.com/rdev/liquid-glass-react) | React 版 Apple Liquid Glass 效果 | React |  | 免费 |
| [neobrutal-ui](https://neobrutal-ui.andongmin.com) | 基于 Base UI 的新粗野主义 React 组件（分段按压反馈、共享主题、可编辑的 Next.js 页面模板）；要 Base UI 底座的 neobrutalism 风格时选，项目很新 | React, Base UI, Tailwind | `npx shadcn@latest add @neobrutal-ui/neobrutal-ui` | 开源 |
| [NeoBrutalism（原 RetroUI）](https://neobrutalism.com) | 复古/粗野风组件、区块、模板、主题（注意与 neobrutalism.dev 区分） | React, Tailwind | `npx shadcn@latest add @retroui/<item>` | 免费+付费 |
| [NES.css](https://nostalgic-css.github.io/NES.css/) | 红白机风 CSS 框架 | CSS |  | 免费 |
| [Pixelact UI](https://www.pixelactui.com) | 像素风 shadcn 组件 | React, Tailwind | `npx shadcn@latest add @pixelact-ui/<item>` | 免费 |
| [React95](https://react95.io) | Windows 95 风 React 组件 | React |  | 免费 |
| [Rough.js](https://roughjs.com) | 手绘风 canvas/SVG 图形库，多数草图 UI 的底层 |  | `npm install roughjs` | 免费 |
| [RoughNotation](https://roughnotation.com) | 手绘动画标注（下划线、圈出、高亮） |  | `npm install rough-notation` | 免费 |
| [termcn](https://termcn.dev) | shadcn-labs 的终端 UI 组件集（基于 Ink 与 OpenTUI，340+ 条目）；用 React 写命令行工具界面时选（注意是终端渲染，不是网页） | React, Ink, OpenTUI | `npx shadcn@latest add @termcn/<item>` | 开源 |
| [Terminal CSS](https://terminalcss.xyz) | 终端风 CSS 框架 | CSS |  | 免费 |
| [The Gridcn](https://thegridcn.com) | 《创：战纪》风格的 shadcn 主题系统（希腊神祇配色、发光强度分级、科幻 HUD 组件）；做赛博/科幻风界面时选 | React, shadcn, Tailwind | `npx shadcn@latest add @thegridcn/radix-vega` | 免费 |
| [tuiparts](https://tuiparts.sh) | OpenTUI 的终端界面原语与 Recipe（Core/React/Solid 三种运行时，用 shadcn CLI 把源码装进项目）；做真正跑在终端里的 TUI 应用时选（注意不是网页组件） | OpenTUI, React, Solid | `pnpm dlx shadcn@4.13.0 add @tuiparts/react/checkbox` | 开源 |
| [WebTUI](https://webtui.ironclad.sh) | 把终端 TUI 美学带进浏览器的模块化 CSS | CSS |  | 免费 |
| [Wired Elements](https://wiredjs.com) | 基于 Rough.js 的草图风 Web Components，任意框架可用 | Web Components | `npm install wired-elements` | 免费 |
