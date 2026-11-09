# AI 应用 Starter 与 Agent 框架

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="scaffold-ai"></a>

## AI 应用 Starter 与 Agent 框架

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) | 驱动 Claude Code 的 Agent 循环：工具、子 Agent、hooks、MCP | TS, Python | `npm i @anthropic-ai/claude-agent-sdk`<br>`pip install claude-agent-sdk` | 开源 |
| ⭐ [Dify](https://github.com/langgenius/dify) | 可自托管的可视化 LLM 应用 / Agent 工作流 / RAG 构建平台（161k★） |  | `git clone https://github.com/langgenius/dify && cd dify/docker && cp .env.example .env`<br>docker compose up -d（先把 .env 里的 DIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKEN 设成 openssl rand -hex 32 的输出） | 开源 |
| ⭐ [LangGraph](https://langchain-ai.github.io/langgraph/) | 持久化、有状态的图式 Agent，支持人在环中。Python 多 Agent / 复杂控制流首选 | Python, TS | `pip install -U langgraph` | 开源 |
| ⭐ [Mastra](https://mastra.ai/docs) | TS Agent 框架：Agent、workflow、RAG、记忆、评测、本地 playground | TS | `npm create mastra@latest` | 开源 |
| ⭐ [n8n](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-npm) | 工作流自动化，内置 AI Agent 节点（210k★） |  | `npx n8n` | 开源 |
| ⭐ [OpenAI Customer Service Agents Demo](https://github.com/openai/openai-cs-agents-demo) | 多 Agent 客服系统完整示例：Python（Agents SDK）后端做分流与 handoff，Next.js 前端实时显示每步 Agent、工具调用和 guardrail。做客服/分流类多 Agent 直接照它改 | Python, Next.js | `git clone https://github.com/openai/openai-cs-agents-demo` | 开源 |
| ⭐ [Pydantic AI](https://pydantic.dev/docs/ai/overview/) | Pydantic 团队出品的类型安全 Python Agent 框架。Python 单 Agent / 结构化输出首选 | Python | `pip install pydantic-ai` | 开源 |
| ⭐ [Vercel AI SDK](https://ai-sdk.dev) | TS 工具包：流式输出、工具调用、Agent、生成式 UI，跨模型厂商（v7） | TS | `npm i ai` | 开源 |
| ⭐ [Vercel Chatbot](https://github.com/vercel/chatbot) | 完整 Next.js 聊天应用：AI SDK + AI Gateway + Neon + Blob + 认证（原 ai-chatbot） | Next.js | `git clone https://github.com/vercel/chatbot` | 开源 |
| [Agno](https://github.com/agno-agi/agno) | Python 多 Agent 框架与运行时 | Python | `pip install agno` | 开源 |
| [Claude Quickstarts](https://github.com/anthropics/claude-quickstarts) | Anthropic 官方示例应用（客服 Agent 是 Next.js/TS；computer use、浏览器工具有 Python 版） | TS, Python | `git clone https://github.com/anthropics/claude-quickstarts` | 开源 |
| [CrewAI](https://docs.crewai.com) | Python 角色化多 Agent「团队」与 flows | Python | `pip install crewai && crewai create crew my_crew` | 开源 |
| [E2B Fragments](https://github.com/e2b-dev/fragments) | 生成并在沙箱里运行代码的 Next.js 模板（类 v0/Artifacts） | Next.js |  | 开源 |
| [Google ADK](https://github.com/google/adk-python) | 代码优先的 Agent 构建、评测、部署工具包 | Python | `pip install google-adk` | 开源 |
| [LlamaIndex](https://github.com/run-llama/llama_index) | RAG 与文档 Agent（create-llama 脚手架已归档，别用） | Python | `pip install llama-index-core` | 开源 |
| [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) | 轻量多 Agent：handoff（Agent 间转交）、guardrail、内置 tracing、语音。客服分流类场景顺手 | Python, TS | `pip install openai-agents`<br>`npm i @openai/agents` | 开源 |

<a id="scaffold-mcp"></a>

## MCP Server 开发模板

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [FastMCP](https://gofastmcp.com) | 最快的 Python MCP 服务端/客户端写法（v4，已迁到 PrefectHQ） | Python | `pip install fastmcp` | 开源 |
| ⭐ [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) | 官方 MCP SDK（v2）：服务端装 server 包，客户端装 client 包。旧的 @modelcontextprotocol/sdk 是 v1，只做维护 | TS | `npm install @modelcontextprotocol/server`<br>`npm install @modelcontextprotocol/client` | 开源 |
| [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 官方 Python SDK（含 FastMCP 风格 API） | Python | `pip install "mcp[cli]"` | 开源 |
| [MCP 官方参考服务器](https://github.com/modelcontextprotocol/servers) | 官方参考实现，照抄模式 |  |  | 开源 |
