# 基础组件库

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="ui-core"></a>

## 基础 / 无头组件库

做产品的底座：可访问性、表单、弹层、表格。默认首选 shadcn/ui + Radix/Base UI。

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Base UI](https://base-ui.com) | MUI 团队的无头组件，shadcn 新底座选项之一 | React | llms.txt: https://base-ui.com/llms.txt | 免费 |
| ⭐ [shadcn/ui](https://ui.shadcn.com) | 复制进项目的组件（代码归你），AI 生态事实标准；registry + MCP + Skill 齐全 | React, Tailwind | `npx shadcn@latest init`<br>`npx shadcn@latest add <component>` | 免费 |
| [8StarLabs UI](https://ui.8starlabs.com) | 标准库里找不到的小众实用组件（状态指示器、时间线、行程图等），shadcn 方式安装；需要这些特定业务组件时来取 | React, shadcn, Tailwind | `npx shadcn@latest add @8starlabs-ui/<item>` | 开源 |
| [Ark UI / Park UI](https://ark-ui.com) | 跨框架无头组件（React/Vue/Solid/Svelte） |  | llms.txt: https://ark-ui.com/llms.txt | 免费 |
| [Astryx](https://astryx.atmeta.com) | Meta 开源的设计系统（React 19 + StyleX，可访问组件、hooks、页面模板，支持 shadcn CLI 与 Agent），目前 Beta；想用大厂维护、可完全换主题的非 Tailwind 方案时选 | React, StyleX | `npm install @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex`<br>`npx shadcn@latest add @astryx/<item>` | 开源 |
| [basecn](https://basecn.dev) | 把 shadcn/ui 组件改用 Base UI 实现的注册表（API 与样式保持一致）；老 shadcn 项目想从 Radix 换到 Base UI 时对照使用 | React, Base UI, Tailwind | `npx shadcn@latest add @basecn/<item>` | 开源 |
| [Chakra UI](https://chakra-ui.com) | 可组合的 React 组件 v3 | React | `claude mcp add chakra-ui -- npx -y @chakra-ui/react-mcp`<br>llms.txt: https://chakra-ui.com/llms.txt | 免费 |
| [Cnippet UI](https://ui.cnippet.dev) | 基于 Base UI + Tailwind 的可组合组件与区块集（1400+ registry 条目，含图表与动效）；项目选 Base UI 底座、想要大量现成变体时可用，项目较新 | React, Base UI, Tailwind | `npx shadcn@latest add @cnippet/button` | 开源 |
| [coss ui（原 Origin UI）](https://coss.com/ui) | Cal.com 团队，基于 Base UI 的大型应用 UI 集 | React, Tailwind | `npx shadcn@latest add @coss/<item>` | 免费 |
| [daisyUI](https://daisyui.com) | Tailwind 插件式组件类名，框架无关 | Tailwind | llms.txt: https://daisyui.com/llms.txt | 免费 |
| [devl](https://devl.dev) | 建在 coss ui（Base UI + Tailwind）上的 270+ 免费组件、区块与整屏界面，附 llms.txt；用 coss ui 的项目找更上层的应用界面时用 | React, Base UI, Tailwind | `npx shadcn@latest add @devl/<item>` | 开源 |
| [Dice UI](https://www.diceui.com) | 补齐 shadcn 缺口的可访问组件集（看板、数据表格、可排序、标签输入、媒体播放器、取色器等，sadmann7 出品）；shadcn 没有的复杂交互组件先来这里找 | React, shadcn, Tailwind | `npx shadcn@latest add @diceui/kanban` | 开源 |
| [Elements](https://www.tryelements.dev) | 带后端逻辑的全栈 shadcn 组件（Clerk 登录、Polar 定价、上传、AI、品牌 Logo 等一条命令装好）；想把认证/支付这类集成当组件装时选 | Next.js, shadcn, TS | `npx shadcn@latest add @elements/clerk-sign-in` | 开源 |
| [Flowbite](https://flowbite.com) | Tailwind 组件（多框架） |  | `npx -y flowbite-mcp`（需 FIGMA_ACCESS_TOKEN） | 免费+付费 |
| [HeroUI](https://www.heroui.com) | 美观的 React 组件库（原 NextUI），v3 | React, Tailwind | `claude mcp add heroui-react -- npx -y @heroui/react-mcp@latest`<br>llms.txt: https://www.heroui.com/llms.txt | 免费 |
| [Intent UI](https://intentui.com) | 基于 React Aria Components + Tailwind 的复制粘贴组件库（原 Justd，580+ registry 条目）；想要 shadcn 的工作流但底座换成 React Aria 时选 | React, React Aria, Tailwind | `npx shadcn@latest add @intentui/button` | 开源 |
| [Joly UI](https://www.jolyui.dev) | 基于 shadcn/ui 与 Radix 的免费组件集（约 200 个 registry 条目，含动效与表单增强）；想在官方 shadcn 之外多一些现成变体时用 | React, shadcn, Tailwind | `npx shadcn@latest add @jolyui/<item>` | 开源 |
| [Kibo UI](https://www.kibo-ui.com) | shadcn 缺的高级组件（看板、甘特、代码块…） | React, Tailwind | `npx shadcn@latest add @kibo-ui/<item>` | 免费 |
| [Mantine](https://mantine.dev) | 全功能 React 组件 + hooks | React | `claude mcp add mantine -- npx -y @mantine/mcp-server`<br>llms.txt: https://mantine.dev/llms.txt | 免费 |
| [MUI](https://mui.com) | Material Design 组件 + MUI X 数据表格/图表 | React | `claude mcp add mui -- npx -y @mui/mcp`<br>llms.txt: https://mui.com/material-ui/llms.txt | 免费+付费 |
| [MUI Treasury](https://www.mui-treasury.com) | 建在 MUI 之上的手工界面合集（布局、卡片、登录页、聊天等，可用 shadcn CLI 安装）；Material UI 项目想要现成组合界面时用 | React, MUI | `npx shadcn@latest add @mui-treasury/<item>` | 开源 |
| [Nuxt UI](https://ui.nuxt.com) | Vue/Nuxt 官方组件库 | Vue | MCP 配置见 https://ui.nuxt.com/docs/getting-started/ai/mcp | 免费 |
| [Park UI](https://park-ui.com) | 建在 Ark UI + Panda CSS 之上的成品样式组件（React/Solid/Vue，CLI 复制源码）；用 Panda CSS 而非 Tailwind、又想要 shadcn 式体验时选 | React, Vue, Solid, Ark UI, Panda CSS | `npx @park-ui/cli init` | 开源 |
| [Radix UI](https://www.radix-ui.com) | 无样式可访问原语（shadcn 默认底座）；无 llms.txt，用 Context7 | React |  | 免费 |
| [ReUI](https://reui.io) | shadcn 扩展组件，带 MCP 与 Skill | React, Tailwind | `npx shadcn@latest add @reui/<item>` | 免费 |
| [Roi UI](https://www.roiui.com) | 基于 Base UI 的组件与区块，同时提供 CSS Modules 与 Tailwind 两种样式版本；不用 Tailwind 也想走 shadcn registry 流程时选 | React, Base UI, CSS Modules, Tailwind | `npx shadcn@latest add @roiui/<item>` | 开源 |
| [shadcn-svelte](https://www.shadcn-svelte.com) | shadcn 的 Svelte 移植 | Svelte | `npx shadcn-svelte@latest init` | 免费 |
| [shadcn-vue](https://www.shadcn-vue.com) | shadcn 的 Vue 移植 | Vue | `npx shadcn-vue@latest init` | 免费 |
| [shadcn/studio](https://shadcnstudio.com) | 组件、区块、主题生成器 | React, Tailwind | `npx shadcn@latest add @shadcn-studio/<item>` | 免费+付费 |
| [shadcnblocks](https://www.shadcnblocks.com) | 5000+ 页面区块 | React, Tailwind | `npx shadcn@latest add @shadcnblocks/<item>` | 免费+付费 |
| [Spectrum UI](https://ui.spectrumhq.in) | 基于 shadcn/ui 与 Tailwind 的组件与区块集（300+ registry 条目，附 MCP Server）；想要一批风格统一的仪表盘与营销组件时用 | React, shadcn, Tailwind | `npx shadcn@latest add @spectrumui/animated-drawer`<br>`npx -y @spectrumui/mcp` | 开源 |
| [Supabase UI Library](https://supabase.com/library) | Supabase 官方的 shadcn 区块（密码/社交登录、文件上传 Dropzone、实时光标与聊天、当前用户头像等，支持 Next.js/React Router/TanStack/Vue）；后端用 Supabase 时一条命令接好前后端 | React, Vue, shadcn, Supabase | `npx shadcn@latest add https://supabase.com/library/r/password-based-auth-nextjs.json` | 开源 |
| [Tailark](https://tailark.com) | 营销页区块 | React, Tailwind | `npx shadcn@latest add @tailark/<item>` | 免费 |
| [Tremor](https://tremor.so) | 仪表盘与图表组件 | React, Tailwind | `npm install @tremor/react` | 免费 |
| [UIAble](https://uiable.com) | CodedThemes 的 shadcn 设计系统（770+ 组件、720+ 区块、模板与仪表盘，附 MCP）；想要一站式成套 shadcn 资产时用（社区版 MIT，Pro 一次买断） | React, Next.js, shadcn, Tailwind | `npx shadcn@latest add @uiable/<item>` | 免费+付费 |
| [Untitled UI React](https://www.untitledui.com) | 大型商业设计系统的 React 版，带 MCP |  | MCP / llms.txt: https://www.untitledui.com/llms.txt | 免费+付费 |
