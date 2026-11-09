# AI 产品专用 UI 组件

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="ui-ai-product"></a>

## AI 产品 UI（聊天 / Agent / 可观测性）

做 Chatbot、Copilot、Agent 面板、工具调用可视化时用。

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [affectUI](https://www.affectui.com) | 「给 AI 产品的 Agent-ready React UI」：173 个条目，Agent 可观测性做得很深（检查点、审批闸门、Agent 图、上下文窗口地图、成本与 trace 瀑布、权限页）；每个是零依赖单文件 .tsx | React | `npx shadcn@latest add @affectui/<item>`<br>MCP https://www.affectui.com/api/mcp | 免费+付费 |
| ⭐ [AI Elements（Vercel）](https://elements.ai-sdk.dev) | 基于 shadcn 的 AI 原生组件（消息、工具调用、推理过程…） | React, AI SDK | `npx shadcn@latest add @ai-elements/<item>` | 免费 |
| ⭐ [assistant-ui](https://www.assistant-ui.com) | AI 聊天 React 组件 + runtime：流式、工具、持久化；兼容 AI SDK/LangGraph/Mastra | React | `npx assistant-ui@latest create` | 免费+付费 |
| [A2UI](https://a2ui.org) | Agent 驱动 UI 的流式协议 |  |  | 免费 |
| [AG-UI 协议](https://docs.ag-ui.com) | Agent 后端 ↔ 前端的流式事件协议：让 Python（LangGraph、Pydantic AI、CrewAI…）Agent 把消息、工具调用、状态推给 React 界面。CopilotKit 是它的参考前端 |  |  | 免费 |
| [agentcn](https://www.agentcn.run) | 「生产级 Agent」shadcn registry | React, Tailwind | `npx shadcn@latest add @agentcn/<item>` | 免费 |
| [Arize Phoenix](https://phoenix.arize.com) | 开源 Agent tracing 与评测（基于 OpenTelemetry），本地一条命令起面板 | Python | `pip install arize-phoenix` | 免费+付费 |
| [CopilotKit](https://www.copilotkit.ai) | 应用内 Agent 与生成式 UI 前端栈（AG-UI 协议） | React, Angular | `npx copilotkit@latest create` | 免费+付费 |
| [ElevenLabs UI](https://ui.elevenlabs.io) | 语音/音频 UI 组件 | React, Tailwind | `npx shadcn@latest add @elevenlabs-ui/<item>` | 免费 |
| [json-render](https://json-render.dev) | 限制在你定义的组件内的生成式 UI 框架 |  |  | 免费 |
| [Langfuse](https://langfuse.com) | 开源 LLM 可观测性后端：记录每步调用、工具、token 与成本，可自托管。前端面板（如 affectUI）的数据来源 | Python, TS | `pip install langfuse` | 免费+付费 |
| [LiveKit Agents UI](https://livekit.com/products/agents-ui) | 语音 Agent 界面 shadcn 组件 | React, Tailwind | `npx shadcn@latest add @agents-ui/<item>` | 免费 |
| [MCP-UI](https://mcpui.dev) | 给 MCP 工具返回交互式 UI |  |  | 免费 |
| [prompt-kit](https://www.prompt-kit.com) | AI 界面积木 | React, Tailwind | `npx shadcn@latest add @prompt-kit/<item>` | 免费 |
| [shadcn-chatbot-kit](https://shadcn-chatbot-kit.vercel.app) | 基于 shadcn 的聊天机器人组件 |  |  | 免费 |
| [simple-ai](https://www.simple-ai.dev) | AI 组件与 Agent 示例 | React, Tailwind | `npx shadcn@latest add @simple-ai/<item>` | 免费 |
| [Tambo](https://tambo.co) | AI 选择并流式渲染 React 组件的生成式 UI SDK | React |  | 免费+付费 |
