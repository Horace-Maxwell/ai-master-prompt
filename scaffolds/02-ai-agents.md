# AI 应用 Starter 与 Agent 框架

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

## AI 应用 Starter 与 Agent 框架

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Claude Agent SDK](https://docs.claude.com/en/docs/agent-sdk/overview) | 驱动 Claude Code 的 Agent 循环：工具、子 Agent、hooks、MCP | TS, Python | `npm i @anthropic-ai/claude-agent-sdk / pip install claude-agent-sdk` | 开源 |
| ⭐ [Dify](https://dify.ai) | 可自托管的可视化 LLM 应用 / Agent 工作流 / RAG 构建平台（161k★） |  | `cd docker && docker compose up -d` | 开源 |
| ⭐ [Mastra](https://mastra.ai/docs) | TS Agent 框架：Agent、workflow、RAG、记忆、评测、本地 playground | TS | `npm create mastra@latest` | 开源 |
| ⭐ [n8n](https://docs.n8n.io/hosting/installation/npm/) | 工作流自动化，内置 AI Agent 节点（210k★） |  | `npx n8n` | 开源 |
| ⭐ [Vercel AI SDK](https://ai-sdk.dev) | TS 工具包：流式输出、工具调用、Agent、生成式 UI，跨模型厂商（v7） | TS | `npm i ai` | 开源 |
| ⭐ [Vercel Chatbot](https://github.com/vercel/chatbot) | 完整 Next.js 聊天应用：AI SDK + AI Gateway + Neon + Blob + 认证（原 ai-chatbot） | Next.js | `git clone https://github.com/vercel/chatbot` | 开源 |
| [Agno](https://github.com/agno-agi/agno) | Python 多 Agent 框架与运行时 | Python | `pip install agno` | 开源 |
| [Claude Quickstarts](https://github.com/anthropics/claude-quickstarts) | Anthropic 官方示例应用（客服、computer use、自主编码 Agent） |  |  | 开源 |
| [CrewAI](https://docs.crewai.com) | Python 角色化多 Agent「团队」与 flows | Python | `pip install crewai && crewai create crew my_crew` | 开源 |
| [E2B Fragments](https://github.com/e2b-dev/fragments) | 生成并在沙箱里运行代码的 Next.js 模板（类 v0/Artifacts） | Next.js |  | 开源 |
| [Google ADK](https://github.com/google/adk-python) | 代码优先的 Agent 构建、评测、部署工具包 | Python | `pip install google-adk` | 开源 |
| [LangGraph](https://langchain-ai.github.io/langgraph/) | 持久化、有状态的图式 Agent，支持人在环中；复杂控制流选它 | Python, TS | `pip install -U langgraph` | 开源 |
| [LlamaIndex](https://github.com/run-llama/llama_index) | RAG 与文档 Agent（create-llama 脚手架已归档，别用） | Python | `pip install llama-index-core` | 开源 |
| [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) | 轻量多 Agent：handoff、guardrail、tracing、语音 | Python, TS | `pip install openai-agents / npm i @openai/agents` | 开源 |
| [Pydantic AI](https://ai.pydantic.dev) | Pydantic 团队出品的类型安全 Python Agent 框架 | Python | `pip install pydantic-ai` | 开源 |

## MCP Server 开发模板

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [FastMCP](https://gofastmcp.com) | 最快的 Python MCP 服务端/客户端写法（v4，已迁到 PrefectHQ） | Python | `pip install fastmcp` | 开源 |
| ⭐ [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | 官方 MCP 服务端/客户端 SDK | TS | `npm i @modelcontextprotocol/sdk` | 开源 |
| [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 官方 Python SDK（含 FastMCP 风格 API） | Python | `pip install "mcp[cli]"` | 开源 |
| [MCP 官方参考服务器](https://github.com/modelcontextprotocol/servers) | 官方参考实现，照抄模式 |  |  | 开源 |
