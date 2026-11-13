# MCP 目录与常用 MCP 服务器

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="mcp-directories"></a>

## MCP 目录站

想找某个服务有没有 MCP，先搜这些目录。

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [Claude Connectors 目录](https://claude.com/connectors) | Anthropic 官方审核的 Claude 连接器（远程 MCP）目录，给 Claude / Claude Code 找官方认可的集成时用 |  | 免费 |
| ⭐ [Docker MCP Catalog](https://hub.docker.com/mcp) | Docker 官方审核、容器化运行的 MCP 服务器目录，想隔离运行第三方服务器时用（⚠ 需 Docker Desktop） |  | 免费 |
| ⭐ [PulseMCP](https://www.pulsemcp.com/servers) | 每日更新的 MCP 服务器与客户端目录，附下载量估算和周报，追踪生态动态时用 |  | 免费 |
| ⭐ [官方 MCP Registry](https://registry.modelcontextprotocol.io) | MCP 官方维护的服务器注册表（带 API），想确认某个 MCP 服务器是否由厂商正式发布时先查这里 |  | 免费 |
| [awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients) | 支持 MCP 的客户端清单，确认某个 IDE / 聊天应用是否能接 MCP 时用 |  | 免费 |
| [Cline MCP Marketplace](https://cline.bot/mcp-marketplace) | Cline 内置的 MCP 市场，在 Cline 里一键安装服务器时用 |  | 免费 |
| [cursor.directory MCP](https://cursor.directory/mcp) | cursor.directory 的 MCP 板块，给 Cursor 找可一键添加的服务器时用 |  | 免费 |
| [GitHub MCP Registry](https://github.com/mcp) | GitHub 上的 MCP 服务器精选目录，给 Copilot / VS Code 一键安装时用 |  | 免费 |
| [Glama MCP 目录](https://glama.ai/mcp/servers) | 带安全/质量评分的 MCP 服务器目录，挑选社区服务器前先看评分时用 |  | 免费+付费 |
| [Higress MCP Marketplace](https://mcp.higress.ai) | Higress 网关托管的 MCP 市场，把国内常用 API 转成远程 MCP 时用 |  | 免费+付费 |
| [jaw9c/awesome-remote-mcp-servers](https://github.com/jaw9c/awesome-remote-mcp-servers) | 只收录官方远程（HTTP/SSE）MCP 服务器及其 URL 的列表，想找免本地安装的服务器时用 |  | 免费 |
| [LobeHub MCP Marketplace](https://lobehub.com/mcp) | LobeHub 的 MCP 服务器市场，带评分和安装方式，中英文都可浏览 |  | 免费 |
| [MCP Inspector](https://github.com/modelcontextprotocol/inspector) | 官方的 MCP 服务器调试工具，装完任何服务器后用它检查工具列表和调用结果 | `npx @modelcontextprotocol/inspector` | 开源 |
| [MCP Market](https://mcpmarket.com) | 按类别和排行榜浏览 MCP 服务器与 Skill 的市场站，想看热门榜单时用 |  | 免费 |
| [mcp.so](https://mcp.so) | 收录量最大的社区 MCP 服务器目录，按分类和热度找冷门服务器时用 |  | 免费 |
| [MCPHub](https://github.com/samanhappy/mcphub) | 自托管的 MCP 网关与控制台，把多个服务器聚合成一个端点并分组管理时用 | docker run -p 3000:3000 -v ./data:/app/data samanhappy/mcphub | 开源 |
| [mcpservers.org](https://mcpservers.org) | wong2/awesome-mcp-servers 的可搜索网站版，按类别快速浏览服务器时用 |  | 免费 |
| [Metorial](https://github.com/metorial/metorial) | 开源的 MCP 集成平台，收录上千个可托管的服务器，给自家 Agent 批量接集成时用 |  | 开源 |
| [Pipedream MCP](https://mcp.pipedream.com) | 为数千个 API 提供托管 MCP 服务器和 OAuth 的平台，需要按应用生成专属 MCP 端点时用（⚠ 需账号） |  | 免费+付费 |
| [ToolHive](https://github.com/stacklok/toolhive) | 在容器里一键运行并管理 MCP 服务器的工具与注册表，团队要统一、安全地分发服务器时用 |  | 开源 |
| [Zapier MCP](https://zapier.com/mcp) | 把 Zapier 的 8000+ 应用动作暴露成一个 MCP 端点，让 Agent 直接操作各类 SaaS 时用（⚠ 需 Zapier 账号，按任务计费） |  | 免费+付费 |
| [魔搭 ModelScope MCP 广场](https://modelscope.cn/mcp) | 阿里魔搭社区的中文 MCP 服务器广场，找国内服务（地图、支付、办公）的 MCP 时用 |  | 免费 |

<a id="mcp-servers"></a>

## 常用 MCP 服务器

命令以 Claude Code 为例，其他 Agent 的写法见仓库根目录 AGENTS.md。UI 相关的 MCP 在 ui/catalog/12。需要 API key 或付费的已标注。

本类分组：开发与代码托管 · 数据库与后端服务 · 搜索与网页抓取 · 文档与知识 · 项目管理与协作 · 云与运维 · 监控与分析 · 浏览器与桌面自动化 · 设计与多媒体 · 移动与游戏开发 · 国内服务 · 通用工具

### 开发与代码托管

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [GitHub MCP（官方）](https://github.com/github/github-mcp-server) | GitHub 官方 MCP，让 Agent 读写仓库、Issue、PR 和 Actions 时用（⚠ 需 PAT 或 OAuth） |  | `claude mcp add-json github '{"type":"http","url":"https://api.githubcopilot.com/mcp","headers":{"Authorization":"Bearer YOUR_GITHUB_PAT"}}'` | 开源 |
| ⭐ [Serena](https://github.com/oraios/serena) | 基于语言服务器的语义检索与符号级编辑 MCP，在大型代码库里省 token 地精确改代码时用 |  | `uv tool install -p 3.13 serena-agent`<br>`claude mcp add --scope user serena -- serena start-mcp-server --context claude-code --project-from-cwd` | 开源 |
| [Angular CLI MCP](https://angular.dev/ai/mcp) | Angular CLI 自带的 MCP 服务器，让 Agent 按最新最佳实践生成和迁移 Angular 代码时用 | Angular | `npx @angular/cli mcp` | 开源 |
| [Claude Context（Zilliz）](https://github.com/zilliztech/claude-context) | 用向量库给整个代码库做语义索引的 MCP，仓库太大、grep 不够用时用（⚠ 需 OpenAI 和 Zilliz/Milvus 密钥） |  | `claude mcp add claude-context -e OPENAI_API_KEY=sk-your-openai-api-key -e MILVUS_ADDRESS=your-zilliz-cloud-public-endpoint -e MILVUS_TOKEN=your-zilliz-cloud-api-key -- npx @zilliz/claude-context-mcp@latest` | 开源 |
| [DeepWiki MCP](https://docs.devin.ai/work-with-devin/deepwiki-mcp) | Devin 提供的免费远程 MCP，针对任意公开 GitHub 仓库查文档和提问时用 |  | `claude mcp add -s user -t http deepwiki https://mcp.deepwiki.com/mcp` | 免费 |
| [Git MCP（参考实现）](https://github.com/modelcontextprotocol/servers/tree/main/src/git) | 官方参考服务器，让 Agent 读取、搜索和操作本地 Git 仓库时用 |  | `uvx mcp-server-git` | 开源 |
| [GitLab MCP（官方）](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server/) | GitLab 内置的远程 MCP 服务器，让 Agent 操作 Issue、MR 和流水线时用（⚠ 把域名换成自己的实例，需相应 GitLab 版本） |  | `claude mcp add -s user --transport http GitLab https://<gitlab.example.com>/api/v4/mcp` | 免费+付费 |
| [GitMCP](https://github.com/idosal/git-mcp) | 把任意 GitHub 仓库变成远程文档 MCP 的免费服务，想让 Agent 读某个库的最新文档防幻觉时用 |  | `npx mcp-remote https://gitmcp.io/{owner}/{repo}` | 开源 |
| [Grep MCP（Vercel）](https://vercel.com/blog/grep-a-million-github-repositories-via-mcp) | Vercel 的 grep.app 远程 MCP，在上百万公开仓库里搜真实代码用法时用 |  | `claude mcp add --transport http grep https://mcp.grep.app` | 免费 |
| [JetBrains IDE MCP](https://www.jetbrains.com/help/idea/mcp-server.html) | JetBrains IDE（2025.2 起）内置的 MCP 服务器，让外部 Agent 调用 IDE 的索引、重构和运行配置时用 |  |  | 免费+付费 |
| [Laravel Boost](https://github.com/laravel/boost) | Laravel 官方的 MCP 与规则包，让 Agent 了解本项目的路由、数据库和对应版本文档时用 | Laravel, PHP |  | 开源 |
| [Next.js DevTools MCP](https://github.com/vercel/next-devtools-mcp) | Vercel 官方 MCP，让 Agent 读取 Next.js 开发服务器的报错、路由和升级指引时用 | Next.js | `claude mcp add next-devtools npx next-devtools-mcp@latest` | 开源 |
| [Octocode MCP](https://github.com/bgauryy/octocode) | 面向 Agent 的 GitHub 代码研究 MCP，跨仓库查实现和追调用链时用 |  | `claude mcp add-json octocode --scope user '{"command":"npx","type":"stdio","args":["octocode-mcp@latest"]}'` | 开源 |
| [Postman MCP](https://github.com/postmanlabs/postman-mcp-server) | Postman 官方 MCP，让 Agent 管理集合、环境并生成 API 调用代码时用（⚠ 需 Postman API key） |  | `npx @postman/postman-mcp-server` | 免费+付费 |
| [Repomix MCP](https://github.com/yamadashy/repomix) | 把整个仓库打包成单个 AI 友好文件的工具及其 MCP，需要把代码库整体喂给模型时用 |  | `claude mcp add repomix -- npx -y repomix --mcp` | 开源 |
| [Shopify Dev MCP](https://shopify.dev/docs/apps/build/devmcp) | Shopify 官方开发者 MCP，查 Admin API、Liquid 和 Polaris 文档并校验 GraphQL 时用 | Shopify | `claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest` | 免费 |
| [SonarQube MCP](https://github.com/SonarSource/sonarqube-mcp-server) | SonarSource 官方 MCP，让 Agent 拉取代码质量与安全问题并就地修复时用（⚠ 需 SonarQube 令牌，Docker 运行） |  |  | 免费+付费 |
| [Svelte MCP（官方）](https://svelte.dev/docs/mcp/remote-setup) | Svelte 官方 MCP，提供 Svelte 5 / SvelteKit 文档和代码自动修正，写 Svelte 时用 | Svelte | `claude mcp add -t http -s [scope] svelte https://mcp.svelte.dev/mcp` | 免费 |

### 数据库与后端服务

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Supabase MCP（官方）](https://github.com/supabase/mcp) | Supabase 官方远程 MCP，让 Agent 建表、跑迁移、查日志和生成类型时用（⚠ 生产库建议加 read_only） | Postgres | `claude mcp add --scope project --transport http supabase "https://mcp.supabase.com/mcp"` | 免费+付费 |
| [Auth0 MCP](https://github.com/auth0/auth0-mcp-server) | Auth0 官方 MCP，用自然语言管理应用、API、Action 和日志时用 |  | `npx @auth0/auth0-mcp-server init --client claude-code` | 免费+付费 |
| [Chroma MCP](https://github.com/chroma-core/chroma-mcp) | Chroma 官方 MCP，在本地或云端向量集合里做检索增强时用（⚠ 仓库 2025 年 9 月后更新少） |  | `uvx chroma-mcp` | 开源 |
| [Clerk MCP](https://clerk.com/docs/guides/ai/mcp/clerk-mcp-server) | Clerk 官方 MCP，提供最新 SDK 片段和接入模式，给应用加登录鉴权时用 |  | `claude mcp add clerk --transport http https://mcp.clerk.com/mcp` | 免费+付费 |
| [ClickHouse MCP](https://github.com/ClickHouse/mcp-clickhouse) | ClickHouse 官方 MCP，让 Agent 对分析型数据库跑只读 SQL 时用 |  | `pip install mcp-clickhouse` | 开源 |
| [Convex MCP](https://docs.convex.dev/ai/convex-mcp-server) | Convex 自带的 MCP 服务器，让 Agent 查看表结构、运行函数和读日志时用 | Convex | `npx -y convex@latest mcp start` | 免费+付费 |
| [DBHub](https://github.com/bytebase/dbhub) | Bytebase 出品的省 token 通用数据库 MCP，一个服务器连 Postgres / MySQL / SQL Server / SQLite 时用 |  | `npx @bytebase/dbhub@latest --transport http --port 8080 --dsn "postgres://user:password@localhost:5432/dbname?sslmode=disable"` | 开源 |
| [dbt MCP](https://github.com/dbt-labs/dbt-mcp) | dbt Labs 官方 MCP，让 Agent 浏览模型血缘、跑 dbt 命令和查语义层时用 |  |  | 开源 |
| [DuckDB / MotherDuck MCP](https://github.com/motherduckdb/mcp-server-motherduck) | MotherDuck 官方 MCP，用 DuckDB 在本地文件或云端做数据分析时用 |  | `claude mcp add --scope user duckdb --transport stdio -- uvx mcp-server-motherduck --db-path :memory: --read-write --allow-switch-databases` | 开源 |
| [Firebase MCP](https://firebase.google.com/docs/ai-assistance/mcp-server) | Firebase CLI 自带的 MCP，管理 Auth、Firestore、Hosting 等并初始化项目时用 | Firebase | `claude mcp add firebase npx -- -y firebase-tools@latest mcp` | 免费+付费 |
| [MCP Toolbox for Databases（Google）](https://github.com/googleapis/mcp-toolbox) | Google 开源的数据库 MCP 服务器，一套配置连接 Postgres、MySQL、SQLite、BigQuery 等多种库时用 |  | `brew install mcp-toolbox`<br>`npx @toolbox-sdk/server --config tools.yaml` | 开源 |
| [MongoDB MCP（官方）](https://github.com/mongodb-js/mongodb-mcp-server) | MongoDB 官方 MCP，查询集合、看索引和管理 Atlas 集群时用（⚠ 生产环境加 --readOnly） |  | `npx -y mongodb-mcp-server@latest setup` | 开源 |
| [Neon MCP](https://github.com/neondatabase/mcp-server-neon) | Neon 官方 MCP，用自然语言管理 Serverless Postgres 项目、分支和迁移时用 | Postgres | `npx neon@latest init`<br>`npx add-mcp https://mcp.neon.tech/mcp` | 免费+付费 |
| [Pinecone MCP](https://github.com/pinecone-io/pinecone-mcp) | Pinecone 官方 MCP，查文档、建索引和上载检索数据时用（⚠ 需 PINECONE_API_KEY） |  | `npx -y @pinecone-database/mcp` | 免费+付费 |
| [Postgres MCP Pro](https://github.com/crystaldba/postgres-mcp) | 支持只读/读写模式并带索引调优与健康检查的 Postgres MCP，连接自建 Postgres 时用（⚠ 需设置 DATABASE_URI） | Postgres | pipx install postgres-mcp | 开源 |
| [Prisma MCP](https://www.prisma.io/docs/postgres/integrations/mcp-server) | Prisma 官方远程 MCP，创建和管理 Prisma Postgres 数据库、跑迁移时用 | Prisma | `claude mcp add --transport http prisma https://mcp.prisma.io/mcp` | 免费+付费 |
| [Qdrant MCP](https://github.com/qdrant/mcp-server-qdrant) | Qdrant 官方 MCP，把向量库当语义记忆层存取时用（⚠ 需 QDRANT_URL 和 COLLECTION_NAME） |  | `uvx mcp-server-qdrant` | 开源 |
| [Redis MCP（官方）](https://github.com/redis/mcp-redis) | Redis 官方 MCP，让 Agent 读写键值、流、向量索引时用 |  | `uvx --from redis-mcp-server@latest redis-mcp-server --url redis://localhost:6379/0` | 开源 |
| [Resend MCP](https://github.com/resend/resend-mcp) | Resend 官方 MCP，让 Agent 发邮件、管理域名和联系人时用（⚠ 需 API key） |  | `claude mcp add --transport http resend https://mcp.resend.com/mcp` | 免费+付费 |
| [Stripe MCP（官方）](https://docs.stripe.com/mcp) | Stripe 官方远程 MCP，查文档、建产品价格和排查支付集成问题时用（⚠ 用受限密钥或测试模式） |  | `claude mcp add --transport http stripe https://mcp.stripe.com/` | 免费 |
| [Upstash MCP](https://github.com/upstash/mcp-server) | Upstash 官方 MCP，管理 Serverless Redis、QStash 和 Vector 资源时用 |  | `claude mcp add --scope user --transport http upstash https://mcp.upstash.com/mcp` | 免费+付费 |

### 搜索与网页抓取

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [Firecrawl MCP](https://github.com/firecrawl/firecrawl-mcp-server) | Firecrawl 官方 MCP，把网页抓成干净 Markdown、整站爬取和结构化提取时用（⚠ 需 API key） | env FIRECRAWL_API_KEY=fc-YOUR_API_KEY npx -y firecrawl-mcp | 免费+付费 |
| [Apify MCP](https://github.com/apify/apify-mcp-server) | Apify 官方 MCP，调用数千个现成爬虫 Actor 抓社媒、电商和地图数据时用（⚠ 按用量计费） | `claude mcp add apify "https://mcp.apify.com" -t http` | 免费+付费 |
| [Brave Search MCP](https://github.com/brave/brave-search-mcp-server) | Brave 官方 MCP，提供网页、本地、图片、新闻搜索，想要独立索引的搜索结果时用（⚠ 需 BRAVE_API_KEY） | `npx -y @brave/brave-search-mcp-server` | 免费+付费 |
| [Bright Data MCP](https://github.com/brightdata/brightdata-mcp) | Bright Data 官方 MCP，带反爬解锁的搜索与抓取，目标站封锁严重时用（⚠ 需 API token，超出免费额度收费） | `claude mcp add --transport http brightdata "https://mcp.brightdata.com/mcp?token=YOUR_API_TOKEN"` | 免费+付费 |
| [DuckDuckGo MCP](https://github.com/nickclyde/duckduckgo-mcp-server) | 社区维护的 DuckDuckGo 搜索 MCP，不想申请任何 API key 就能联网搜索时用 | `claude mcp add ddg-search uvx duckduckgo-mcp-server` | 开源 |
| [Exa MCP](https://github.com/exa-labs/exa-mcp-server) | Exa 官方 MCP，做面向 AI 的语义网页搜索和代码上下文检索时用 | `claude plugin install exa@claude-plugins-official`<br>MCP https://mcp.exa.ai/mcp | 免费+付费 |
| [Fetch MCP（参考实现）](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) | 官方参考服务器，把任意 URL 抓下来转成 Markdown 给模型读时用 | `uvx mcp-server-fetch` | 开源 |
| [Jina AI MCP](https://github.com/jina-ai/MCP) | Jina 官方远程 MCP，提供 Reader 读网页、搜索、Embedding 和 Reranker 时用（⚠ 高频使用需 API key） | `claude mcp add -s user --transport http jina https://mcp.jina.ai/v1 --header "Authorization: Bearer ${JINA_API_KEY}"` | 免费+付费 |
| [Kagi MCP](https://github.com/kagisearch/kagimcp) | Kagi 官方 MCP，使用无广告的付费搜索和摘要器时用（⚠ 需 Kagi API key） | `claude mcp add kagi -e KAGI_API_KEY="YOUR_API_KEY_HERE" -- uvx kagimcp` | 付费 |
| [open-webSearch](https://github.com/Aas-ee/open-webSearch) | 免 API key 的多引擎搜索 MCP（Bing、百度、DuckDuckGo、CSDN 等），国内网络环境下联网搜索时用 | `npx open-websearch@latest` | 开源 |
| [Perplexity MCP](https://github.com/perplexityai/modelcontextprotocol) | Perplexity 官方 MCP，调用 Sonar 做带引用的联网问答和深度研究时用（⚠ 需 API key，按量付费） | `claude mcp add perplexity --env PERPLEXITY_API_KEY="your_key_here" -- npx -y @perplexity-ai/mcp-server` | 付费 |
| [Tavily MCP](https://github.com/tavily-ai/tavily-mcp) | Tavily 官方 MCP，提供实时搜索、提取、站点地图和爬取，Agent 需要联网查资料时用（⚠ 需 API key） | `claude mcp add --transport http tavily https://mcp.tavily.com/mcp/?tavilyApiKey=<your-api-key>` | 免费+付费 |

### 文档与知识

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| [arXiv MCP](https://github.com/blazickjp/arxiv-mcp-server) | 搜索、下载并阅读 arXiv 论文的本地 MCP，做文献调研时用 | `claude mcp add --transport stdio --scope user arxiv -- uvx arxiv-mcp-server` | 开源 |
| [Basic Memory](https://github.com/basicmachines-co/basic-memory) | 把对话沉淀成本地 Markdown 知识图谱的记忆 MCP，想让 Agent 跨会话记住项目背景时用 | `claude mcp add basic-memory -- uvx --prerelease=allow basic-memory mcp` | 开源 |
| [Excel MCP](https://github.com/haris-musa/excel-mcp-server) | 无需安装 Excel 就能创建和编辑 xlsx（公式、图表、透视表）的 MCP，批量处理表格时用 | `claude mcp add excel --scope user -- uvx excel-mcp-server stdio --allow-dir /path/to/workbooks` | 开源 |
| [Google Workspace MCP（社区）](https://github.com/taylorwilsdon/google_workspace_mcp) | 社区最完整的 Google Workspace MCP，操作 Gmail、Drive、Docs、Sheets、Calendar 时用（⚠ 需自建 Google OAuth 凭据） | `uvx workspace-mcp --tool-tier core` | 开源 |
| [LangChain Docs MCP](https://docs.langchain.com/use-these-docs) | LangChain 官方文档 MCP，查 LangChain / LangGraph / LangSmith 最新文档时用 | `claude mcp add --transport http docs-langchain https://docs.langchain.com/mcp` | 免费 |
| [MarkItDown MCP（微软）](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp) | 微软 MarkItDown 的 MCP 版，把 PDF、Office、图片等文件转成 Markdown 喂给模型时用 | `pip install markitdown-mcp` | 开源 |
| [mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) | 社区的 Obsidian MCP，通过 Local REST API 插件读写和搜索笔记库时用（⚠ 需先装插件并提供 OBSIDIAN_API_KEY） | `uvx mcp-obsidian` | 开源 |
| [Microsoft Learn MCP](https://github.com/MicrosoftDocs/mcp) | 微软官方文档 MCP，查 Azure、.NET、Microsoft 365 的最新官方文档和代码示例时用 | `/plugin install microsoft-docs@claude-plugins-official`<br>MCP https://learn.microsoft.com/api/mcp | 免费 |
| [Notion MCP（官方）](https://developers.notion.com/docs/get-started-with-mcp) | Notion 官方远程 MCP，让 Agent 搜索、读取和创建页面与数据库时用 | `claude mcp add --transport http notion https://mcp.notion.com/mcp` | 免费+付费 |
| [OpenAI Docs MCP](https://developers.openai.com/learn/docs-mcp) | OpenAI 官方开发者文档 MCP，写 OpenAI API / Agents SDK / Codex 相关代码前查最新文档时用 | `claude mcp add --transport http openaiDeveloperDocs https://developers.openai.com/mcp` | 免费 |
| [Ref](https://github.com/ref-tools/ref-tools-mcp) | 省 token 的技术文档检索 MCP，可搜公开库文档和私有仓库，写代码前核对 API 时用（⚠ 需 API key，免费额度有限） | MCP https://api.ref.tools/mcp?apiKey=YOUR_API_KEY | 免费+付费 |
| [Zotero MCP](https://github.com/54yyyu/zotero-mcp) | 把 Zotero 文献库接给 Agent 的 MCP，按库内论文做语义检索和引用整理时用 | `uv tool install zotero-mcp-server` | 开源 |

### 项目管理与协作

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| [Airtable MCP（官方）](https://support.airtable.com/docs/using-the-airtable-mcp-server) | Airtable 官方远程 MCP，查询和修改 Base 里的表与记录时用 | `claude mcp add --transport http airtable https://mcp.airtable.com/mcp` | 免费+付费 |
| [Asana MCP（官方）](https://developers.asana.com/docs/using-asanas-mcp-server) | Asana 官方远程 MCP，查任务、项目和目标并更新进度时用 | `claude mcp add --transport sse asana https://mcp.asana.com/sse` | 免费+付费 |
| [Atlassian MCP（官方）](https://github.com/atlassian/atlassian-mcp-server) | Atlassian 官方远程 MCP，连接 Jira、Confluence 和 Compass 云端数据时用（⚠ 仅支持 Cloud） | `claude mcp add --transport http atlassian https://mcp.atlassian.com/v2/mcp` | 免费+付费 |
| [Google Calendar MCP（社区）](https://github.com/nspady/google-calendar-mcp) | 社区的 Google 日历 MCP，支持多账号查空闲、建日程和改期时用（⚠ 需自建 Google OAuth 凭据） | `npx @cocal/google-calendar-mcp auth` | 开源 |
| [Linear MCP（官方）](https://linear.app/docs/mcp) | Linear 官方远程 MCP，让 Agent 查、建、更新 Issue 和项目时用 | `claude mcp add --transport http linear-server https://mcp.linear.app/mcp` | 免费+付费 |
| [mcp-atlassian（社区）](https://github.com/sooperset/mcp-atlassian) | 社区维护的 Jira / Confluence MCP，同时支持 Cloud 和自建 Server / Data Center 时用 | `uvx mcp-atlassian` | 开源 |
| [monday.com MCP](https://github.com/mondaycom/mcp) | monday.com 官方 MCP，读写看板、条目和文档时用（⚠ 需 API token） | MCP https://mcp.monday.com/mcp | 免费+付费 |
| [Slack MCP（官方）](https://docs.slack.dev/ai/slack-mcp-server/) | Slack 官方远程 MCP，搜索频道消息、读线程和发消息时用（⚠ 需工作区管理员批准） | `claude plugin install slack`<br>MCP https://mcp.slack.com/mcp | 免费+付费 |

### 云与运维

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| [AWS MCP Servers（awslabs）](https://github.com/awslabs/mcp) | AWS 官方开源的几十个 MCP 服务器合集（API、文档、IaC、Serverless 等），在 AWS 上开发运维时用（⚠ 需本地 AWS 凭据） | `claude mcp add aws-api uvx awslabs.aws-api-mcp-server@latest`<br>`claude mcp add aws-docs uvx awslabs.aws-documentation-mcp-server@latest` | 开源 |
| [Azure MCP（microsoft/mcp）](https://github.com/microsoft/mcp) | 微软官方 MCP 服务器目录仓库，含 Azure MCP、Azure DevOps、Fabric 等，在 Azure 上开发运维时用 | `npx -y @azure/mcp@latest server start` | 开源 |
| [Cloud Run MCP](https://github.com/GoogleCloudPlatform/cloud-run-mcp) | Google 官方 MCP，让 Agent 直接把当前项目部署到 Cloud Run 时用（⚠ 需 gcloud 登录） |  | 开源 |
| [Cloudflare MCP（官方）](https://github.com/cloudflare/mcp-server-cloudflare) | Cloudflare 官方的一组远程 MCP，管理 Workers、KV、R2、D1 并查文档和可观测数据时用 | MCP https://mcp.cloudflare.com/mcp<br>MCP https://docs.mcp.cloudflare.com/mcp | 免费+付费 |
| [Docker MCP Toolkit / Gateway](https://github.com/docker/mcp-gateway) | Docker 官方的 MCP 网关与 CLI 插件，把多个容器化服务器聚合成一个端点并统一管密钥时用 | docker mcp gateway run | 开源 |
| [Google Cloud MCP（google/mcp）](https://github.com/google/mcp) | Google 官方的远程与开源 MCP 服务器总表（BigQuery、GKE、Maps、Workspace 等），找 Google 系服务的官方 MCP 时用 |  | 免费 |
| [Heroku MCP](https://github.com/heroku/heroku-mcp-server) | Heroku 官方 MCP，管理应用、Dyno、插件和日志时用（⚠ 需 HEROKU_API_KEY） | `npx -y @heroku/mcp-server` | 付费 |
| [Kubernetes MCP Server](https://github.com/containers/kubernetes-mcp-server) | 原生实现的 Kubernetes / OpenShift MCP，无需 kubectl 即可查资源、日志和执行 Helm 时用 | `npx -y kubernetes-mcp-server@latest` | 开源 |
| [mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) | 基于 kubectl 的社区 Kubernetes MCP，用当前 kubeconfig 管理集群时用 | `claude mcp add kubernetes -- npx mcp-server-kubernetes` | 开源 |
| [Netlify MCP](https://docs.netlify.com/build/build-with-ai/netlify-mcp-server/) | Netlify 官方 MCP，创建站点、部署和管理环境变量时用 | `npx -y add-mcp https://mcp.netlify.com/mcp` | 免费+付费 |
| [Railway MCP](https://docs.railway.com/reference/mcp-server) | Railway CLI 自带的 MCP，创建项目、部署服务和管理变量时用（⚠ 需先安装并登录 Railway CLI） | `claude mcp add railway railway mcp` | 免费+付费 |
| [Render MCP](https://github.com/render-oss/render-mcp-server) | Render 官方 MCP，创建服务、查日志和数据库指标时用（⚠ 需 API key） | `claude mcp add --transport http render https://mcp.render.com/mcp --header "Authorization: Bearer <YOUR_API_KEY>"` | 免费+付费 |
| [Terraform MCP（HashiCorp）](https://github.com/hashicorp/terraform-mcp-server) | HashiCorp 官方 MCP，查 Registry 里的 provider / module 文档并管理 HCP Terraform 工作区时用 | `claude mcp add terraform -s user -t stdio -- docker run -i --rm hashicorp/terraform-mcp-server` | 开源 |
| [Vercel MCP（官方）](https://vercel.com/docs/mcp/vercel-mcp) | Vercel 官方远程 MCP，查项目、部署日志和文档时用 | `claude mcp add --transport http vercel https://mcp.vercel.com` | 免费+付费 |

### 监控与分析

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| [Datadog MCP](https://docs.datadoghq.com/bits_ai/mcp_server/setup/) | Datadog 官方远程 MCP，查日志、指标、Trace 和事故时用（⚠ 需 Datadog 账号） |  | 付费 |
| [Grafana MCP](https://github.com/grafana/mcp-grafana) | Grafana 官方 MCP，查仪表盘、Prometheus / Loki 数据和告警时用（⚠ 需 GRAFANA_URL 和服务账号令牌） | `uvx mcp-grafana` | 开源 |
| [PostHog MCP](https://posthog.com/docs/model-context-protocol) | PostHog 官方 MCP，查产品分析、功能开关、实验和错误追踪时用 | `npx @posthog/wizard mcp add`<br>MCP https://mcp.posthog.com/mcp | 免费+付费 |
| [Sentry MCP（官方）](https://github.com/getsentry/toolkit) | Sentry 官方 MCP 与插件，让 Agent 拉取报错堆栈、搜索 Issue 并用 Seer 分析根因时用 | `claude plugin marketplace add getsentry/sentry-mcp`<br>`claude plugin install sentry-mcp@sentry-mcp`<br>MCP https://mcp.sentry.dev/mcp | 免费+付费 |

### 浏览器与桌面自动化

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [Browser MCP](https://github.com/BrowserMCP/mcp) | 通过浏览器扩展操控你本机已登录的 Chrome 的 MCP，需要复用现有登录态时用 |  | `npx @browsermcp/mcp@latest` | 开源 |
| [browser-use MCP](https://github.com/browser-use/browser-use) | 最流行的开源 AI 浏览器 Agent 库及其 MCP，让 Agent 自主完成多步网页操作时用 |  | `claude mcp add browser-use -- uvx --from 'browser-use[cli]' browser-use --mcp` | 开源 |
| [Browserbase MCP](https://docs.browserbase.com/integrations/mcp/setup) | Browserbase 托管的云浏览器 MCP（Stagehand 驱动），需要云端无头浏览器和反检测时用（⚠ 需 API key） |  | `claude mcp add --transport http browserbase "https://mcp.browserbase.com/mcp?browserbaseApiKey=YOUR_BROWSERBASE_API_KEY"` | 免费+付费 |
| [Chrome MCP Server（hangwin）](https://github.com/hangwin/mcp-chrome) | 国人开发的 Chrome 扩展式 MCP，直接操作日常浏览器并支持语义搜索标签页内容时用（⚠ 需手动安装扩展） |  | `npm install -g mcp-chrome-bridge` | 开源 |
| [Desktop Commander](https://github.com/wonderwhy-er/DesktopCommanderMCP) | 给 Agent 终端控制、文件搜索和差异编辑能力的本地 MCP，在 Claude Desktop 等无终端的客户端里干活时用 |  | `claude mcp add --scope user desktop-commander -- npx -y @wonderwhy-er/desktop-commander@latest` | 开源 |
| [Peekaboo](https://github.com/openclaw/Peekaboo) | macOS 截屏与 GUI 自动化 CLI，自带 MCP 模式，让 Agent 看屏幕并操作原生应用时用（⚠ 仅 macOS） | macOS | `brew install openclaw/tap/peekaboo`<br>peekaboo mcp | 开源 |

### 设计与多媒体

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [MCP for Blender（原 blender-mcp）](https://github.com/ahujasid/mcp-for-blender) | 用自然语言操控 Blender 建模、材质和场景的社区 MCP，快速做 3D 原型时用（⚠ 需在 Blender 内装配套插件） | Blender | `claude mcp add blender uvx mcp-for-blender` | 开源 |
| [Replicate MCP](https://replicate.com/docs/reference/mcp) | Replicate 官方 MCP，搜索并运行平台上的图像、视频、音频模型时用（⚠ 需 API token，按量付费） |  | `npx -y replicate-mcp`<br>MCP https://mcp.replicate.com | 付费 |
| [Webflow MCP](https://github.com/webflow/mcp-server) | Webflow 官方 MCP，读写站点、CMS 集合和 Designer 画布时用 |  | `npx -y webflow-mcp-server@latest` | 免费+付费 |

### 移动与游戏开发

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [Expo MCP](https://docs.expo.dev/eas/ai/mcp/) | Expo 官方远程 MCP，查最新 Expo SDK 文档并操作本地开发服务器和模拟器时用（⚠ 需 EAS 付费计划） | Expo, React Native | `claude mcp add --transport http expo https://mcp.expo.dev/mcp` | 付费 |
| [iOS Simulator MCP](https://github.com/joshuayoes/ios-simulator-mcp) | 操作 iOS 模拟器（点击、输入、截图、读无障碍树）的 MCP，自动验证界面时用（⚠ 需 macOS 和 Facebook IDB） | iOS | `claude mcp add ios-simulator npx ios-simulator-mcp` | 开源 |
| [MCP for Unity](https://github.com/CoplayDev/unity-mcp) | 连接 Unity 编辑器的 MCP，让 Agent 管理场景、资源、脚本并自动跑测试时用（通过 Unity Package Manager 添加 Git URL 安装） | Unity | https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#main | 开源 |
| [Mobile MCP](https://github.com/mobile-next/mobile-mcp) | 同时驱动 iOS 与 Android 模拟器和真机的 MCP，做跨平台移动端自动化测试时用 | iOS, Android | `claude mcp add mobile-mcp -- npx -y @mobilenext/mobile-mcp@latest` | 开源 |
| [MobileBuildMCP（原 XcodeBuildMCP）](https://github.com/getsentry/MobileBuildMCP) | 让 Agent 构建、运行、测试 Xcode 项目并操作模拟器和真机的 MCP，做 iOS / macOS 开发时用 | Xcode, iOS | `claude mcp add MobileBuildMCP -- npx -y mobilebuildmcp@latest mcp` | 开源 |
| [Xcode MCP（Apple 官方）](https://developer.apple.com/documentation/xcode/giving-agentic-coding-tools-access-to-xcode) | Apple 官方文档：Xcode 26.3 起通过 mcpbridge 把工程、构建和预览开放给外部 Agent，想让 Claude Code / Codex 直接驱动 Xcode 时读 | Xcode |  | 免费 |

### 国内服务

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [高德地图 MCP（官方）](https://lbs.amap.com/api/mcp-server/summary) | 高德开放平台官方 MCP，做地理编码、路径规划、周边搜索和天气查询时用（⚠ 需申请高德 key） | `npx -y @amap/amap-maps-mcp-server`（需 AMAP_MAPS_API_KEY）<br>MCP https://mcp.amap.com/mcp?key=您在高德官网上申请的key | 免费+付费 |
| [12306 MCP（社区）](https://github.com/Joooook/12306-mcp) | 查询 12306 余票、中转和经停站的社区 MCP，做出行规划时用（⚠ 非官方，仅查询不购票） | `npx -y 12306-mcp` | 开源 |
| [EdgeOne Makers MCP（原 Pages MCP）](https://github.com/TencentEdgeOne/edgeone-makers-mcp) | 腾讯 EdgeOne 官方 MCP，把 HTML 或整个前端项目快速部署成公网可访问页面时用 | `npx @edgeone/makers-mcp@latest` | 免费+付费 |
| [MiniMax MCP](https://github.com/MiniMax-AI/MiniMax-MCP) | MiniMax 官方 MCP，调用语音合成、声音克隆、图像和视频生成时用（⚠ 需 MINIMAX_API_KEY，按量付费） | `uvx minimax-mcp` | 付费 |
| [xiaohongshu-mcp（社区）](https://github.com/xpzouying/xiaohongshu-mcp) | Star 最多的小红书 MCP，支持搜索、读取详情和发布图文（⚠ 非官方，需本地先启动服务并扫码登录，注意账号风控） | `claude mcp add --transport http xiaohongshu-mcp http://localhost:18060/mcp` | 开源 |
| [微信读书 MCP（社区）](https://github.com/freestylefly/mcp-server-weread) | 社区的微信读书 MCP，导出书架、划线和笔记做读书总结时用（⚠ 非官方，需 Cookie，2025 年后更新少） | `npx -y mcp-server-weread` | 开源 |
| [火山引擎 MCP Servers](https://github.com/volcengine/mcp-server) | 字节火山引擎官方 MCP 服务器合集（云服务、搜索、知识库等），用火山引擎产品时来这里找 |  | 开源 |
| [百度地图 MCP（官方）](https://github.com/baidu-maps/mcp) | 百度地图官方 MCP，提供地点检索、路线规划、逆地理编码和路况时用（⚠ 需 BAIDU_MAP_API_KEY，仓库 2025 年 8 月后更新少） | `npx -y @baidumap/mcp-server-baidu-map` | 免费+付费 |
| [腾讯云 CloudBase MCP](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit) | 腾讯云开发官方 MCP 与工具包，让 Agent 一键部署小程序 / Web 后端、数据库和云函数时用 | `npx @cloudbase/cloudbase-mcp@latest` | 免费+付费 |
| [语雀 MCP](https://github.com/yuque/yuque-mcp-server) | 语雀官方 MCP，搜索和读写知识库文档时用（⚠ 需语雀 Token） | `claude mcp add yuque -- npx -y yuque-mcp --token=YOUR_TOKEN` | 开源 |
| [钉钉 MCP（官方）](https://github.com/open-dingtalk/dingtalk-mcp) | 钉钉开放平台出品的 MCP，操作通讯录、日程、待办等时用（⚠ 需企业内部应用凭据，仓库更新较少） | `npx -y dingtalk-mcp@latest` | 开源 |
| [阿里云运维 MCP](https://github.com/aliyun/alibaba-cloud-ops-mcp-server) | 阿里云官方 MCP，管理 ECS、RDS、OSS 和云监控等资源时用（⚠ 需 AccessKey） | `uvx alibaba-cloud-ops-mcp-server@latest` | 开源 |
| [飞书 / Lark OpenAPI MCP（官方）](https://github.com/larksuite/lark-openapi-mcp) | 飞书官方 MCP，把开放平台 API（消息、文档、多维表格、日历）变成工具，做飞书自动化时用（⚠ 需自建应用的 App ID / Secret，仓库 2025 年 8 月后更新少） | `npx -y @larksuiteoapi/lark-mcp mcp -a <your_app_id> -s <your_app_secret>` | 开源 |

### 通用工具

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| [Filesystem MCP（参考实现）](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | 官方参考服务器，给没有文件工具的客户端提供受限目录内的读写能力时用 | `npx -y @modelcontextprotocol/server-filesystem <允许访问的目录>` | 开源 |
| [Hugging Face MCP（官方）](https://github.com/huggingface/hf-mcp-server) | Hugging Face 官方 MCP，搜索模型、数据集、论文并调用 Spaces 里的工具时用 | `claude mcp add hf-mcp-server -t http https://huggingface.co/mcp?login` | 免费+付费 |
| [Memory MCP（参考实现）](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) | 官方参考服务器，用本地知识图谱给 Agent 提供跨会话持久记忆时用 | `npx -y @modelcontextprotocol/server-memory` | 开源 |
| [n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | 让 Agent 了解全部 n8n 节点并直接生成、校验工作流的 MCP，用 AI 搭 n8n 自动化时用 | `claude mcp add n8n-mcp -e MCP_MODE=stdio -e LOG_LEVEL=error -e DISABLE_CONSOLE_OUTPUT=true -- npx n8n-mcp` | 开源 |
| [Sequential Thinking MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking) | 官方参考服务器，引导模型分步思考、可回溯修正，拆解复杂问题时用 | `npx -y @modelcontextprotocol/server-sequential-thinking` | 开源 |
| [Supergateway](https://github.com/supercorp-ai/supergateway) | 把 stdio MCP 服务器转成 HTTP / SSE（或反向）的桥接工具，客户端与服务器传输方式不匹配时用 |  | 开源 |
| [Time MCP（参考实现）](https://github.com/modelcontextprotocol/servers/tree/main/src/time) | 官方参考服务器，提供当前时间和时区换算，Agent 需要可靠日期时间时用 | `uvx mcp-server-time` | 开源 |
| [YouTube Transcript MCP](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) | 抓取 YouTube 视频字幕的社区 MCP，总结视频或做内容二次创作时用 | `npx -y @kimtaeyoon83/mcp-server-youtube-transcript` | 开源 |
