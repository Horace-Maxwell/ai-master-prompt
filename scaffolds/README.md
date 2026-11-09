# 脚手架、Agent 框架与架构参考

| 文件 | 内容 |
|---|---|
| [01-starters.md](01-starters.md) | 全栈 Web、移动/桌面、后端 API 的 Starter 与创建命令 |
| [02-ai-agents.md](02-ai-agents.md) | AI 应用模板、Agent 框架、MCP Server 开发 SDK |
| [03-architecture.md](03-architecture.md) | 系统设计、架构模式、C4、ADR、SRE |
| [04-awesome-lists.md](04-awesome-lists.md) | 巨型 awesome 列表、Prompt 合集、系统提示词合集 |

## 快速选型

| 我要做… | 首选 | 命令 |
|---|---|---|
| 一般 React 全栈网站 | Next.js + shadcn | `npx create-next-app@latest` → `npx shadcn@latest init` |
| 纯前端 SPA / 小工具 | Vite | `npm create vite@latest` |
| 内容站 / 博客 / 文档 | Astro（文档用 Starlight） | `npm create astro@latest` |
| 正经 SaaS（认证+支付+后台） | next-forge 或 Open SaaS | `npx next-forge@latest init` / `wasp new` |
| 后台管理 / CRUD | Refine | `npm create refine-app@latest` |
| Vue 全栈 | Nuxt | `npm create nuxt@latest` |
| 移动 App | Expo | `npx create-expo-app@latest` |
| 桌面 App | Tauri（轻）/ Electron（生态大） | `npm create tauri-app@latest` |
| Python API / 全栈 | Full Stack FastAPI Template | `git clone https://github.com/fastapi/full-stack-fastapi-template` |
| 边缘 / 轻量 TS API | Hono | `npm create hono@latest` |
| 企业级 Node API | NestJS | `npx @nestjs/cli new my-api` |
| AI 聊天应用 | Vercel Chatbot 模板（AI SDK） | `git clone https://github.com/vercel/chatbot` |
| TS Agent | Mastra / Claude Agent SDK | `npm create mastra@latest` |
| Python Agent | Pydantic AI / LangGraph / OpenAI Agents SDK | `pip install pydantic-ai` |
| 无代码 AI 工作流 | Dify / n8n | `npx n8n` |
| MCP Server | FastMCP（Python）/ 官方 TS SDK | `pip install fastmcp` |

## 已失效 / 不推荐（2026-11 核实）

- `create-llama`（2025-07 归档）、`langchain-ai/agent-chat-ui`、`open-agent-platform`（已归档）
- `@modelcontextprotocol/create-server`：源仓库 2024-11 已归档，改用 FastMCP 或官方 SDK
- `mckaywrigley/chatbot-ui`（2024-08 后停更）、`vercel/nextjs-subscription-payments`（已归档）
- create-t3-app 仍可用，但 2025-12 后更新放缓
