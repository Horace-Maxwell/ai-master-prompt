# 脚手架、Agent 框架与架构参考

| 文件 | 内容 |
|---|---|
| [01-starters.md](01-starters.md) | 全栈 Web、移动/桌面、后端 API 的 Starter 与创建命令 |
| [02-ai-agents.md](02-ai-agents.md) | AI 应用模板、Agent 框架、MCP Server 开发 SDK |
| [03-architecture.md](03-architecture.md) | 系统设计、架构模式、画图工具（Mermaid / D2 / Excalidraw）、C4、ADR、SRE |
| [04-awesome-lists.md](04-awesome-lists.md) | 巨型 awesome 列表、Prompt 合集、系统提示词合集 |
| [05-services.md](05-services.md) | 认证、数据库与 ORM、支付、邮件、存储、部署、队列、实时、搜索、监控、国际化、国内可用替代；文档站与 CMS |
| [06-ai-infra.md](06-ai-infra.md) | 模型网关、官方 SDK、本地模型、向量库、文档解析、记忆、评测、沙箱、语音、图像视频生成、国内模型平台 |
| [07-common-libs.md](07-common-libs.md) | 状态管理、数据请求、校验、测试、构建工具链、CLI、Python 常用库 |

05–07 每个文件都有上百条，按 `### 小标题` 分组。只想要默认选择就看仓库根目录的 [PICKS.md](../PICKS.md)。

## 快速选型

| 我要做… | 首选 | 命令 |
|---|---|---|
| 一般 React 全栈网站 | Next.js + shadcn | `npx create-next-app@latest` → `npx shadcn@latest init` |
| 纯前端 SPA / 小工具 | Vite | `npm create vite@latest` |
| 内容站 / 博客 / 文档 | Astro（文档用 Starlight） | `npm create astro@latest` |
| 正经 SaaS（认证+支付+后台） | next-forge 或 Open SaaS | `npx next-forge@latest init` / `npm i -g @wasp.sh/wasp-cli && wasp new -t saas` |
| 后台管理 / CRUD | Refine | `npm create refine-app@latest` |
| Vue 全栈 | Nuxt | `npm create nuxt@latest` |
| 移动 App | Expo | `npx create-expo-app@latest` |
| 桌面 App | Tauri（轻）/ Electron（生态大） | `npm create tauri-app@latest` |
| Python API / 全栈 | Full Stack FastAPI Template | `git clone https://github.com/fastapi/full-stack-fastapi-template` |
| 边缘 / 轻量 TS API | Hono | `npm create hono@latest` |
| 企业级 Node API | NestJS | `npx @nestjs/cli new my-api` |
| AI 聊天应用 | Vercel Chatbot 模板（AI SDK） | `git clone https://github.com/vercel/chatbot` |
| TS Agent | Mastra / Claude Agent SDK | `npm create mastra@latest` |
| Python 单 Agent / 结构化输出 | Pydantic AI | `pip install pydantic-ai` |
| Python 多 Agent / 复杂流程 | LangGraph（有状态图、人在环中）；轻量分流用 OpenAI Agents SDK（handoff） | `pip install -U langgraph` / `pip install openai-agents` |
| 多 Agent 客服（带前端面板） | OpenAI Customer Service Agents Demo（Python 后端 + Next.js 面板） | `git clone https://github.com/openai/openai-cs-agents-demo` |
| Python Agent 接 React 前端 | AG-UI 协议（CopilotKit 是参考前端）；面板组件 affectUI / AI Elements | 见 [ui/catalog/07](../ui/catalog/07-ai-product-ui.md) |
| 看每步调用和成本 | Langfuse / Arize Phoenix（数据）+ affectUI（界面） | `pip install langfuse` |
| 无代码 AI 工作流 | Dify / n8n | `npx n8n` |
| MCP Server | FastMCP（Python）/ 官方 TS SDK v2 | `pip install fastmcp` / `npm install @modelcontextprotocol/server` |

## 已失效 / 不推荐（2026-11 核实）

- `create-llama`（2025-07 归档）、`langchain-ai/agent-chat-ui`、`open-agent-platform`（已归档）
- `@modelcontextprotocol/create-server`：源仓库 2024-11 已归档，改用 FastMCP 或官方 SDK
- `mckaywrigley/chatbot-ui`（2024-08 后停更）、`vercel/nextjs-subscription-payments`（已归档）
- create-t3-app 仍可用，但 2025-12 后更新放缓
