# 基础组件库

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="ui-core"></a>

## 基础 / 无头组件库

做产品的底座：可访问性、表单、弹层、表格。默认首选 shadcn/ui + Radix/Base UI。

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Base UI](https://base-ui.com) | MUI 团队的无头组件，shadcn 新底座选项之一 | React | llms.txt: https://base-ui.com/llms.txt | 免费 |
| ⭐ [shadcn/ui](https://ui.shadcn.com) | 复制进项目的组件（代码归你），AI 生态事实标准；registry + MCP + Skill 齐全 | React, Tailwind | `npx shadcn@latest init`<br>`npx shadcn@latest add <component>` | 免费 |
| [Ark UI / Park UI](https://ark-ui.com) | 跨框架无头组件（React/Vue/Solid/Svelte） |  | llms.txt: https://ark-ui.com/llms.txt | 免费 |
| [Chakra UI](https://chakra-ui.com) | 可组合的 React 组件 v3 | React | `claude mcp add chakra-ui -- npx -y @chakra-ui/react-mcp`<br>llms.txt: https://chakra-ui.com/llms.txt | 免费 |
| [coss ui（原 Origin UI）](https://coss.com/ui) | Cal.com 团队，基于 Base UI 的大型应用 UI 集 | React, Tailwind | `npx shadcn@latest add @coss/<item>` | 免费 |
| [daisyUI](https://daisyui.com) | Tailwind 插件式组件类名，框架无关 | Tailwind | llms.txt: https://daisyui.com/llms.txt | 免费 |
| [Flowbite](https://flowbite.com) | Tailwind 组件（多框架） |  | `npx -y flowbite-mcp`（需 FIGMA_ACCESS_TOKEN） | 免费+付费 |
| [HeroUI](https://www.heroui.com) | 美观的 React 组件库（原 NextUI），v3 | React, Tailwind | `claude mcp add heroui-react -- npx -y @heroui/react-mcp@latest`<br>llms.txt: https://www.heroui.com/llms.txt | 免费 |
| [Kibo UI](https://www.kibo-ui.com) | shadcn 缺的高级组件（看板、甘特、代码块…） | React, Tailwind | `npx shadcn@latest add @kibo-ui/<item>` | 免费 |
| [Mantine](https://mantine.dev) | 全功能 React 组件 + hooks | React | `claude mcp add mantine -- npx -y @mantine/mcp-server`<br>llms.txt: https://mantine.dev/llms.txt | 免费 |
| [MUI](https://mui.com) | Material Design 组件 + MUI X 数据表格/图表 | React | `claude mcp add mui -- npx -y @mui/mcp`<br>llms.txt: https://mui.com/material-ui/llms.txt | 免费+付费 |
| [Nuxt UI](https://ui.nuxt.com) | Vue/Nuxt 官方组件库 | Vue | MCP 配置见 https://ui.nuxt.com/docs/getting-started/ai/mcp | 免费 |
| [Radix UI](https://www.radix-ui.com) | 无样式可访问原语（shadcn 默认底座）；无 llms.txt，用 Context7 | React |  | 免费 |
| [ReUI](https://reui.io) | shadcn 扩展组件，带 MCP 与 Skill | React, Tailwind | `npx shadcn@latest add @reui/<item>` | 免费 |
| [shadcn-svelte](https://www.shadcn-svelte.com) | shadcn 的 Svelte 移植 | Svelte | `npx shadcn-svelte@latest init` | 免费 |
| [shadcn-vue](https://www.shadcn-vue.com) | shadcn 的 Vue 移植 | Vue | `npx shadcn-vue@latest init` | 免费 |
| [shadcn/studio](https://shadcnstudio.com) | 组件、区块、主题生成器 | React, Tailwind | `npx shadcn@latest add @shadcn-studio/<item>` | 免费+付费 |
| [shadcnblocks](https://www.shadcnblocks.com) | 5000+ 页面区块 | React, Tailwind | `npx shadcn@latest add @shadcnblocks/<item>` | 免费+付费 |
| [Tailark](https://tailark.com) | 营销页区块 | React, Tailwind | `npx shadcn@latest add @tailark/<item>` | 免费 |
| [Tremor](https://tremor.so) | 仪表盘与图表组件 | React, Tailwind | `npm install @tremor/react` | 免费 |
| [Untitled UI React](https://www.untitledui.com) | 大型商业设计系统的 React 版，带 MCP |  | MCP / llms.txt: https://www.untitledui.com/llms.txt | 免费+付费 |
