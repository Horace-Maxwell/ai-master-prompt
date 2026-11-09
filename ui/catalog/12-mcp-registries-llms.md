# UI 相关 MCP / shadcn Registry / llms.txt

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

## UI 相关 MCP 服务器

装上之后 Agent 能直接搜索、安装组件。

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [21st MCP（原 Magic MCP）](https://21st.dev/mcp) | 搜索并获取 21st.dev 上万个组件；AI 生成需付费。旧 Magic API key 已重置 |  | `npx @21st-dev/cli@latest init --client claude` | 免费+付费 |
| ⭐ [Context7](https://context7.com) | 几乎任何库的最新文档（Tailwind、Radix 这类没有 llms.txt/MCP 的库靠它兜底） |  | `claude mcp add context7 -- npx -y @upstash/context7-mcp` | 免费 |
| ⭐ [Figma MCP（官方）](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation) | 读取设计稿上下文、变量、截图、Code Connect，也能写回 Figma |  | `claude mcp add --transport http figma https://mcp.figma.com/mcp` | 免费+付费 |
| ⭐ [Motion AI Kit](https://motion.dev/docs/ai-kit) | Motion 官方 /motion Skill + 文档 MCP（免费）；Motion+ 版加示例和性能诊断 |  | `npx motion-ai` | 免费+付费 |
| ⭐ [shadcn MCP（官方）](https://ui.shadcn.com/docs/mcp) | 在任何已配置的 registry（含 @命名空间）里浏览、搜索、安装组件。装这一个就能接入几百个组件库 |  | `npx shadcn@latest mcp init --client claude` | 免费 |
| [Chakra UI MCP](https://chakra-ui.com/docs/get-started/ai/mcp-server) | Chakra v3 组件、props、示例 |  | `claude mcp add chakra-ui -- npx -y @chakra-ui/react-mcp` | 免费 |
| [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 让 Agent 打开浏览器看自己做出来的 UI、查 console、测性能 |  | `claude mcp add chrome-devtools -- npx chrome-devtools-mcp@latest` | 免费 |
| [daisyUI Blueprint](https://daisyui.com/blueprint/) | 设计方向 + daisyUI 语法 MCP（$22/月或 $600 终身） |  |  | 付费 |
| [Flowbite MCP](https://flowbite.com/docs/getting-started/mcp/) | Figma → Flowbite/Tailwind 组件 |  | `npx -y flowbite-mcp（需 FIGMA_ACCESS_TOKEN）` | 免费 |
| [Framelink Figma MCP（社区）](https://github.com/GLips/Figma-Context-MCP) | 为 Agent 精简过的 Figma 数据 |  | `npx -y figma-developer-mcp --figma-api-key=KEY --stdio` | 免费 |
| [HeroUI MCP](https://www.heroui.com/docs/guide/mcp-server) | HeroUI React v3 与 Native 文档 |  | `claude mcp add heroui-react -- npx -y @heroui/react-mcp@latest` | 免费 |
| [LottieFiles MCP](https://docs.lottiefiles.com/en/platform/mcp) | 搜索和管理 Lottie 动画 |  | `claude mcp add --transport http lottiefiles https://mcp.lottiefiles.com/mcp` | 免费+付费 |
| [Magic UI MCP](https://magicui.design/docs/mcp) | 搜索并安装 Magic UI 组件 |  | `npx @magicuidesign/cli@latest install claude` | 免费 |
| [Mantine MCP](https://mantine.dev/mcp) | Mantine 文档 |  | `claude mcp add mantine -- npx -y @mantine/mcp-server` | 免费 |
| [MUI MCP](https://mui.com/material-ui/getting-started/mcp/) | Material UI 与 MUI X 文档 |  | `claude mcp add mui -- npx -y @mui/mcp` | 免费 |
| [Nuxt UI MCP](https://ui.nuxt.com/docs/getting-started/ai/mcp) | Nuxt UI（Vue）文档 |  |  | 免费 |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | 浏览器自动化，Agent 自测 UI |  | `claude mcp add playwright -- npx @playwright/mcp@latest` | 免费 |
| [pmndrs docs MCP（R3F / drei）](https://docs.pmnd.rs) | React Three Fiber 及 pmndrs 生态文档 |  | `claude mcp add --transport http pmndrs https://docs.pmnd.rs/api/mcp` | 免费 |
| [Storybook MCP](https://storybook.js.org/docs/ai/mcp/overview) | 把你自己项目的组件清单和 stories 暴露给 Agent，可写和测 stories（预览版） |  | `npx storybook add @storybook/addon-mcp` | 免费 |

## shadcn 命名空间 Registry

在 components.json 里配置后可 `npx shadcn add @命名空间/组件名`。见 ui/README.md 的用法说明。

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [registry.directory](https://registry.directory) | 跨 registry 的发现层，约 2.4 万个条目，提供 items.json / openapi.json |  | `npx shadcn add @registrydirectory/<item>` | 免费 |
| ⭐ [shadcn 官方 Registry 索引](https://ui.shadcn.com/docs/directory) | 548 个命名空间，带健康分和条目数；机器可读版 ui.shadcn.com/r/registries.json。已收录的命名空间无需配置即可 npx shadcn add @ns/item |  | `npx shadcn@latest search @<ns> --query "<关键词>"` | 免费 |

## llms.txt（喂给 AI 的官方文档）

让 Agent 读最新官方文档，避免用过时 API。

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [21st.dev llms.txt](https://21st.dev/llms.txt) | 21st.dev 组件目录 |  |  | 免费 |
| [Aceternity UI llms.txt](https://ui.aceternity.com/llms.txt) | 每个组件附带 npx shadcn add @aceternity/... 命令 |  |  | 免费 |
| [Base UI llms.txt](https://base-ui.com/llms.txt) | Radix 没有 llms.txt，Base UI 有 |  |  | 免费 |
| [Chakra UI llms.txt](https://chakra-ui.com/llms.txt) | 另有 components/charts/styling/theming 分卷 |  |  | 免费 |
| [daisyUI llms.txt](https://daisyui.com/llms.txt) | 80KB 完整用法 |  |  | 免费 |
| [GSAP llms.txt](https://gsap.com/llms.txt) | 另有 llms-full.txt |  |  | 免费 |
| [HeroUI llms.txt](https://www.heroui.com/llms.txt) | 另有 llms-full.txt |  |  | 免费 |
| [Lenis llms.txt](https://lenis.dev/llms.txt) | Lenis 平滑滚动文档 |  |  | 免费 |
| [LottieFiles llms.txt](https://lottiefiles.com/llms.txt) | LottieFiles 平台文档 |  |  | 免费 |
| [Magic UI llms.txt](https://magicui.design/llms.txt) | Magic UI 全部组件文档 |  |  | 免费 |
| [Mantine llms.txt](https://mantine.dev/llms.txt) | 另有 llms-full.txt |  |  | 免费 |
| [Motion llms.txt](https://motion.dev/llms.txt) | 另有 llms-full.txt（842KB） |  |  | 免费 |
| [MUI llms.txt](https://mui.com/material-ui/llms.txt) | MUI X 在 mui.com/x/llms.txt |  |  | 免费 |
| [React Bits llms.txt](https://reactbits.dev/llms.txt) | React Bits 全部组件文档 |  |  | 免费 |
| [React Three Fiber llms.txt](https://r3f.docs.pmnd.rs/llms.txt) | R3F 官方文档 |  |  | 免费 |
| [Rive llms.txt](https://rive.app/docs/llms.txt) | 另有 llms-full.txt |  |  | 免费 |
| [shadcn/ui llms.txt](https://ui.shadcn.com/llms.txt) | shadcn 官方文档（AI 版） |  |  | 免费 |
| [Three.js llms.txt](https://threejs.org/docs/llms.txt) | 另有 llms-full.txt |  |  | 免费 |
