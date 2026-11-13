# 动画 / 稀有特效组件库

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="ui-animated"></a>

## 动画与稀有特效组件

落地页、Hero、文字动效、背景特效。多数支持 `npx shadcn add` 一键装入。

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Aceternity UI](https://ui.aceternity.com) | 200+ 酷炫暗色 Hero/落地页特效（Spotlight、Beams、3D Card）+ 区块模板 | React, Tailwind, Motion | `npx shadcn@latest add @aceternity/<item>` | 免费+付费 |
| ⭐ [Animate UI](https://animate-ui.com) | 给 Radix/Base UI/React Aria 加动画的原语：换个 import，shadcn 组件就会动 | React, Motion | `npx shadcn@latest add @animate-ui/<item>`<br>`npm install @animate-ui/react motion && npx @animate-ui/cli@latest animate all`（v2：给现有 shadcn 组件批量加动画） | 免费 |
| ⭐ [Magic UI](https://magicui.design) | 150+ 落地页动画组件与特效（Marquee、Globe、Bento…） | React, Tailwind, Motion | `npx shadcn@latest add @magicui/<item>` | 免费+付费 |
| ⭐ [React Bits](https://reactbits.dev) | 超大创意库：动画文字、背景、组件（1274 条目，51.6k★） | React | `npx shadcn@latest add @react-bits/<Component>-TS-TW`（条目名必须带变体后缀：TS 或 JS + TW 或 CSS，例如 DecryptedText-TS-TW） | 免费+付费 |
| [000h by Cojeev](https://cojeev.com/ui/) | 强调有机形状与有目的动效的表现型 React 组件（React 19 + Tailwind v4，含动画图标，1800+ registry 条目）；想要不那么“模板味”的造型时可取用，项目较新 | React, Tailwind, Motion | `npx shadcn@latest add @000h-cojeev/<item>` | 开源 |
| [Animata](https://animata.design) | 手工打磨的动画 React 组件 |  | llms.txt: https://animata.design/llms.txt | 免费 |
| [Canvas UI](https://canvasui.dev) | React Bits 作者的 html-in-canvas 创意特效库（把真实 DOM 渲染进 WebGL/WebGPU 做液态、粒子、扭曲，支持 React/Vue/Svelte/Solid/原生）；要对实时 HTML 做着色器级特效时选（⚠ MIT + Commons Clause，不可转售库本身） | React, Vue, Svelte, Solid, WebGL, WebGPU | `npx shadcn@latest add @canvas-ui/liquid-react` | 开源 |
| [Cult UI](https://www.cult-ui.com) | 动画 shadcn 组件、区块、完整模板 | React, Tailwind | `npx shadcn@latest add @cult-ui/<item>` | 免费+付费 |
| [Eldora UI](https://www.eldoraui.site) | 动画落地页组件与模板 | React, Tailwind | `npx shadcn@latest add @eldoraui/<item>` | 免费+付费 |
| [Fancy Components](https://www.fancycomponents.dev) | 「有趣又怪」的动画组件 |  | llms.txt: https://www.fancycomponents.dev/llms.txt | 免费 |
| [HextaUI](https://hextaui.com) | shadcn 组件与区块，近期转向 AI 聊天 UI | React, Tailwind | `npx shadcn@latest add @hextaui/<item>` | 免费+付费 |
| [Hover.dev](https://www.hover.dev) | 重交互的动画组件与模板 |  |  | 免费+付费 |
| [Indie UI](https://ui.indie-starter.dev) | React + shadcn + Framer Motion 的落地页动效组件（卡片、Bento、文字动画、按钮）；独立开发者做落地页想要一点差异化时用（2026 年初后更新较少） | React, shadcn, Motion |  | 开源 |
| [Inspira UI](https://inspira-ui.com) | Aceternity/Magic 风格特效的 Vue 移植 | Vue, Nuxt | llms.txt: https://inspira-ui.com/llms.txt | 免费 |
| [Kokonut UI](https://kokonutui.com) | 「一条命令或一句 Prompt」装入的开源组件 | React, Tailwind | `npx shadcn@latest add @kokonutui/<item>` | 免费+付费 |
| [Lightswind UI](https://lightswind.com) | 300+ 动画 React 组件与 500+ 区块（3D、背景、AI 界面等，自带 CLI）；想从一个库里拿大量花哨动效组件时用（基础组件 MIT，Pro 模板一次买断） | React, Tailwind, Motion | `npx lightswind@latest init` | 免费+付费 |
| [Lukacho UI](https://ui.lukacho.com) | Next.js + Tailwind + Framer Motion 的动画组件小集合（落地页与仪表盘用，复制粘贴）；找几个精致的动效卡片/导航参考时用（现成组件免费，定制开发另收费） | React, Next.js, Tailwind, Motion |  | 免费 |
| [Motion Primitives](https://motion-primitives.com) | 开源动画界面原语 | React, Tailwind | `npx shadcn@latest add @motion-primitives/<item>` | 免费+付费 |
| [Rare UI](https://www.rareui.com) | 「稀有」Motion 动画组件（Fluid Orb、Gravity Letters、Liquid Glass、径向滑块），尊重 reduced-motion。⚠ 许可证 MIT + Commons Clause + 必须署名链接；与 rareui.in 不是同一项目 | Next.js, Tailwind, Motion | `npx shadcn@latest add swamimalode07/rare-ui/<component>`（例如 swamimalode07/rare-ui/fluid-orb） | 免费 |
| [RareUI（rareui.in，另一项目）](https://rareui.in) | 100+ 动画组件，自有 CLI | React, Tailwind, Motion | `npx rareui add liquid-metal` | 免费 |
| [Remocn](https://remocn.dev) | 给 Remotion 用的 shadcn 式视频组件（文字动画、背景、转场、应用界面模拟、整段场景，900+ 条目，带 Skill）；让 Agent 生成产品演示视频时用 | React, Remotion | `npx shadcn@latest add @remocn/soft-blur-in`<br>`npx skills add Remocn/remocn --yes` | 开源 |
| [ScrollX UI](https://www.scrollxui.dev) | 开源的滚动与交互动效组件库（shadcn 兼容，180 个 registry 条目）；想给页面加滚动触发类动画时用 | React, shadcn, Tailwind, Motion | `npx shadcn@latest add @scrollxui/<item>` | 开源 |
| [shadcn Motion Blocks](https://componentblocks.com) | 35 个带动效的 shadcn 营销区块（Framer Motion + Lenis，尊重 reduced-motion，单文件复制）；想低价买一套完整动效落地页段落时选（⚠ 付费，€19 一次买断） | React, shadcn, Tailwind, Motion |  | 付费 |
| [Skiper UI](https://skiper-ui.com) | 「不常见」的 shadcn 组件 | React, Tailwind | `npx shadcn@latest add @skiper-ui/<item>` | 免费+付费 |
| [SmoothUI](https://smoothui.dev) | shadcn 动画组件 | React, Tailwind | `npx shadcn@latest add @smoothui/<item>` | 免费 |
| [Sora UI](https://ui.soralabs.studio) | Motion 优先的 shadcn 动画原语与组件（Motion + Tailwind + GSAP，Base UI/Radix 双版本，含动画图标）；想给 shadcn 项目加流畅交互动效时用，项目较新 | React, shadcn, Motion, GSAP | `npx shadcn@latest add @soralabs/<item>` | 开源 |
| [Space UI](https://www.spaceui.one) | 面向人和 AI 的开源交互组件库（原语、交互、区块、模板与创意小工具，1100+ 条目，带 MCP 与 Skills）；想要大量带动效的转化型区块时用（Pro 区块付费） | React, Tailwind, Motion | `npx shadcn@latest add @spaceui/<item>` | 免费+付费 |
| [Svelte Bits](https://sveltebits.xyz) | React Bits 的 Svelte 版动画组件集（文字、背景、交互特效）；Svelte/SvelteKit 项目要同款动效时选 | Svelte, Tailwind | `npx jsrepo add https://sveltebits.xyz/r/aurora.json` | 开源 |
| [SyntaxUI](https://syntaxui.com) | 免费 React/Tailwind/Framer 组件 |  |  | 免费 |
| [UI Layouts](https://www.ui-layouts.com) | 100+ 动画组件与布局 | React, Tailwind | `npx shadcn@latest add @ui-layouts/<item>` | 免费 |
| [UI TripleD](https://ui.tripled.work) | 基于 shadcn/ui + Framer Motion 的开源动效组件与区块（微交互、页面段落，280+ 条目）；需要生产可用的带动效区块时用 | React, shadcn, Motion | `npx shadcn@latest add @uitripled/<item>` | 开源 |
| [uibrik](https://uibrik.com) | 「给 AI Agent 的 UI kit」：279 个动画组件，Agent 通过 MCP 搜索 |  | `claude mcp add --transport http uibrik https://uibrik.com/mcp` | 免费+付费 |
| [unlumen UI](https://ui.unlumen.com) | 注重动效与细节的 React 原语与组件（TypeScript + Tailwind + Motion，230+ 条目）；找 Apple 式精致开关、切换、列表动效时用 | React, Tailwind, Motion | `npx shadcn@latest add @unlumen-ui/<item>` | 开源 |
| [Vue Bits](https://vue-bits.dev) | React Bits 的官方 Vue 移植版（200+ 动画、交互、背景组件，通过 jsrepo 安装）；Vue/Nuxt 项目要 React Bits 同款动效时选 | Vue, Nuxt, Tailwind |  | 开源 |
| [Watermelon UI](https://ui.watermelon.sh) | 组件、区块、仪表盘；免 key 公共 MCP |  | MCP https://mcp.watermelon.sh/mcp | 免费 |
