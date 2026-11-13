# AI 基础设施

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="stack-ai"></a>

## AI 基础设施（模型网关 / 向量库 / 评测 / 沙箱 / 语音 / 生成 API）

做 AI 应用时在 Agent 框架之外要选的东西。

本类分组：模型网关与路由 · 官方 SDK · 本地模型 · 向量库与检索 · 文档解析与抓取 · 记忆 · 评测与可观测性 · 结构化输出与护栏 · Agent 沙箱与浏览器 · 语音 · 图像 / 视频 / 音乐生成 · 推理与微调平台 · 国内模型平台

### 模型网关与路由

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [OpenRouter](https://openrouter.ai) | 一个 API Key 调用数百个模型的聚合网关，OpenAI 兼容接口、自动故障转移、按量透传计费；想快速对比和切换各家模型时首选，⚠ 国内访问受限，需国际信用卡或加密货币充值 | OpenAI API | `npm i @openrouter/ai-sdk-provider`<br>llms.txt: https://openrouter.ai/llms.txt | 付费 |
| [Bifrost](https://github.com/maximhq/bifrost) | Maxim 开源的 Go 语言 AI 网关，主打极低开销，带故障转移、负载均衡、语义缓存和 MCP 网关；高并发场景嫌 LiteLLM 慢时选 | Go, Docker | `npx -y @maximhq/bifrost`<br>llms.txt: https://www.getmaxim.ai/bifrost/llms.txt | 开源 |
| [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/) | Cloudflare 边缘上的模型代理：缓存、限流、重试、日志和统一计费，改一行 base URL 即可接入；想零成本给现有调用加缓存和观测时选 | OpenAI API, Workers | llms.txt: https://developers.cloudflare.com/ai-gateway/llms.txt | 免费+付费 |
| [Helicone](https://www.helicone.ai) | 开源的 LLM 可观测平台兼 AI 网关，通过代理一行接入，记录请求、成本、延迟并支持缓存与提示词管理；想最快看到每次调用花了多少钱时选，⚠ 2026 年公司归属有变动（曾并入 Mintlify 后又分离），选型前先确认维护状态 | OpenAI API | `npx @helicone/mcp@latest`<br>llms.txt: https://www.helicone.ai/llms.txt | 免费+付费 |
| [LiteLLM](https://www.litellm.ai) | 开源的 Python SDK + 代理服务器，把 100+ 家模型统一成 OpenAI 格式，带虚拟 Key、预算、限流和日志；要自托管团队内部的模型网关时选 | Python, Docker | `pip install litellm`<br>llms.txt: https://www.litellm.ai/llms.txt | 开源 |
| [New API](https://github.com/QuantumNous/new-api) | 国内社区最活跃的开源大模型网关与额度分发系统（One API 的续作），统一成 OpenAI/Claude/Gemini 格式并管理渠道、令牌和计费；自建国内中转站或团队内部分发 Key 时选，⚠ AGPL 许可 | Go, Docker |  | 开源 |
| [Portkey](https://portkey.ai) | AI 网关 + 可观测 + 护栏 + 提示词管理的一体化平台，网关核心开源；生产环境需要回退、缓存、预算和审计等治理能力时选 | TS, Python | `npm i portkey-ai`<br>llms.txt: https://portkey.ai/llms.txt | 免费+付费 |
| [Requesty](https://www.requesty.ai) | 托管的 LLM 路由网关，带智能路由、回退、缓存和成本分析；想要 OpenRouter 之外带治理功能的托管路由时选 | OpenAI API | llms.txt: https://www.requesty.ai/llms.txt | 付费 |
| [TensorZero](https://www.tensorzero.com) | Rust 写的开源 LLM 基础设施栈：高性能网关、可观测、评测、实验和基于反馈的优化闭环；对延迟敏感、想把线上数据用于持续优化提示词和模型时选 | Rust, Docker | `pip install tensorzero` | 开源 |
| [Vercel AI Gateway](https://vercel.com/ai-gateway) | Vercel 的模型网关：统一接口访问各家模型，零加价、自动重试与故障转移，与 AI SDK 直接打通（模型写成 "provider/model" 字符串即可）；项目用 AI SDK 或部署在 Vercel 时选 | AI SDK, OpenAI API | `npm i @ai-sdk/gateway`<br>llms.txt: https://vercel.com/llms.txt | 付费 |

### 官方 SDK

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Anthropic SDK（Claude API）](https://platform.claude.com/docs) | Claude 官方 TypeScript/Python SDK：Messages API、工具调用、提示词缓存、扩展思考、批处理和文件；直接调用 Claude 模型时用，⚠ 国内无法直接访问 | TS, Python | `npm install @anthropic-ai/sdk`<br>`pip install anthropic`<br>llms.txt: https://platform.claude.com/llms.txt | 付费 |
| [Amazon Bedrock](https://aws.amazon.com/bedrock/) | AWS 上的托管模型服务，在自己的云账号里调用 Claude、Nova、Llama、Mistral 等并提供 AgentCore；企业有数据合规要求、要走 AWS 账单时选 | AWS, TS, Python | `npm i @aws-sdk/client-bedrock-runtime` | 付费 |
| [Azure AI Foundry](https://ai.azure.com) | 微软的企业级模型平台，提供 OpenAI 全系模型及第三方模型的 Azure 托管版本；企业需要 Azure 合规、区域部署和 SLA 时选 | Azure, TS, Python | `pip install azure-ai-projects` | 付费 |
| [Cohere SDK](https://docs.cohere.com) | Cohere 官方 SDK：Command 对话模型、Embed 多语言嵌入和业界常用的 Rerank 重排；做企业检索、需要重排提升 RAG 质量时选 | TS, Python | `npm i cohere-ai`<br>`pip install cohere`<br>llms.txt: https://docs.cohere.com/llms.txt | 免费+付费 |
| [Google Gen AI SDK（Gemini API）](https://ai.google.dev/gemini-api/docs) | Gemini 官方统一 SDK，同一套代码可切换 Gemini Developer API 和 Vertex AI，支持多模态、Live API、图像与视频生成；调用 Gemini/Imagen/Veo 时用，免费额度可观 | TS, Python | `npm install @google/genai`<br>`pip install google-genai`<br>llms.txt: https://ai.google.dev/gemini-api/docs/llms.txt | 免费+付费 |
| [Mistral AI SDK](https://docs.mistral.ai) | Mistral 官方 SDK，覆盖对话、嵌入、OCR、Codestral 代码补全和 Agents API；需要欧洲数据驻留或用其 OCR/代码模型时选 | TS, Python | `npm install @mistralai/mistralai`<br>`pip install mistralai`<br>llms.txt: https://docs.mistral.ai/llms.txt | 免费+付费 |
| [OpenAI SDK](https://developers.openai.com/api/docs) | OpenAI 官方 TypeScript/Python SDK（Responses API、Realtime、图像、语音、嵌入），其接口格式是事实标准，多数国产模型也兼容；调用 GPT 系列或任何 OpenAI 兼容端点时用 | TS, Python | `npm install openai`<br>`pip install openai`<br>`claude mcp add --transport http openaiDeveloperDocs https://developers.openai.com/mcp`<br>llms.txt: https://developers.openai.com/llms.txt | 付费 |
| [xAI API（Grok）](https://docs.x.ai) | Grok 模型的官方 API，OpenAI/Anthropic 兼容，带实时 X 与网页搜索工具；需要实时社交媒体信息或 Grok 模型时选 | OpenAI API | `pip install xai-sdk`<br>llms.txt: https://docs.x.ai/llms.txt | 付费 |

### 本地模型

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Ollama](https://ollama.com) | 最易用的本地模型运行器：一条命令拉取并运行开源模型，提供 OpenAI 兼容接口；本地开发、离线或隐私场景跑 LLM 的默认选择 | CLI, OpenAI API | `curl -fsSL https://ollama.com/install.sh \| sh`<br>`npm i ollama`<br>`pip install ollama`<br>llms.txt: https://ollama.com/llms.txt | 开源 |
| [Jan](https://jan.ai) | 开源的离线 ChatGPT 替代桌面应用，本地跑模型并提供 OpenAI 兼容服务；想要完全开源的本地聊天客户端时选 | Desktop | llms.txt: https://jan.ai/docs/llms.txt | 开源 |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | C/C++ 的 LLM 推理引擎，GGUF 量化格式的源头，CPU/GPU/Apple Silicon 都能跑，自带 llama-server；要最底层、最省资源地在端侧或服务器上嵌入推理时选 | C++ | `brew install llama.cpp` | 开源 |
| [LM Studio](https://lmstudio.ai) | 带图形界面的本地模型桌面应用，可搜索下载 GGUF/MLX 模型并起本地 OpenAI 兼容服务，支持 MCP；想用界面管理本地模型时选 | Desktop, OpenAI API | `npm i @lmstudio/sdk`<br>llms.txt: https://lmstudio.ai/llms.txt | 免费 |
| [LocalAI](https://localai.io) | 开源的本地 OpenAI 替代服务，一个容器同时提供文本、图像、语音、嵌入等接口，可无 GPU 运行；想自托管一套与 OpenAI API 兼容的多模态后端时选 | Go, Docker |  | 开源 |
| [MLX / mlx-lm](https://github.com/ml-explore/mlx-lm) | Apple 的 MLX 机器学习框架及其 LLM 工具包，针对 Apple Silicon 统一内存优化，支持推理和 LoRA 微调；在 Mac 上跑或微调模型时选 | Python, macOS | `pip install mlx-lm` | 开源 |
| [Open WebUI](https://openwebui.com) | 可自托管的 ChatGPT 式界面，对接 Ollama 和任意 OpenAI 兼容接口，带 RAG、用户管理和工具；想给团队搭一个私有聊天前端时选 | Python, Docker | `pip install open-webui`<br>llms.txt: https://openwebui.com/llms.txt | 开源 |
| [SGLang](https://docs.sglang.io) | 高性能开源 LLM/VLM 推理服务框架，RadixAttention 前缀缓存对结构化输出和 Agent 负载友好；大规模自部署、追求极限吞吐时与 vLLM 对比选用 | Python, GPU | `pip install sglang`<br>llms.txt: https://docs.sglang.io/llms.txt | 开源 |
| [Transformers.js](https://huggingface.co/docs/transformers.js) | 在浏览器和 Node.js 里用 ONNX Runtime/WebGPU 直接跑 Hugging Face 模型；要做纯前端推理（嵌入、语音识别、小模型）时选 | JS, WebGPU | `npm i @huggingface/transformers`<br>llms.txt: https://huggingface.co/docs/transformers.js/llms.txt | 开源 |
| [vLLM](https://docs.vllm.ai) | 面向高吞吐的开源 GPU 推理服务引擎（连续批处理、PagedAttention），提供 OpenAI 兼容接口；有自己的 GPU、要把开源模型做成生产级服务时选 | Python, GPU | `pip install vllm` | 开源 |
| [WebLLM](https://webllm.mlc.ai) | 基于 WebGPU 的浏览器内 LLM 推理引擎，OpenAI 兼容接口；想让大模型完全在用户浏览器里运行、不经服务器时选 | JS, WebGPU | `npm i @mlc-ai/web-llm` | 开源 |
| [Xinference](https://inference.readthedocs.io) | 国内团队开源的模型推理平台，一个接口统一部署 LLM、嵌入、重排、语音和图像模型，默认可从 ModelScope 下载；国内私有化部署多类模型时选 | Python, Docker | `pip install xinference` | 开源 |

### 向量库与检索

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [pgvector](https://github.com/pgvector/pgvector) | Postgres 的向量相似度检索扩展（HNSW/IVFFlat），Supabase、Neon 等均内置；已经在用 Postgres 时的默认向量方案，不必再加一个数据库 | Postgres | `npm i pgvector` | 开源 |
| [BGE（FlagEmbedding）](https://github.com/FlagOpen/FlagEmbedding) | 智源研究院开源的 BGE 系列嵌入与重排模型（bge-m3、bge-reranker 等），中文检索的常用基线；需要本地部署中文嵌入模型时选 | Python | `pip install FlagEmbedding` | 开源 |
| [Brave Search API](https://brave.com/search/api/) | 基于 Brave 独立索引的搜索 API，有免费额度和 LLM 上下文专用端点；想要不依赖 Google/Bing 的联网搜索来源时选 | API | `npx -y @brave/brave-search-mcp-server` | 免费+付费 |
| [Chroma](https://www.trychroma.com) | 对开发者最友好的开源向量库，pip 装完即可内嵌运行，另有 Serverless 云版；原型和中小规模 RAG 想最快跑起来时选 | Python, TS | `pip install chromadb`<br>`npm install chromadb`<br>`uvx chroma-mcp`<br>llms.txt: https://www.trychroma.com/llms.txt | 开源 |
| [Cloudflare Vectorize](https://developers.cloudflare.com/vectorize/) | Cloudflare 的全球分布式向量数据库，与 Workers AI 和 AI Search 配套；应用在 Workers 上时最顺手的向量存储 | Workers | llms.txt: https://developers.cloudflare.com/vectorize/llms.txt | 免费+付费 |
| [Exa](https://exa.ai) | 面向 AI 的语义搜索引擎 API，按含义而非关键词找网页并返回正文，支持深度研究端点；Agent 需要高质量的网页与论文检索时选 | API, TS, Python | `npm i exa-js`<br>MCP https://mcp.exa.ai/mcp<br>`npx -y exa-mcp-server`<br>llms.txt: https://exa.ai/llms.txt | 免费+付费 |
| [Haystack](https://haystack.deepset.ai) | deepset 开源的 Python RAG 与 Agent 编排框架，管线以组件显式连接、便于评测和上生产；想要比 LangChain 更工程化的检索管线时选 | Python | `pip install haystack-ai`<br>llms.txt: https://haystack.deepset.ai/llms.txt | 开源 |
| [Jina Embeddings / Reranker](https://jina.ai/embeddings/) | Jina AI 的多语言、多模态嵌入与重排 API，中文效果好，模型开源可自部署；做中英混合语料检索时选 | API |  | 免费+付费 |
| [LanceDB](https://lancedb.com) | 基于 Lance 列式格式的嵌入式多模态向量库，数据直接存在本地磁盘或对象存储；要在应用进程内做检索、或管理图文视频等多模态数据集时选 | Python, TS, Rust | `pip install lancedb`<br>`npm install @lancedb/lancedb`<br>llms.txt: https://lancedb.com/llms.txt | 开源 |
| [LangChain](https://www.langchain.com) | 最大的 LLM 应用集成库：统一的模型、向量库、文档加载器、检索器接口和预置 Agent；需要现成集成快速拼出 RAG 管线时选，复杂控制流用同团队的 LangGraph | Python, TS | `pip install -U langchain`<br>`npm install langchain`<br>`claude mcp add --transport http docs-langchain https://docs.langchain.com/mcp`<br>llms.txt: https://docs.langchain.com/llms.txt | 开源 |
| [LightRAG](https://github.com/HKUDS/LightRAG) | 港大开源的轻量图谱增强 RAG，自动抽取实体关系并做双层检索；想要 GraphRAG 的效果但成本和复杂度更低时选 | Python | `pip install lightrag-hku` | 开源 |
| [Microsoft GraphRAG](https://microsoft.github.io/graphrag/) | 微软开源的图谱式 RAG：用 LLM 构建知识图谱和社区摘要，擅长回答跨文档的全局性问题；语料需要整体归纳而非片段检索时选，⚠ 建索引的 token 成本高 | Python | `pip install graphrag` | 开源 |
| [Milvus](https://milvus.io) | 面向十亿级规模的开源分布式向量数据库（Zilliz 出品），有轻量版 Milvus Lite 和托管的 Zilliz Cloud，国内生态好；数据量巨大或需要国内云托管时选 | Go, C++, Docker | `pip install pymilvus`<br>llms.txt: https://milvus.io/llms.txt | 开源 |
| [Pinecone](https://www.pinecone.io) | 全托管的 Serverless 向量数据库，免运维、支持混合检索、内置嵌入与重排推理；想要省心的托管向量库且数据规模较大时选 | API, TS, Python | `npm i @pinecone-database/pinecone`<br>`npx -y @pinecone-database/mcp`<br>llms.txt: https://www.pinecone.io/llms.txt | 免费+付费 |
| [Qdrant](https://qdrant.tech) | Rust 写的开源向量数据库，过滤能力强、支持量化和混合检索，可自托管也有云版；需要复杂元数据过滤和高性能自托管时选 | Rust, Docker | `npm i @qdrant/js-client-rest`<br>`claude mcp add --transport http qdrant-cloud https://api.cloud.qdrant.io/mcp`<br>llms.txt: https://qdrant.tech/llms.txt | 开源 |
| [RAGFlow](https://ragflow.io) | 国内团队开源的 RAG 引擎，强在深度文档理解（版面分析、表格、扫描件）和带引用的问答，可私有化；企业知识库文档格式复杂时选 | Python, Docker |  | 开源 |
| [Sentence Transformers](https://sbert.net) | 计算文本/图像嵌入与重排的 Python 标准库，可加载 Hugging Face 上万个模型并微调；要在本地跑或训练自己的嵌入模型时选 | Python | `pip install sentence-transformers` | 开源 |
| [sqlite-vec](https://github.com/asg017/sqlite-vec) | 给 SQLite 加向量检索的轻量扩展，纯 C、无依赖，可跑在浏览器 WASM 和移动端；本地优先或端侧应用要做小规模向量搜索时选 | SQLite | `npm install sqlite-vec`<br>`pip install sqlite-vec` | 开源 |
| [Tavily](https://www.tavily.com) | 为 LLM 设计的搜索、抓取、爬取 API，返回已清洗、带引用的结果；给 Agent 加联网搜索能力时的常见选择 | API, TS, Python | `npm i @tavily/core`<br>`claude mcp add tavily --transport http https://mcp.tavily.com/mcp/`<br>llms.txt: https://www.tavily.com/llms.txt | 免费+付费 |
| [turbopuffer](https://turbopuffer.com) | 构建在对象存储上的 Serverless 向量与全文检索引擎，成本低、命名空间近乎无限（Cursor、Notion 在用）；多租户、数据量大且对成本敏感时选，⚠ 有最低月消费 | API, TS, Python | `npm i @turbopuffer/turbopuffer`<br>llms.txt: https://turbopuffer.com/llms.txt | 付费 |
| [Upstash Vector](https://upstash.com/docs/vector/overall/getstarted) | 按请求计费的 Serverless 向量库，走 HTTP、内置嵌入模型和混合检索；Edge/Serverless 应用需要小而省的向量存储时选 | TS, HTTP | `npm i @upstash/vector`<br>llms.txt: https://upstash.com/llms.txt | 免费+付费 |
| [Voyage AI](https://www.voyageai.com) | 专做嵌入与重排模型的服务（已并入 MongoDB），在检索基准上长期领先，有代码、法律、金融等领域模型；RAG 质量卡在检索、想换更强嵌入时选 | API, Python | `pip install voyageai`<br>llms.txt: https://docs.voyageai.com/llms.txt | 免费+付费 |
| [Weaviate](https://weaviate.io) | 开源的 AI 原生向量数据库，内置向量化模块、混合检索、多租户和生成式查询；想让数据库自己负责嵌入和 RAG 管线时选 | Go, Docker | `npm i weaviate-client`<br>MCP https://weaviate-docs.mcp.kapa.ai（文档）<br>llms.txt: https://weaviate.io/llms.txt | 开源 |

### 文档解析与抓取

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Docling](https://docling-project.github.io/docling/) | IBM 开源（现属 LF AI）的文档解析库，把 PDF、DOCX、PPTX、图片等转成保留版面、表格和阅读顺序的 Markdown/JSON，可完全本地运行；RAG 入库前解析文档的开源首选 | Python | `pip install docling`<br>`uvx --from=docling-mcp docling-mcp-server` | 开源 |
| ⭐ [Firecrawl](https://www.firecrawl.dev) | 把任意网站抓取、爬取、搜索并转成干净 Markdown 或结构化数据的 API，处理 JS 渲染和反爬，核心开源；给 LLM 喂网页内容时首选 | API, TS, Python | `npm i @mendable/firecrawl-js`<br>MCP https://mcp.firecrawl.dev/v2/mcp<br>llms.txt: https://www.firecrawl.dev/llms.txt | 免费+付费 |
| [Apify](https://apify.com) | 网页抓取与自动化平台，商店里有上千个现成的抓取器（Actor），可通过 MCP 让 Agent 直接调用；需要现成的社交媒体、电商、地图数据抓取器时选 | API, TS, Python | `npm i apify-client`<br>`npx @apify/actors-mcp-server`<br>MCP https://mcp.apify.com<br>llms.txt: https://apify.com/llms.txt | 免费+付费 |
| [Chonkie](https://docs.chonkie.ai) | 专注文本分块的轻量库，提供 token、句子、语义、代码等多种分块器；想把 RAG 的切块环节单独做好而不引入大框架时选 | Python, TS | `pip install chonkie`<br>llms.txt: https://docs.chonkie.ai/llms.txt | 开源 |
| [Crawl4AI](https://docs.crawl4ai.com) | 开源的 LLM 友好爬虫框架，基于 Playwright 异步抓取并输出干净 Markdown，支持提取策略和深度爬取；想免费自托管网页抓取管线时选 | Python, Playwright | `pip install -U crawl4ai && crawl4ai-setup` | 开源 |
| [Jina Reader](https://jina.ai/reader/) | 在任意网址前加 r.jina.ai/ 即返回适合 LLM 的 Markdown，s.jina.ai 做搜索；无需写代码、临时让 Agent 读网页时最省事 | HTTP API | `claude mcp add -s user --transport http jina https://mcp.jina.ai/v1 --header "Authorization: Bearer ${JINA_API_KEY}"` | 免费+付费 |
| [LlamaParse（LlamaCloud）](https://www.llamaindex.ai/llamaparse) | LlamaIndex 的托管文档解析服务，用视觉模型处理复杂表格、图表和扫描件；对解析精度要求高、接受把文件发到云端时选 | API, Python, TS | llms.txt: https://www.llamaindex.ai/llms.txt | 免费+付费 |
| [Marker](https://github.com/datalab-to/marker) | 把 PDF、图片、Office 文档高质量转成 Markdown/JSON 的开源工具，可选 LLM 增强；本地批量转换书籍和论文时选，⚠ 模型权重商用受限 | Python, GPU | `pip install marker-pdf` | 开源 |
| [MarkItDown](https://github.com/microsoft/markitdown) | 微软开源的轻量工具，把 Office、PDF、图片、音频、HTML 等转成 Markdown，自带 MCP 服务器；只要快速把常见文件变成 LLM 可读文本时选 | Python | `pip install 'markitdown[all]'`<br>`pip install markitdown-mcp` | 开源 |
| [MinerU](https://mineru.net) | 上海 OpenDataLab 开源的高精度 PDF 解析工具，对中文、公式、表格和多栏论文效果突出，输出 Markdown/JSON；解析中文论文、教材和扫描件时首选，⚠ AGPL 许可 | Python, GPU | `pip install mineru`<br>llms.txt: https://mineru.net/llms.txt | 开源 |
| [Mistral OCR](https://docs.mistral.ai/studio/document-processing/basic_ocr) | Mistral 的文档 OCR API，把 PDF 和图片转成保留结构的 Markdown，支持批量和结构化标注；要便宜、快速地云端处理大量扫描文档时选 | API | llms.txt: https://docs.mistral.ai/llms.txt | 付费 |
| [PaddleOCR](https://www.paddleocr.ai) | 百度飞桨开源的 OCR 与文档解析工具集（PP-OCR、PP-Structure、PaddleOCR-VL），中文识别强、可离线部署；中文票据、证件、扫描件识别时选 | Python | `pip install paddleocr` | 开源 |
| [Reducto](https://reducto.ai) | 面向企业的高精度文档解析与抽取 API，擅长复杂表格、图表和手写内容；金融、医疗等对准确率要求极高的文档流程选 | API | `pip install reductoai`<br>llms.txt: https://reducto.ai/llms.txt | 付费 |
| [Unstructured](https://unstructured.io) | 把 PDF、HTML、Office、邮件等几十种格式切成带类型元素的 ETL 工具，有开源库和托管平台；企业数据源杂、需要连接器和统一分块时选 | Python | `pip install unstructured`<br>llms.txt: https://unstructured.io/llms.txt | 免费+付费 |

### 记忆

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Mem0](https://mem0.ai) | 给 AI 应用加长期记忆的开源层：自动从对话中抽取、更新和检索用户事实，有托管平台和自托管版；想让助手跨会话记住用户偏好时首选 | Python, TS | `pip install mem0ai`<br>`npm install mem0ai`<br>MCP https://mcp.mem0.ai/mcp<br>llms.txt: https://mem0.ai/llms.txt | 免费+付费 |
| [Cognee](https://www.cognee.ai) | 开源的 AI 记忆引擎，把原始数据经 ECL 管线变成知识图谱 + 向量的统一记忆；需要可解释、结构化的 Agent 记忆时选 | Python | `pip install cognee`<br>llms.txt: https://www.cognee.ai/llms.txt | 开源 |
| [Graphiti](https://github.com/getzep/graphiti) | Zep 开源的时序知识图谱框架，增量写入、带时间有效性的事实并支持混合检索；想自建图谱式 Agent 记忆时选 | Python, Neo4j | `pip install graphiti-core` | 开源 |
| [LangMem](https://langchain-ai.github.io/langmem/) | LangChain 出的记忆 SDK，为 LangGraph Agent 提供语义、情景和程序性记忆的抽取与管理工具；已经用 LangGraph 时选 | Python, LangGraph | `pip install langmem` | 开源 |
| [Letta](https://www.letta.com) | 原 MemGPT：构建有状态 Agent 的开源平台，Agent 自己编辑分层记忆块并持久化；想要能长期运行、自我管理记忆的 Agent 服务时选 | Python, TS | `pip install letta-client`<br>`npm install @letta-ai/letta-client`<br>llms.txt: https://www.letta.com/llms.txt | 开源 |
| [Supermemory](https://supermemory.ai) | 通用记忆 API：把文档、对话、网页统一存成可检索的用户记忆并提供 MCP；想用一个接口同时解决 RAG 和用户记忆时选 | API, TS | `npm i supermemory`<br>MCP https://mcp.supermemory.ai/mcp<br>llms.txt: https://supermemory.ai/llms.txt | 免费+付费 |
| [Zep](https://www.getzep.com) | 基于时序知识图谱的 Agent 记忆与上下文工程平台，能追踪事实随时间的变化，核心引擎 Graphiti 开源；企业级 Agent 需要融合对话和业务数据的记忆时选 | Python, TS, Go | `pip install zep-cloud`<br>llms.txt: https://www.getzep.com/llms.txt | 免费+付费 |

### 评测与可观测性

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [promptfoo](https://www.promptfoo.dev) | 开源的提示词与模型评测 CLI：用 YAML 声明测试用例和断言，横向对比多模型并支持红队安全测试；想把提示词改动纳入 CI 回归测试时首选 | CLI, YAML | `npx promptfoo@latest init`<br>`npx promptfoo@latest mcp --transport stdio`<br>llms.txt: https://www.promptfoo.dev/llms.txt | 开源 |
| [AgentOps](https://www.agentops.ai) | 面向 Agent 的可观测平台，会话回放、成本追踪并集成主流 Agent 框架；想直观回放多 Agent 执行过程时选 | Python, TS | `pip install agentops`<br>llms.txt: https://docs.agentops.ai/llms.txt | 免费+付费 |
| [Braintrust](https://www.braintrust.dev) | 评测优先的 LLM 工程平台：数据集、实验对比、在线打分、追踪和 Playground；团队要系统化地做评测驱动开发时选 | TS, Python | `npm install braintrust autoevals`<br>MCP https://api.braintrust.dev/mcp<br>llms.txt: https://www.braintrust.dev/llms.txt | 免费+付费 |
| [DeepEval](https://deepeval.com) | pytest 风格的开源 LLM 评测框架，内置 RAG、Agent、对话等数十种指标；Python 项目想像写单元测试一样写 LLM 测试时选 | Python | `pip install deepeval`<br>llms.txt: https://deepeval.com/llms.txt | 开源 |
| [Evalite](https://www.evalite.dev) | 基于 Vitest 的 TypeScript LLM 评测工具，本地运行并带 Web UI；TS 项目想用熟悉的测试写法做评测时选 | TS, Vitest | `npm i evalite` | 开源 |
| [Inspect AI](https://inspect.aisi.org.uk) | 英国 AI 安全研究所开源的评测框架，数据集、求解器、打分器可组合，支持沙箱里的 Agent 评测；做严肃的模型能力或安全评测时选 | Python | `pip install inspect-ai`<br>llms.txt: https://inspect.aisi.org.uk/llms.txt | 开源 |
| [Laminar](https://laminar.sh) | 开源的 Agent 可观测平台（Rust 后端），擅长长时间运行 Agent 和浏览器 Agent 的追踪与回放；调试 Browser Use/Stagehand 类 Agent 时选 | TS, Python | `pip install lmnr`<br>llms.txt: https://laminar.sh/docs/llms.txt | 开源 |
| [LangSmith](https://www.langchain.com/langsmith) | LangChain 的可观测与评测平台：追踪、数据集、评测、提示词管理和部署，不用 LangChain 也能接；技术栈在 LangChain/LangGraph 上时最顺 | Python, TS | `pip install -U langsmith`<br>`npm install langsmith`<br>MCP https://api.smith.langchain.com/mcp<br>llms.txt: https://docs.langchain.com/llms.txt | 免费+付费 |
| [MLflow](https://mlflow.org) | 开源的 ML/GenAI 生命周期平台：实验跟踪、模型注册、LLM 追踪和评测；团队同时做传统机器学习和 LLM 应用时选 | Python | `pip install mlflow`<br>llms.txt: https://mlflow.org/llms.txt | 开源 |
| [OpenLLMetry（Traceloop）](https://www.traceloop.com/openllmetry) | 基于 OpenTelemetry 的开源 LLM 埋点库，自动为各家模型、向量库和框架生成标准 span；想把 LLM 追踪发到已有的可观测后端时选 | Python, TS, OTel | `pip install traceloop-sdk`<br>`npm install @traceloop/node-server-sdk`<br>llms.txt: https://www.traceloop.com/docs/llms.txt | 开源 |
| [Opik（Comet）](https://www.comet.com/site/products/opik/) | Comet 开源的 LLM 追踪、评测与提示词优化平台，可完全自托管；想要开源且带自动提示词优化的评测平台时选 | Python, TS | `pip install opik`<br>`uvx opik mcp configure` | 开源 |
| [Pydantic Logfire](https://pydantic.dev/logfire) | Pydantic 团队基于 OpenTelemetry 的可观测平台，对 Python、Pydantic AI 和 LLM 调用开箱即用，可用 SQL 查询；Python 后端想把应用与 LLM 追踪放一起看时选 | Python, OTel | `pip install logfire`<br>`claude mcp add --transport http logfire https://logfire-us.pydantic.dev/mcp`<br>llms.txt: https://pydantic.dev/logfire/llms.txt | 免费+付费 |
| [Ragas](https://docs.ragas.io) | 专注 RAG 与 Agent 评测的开源库（忠实度、上下文精确率/召回率等指标），可生成合成测试集；要量化检索和生成质量时选 | Python | `pip install ragas`<br>llms.txt: https://docs.ragas.io/llms.txt | 开源 |
| [W&B Weave](https://wandb.ai/site/weave) | Weights & Biases 的 LLM 应用追踪与评测工具，一个装饰器记录调用树；团队已用 W&B 管实验时选 | Python, TS | `pip install weave`<br>llms.txt: https://docs.wandb.ai/llms.txt | 免费+付费 |

### 结构化输出与护栏

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Instructor](https://python.useinstructor.com) | 最流行的结构化输出库：用 Pydantic 模型定义期望结果，自动校验并重试，支持十多家模型；Python 里从 LLM 拿可靠 JSON 的默认做法 | Python | `pip install instructor`<br>llms.txt: https://python.useinstructor.com/llms.txt | 开源 |
| [BAML](https://boundaryml.com) | 把提示词写成带类型函数的领域语言，编译出 Python/TS/Ruby 等类型安全客户端，容错解析对不支持工具调用的模型也有效；提示词多、想像管理代码一样管理并测试它们时选 | Python, TS | `pip install baml-py`<br>`npm install @boundaryml/baml`<br>llms.txt: https://docs.boundaryml.com/llms.txt | 开源 |
| [DSPy](https://dspy.ai) | 用声明式签名和模块编写 LLM 程序，再由优化器根据指标自动调提示词和示例；想用数据而不是手工反复改 prompt 来提升效果时选 | Python | `pip install dspy` | 开源 |
| [Guardrails AI](https://www.guardrailsai.com) | 开源的 LLM 输入输出校验框架，Hub 里有敏感信息、毒性、幻觉等现成校验器；要给模型输出加可组合的合规检查时选 | Python | `pip install guardrails-ai` | 开源 |
| [jsonrepair](https://github.com/josdejong/jsonrepair) | 修复 LLM 输出里不合法 JSON（缺引号、多逗号、被截断）的小库；模型不支持严格结构化输出、需要兜底解析时用 | TS | `npm i jsonrepair` | 开源 |
| [Lakera Guard](https://www.lakera.ai) | 托管的 LLM 安全防护 API（现属 Check Point），实时检测提示注入、越狱和数据泄露；面向公众的 AI 产品需要一层低延迟安全网关时选 | API | llms.txt: https://docs.lakera.ai/llms.txt | 免费+付费 |
| [LLM Guard](https://protectai.github.io/llm-guard/) | Protect AI 开源的输入输出扫描器集合（提示注入、PII 脱敏、毒性、密钥泄露），可本地运行；想自托管一层 LLM 安全过滤时选 | Python | `pip install llm-guard` | 开源 |
| [Mirascope](https://mirascope.com) | 轻量的 Python LLM 工具包，用装饰器把函数变成带类型的模型调用，统一各家接口并支持结构化输出；想要比 LangChain 更贴近原生 Python 的抽象时选 | Python | `pip install mirascope`<br>llms.txt: https://mirascope.com/llms.txt | 开源 |
| [NeMo Guardrails](https://docs.nvidia.com/nemo/guardrails/) | NVIDIA 开源的可编程对话护栏工具包，用 Colang 定义话题边界、越狱防护和事实核查流程；对话机器人需要严格控制可聊范围时选 | Python | `pip install nemoguardrails`<br>llms.txt: https://docs.nvidia.com/nemo/guardrails/llms.txt | 开源 |
| [Outlines](https://dottxt-ai.github.io/outlines/) | 在解码阶段约束生成的结构化输出库，保证结果符合 JSON Schema、正则或语法；用本地/开源模型且必须百分之百合规格时选 | Python | `pip install outlines` | 开源 |

### Agent 沙箱与浏览器

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [E2B](https://e2b.dev) | 给 AI Agent 用的云端安全沙箱（Firecracker 微虚拟机），毫秒级启动，可运行代码、终端和桌面环境，SDK 开源；要执行模型生成的代码时首选 | TS, Python | `npm i e2b`<br>`pip install e2b`<br>llms.txt: https://e2b.dev/llms.txt | 免费+付费 |
| [Arcade](https://www.arcade.dev) | Agent 工具调用的授权与运行平台，让 Agent 以用户身份安全调用需要 OAuth 的工具，并可作为 MCP 运行时；多用户 Agent 产品要解决「替谁授权」问题时选 | Python, TS | `pip install arcadepy`<br>llms.txt: https://www.arcade.dev/llms.txt | 免费+付费 |
| [Blaxel](https://blaxel.ai) | 为 Agent 设计的计算平台，沙箱可在数十毫秒内从待机恢复并长期保留状态；需要大量常驻但多数时间空闲的 Agent 环境时选 | TS, Python | `npm i @blaxel/core`<br>llms.txt: https://blaxel.ai/llms.txt | 免费+付费 |
| [Browser Use](https://browser-use.com) | 最流行的开源浏览器 Agent 库，让 LLM 自主操作网页完成任务，另有托管云；想用 Python 快速做出能自己上网办事的 Agent 时选 | Python | `pip install browser-use`<br>`claude mcp add browser-use -- uvx --from 'browser-use[cli]' browser-use --mcp`<br>llms.txt: https://browser-use.com/llms.txt | 开源 |
| [Browserbase](https://www.browserbase.com) | 给 Agent 用的云端无头浏览器平台，带会话录像、验证码处理、代理和持久上下文，兼容 Playwright/Puppeteer；要在生产环境大规模跑浏览器自动化时选 | Playwright, TS, Python | `npm i @browserbasehq/sdk`<br>`claude mcp add --transport http browserbase "https://mcp.browserbase.com/mcp?browserbaseApiKey=YOUR_BROWSERBASE_API_KEY"`<br>llms.txt: https://www.browserbase.com/llms.txt | 免费+付费 |
| [Cloudflare Sandbox SDK](https://developers.cloudflare.com/sandbox/) | 在 Cloudflare 容器里运行不可信代码的 SDK，可执行命令、管理文件并暴露服务；Agent 跑在 Workers 上、需要就近的代码执行环境时选 | Workers, TS | `npm i @cloudflare/sandbox`<br>llms.txt: https://developers.cloudflare.com/sandbox/llms.txt | 付费 |
| [Composio](https://composio.dev) | 给 Agent 接入数百个第三方应用（GitHub、Gmail、Slack 等）的工具平台，托管 OAuth 授权并可按需暴露成 MCP；Agent 要代表用户操作外部 SaaS 时选 | TS, Python | `npm i @composio/core`<br>MCP https://connect.composio.dev/mcp<br>llms.txt: https://composio.dev/llms.txt | 免费+付费 |
| [Daytona](https://www.daytona.io) | 面向 AI 生成代码的开源沙箱基础设施，启动快、沙箱有状态且可长期保留，带文件、Git 和 LSP 接口；Agent 需要长生命周期开发环境时选 | TS, Python | `npm install @daytonaio/sdk`<br>`pip install daytona`<br>daytona mcp init claude<br>llms.txt: https://www.daytona.io/llms.txt | 免费+付费 |
| [Hyperbrowser](https://www.hyperbrowser.ai) | 面向 Agent 的云浏览器基础设施，内置抓取、爬取、结构化抽取和多家 computer-use Agent 接口；想在一个 API 里同时拿到浏览器会话和抓取能力时选 | TS, Python | `npm i @hyperbrowser/sdk`<br>`npx hyperbrowser-mcp`<br>llms.txt: https://www.hyperbrowser.ai/llms.txt | 免费+付费 |
| [Modal](https://modal.com) | 用 Python 代码定义的 Serverless 计算平台，秒级冷启动的 GPU 容器、批任务和沙箱；要跑模型推理、微调或大规模并行任务又不想管基础设施时选 | Python | `pip install modal`<br>llms.txt: https://modal.com/llms.txt | 免费+付费 |
| [Skyvern](https://www.skyvern.com) | 用视觉模型 + LLM 自动化浏览器工作流的开源工具，不依赖固定选择器；要批量自动填表、下载发票这类跨站点流程时选 | Python | `pip install skyvern`<br>llms.txt: https://www.skyvern.com/llms.txt | 开源 |
| [Smithery](https://smithery.ai) | MCP 服务器的注册表与托管平台，可搜索、一键安装并托管远程 MCP；找现成 MCP 或发布自己的 MCP 服务器时用 | MCP | `npx -y @smithery/cli@latest` | 免费+付费 |
| [Stagehand](https://www.stagehand.dev) | Browserbase 开源的 AI 浏览器自动化框架，提供 act、extract、observe、agent 四个原语，把自然语言和确定性代码混用；想写可维护、可复现的网页自动化时选 | TS, Python | `npm i @browserbasehq/stagehand`<br>llms.txt: https://www.stagehand.dev/llms.txt | 开源 |
| [Steel](https://steel.dev) | 开源的浏览器 API，为 Agent 提供可自托管的云浏览器会话，处理代理、指纹和验证码；想要开源可自建的 Browserbase 替代时选 | TS, Python | `npm i steel-sdk`<br>llms.txt: https://steel.dev/llms.txt | 免费+付费 |
| [Vercel Sandbox](https://vercel.com/docs/vercel-sandbox) | Vercel 的临时微虚拟机沙箱，用来安全运行不可信或 AI 生成的代码；Agent 后端已在 Vercel 上时选 | TS, Python | `npm i @vercel/sandbox`<br>llms.txt: https://vercel.com/llms.txt | 免费+付费 |

### 语音

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [LiveKit Agents](https://docs.livekit.io/agents/) | 开源的实时语音/视频 Agent 框架，基于 WebRTC，把语音识别、LLM、语音合成和打断处理串成低延迟管线，可接电话；做生产级实时语音助手时首选 | Python, TS, WebRTC | `pip install livekit-agents`<br>`claude mcp add --transport http livekit-docs https://docs.livekit.io/mcp`<br>llms.txt: https://docs.livekit.io/agents/llms.txt | 开源 |
| [AssemblyAI](https://www.assemblyai.com) | 语音转写与音频理解 API，支持说话人分离、流式识别和基于转写的 LLM 分析；做会议纪要、通话质检这类音频分析时选 | API, TS, Python | `npm i assemblyai`<br>`claude mcp add assemblyai-docs --transport http https://assemblyai.com/docs/mcp`<br>llms.txt: https://www.assemblyai.com/llms.txt | 免费+付费 |
| [Cartesia](https://cartesia.ai) | 超低延迟的语音合成（Sonic）与识别（Ink）API，首包延迟极低；实时语音 Agent 的合成环节对延迟敏感时选 | API, TS, Python | `npm i @cartesia/cartesia-js`<br>`claude mcp add --transport http --scope user cartesia https://mcp.cartesia.ai/mcp`<br>llms.txt: https://cartesia.ai/llms.txt | 免费+付费 |
| [CosyVoice](https://github.com/QwenAudio/CosyVoice) | 阿里通义实验室开源的多语言语音合成大模型，支持零样本音色克隆、方言和情感控制；需要可本地部署的高质量中文 TTS 时选 | Python, GPU |  | 开源 |
| [Deepgram](https://deepgram.com) | 低延迟的语音识别与合成 API（Nova、Flux、Aura），流式转写速度快，另有语音 Agent API；实时字幕或语音 Agent 的识别环节选 | API, TS, Python | `npm i @deepgram/sdk`<br>dg mcp（需先装 Deepgram CLI）<br>llms.txt: https://deepgram.com/llms.txt | 免费+付费 |
| [ElevenLabs](https://elevenlabs.io) | 音质领先的语音 AI 平台：文本转语音、语音克隆、转写（Scribe）、配音、音效、音乐和对话式 Agent；需要最自然的配音或多语言语音时选 | API, TS, Python | `npm install @elevenlabs/elevenlabs-js`<br>`pip install elevenlabs`<br>MCP https://api.elevenlabs.io/v1/mcp<br>llms.txt: https://elevenlabs.io/llms.txt | 免费+付费 |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | 基于 CTranslate2 重新实现的 Whisper，速度快数倍且更省显存；自部署批量转写时替代原版 Whisper | Python | `pip install faster-whisper` | 开源 |
| [Fish Audio](https://fish.audio) | 语音合成与音色克隆平台，中英日等多语言效果好，开源模型 Fish Speech/OpenAudio 可自部署；需要中文效果好且比 ElevenLabs 便宜的 TTS 时选 | API, Python | `pip install fish-audio-sdk`<br>llms.txt: https://docs.fish.audio/llms.txt | 免费+付费 |
| [FunASR](https://github.com/modelscope/FunASR) | 阿里达摩院开源的语音识别工具包（Paraformer、SenseVoice 等），中文和方言识别强，支持流式与热词；中文语音转写需要本地部署时首选 | Python | `pip install funasr` | 开源 |
| [Hume AI](https://www.hume.ai) | 带情感理解的语音接口（EVI）与表现力强的语音合成（Octave）；希望语音助手能感知并表达情绪时选 | API, TS, Python | `npm i hume`<br>llms.txt: https://www.hume.ai/docs/llms.txt | 免费+付费 |
| [Kokoro](https://github.com/hexgrad/kokoro) | 仅 8200 万参数的开源语音合成模型，Apache 许可，CPU 上也能实时生成；要免费、可本地部署的 TTS 时选 | Python | `pip install kokoro` | 开源 |
| [OpenAI Realtime API](https://developers.openai.com/api/docs/guides/realtime) | OpenAI 的语音到语音实时接口（WebRTC/WebSocket/SIP），单模型完成听、想、说并支持工具调用；想用最少组件做自然打断的语音对话时选 | WebRTC, TS, Python | llms.txt: https://developers.openai.com/llms.txt | 付费 |
| [Pipecat](https://www.pipecat.ai) | Daily 开源的 Python 实时语音与多模态对话框架，按帧管线组合各家识别、模型和合成服务，传输层可换；想自由拼装语音 Agent 且不绑定某家平台时选 | Python | `pip install pipecat-ai`<br>llms.txt: https://docs.pipecat.ai/llms.txt | 开源 |
| [Retell AI](https://www.retellai.com) | 电话语音 Agent 平台，延迟低、对话流可视化配置，带批量外呼和通话分析；呼叫中心类场景与 Vapi 对比选用 | API | `npm i retell-sdk`<br>llms.txt: https://www.retellai.com/llms.txt | 付费 |
| [Vapi](https://vapi.ai) | 面向开发者的语音 Agent 托管平台，电话号码、打断、工具调用和各家模型编排开箱即用；想几小时内上线电话客服或外呼机器人时选 | API, TS, Python | `npm i @vapi-ai/web`<br>`npx -y @vapi-ai/mcp-server`<br>llms.txt: https://vapi.ai/llms.txt | 付费 |
| [Whisper](https://github.com/openai/whisper) | OpenAI 开源的多语言语音识别模型，可本地运行；离线转写音视频、生成字幕的基础模型，生产环境常用下方更快的实现 | Python | `pip install openai-whisper` | 开源 |
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | Whisper 的 C/C++ 移植，无依赖，可在 CPU、Apple Silicon 和移动端高效运行；要把语音识别嵌入桌面或移动应用时选 | C++ | `brew install whisper-cpp` | 开源 |

### 图像 / 视频 / 音乐生成

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [fal](https://fal.ai) | 生成式媒体推理平台，一个 API 调用数百个图像、视频、语音、3D 模型（FLUX、Kling、Veo、Seedance 等），速度快、按量计费；应用里要接图像或视频生成时首选 | API, TS, Python | `npm install --save @fal-ai/client`<br>`pip install fal-client`<br>`claude mcp add --transport http --scope user fal https://mcp.fal.ai/mcp-relay`<br>llms.txt: https://fal.ai/llms.txt | 付费 |
| [Black Forest Labs（FLUX）](https://bfl.ai) | FLUX 系列图像模型的原厂 API，文生图、参考图编辑（Kontext）与多图融合质量领先；需要最好的写实图像或图像编辑时选，开源权重版 ⚠ 非商用许可 | API | `claude mcp add --transport http FLUX https://mcp.bfl.ai`<br>llms.txt: https://bfl.ai/llms.txt | 付费 |
| [ComfyUI](https://www.comfy.org) | 节点式的开源生成工作流引擎，图像、视频、3D、音频模型通吃，社区节点和工作流最丰富，可导出为 API；要本地跑或精细控制生成流程时选 | Python, GPU | `pip install comfy-cli && comfy install`<br>llms.txt: https://www.comfy.org/llms.txt | 开源 |
| [Diffusers](https://huggingface.co/docs/diffusers) | Hugging Face 的扩散模型 Python 库，统一加载和运行图像、视频、音频生成模型并支持 LoRA 训练；要在自己的 GPU 上用代码跑或微调生成模型时选 | Python, PyTorch | `pip install diffusers`<br>llms.txt: https://huggingface.co/docs/diffusers/llms.txt | 开源 |
| [Gemini API：Veo / Imagen / Nano Banana](https://ai.google.dev/gemini-api/docs/video) | 通过 Gemini API 调用 Veo（带原生音频的视频）、Imagen 和 Gemini 图像模型（对话式改图）；已经在用 Gemini、想同一套 SDK 做图像和视频时选 | API, TS, Python | `npm i @google/genai` | 付费 |
| [HeyGen API](https://developers.heygen.com) | 数字人视频生成 API：用头像和脚本批量生成口播视频，支持视频翻译和实时互动头像；做营销口播、课程或多语言本地化视频时选 | API | MCP https://mcp.heygen.com/mcp/v1/<br>llms.txt: https://developers.heygen.com/llms.txt | 付费 |
| [Ideogram API](https://developer.ideogram.ai) | 擅长在图中准确生成文字和平面设计风格的图像模型 API；做海报、Logo、带标题的封面图时选 | API | llms.txt: https://developer.ideogram.ai/llms.txt | 付费 |
| [Luma Dream Machine API](https://lumalabs.ai/api) | Luma 的 Ray 系列视频与 Photon 图像模型 API，运镜自然、支持关键帧和循环；做电影感短片段时选 | API, TS, Python | `npm i lumaai`<br>llms.txt: https://lumalabs.ai/llms.txt | 付费 |
| [Meshy](https://www.meshy.ai) | 文本或图片生成 3D 模型的服务与 API，可自动贴图、重拓扑和绑定骨骼；游戏和 Web 3D 需要快速产出模型资产时选 | API | llms.txt: https://www.meshy.ai/llms.txt | 免费+付费 |
| [OpenAI 图像与视频 API（gpt-image / Sora）](https://developers.openai.com/api/docs/guides/image-generation) | OpenAI 的图像生成与编辑（gpt-image 系列，文字渲染和指令遵循强）以及 Sora 视频 API；需要准确排版文字的图片或已在 OpenAI 生态时选 | API, TS, Python | `npm i openai`<br>llms.txt: https://developers.openai.com/llms.txt | 付费 |
| [Recraft API](https://www.recraft.ai/docs) | 面向设计师的图像模型，可直接生成 SVG 矢量图、图标和统一品牌风格的插画；需要矢量输出或风格一致的成套素材时选 | API | `claude mcp add --transport http recraft https://mcp.recraft.ai/mcp`<br>llms.txt: https://www.recraft.ai/llms.txt | 免费+付费 |
| [Replicate](https://replicate.com) | 用一行代码运行数万个开源与官方模型的云 API（现属 Cloudflare），可用 Cog 部署自定义模型；想试各种社区模型或托管自己的模型时选 | API, TS, Python | `npm install replicate`<br>`pip install replicate`<br>`npx -y replicate-mcp`<br>MCP https://mcp.replicate.com<br>llms.txt: https://replicate.com/llms.txt | 付费 |
| [Runway API](https://docs.dev.runwayml.com) | Runway 视频生成模型（Gen-4 系列、Aleph、Act-Two）的开发者 API；需要可控性强的图生视频和视频转绘时选 | API, TS, Python | `npm install --save @runwayml/sdk`<br>`pip install runwayml`<br>llms.txt: https://docs.dev.runwayml.com/llms.txt | 付费 |
| [Stability AI](https://platform.stability.ai) | Stable Diffusion 系列的原厂 API（图像生成、编辑、放大、3D、音频），模型权重可自部署；需要开放权重可私有化的图像模型时选 | API | llms.txt: https://platform.stability.ai/llms.txt | 付费 |
| [Stable Audio](https://stableaudio.com) | Stability AI 的音乐与音效生成模型，Stable Audio Open 权重可本地运行；需要可自部署的音频生成模型时选 | API, Python |  | 免费+付费 |
| [Suno](https://suno.com) | 最流行的 AI 歌曲生成产品，带人声、歌词和编曲；给视频或产品做完整歌曲时用，⚠ 暂无面向公众的官方 API，第三方接口有风险 | Web | llms.txt: https://suno.com/llms.txt | 免费+付费 |
| [Tripo AI](https://www.tripo3d.ai) | 国内团队的 AI 3D 生成平台，文生/图生 3D 速度快、拓扑干净，提供 API；与 Meshy 对比选用，国内访问更顺 | API | llms.txt: https://www.tripo3d.ai/llms.txt | 免费+付费 |
| [可灵 Kling AI 开放平台](https://kling.ai/document-api) | 快手可灵的视频与图像生成 API，动作幅度和人物一致性突出，支持首尾帧、多图参考和对口型；要高质量文生/图生视频时选，国内站为 klingai.kuaishou.com | API | llms.txt: https://kling.ai/llms.txt | 付费 |
| [火山引擎 Seedream / Seedance](https://www.volcengine.com/product/doubao) | 字节跳动的图像（Seedream）与视频（Seedance）生成模型，通过火山方舟 API 调用，中文提示词理解和性价比突出；国内项目接图像视频生成时选 | API, OpenAI API |  | 付费 |
| [通义万相 Wan](https://tongyi.aliyun.com/wan/) | 阿里的图像与视频生成模型，Wan 系列权重开源、可本地部署，也可通过百炼 API 调用；想用开源视频模型或走阿里云账单时选 | API, GPU |  | 免费+付费 |

### 推理与微调平台

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Hugging Face](https://huggingface.co) | 开源模型、数据集和 Demo 的中心仓库，Inference Providers 用一个接口路由到多家推理服务，官方提供 MCP；找模型、下权重、托管 Demo 都从这里开始，⚠ 国内需镜像（hf-mirror.com） | Python, TS | `pip install -U huggingface_hub`<br>`npm install @huggingface/inference`<br>MCP https://huggingface.co/mcp | 免费+付费 |
| [Axolotl](https://axolotl.ai) | 用 YAML 配置驱动的开源微调工具，支持多 GPU 和多种训练方法；想要可复现、可版本管理的微调配置时选 | Python, GPU | `pip install axolotl` | 开源 |
| [Baseten](https://www.baseten.co) | 面向生产的模型推理平台，用 Truss 打包任意模型并自动伸缩 GPU，延迟优化做得深；要部署自定义或微调后的模型并保证 SLA 时选 | Python | `pip install truss`<br>llms.txt: https://www.baseten.co/llms.txt | 付费 |
| [Cerebras Inference](https://www.cerebras.ai/inference) | 晶圆级芯片驱动的推理服务，开源大模型输出速度可达每秒上千 token；需要近乎即时的长文本生成或代码生成时选 | OpenAI API | `pip install cerebras_cloud_sdk`<br>`npm install @cerebras/cerebras_cloud_sdk` | 免费+付费 |
| [DeepInfra](https://deepinfra.com) | 低价的开源模型 Serverless 推理 API，覆盖对话、嵌入、语音和图像；只求便宜地按 token 调用开源模型时选 | OpenAI API | llms.txt: https://docs.deepinfra.com/llms.txt | 付费 |
| [Fireworks AI](https://fireworks.ai) | 高性能开源模型推理平台，支持 Serverless、专属部署和微调，函数调用与结构化输出稳定；要把开源模型用于生产并保证吞吐时选 | OpenAI API | `pip install fireworks-ai`<br>llms.txt: https://fireworks.ai/llms.txt | 付费 |
| [Groq](https://groq.com) | 基于自研 LPU 芯片的超高速推理云，开源模型每秒数百 token，OpenAI 兼容并有免费额度；实时对话、语音 Agent 等对延迟极敏感的场景选 | OpenAI API | `npm install groq-sdk`<br>`pip install groq` | 免费+付费 |
| [Lightning AI](https://lightning.ai) | PyTorch Lightning 团队的 AI 开发云：云端 Studio、GPU 训练、模型部署一体，LitServe/LitGPT 开源；想要带持久环境的云端 GPU 开发机时选 | Python, PyTorch | `pip install lightning`<br>llms.txt: https://lightning.ai/llms.txt | 免费+付费 |
| [LLaMA-Factory](https://github.com/hiyouga/LlamaFactory) | 国内最流行的开源大模型微调框架，Web 界面零代码配置 LoRA/QLoRA、全参微调和评测，支持上百种模型；想用图形界面微调且需要中文文档时选 | Python, GPU | `pip install llamafactory` | 开源 |
| [Nebius Token Factory](https://nebius.com) | Nebius 的开源模型推理与微调服务，欧洲数据中心、价格有竞争力；需要欧洲区域合规的开源模型推理时选 | OpenAI API | llms.txt: https://nebius.com/llms.txt | 付费 |
| [Novita AI](https://novita.ai) | 提供开源大模型 API、GPU 实例和 Agent 沙箱的云平台，价格低；要便宜的开源模型接口或按需 GPU 时选 | OpenAI API | llms.txt: https://novita.ai/llms.txt | 付费 |
| [RunPod](https://www.runpod.io) | 按秒计费的 GPU 云：可租 Pod 当远程工作站，也可用 Serverless 端点部署模型；想低价租 GPU 跑训练、ComfyUI 或自定义推理时选 | Docker, Python | `pip install runpod`<br>`claude mcp add runpod --scope user -e RUNPOD_API_KEY=your_api_key_here -- npx -y @runpod/mcp-server@latest`<br>llms.txt: https://www.runpod.io/llms.txt | 付费 |
| [SambaNova Cloud](https://sambanova.ai) | 基于自研 RDU 芯片的高速推理云，主打大参数开源模型的高吞吐；需要快速运行大尺寸开源模型时与 Groq、Cerebras 对比选用 | OpenAI API |  | 免费+付费 |
| [Together AI](https://www.together.ai) | 开源模型的推理、微调和 GPU 集群云，模型上新快，覆盖对话、图像、嵌入和重排；想托管调用并微调主流开源模型时选 | OpenAI API, Python, TS | `pip install together`<br>`npm install together-ai`<br>`claude mcp add --transport http "TogetherAIDocs" https://docs.together.ai/mcp`<br>llms.txt: https://www.together.ai/llms.txt | 付费 |
| [Transformers](https://huggingface.co/docs/transformers) | Hugging Face 的模型定义与训练推理标准库，几乎所有开源模型的参考实现；要直接加载、训练或改造模型时用 | Python, PyTorch | `pip install transformers`<br>llms.txt: https://huggingface.co/docs/transformers/llms.txt | 开源 |
| [Unsloth](https://unsloth.ai) | 让 LLM 微调更快、更省显存的开源库，附大量 Colab 笔记本，可导出 GGUF 给 Ollama 使用；单卡或免费 Colab 上微调开源模型时首选 | Python, GPU | `pip install unsloth`<br>llms.txt: https://unsloth.ai/docs/llms.txt | 开源 |

### 国内模型平台

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [DeepSeek 开放平台](https://platform.deepseek.com) | DeepSeek 官方 API，OpenAI 与 Anthropic 接口双兼容，价格低且有缓存命中折扣；国内项目的默认大模型接口，把 base_url 换成 https://api.deepseek.com 即可 | OpenAI API |  | 付费 |
| [AiHubMix](https://aihubmix.com) | 面向国内开发者的多模型聚合网关，一个 Key 以 OpenAI 兼容格式调用 OpenAI、Claude、Gemini 及国产模型，支持人民币充值；国内直连调用海外模型时选，⚠ 第三方中转，敏感数据慎用 | OpenAI API | llms.txt: https://aihubmix.com/llms.txt | 付费 |
| [HF-Mirror](https://hf-mirror.com) | Hugging Face 的国内公益镜像站，设置 HF_ENDPOINT=https://hf-mirror.com 后即可用官方工具下载模型和数据集；国内服务器拉取 Hugging Face 权重时用 | CLI |  | 免费 |
| [Kimi 开放平台（Moonshot AI）](https://platform.kimi.com) | 月之暗面 Kimi 系列模型 API，长上下文和 Agent 编码能力强，OpenAI/Anthropic 兼容并内置联网搜索工具；需要国产长上下文或编码模型时选 | OpenAI API | llms.txt: https://platform.kimi.com/docs/llms.txt | 付费 |
| [MiniMax 开放平台](https://platform.minimaxi.com/docs/guides/quickstart-preparation) | MiniMax 的文本模型（M 系列，OpenAI/Anthropic 兼容，有 Coding Plan）以及海螺视频、语音合成与克隆、音乐生成 API，官方提供 MCP；需要国产编码模型或一站式接视频、配音、配乐时选 | OpenAI API | `uvx minimax-mcp`<br>llms.txt: https://platform.minimaxi.com/docs/llms.txt | 付费 |
| [PPIO 派欧云](https://ppio.com) | 国内的模型 API 与 GPU 云平台，提供 DeepSeek、Qwen 等开源模型的低价推理和 Agent 沙箱；需要国内高并发、低价的开源模型接口时选 | OpenAI API | llms.txt: https://ppio.com/llms.txt | 付费 |
| [智谱 AI 开放平台（GLM）](https://bigmodel.cn) | 智谱 GLM 系列模型 API，OpenAI/Anthropic 兼容，有长期免费的 Flash 模型和面向编程工具的 Coding Plan 套餐；想在 Claude Code 等工具里用国产模型时常选 | OpenAI API, Python | `pip install zai-sdk`<br>`claude mcp add -s user -t http web-search-prime https://open.bigmodel.cn/api/mcp/web_search_prime/mcp --header "Authorization: Bearer YOUR_API_KEY"`<br>llms.txt: https://docs.bigmodel.cn/llms.txt | 免费+付费 |
| [模力方舟 MoArk（原 Gitee AI）](https://moark.com) | Gitee 旗下的模型推理与部署平台，Serverless API 覆盖文本、图像、语音、嵌入等开源模型，使用国产算力；想用国内账单统一调用多种开源模型时选 | OpenAI API |  | 免费+付费 |
| [火山方舟（豆包大模型）](https://www.volcengine.com/product/ark) | 字节跳动的模型服务平台：豆包系列文本、视觉、语音模型及 Seedream/Seedance，OpenAI 兼容，价格低、并发高；面向国内 C 端高并发或需要多模态全家桶时选 | OpenAI API, Python | `pip install 'volcengine-python-sdk[ark]'`<br>llms.txt: https://docs.volcengine.com/llms.txt | 免费+付费 |
| [百度智能云千帆](https://cloud.baidu.com/product-s/qianfan_home) | 百度的大模型平台：文心 ERNIE 系列及第三方模型，OpenAI 兼容，带 Agent 与 RAG 开发工具；已在百度云生态或需要文心模型时选 | OpenAI API |  | 免费+付费 |
| [硅基流动 SiliconFlow](https://siliconflow.cn) | 国内的开源模型聚合推理平台，一个 Key 调用 DeepSeek、Qwen、GLM、Kimi 以及嵌入、重排、图像、语音模型，部分模型免费；想在国内用一个接口切换多家开源模型时选 | OpenAI API |  | 免费+付费 |
| [腾讯混元大模型](https://cloud.tencent.com/product/hunyuan) | 腾讯云的混元系列模型 API（文本、图像、3D、翻译），OpenAI 兼容，有免费的轻量模型；业务在腾讯云或微信生态时选 | OpenAI API |  | 免费+付费 |
| [讯飞开放平台（星火）](https://www.xfyun.cn) | 科大讯飞的星火大模型以及业内领先的中文语音识别、合成、翻译等能力；项目以中文语音为核心（听写、方言、实时转写）时选 | API |  | 免费+付费 |
| [阶跃星辰开放平台](https://platform.stepfun.com) | 阶跃星辰 Step 系列多模态模型 API（文本、视觉理解、语音、图像生成），OpenAI 兼容；需要国产视频/图像理解或实时语音模型时选 | OpenAI API | llms.txt: https://platform.stepfun.com/docs/llms.txt | 付费 |
| [阿里云百炼（DashScope）](https://bailian.console.aliyun.com) | 阿里云的大模型服务平台：通义千问 Qwen 全系、万相、语音以及第三方模型，OpenAI 兼容端点，新用户有免费额度；需要国内合规、模型种类最全的一站式平台时选 | OpenAI API, Python | `pip install dashscope` | 免费+付费 |
| [魔搭 ModelScope](https://www.modelscope.cn) | 阿里主导的国内模型社区，相当于国内版 Hugging Face，模型与数据集下载无需代理，并提供免费 API-Inference 额度和 MCP 广场；国内下载开源权重或白嫖推理额度时用 | Python | `pip install modelscope`<br>llms.txt: https://www.modelscope.cn/llms.txt | 免费 |
