# 常用服务与基础设施

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="stack-services"></a>

## 服务与基础设施（认证 / 数据库 / 支付 / 邮件 / 部署…）

新项目要接的外部服务。每个子类的 ⭐ 是默认选择；国内访问受限的已用 ⚠ 标出。

本类分组：认证 · 数据库与 ORM · 支付与订阅 · 邮件与通知 · 文件存储与媒体 · 部署与托管 · 后台任务与队列 · 实时与协作 · 搜索 · 分析 / 监控 / 特性开关 · 国际化 · 安全与限流 · 国内可用替代

### 认证

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Better Auth](https://better-auth.com) | TypeScript 开源认证框架，用户数据存自己的数据库，插件覆盖 2FA、组织、passkey、SSO；想免费自托管、不被厂商锁定时首选 | TS, Next.js, Hono | `npm i better-auth`<br>`npx auth@latest mcp --claude-code`<br>llms.txt: https://better-auth.com/llms.txt | 开源 |
| [Auth.js（NextAuth）](https://authjs.dev) | 老牌开源 OAuth/会话库（原 NextAuth.js），存量 Next.js 项目继续用；⚠ 项目已并入 Better Auth 团队、仅做维护，新项目建议直接选 Better Auth | Next.js, SvelteKit | `npm i next-auth` | 开源 |
| [Auth0](https://auth0.com) | Okta 旗下的老牌托管身份平台，协议与合规覆盖最全（SAML、MFA、B2B 组织、Agent 认证）；有合规审计要求的企业项目选，⚠ 用量上来后价格高 | Next.js, Node | `npm i @auth0/nextjs-auth0`<br>`npx @auth0/auth0-mcp-server init`<br>llms.txt: https://auth0.com/llms.txt | 免费+付费 |
| [authentik](https://goauthentik.io) | 开源身份提供方（SSO、LDAP、代理转发认证），界面友好；给自托管的内部工具和家庭实验室统一登录时选 | Python, Docker | llms.txt: https://goauthentik.io/docs/llms.txt | 开源 |
| [Casdoor](https://casdoor.ai) | 国内团队开源的 IAM/SSO 平台（Go + React），内置微信、钉钉、飞书等国内登录方式和中文管理后台；私有化部署并要对接国内生态时选 | Go, React | llms.txt: https://casdoor.ai/llms.txt | 开源 |
| [Clerk](https://clerk.com) | 托管式认证与用户管理，自带登录/注册/组织/计费的现成 React 组件，想最快上线且不自己维护用户表时选；⚠ 国内访问受限，超出免费额度按月活计费 | Next.js, React, Expo | `npm i @clerk/nextjs`<br>`claude mcp add clerk --transport http https://mcp.clerk.com/mcp`<br>llms.txt: https://clerk.com/llms.txt | 免费+付费 |
| [Descope](https://www.descope.com) | 拖拽式流程编排的托管认证平台，支持 passkey、SSO 以及给 AI Agent/MCP 服务器做授权；想用可视化流程而不是写代码配置登录时选 | React, Node | `npm i @descope/nextjs-sdk`<br>llms.txt: https://www.descope.com/llms.txt | 免费+付费 |
| [Hexclave（原 Stack Auth）](https://www.hexclave.com) | 开源的 Clerk 替代品（2026 年由 Stack Auth 更名为 Hexclave），带现成组件、团队/权限和管理面板，可自托管；喜欢 Clerk 的开发体验但要开源可控时选，⚠ 旧包名 @stackframe/stack 的教程已过时 | Next.js, React | `npm i @hexclave/next`<br>`claude mcp add --transport http hexclave https://mcp.hexclave.com/mcp`<br>llms.txt: https://www.hexclave.com/llms.txt | 开源 |
| [Keycloak](https://www.keycloak.org) | Red Hat 主导的开源 IAM（OIDC/SAML/LDAP/用户联邦），企业内网与私有化部署的事实标准；⚠ Java 服务较重，小项目不划算 | Java, Docker |  | 开源 |
| [Kinde](https://kinde.com) | 托管认证 + 权限 + 特性开关 + 计费一体的平台，免费额度大；想用一家服务同时解决登录、角色和订阅时选 | Next.js, React | `npm i @kinde-oss/kinde-auth-nextjs`<br>llms.txt: https://kinde.com/llms.txt | 免费+付费 |
| [Logto](https://logto.io) | 开源身份基础设施（OIDC/OAuth 2.1），支持多租户、SSO、RBAC 和微信/支付宝等国内社交登录，可自托管；面向国内用户或要做 SaaS 多租户时选 | Node, React | `npm i @logto/next`<br>`claude mcp add --transport http logto https://mcp.logto.io`<br>llms.txt: https://logto.io/llms.txt | 开源 |
| [OpenAuth](https://openauth.js.org) | SST 团队出的自托管 OAuth 2.0 服务端，可部署在 Lambda/Workers/Node，自带可换肤登录 UI；要给多个应用搭统一登录中心且不想用重型 IAM 时选 | TS, Hono | `npm i @openauthjs/openauth` | 开源 |
| [OpenFGA](https://openfga.dev) | CNCF 的开源细粒度授权引擎（Google Zanzibar 模型），用关系描述「谁能对什么做什么」；权限超出简单角色、要做文档级共享时选 | Go, Docker | `npm i @openfga/sdk`<br>llms.txt: https://openfga.dev/llms.txt | 开源 |
| [Ory（Kratos / Hydra）](https://www.ory.com) | 模块化开源身份栈：Kratos 管用户、Hydra 做 OAuth2/OIDC 服务端、Keto 做权限；需要自己当 OAuth 提供方或做细粒度授权的大型系统选 | Go, Docker | llms.txt: https://www.ory.com/llms.txt | 开源 |
| [Supabase Auth](https://supabase.com/docs/guides/auth) | Supabase 内置认证（邮箱、OAuth、手机号、匿名、SSO），与行级安全 RLS 直接联动；数据库已经用 Supabase 时不必再引入第三方认证 | Postgres | `npm i @supabase/ssr`<br>llms.txt: https://supabase.com/llms.txt | 免费+付费 |
| [SuperTokens](https://supertokens.com) | 开源认证方案（会话、无密码、多租户、MFA），核心可自托管并提供预置 UI；需要自定义后端登录流程又想自己掌握数据时选 | Node, Python, Go | `npm i supertokens-node`<br>llms.txt: https://supertokens.com/llms.txt | 开源 |
| [WorkOS AuthKit](https://workos.com) | 面向 B2B 的企业级认证：SSO/SAML、SCIM 目录同步、审计日志，AuthKit 前 100 万月活免费；客户是企业、需要对接 Okta/Entra 时选 | Next.js, Node | `npm i @workos-inc/authkit-nextjs`<br>`claude mcp add --transport http workos https://mcp.workos.com/mcp`<br>llms.txt: https://workos.com/llms.txt | 免费+付费 |
| [ZITADEL](https://zitadel.com) | Go 写的开源身份平台，原生多租户、事件溯源审计、OIDC/SAML/Passkey；想要比 Keycloak 更轻、更适合 B2B SaaS 的自托管 IAM 时选 | Go, Docker |  | 开源 |

### 数据库与 ORM

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Drizzle ORM](https://orm.drizzle.team) | 轻量、无运行时代码生成的 TypeScript ORM，写法贴近 SQL，在 Serverless/Edge 上冷启动快；新 TS 项目的默认 ORM，配 drizzle-kit 做迁移 | TS, Postgres, SQLite, MySQL | `npm i drizzle-orm`<br>`npm i -D drizzle-kit`<br>llms.txt: https://orm.drizzle.team/llms.txt | 开源 |
| ⭐ [Supabase](https://supabase.com) | 开源 Firebase 替代品：托管 Postgres + 认证 + 存储 + 实时 + Edge Functions + 向量检索，一个平台包完后端；想用 SQL 且让 Agent 通过 MCP 直接管库时首选，⚠ 国内直连不稳定 | Postgres, TS | `npm i @supabase/supabase-js`<br>`claude mcp add --scope project --transport http supabase "https://mcp.supabase.com/mcp"`<br>llms.txt: https://supabase.com/llms.txt | 免费+付费 |
| [Appwrite](https://appwrite.io) | 开源后端平台（数据库、认证、存储、函数、消息、站点托管），可 Docker 自托管也有云版；想要 Firebase 式体验又要能私有化时选 | Docker, TS | `npm i appwrite`<br>MCP https://mcp.appwrite.io/<br>llms.txt: https://appwrite.io/llms.txt | 开源 |
| [Atlas](https://atlasgo.io) | 声明式数据库表结构管理与迁移工具（像 Terraform 管库），带迁移 lint；多语言项目或想在 CI 里审查迁移安全性时选 | Go, SQL | llms.txt: https://atlasgo.io/llms.txt | 免费+付费 |
| [ClickHouse](https://clickhouse.com) | 列式 OLAP 数据库，亿级行聚合秒出；做埋点分析、日志、指标看板这类分析型查询时选，不要拿来当业务主库 | SQL | `npm i @clickhouse/client`<br>MCP https://mcp.clickhouse.cloud/mcp<br>llms.txt: https://clickhouse.com/llms.txt | 开源 |
| [Cloudflare D1](https://developers.cloudflare.com/d1/) | Cloudflare 的 Serverless SQLite，与 Workers 原生绑定、带读副本和时间点恢复；应用本身部署在 Workers 上时最省事的数据库 | SQLite, Workers | llms.txt: https://developers.cloudflare.com/d1/llms.txt | 免费+付费 |
| [Convex](https://www.convex.dev) | 响应式后端即服务：用 TypeScript 写查询/变更函数，数据自动实时同步到前端，内置定时任务、文件存储和向量检索；做协作或实时应用、不想写 SQL 和缓存失效逻辑时选 | TS, React | `npm i convex`<br>`npx -y convex@latest mcp start`<br>llms.txt: https://www.convex.dev/llms.txt | 免费+付费 |
| [Dexie.js](https://dexie.org) | IndexedDB 的易用封装，带 React hooks 实时查询；纯前端应用需要浏览器端持久化存储时选 | TS, Browser | `npm i dexie`<br>llms.txt: https://dexie.org/llms.txt | 开源 |
| [DuckDB](https://duckdb.org) | 进程内的分析型 SQL 引擎，直接查 Parquet/CSV/JSON；本地数据分析、ETL 脚本、给 Agent 做数据处理时选 | SQL, Python, Node | `pip install duckdb`<br>llms.txt: https://duckdb.org/llms.txt | 开源 |
| [Electric（原 ElectricSQL）](https://electric.ax) | Postgres 同步引擎：通过 HTTP 把表的「shape」实时流到客户端，可与 TanStack DB 组合；要在不换数据库的前提下给前端加实时同步时选 | Postgres, TS | `npm i @electric-sql/client`<br>llms.txt: https://electric.ax/llms.txt | 开源 |
| [Firebase](https://firebase.google.com) | Google 的移动/Web 后端全家桶：Firestore、认证、云函数、推送、托管、Crashlytics；做移动端 MVP 且接受 NoSQL 时选，⚠ 国内无法直连 | NoSQL, Android, iOS | `npm i firebase`<br>`claude mcp add firebase npx -- -y firebase-tools@latest mcp`<br>llms.txt: https://firebase.google.com/docs/llms.txt | 免费+付费 |
| [InstantDB](https://www.instantdb.com) | 面向前端的实时数据库：在客户端直接写关系查询，自带乐观更新、离线和多人同步；做 Linear/Figma 那种即时协作应用且不想写后端时选 | React, React Native | `npm i @instantdb/react`<br>`claude mcp add instant -s user -t http https://mcp.instantdb.com/mcp`<br>llms.txt: https://www.instantdb.com/llms.txt | 免费+付费 |
| [Kysely](https://kysely.dev) | 类型安全的 TypeScript SQL 查询构建器，不是 ORM；想自己写 SQL 但要完整类型推导、不要模型层抽象时选 | TS | `npm i kysely`<br>llms.txt: https://kysely.dev/llms.txt | 开源 |
| [MikroORM](https://mikro-orm.io) | 基于 Data Mapper 与 Unit of Work 的 TypeScript ORM；领域模型复杂、想要类似 Hibernate/Doctrine 的实体管理时选 | TS, Node | `npm i @mikro-orm/core`<br>llms.txt: https://mikro-orm.io/llms.txt | 开源 |
| [MongoDB Atlas](https://www.mongodb.com/products/platform/atlas-database) | 官方托管的文档数据库，带全文与向量检索；数据结构灵活多变、团队熟悉 MongoDB 时选 | MongoDB | `npm i mongodb`<br>`npx mongodb-mcp-server@latest setup`<br>llms.txt: https://www.mongodb.com/llms.txt | 免费+付费 |
| [Mongoose](https://mongoosejs.com) | MongoDB 的 Node.js ODM，提供 schema、校验和中间件；Node + MongoDB 组合的默认数据层 | Node, MongoDB | `npm i mongoose`<br>llms.txt: https://mongoosejs.com/llms.txt | 开源 |
| [Neon](https://neon.com) | Serverless Postgres，存算分离、可缩容到零，支持数据库分支（每个 PR 一份库）；只要一个纯 Postgres、配合 Vercel 或 Agent 临时建库时选 | Postgres | `npm i @neondatabase/serverless`<br>`npx neon@latest mcp`<br>`npx add-mcp https://mcp.neon.tech/mcp`<br>llms.txt: https://neon.com/llms.txt | 免费+付费 |
| [Nhost](https://nhost.io) | 开源后端平台：Postgres + Hasura GraphQL + 认证 + 存储 + 函数；前端想直接用 GraphQL 访问数据库时选 | Postgres, GraphQL | `npm i @nhost/nhost-js`<br>llms.txt: https://docs.nhost.io/llms.txt | 免费+付费 |
| [PGlite](https://pglite.dev) | 编译成 WASM 的完整 Postgres，可跑在浏览器、Node 和 Bun 里并支持 pgvector；做本地开发、单元测试或浏览器内数据库时选 | TS, WASM | `npm i @electric-sql/pglite` | 开源 |
| [PlanetScale](https://planetscale.com) | 高性能托管 MySQL（Vitess）与 Postgres，分支式无锁表结构变更；流量大、要求数据库稳定性的生产业务选，⚠ 已无免费档 | MySQL, Postgres | `npm i @planetscale/database`<br>`claude mcp add --transport http "planetscale" https://mcp.pscale.dev/mcp/planetscale`<br>llms.txt: https://planetscale.com/llms.txt | 付费 |
| [PocketBase](https://pocketbase.io) | 单个 Go 可执行文件的开源后端：内嵌 SQLite + 认证 + 文件 + 实时订阅 + 管理后台；小项目、原型、自托管在一台便宜 VPS 上时选 | Go, SQLite | `npm i pocketbase` | 开源 |
| [PowerSync](https://www.powersync.com) | 把 Postgres/MongoDB/MySQL 同步到客户端 SQLite 的同步服务，离线可写；做 React Native/Flutter 离线优先应用时选 | SQLite, React Native, Flutter | `npm i @powersync/web`<br>llms.txt: https://www.powersync.com/llms.txt | 免费+付费 |
| [Prisma](https://www.prisma.io) | 最普及的 TypeScript ORM：schema 文件 + 生成的类型安全客户端 + 迁移 + Studio，另有托管的 Prisma Postgres；团队想要更高抽象、文档与生态最全时选 | TS, Postgres, MySQL | `npm i -D prisma`<br>`npm i @prisma/client`<br>`claude mcp add --transport http prisma https://mcp.prisma.io/mcp`<br>llms.txt: https://www.prisma.io/llms.txt | 开源 |
| [Redis](https://redis.io) | 内存数据结构库：缓存、会话、排行榜、消息流、向量集合；需要长连接、自托管或 Redis Cloud 全功能时选（Serverless 环境优先 Upstash） | Redis | `npm i redis`<br>`uvx --from redis-mcp-server@latest redis-mcp-server --url redis://localhost:6379/0`<br>llms.txt: https://redis.io/llms.txt | 免费+付费 |
| [TiDB Cloud](https://www.pingcap.com/tidb/cloud/) | PingCAP 的分布式 MySQL 兼容数据库，Serverless 档可自动扩缩并带向量检索；需要水平扩展的 MySQL、或想用国产开源数据库时选 | MySQL | `uvx --from "pytidb[mcp]" tidb-mcp-server`<br>llms.txt: https://www.pingcap.com/llms.txt | 免费+付费 |
| [Turso](https://turso.tech) | 基于 libSQL/SQLite 的边缘数据库，支持嵌入式副本和每租户一库；读多写少、要把数据放到用户附近或每个用户独立数据库时选 | SQLite | `npm i @libsql/client`<br>MCP https://mcp.turso.ai/mcp<br>llms.txt: https://turso.tech/llms.txt | 免费+付费 |
| [TypeORM](https://typeorm.io) | 装饰器风格的老牌 TypeScript ORM，NestJS 生态默认搭配；维护存量 NestJS 项目时用，新项目优先 Drizzle 或 Prisma | TS, NestJS | `npm i typeorm`<br>llms.txt: https://typeorm.io/llms.txt | 开源 |
| [Upstash](https://upstash.com) | 按请求计费的 Serverless Redis，走 HTTP 可在 Edge/Workers 里用，同厂还有 QStash、Vector、Workflow；需要缓存、会话、限流又不想维护 Redis 实例时选 | Redis, TS | `npm i @upstash/redis`<br>`claude mcp add upstash-redis -e UPSTASH_REDIS_REST_URL=https://YOUR_DB.upstash.io -e UPSTASH_REDIS_REST_TOKEN=YOUR_REST_TOKEN -- npx -y @upstash/redis-mcp`<br>llms.txt: https://upstash.com/llms.txt | 免费+付费 |
| [Xata](https://xata.io) | 托管 Postgres 平台，支持写时复制分支、数据脱敏和零停机表结构变更；需要把生产数据安全地复制给预发环境或 Agent 使用时选 | Postgres | llms.txt: https://xata.io/llms.txt | 免费+付费 |
| [Zero（Rocicorp）](https://zero.rocicorp.dev) | 基于查询的同步引擎：把 Postgres 数据按需同步到客户端本地，读写即时；已有 Postgres、想把现有 Web 应用做成秒开的本地优先体验时选，⚠ 仍在快速迭代 | TS, Postgres | `npm i @rocicorp/zero`<br>llms.txt: https://zero.rocicorp.dev/llms.txt | 开源 |

### 支付与订阅

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Stripe](https://stripe.com) | 支付基础设施的事实标准：Checkout、订阅、按量计费、发票、Connect 分账，文档和 Agent 工具最全；主体在海外或香港的项目默认选，⚠ 不支持中国大陆主体开户，税务需自己处理或另开 Stripe Tax | TS, Python | `npm i stripe`<br>`claude mcp add --transport http stripe https://mcp.stripe.com/`<br>llms.txt: https://stripe.com/llms.txt | 付费 |
| [Airwallex 空中云汇](https://www.airwallex.com) | 跨境收付款平台，支持中国大陆与香港主体开户、多币种账户和在线收单；国内公司做出海业务收款与结汇时选 | API | llms.txt: https://www.airwallex.com/llms.txt | 付费 |
| [Autumn](https://useautumn.com) | 架在 Stripe 之上的开源定价与计费层：用配置定义套餐、额度、按量与积分，三个函数完成结账/校验/上报；AI 应用要做积分或用量计费又不想写 webhook 时选 | TS, Stripe | `npm i autumn-js`<br>llms.txt: https://useautumn.com/llms.txt | 免费+付费 |
| [Creem](https://www.creem.io) | 面向独立开发者和 AI 应用的 Merchant of Record，支持订阅、许可证和收入分成，入驻门槛低；国内开发者出海收款时常用的 Stripe 替代 | TS | `npm i creem`<br>llms.txt: https://docs.creem.io/llms.txt | 付费 |
| [Dodo Payments](https://dodopayments.com) | 覆盖 150+ 国家的 Merchant of Record，支持订阅、用量计费和本地支付方式；面向新兴市场或被 Stripe 拒之门外的开发者选 | TS | `npm i dodopayments`<br>`claude mcp add --transport http dodopayments https://mcp.dodopayments.com/mcp`<br>llms.txt: https://dodopayments.com/llms.txt | 付费 |
| [Flowglad](https://www.flowglad.com) | 开源、无 webhook 的支付与计费层，用 React hooks 直接读取订阅和权益状态；想让 Agent 一次性把计费接好时选 | Next.js, React | llms.txt: https://www.flowglad.com/docs/llms.txt | 免费+付费 |
| [Lago](https://www.getlago.com) | 开源的按量计费与发票引擎，可自托管；计费规则复杂（事件计量、阶梯、预付额度）且不想被支付厂商绑定时选 | Docker, API | llms.txt: https://www.getlago.com/llms.txt | 开源 |
| [Lemon Squeezy](https://www.lemonsqueezy.com) | Merchant of Record 支付平台（已被 Stripe 收购），代处理全球销售税，支持订阅与许可证；卖数字产品的存量项目继续用，新项目可对比 Polar/Creem | TS | `npm i @lemonsqueezy/lemonsqueezy.js` | 付费 |
| [Paddle](https://www.paddle.com) | 老牌 Merchant of Record，代缴全球税并处理退款与拒付，支持 B2B 发票；SaaS 面向全球企业客户、要合规省心时选，⚠ 入驻需审核 | TS | `npm i @paddle/paddle-node-sdk`<br>`claude mcp add --transport http paddle-live https://mcp.paddle.com/mcp` | 付费 |
| [Polar](https://polar.sh) | 面向开发者的开源 Merchant of Record：订阅、一次性购买、许可证密钥、按量计费，代缴全球税；独立开发者卖 SaaS/数字产品、不想处理税务时选 | TS, Next.js | `npm i @polar-sh/sdk`<br>`claude mcp add --transport http polar https://mcp.polar.sh/mcp/polar-mcp` | 免费+付费 |
| [RevenueCat](https://www.revenuecat.com) | 封装 App Store/Google Play/Web 内购的订阅后端，统一权益、收据校验和付费墙实验；做移动端订阅应用时几乎必选 | iOS, Android, React Native, Flutter | `npm i react-native-purchases`<br>`claude mcp add --transport http revenuecat https://mcp.revenuecat.ai/mcp`<br>llms.txt: https://www.revenuecat.com/llms.txt | 免费+付费 |
| [Superwall](https://superwall.com) | 移动端远程付费墙：不发版就能改付费墙设计并做 A/B 实验；已有内购、想专门优化转化率时选 | iOS, Android, React Native | llms.txt: https://superwall.com/llms.txt | 免费+付费 |

### 邮件与通知

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Resend](https://resend.com) | 开发者优先的事务邮件 API，与 React Email 同团队，支持收信、广播和 webhook；新项目发验证码、通知邮件的默认选择 | TS, React | `npm i resend`<br>`claude mcp add resend -e RESEND_API_KEY=re_xxxxxxxxx -- npx -y resend-mcp`<br>llms.txt: https://resend.com/llms.txt | 免费+付费 |
| [AgentMail](https://agentmail.to) | 给 AI Agent 用的邮箱 API：按需创建收件箱，收发、线程、附件都走接口；Agent 需要自己的邮箱地址注册或对外沟通时选 | API, TS, Python | `npm i agentmail`<br>`claude mcp add --transport http agentmail https://mcp.agentmail.to/mcp`<br>llms.txt: https://agentmail.to/llms.txt | 免费+付费 |
| [Amazon SES](https://aws.amazon.com/ses/) | AWS 的底层发信服务，单价最低；发信量大、已有 AWS 账号且愿意自己处理模板、退信和信誉时选 | AWS | `npm i @aws-sdk/client-sesv2` | 付费 |
| [Courier](https://www.courier.com) | 多渠道通知 API 与可视化模板设计器，自带收件箱和偏好中心；产品/运营需要自己改通知内容时选 | API | `npm i @trycourier/courier`<br>`claude mcp add --transport http courier https://mcp.courier.com --header api_key:YOUR_COURIER_API_KEY`<br>llms.txt: https://www.courier.com/llms.txt | 免费+付费 |
| [Expo Notifications](https://docs.expo.dev/push-notifications/overview/) | Expo 的推送方案：统一 APNs/FCM 令牌与发送接口，免费；Expo/React Native 应用自己发推送时的默认做法 | Expo, React Native | `npx expo install expo-notifications`<br>llms.txt: https://docs.expo.dev/llms.txt | 免费 |
| [Knock](https://knock.app) | 托管的通知编排平台：跨渠道工作流、批量合并、偏好中心和站内 Feed 组件；B2B SaaS 通知逻辑复杂、不想自建时选 | TS, React | `npm i @knocklabs/node`<br>`claude mcp add --transport http knock https://mcp.knock.app/mcp`<br>llms.txt: https://knock.app/llms.txt | 免费+付费 |
| [Loops](https://loops.so) | 为 SaaS 设计的邮件平台：营销邮件、自动化流程与事务邮件合一，编辑器好用；需要用户引导序列和产品更新邮件时选 | API | `npm i loops`<br>llms.txt: https://loops.so/llms.txt | 免费+付费 |
| [Mailpit](https://mailpit.axllent.org) | 本地开发用的假 SMTP 服务器 + Web 收件箱，拦截所有外发邮件；开发和 CI 里测试发信流程时用 | Go, Docker |  | 开源 |
| [MJML](https://mjml.io) | 响应式邮件标记语言，编译成兼容 Outlook 的表格 HTML；不用 React 或需要给非前端同事维护模板时选 | Node | `npm i mjml` | 开源 |
| [Novu](https://novu.co) | 开源通知基础设施：一套工作流分发到站内信、邮件、短信、推送和聊天，自带收件箱组件；需要多渠道通知和用户偏好设置时选 | TS, React | `npm i @novu/framework`<br>llms.txt: https://novu.co/llms.txt | 开源 |
| [OneSignal](https://onesignal.com) | 推送通知平台（移动推送、Web Push、应用内消息、邮件、短信），免费额度大；以推送为主要触达手段的应用选，⚠ 国内安卓需走厂商通道 | iOS, Android, Web | `npm i react-onesignal`<br>llms.txt: https://onesignal.com/llms.txt | 免费+付费 |
| [Plunk](https://www.useplunk.com) | 基于 SES 的开源邮件平台，事务、营销、自动化三合一，可自托管；想要 Loops 式功能但要便宜或自托管时选 | API, Docker | llms.txt: https://www.useplunk.com/llms.txt | 开源 |
| [Postmark](https://postmarkapp.com) | 以送达率和速度著称的事务邮件服务，事务与营销流分离；对验证码/账单邮件的到达率要求高时选 | API | `npm i postmark`<br>llms.txt: https://postmarkapp.com/llms.txt | 付费 |
| [React Email](https://react.email) | 用 React 组件和 Tailwind 写邮件模板，本地预览后渲染成兼容各邮箱客户端的 HTML；任何发信服务都能搭配 | React, Tailwind | `npx create-email@latest`<br>`npm i @react-email/components`<br>llms.txt: https://react.email/llms.txt | 开源 |
| [Twilio](https://www.twilio.com) | 全球短信、语音、WhatsApp 和验证码（Verify）API；面向海外用户做短信验证或电话通知时选，⚠ 发往中国大陆的短信限制多 | API | `npm i twilio`<br>llms.txt: https://www.twilio.com/llms.txt | 付费 |

### 文件存储与媒体

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Cloudflare R2](https://developers.cloudflare.com/r2/) | 兼容 S3 API 的对象存储，出口流量免费；存用户上传、图片、视频、AI 生成文件的默认选择，⚠ 国内访问需绑自定义域名且速度一般 | S3 API, Workers | llms.txt: https://developers.cloudflare.com/r2/llms.txt | 免费+付费 |
| [Amazon S3](https://aws.amazon.com/s3/) | 对象存储的行业标准，功能最全（生命周期、版本、事件、多种存储级别）；已在 AWS 生态或有合规要求时选，⚠ 出口流量费高 | AWS | `npm i @aws-sdk/client-s3` | 付费 |
| [Backblaze B2](https://www.backblaze.com/cloud-storage) | 低价的 S3 兼容对象存储，与 Cloudflare 等 CDN 互联免流量费；存大量备份、归档或媒体原片时选 | S3 API | llms.txt: https://www.backblaze.com/llms.txt | 付费 |
| [bunny.net](https://bunny.net) | 欧洲的高性价比 CDN、边缘存储与视频流（Bunny Stream）；要便宜的全球 CDN 和视频托管时选 | API | llms.txt: https://bunny.net/docs/llms.txt | 付费 |
| [Cloudinary](https://cloudinary.com) | 图片与视频的上传、转换、优化和 CDN 分发一体化平台，URL 参数即可裁剪/转码/AI 处理；媒体处理需求重、不想自己搭管线时选 | API, React | `npm i cloudinary`<br>`claude mcp add --transport sse cloudinary-asset-mgmt https://asset-management.mcp.cloudinary.com/mcp`<br>llms.txt: https://cloudinary.com/llms.txt | 免费+付费 |
| [Garage](https://garagehq.deuxfleurs.fr) | 轻量的开源自托管 S3 兼容对象存储，单二进制、可跨机房部署；MinIO 社区版停止维护后，小规模自建对象存储选它 | Rust, Docker |  | 开源 |
| [ImageKit](https://imagekit.io) | 实时图片/视频优化、转换与 CDN，带媒体库，可挂接外部存储；想要比 Cloudinary 便宜的同类方案时选 | API | `npm i @imagekit/nodejs`<br>llms.txt: https://imagekit.io/docs/llms.txt | 免费+付费 |
| [imgix](https://www.imgix.com) | 基于 URL 参数的实时图片处理与 CDN，接在你已有的存储桶前面；图片已经存在 S3/R2/GCS、只需要处理和加速时选 | API | llms.txt: https://www.imgix.com/llms.txt | 付费 |
| [Mux](https://www.mux.com) | 视频基础设施 API：上传、转码、自适应码流播放、直播和观看数据；产品里要放点播或直播视频时选 | API, React | `npm i @mux/mux-node @mux/mux-player-react`<br>MCP https://mcp.mux.com<br>llms.txt: https://www.mux.com/llms.txt | 免费+付费 |
| [sharp](https://sharp.pixelplumbing.com) | 基于 libvips 的高性能 Node.js 图片处理库（缩放、裁剪、格式转换）；需要在自己服务端处理图片时选 | Node | `npm i sharp` | 开源 |
| [Tigris](https://www.tigrisdata.com) | 全球自动分布的 S3 兼容对象存储，数据跟着访问位置走、无出口流量费；应用部署在 Fly.io 或多区域时选 | S3 API | llms.txt: https://www.tigrisdata.com/llms.txt | 免费+付费 |
| [Transloadit](https://transloadit.com) | 文件处理管线服务（视频转码、图片处理、文档转换、病毒扫描），Uppy 与 tus 的出品方；上传后要做复杂处理链时选 | API | `claude mcp add --transport http transloadit https://api2.transloadit.com/mcp`<br>llms.txt: https://transloadit.com/llms.txt | 免费+付费 |
| [UploadThing](https://uploadthing.com) | 为 TypeScript 全栈应用做的文件上传服务，服务端定义文件路由和权限、前端给现成上传组件；Next.js 项目想十分钟接好上传时选 | Next.js, React | `npm i uploadthing @uploadthing/react` | 免费+付费 |
| [Uppy](https://uppy.io) | 开源的模块化文件上传组件（拖拽、摄像头、网盘导入、tus 断点续传），可直传 S3；需要自己掌控上传 UI 和后端时选 | JS, React | `npm i @uppy/core @uppy/dashboard`<br>llms.txt: https://uppy.io/llms.txt | 开源 |
| [Vercel Blob](https://vercel.com/docs/vercel-blob) | Vercel 自带的对象存储，支持客户端直传和 CDN 分发；项目已在 Vercel 上、文件量不大时最省事 | Vercel, Next.js | `npm i @vercel/blob`<br>llms.txt: https://vercel.com/llms.txt | 免费+付费 |

### 部署与托管

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Vercel](https://vercel.com) | Next.js 母公司的前端云：Git 推送即部署、预览环境、Fluid Compute、AI Gateway 等一体化；Next.js/React 项目的默认部署平台，⚠ 国内访问需绑自定义域名且仍不稳定 | Next.js, React | `npm i -g vercel`<br>`claude mcp add --transport http vercel https://mcp.vercel.com`<br>llms.txt: https://vercel.com/llms.txt | 免费+付费 |
| [Alchemy](https://alchemy.run) | 纯 TypeScript 的轻量基础设施即代码库，资源就是异步函数，对 Cloudflare 支持最好；想用几十行 TS 管理 Workers/D1/R2 等资源时选 | TS, Cloudflare | `npm i alchemy`<br>llms.txt: https://alchemy.run/llms.txt | 开源 |
| [AWS Amplify](https://aws.amazon.com/amplify/) | AWS 的全栈托管与后端即代码（认证、数据、存储）；公司已绑定 AWS、想要 Vercel 式的前端部署体验时选 | AWS, React, Next.js | `npm i aws-amplify` | 免费+付费 |
| [Cloudflare Workers / Pages](https://developers.cloudflare.com/workers/) | 运行在全球边缘的 Serverless 平台，免费额度大，配套 D1/R2/KV/Queues/Durable Objects；要低成本全球部署、或做有状态的 Agent 与实时服务时选 | Workers, Hono | `npm create cloudflare@latest`<br>MCP https://mcp.cloudflare.com/mcp<br>MCP https://docs.mcp.cloudflare.com/mcp（文档）<br>llms.txt: https://developers.cloudflare.com/workers/llms.txt | 免费+付费 |
| [Coolify](https://coolify.io) | 开源自托管 PaaS，在自己的 VPS 上获得 Vercel/Heroku 式体验，带一键数据库和上百种服务模板；想省钱且愿意自己管服务器时选 | Docker | llms.txt: https://coolify.io/llms.txt | 开源 |
| [Deno Deploy](https://deno.com/deploy) | Deno 官方的全球托管平台，原生跑 TypeScript 和 Web 标准 API；项目用 Deno/Fresh 时选 | Deno | llms.txt: https://docs.deno.com/llms.txt | 免费+付费 |
| [DigitalOcean App Platform](https://www.digitalocean.com/products/app-platform) | DigitalOcean 的托管 PaaS，从 Git 或容器部署，配套托管数据库和 Droplet；想要价格透明的中小型云时选 | Docker | llms.txt: https://www.digitalocean.com/llms.txt | 付费 |
| [Docker](https://docs.docker.com) | 容器构建与运行的标准工具，Compose 用来在本地起整套依赖；几乎所有自托管和 CI 部署的基础，⚠ 国内拉取 Docker Hub 镜像需配置镜像源 | Docker | llms.txt: https://docs.docker.com/llms.txt | 免费+付费 |
| [Dokploy](https://dokploy.com) | 开源自托管 PaaS，基于 Docker 与 Traefik，原生支持 Docker Compose 和多节点；想要比 Coolify 更轻、以 Compose 为中心时选 | Docker | llms.txt: https://dokploy.com/llms.txt | 开源 |
| [Expo EAS](https://docs.expo.dev/eas/) | Expo 的云端构建、提交应用商店、OTA 热更新和 CI 工作流；React Native 应用没有 Mac 也能打 iOS 包并自动上架 | Expo, React Native | `npm i -g eas-cli`<br>llms.txt: https://docs.expo.dev/llms.txt | 免费+付费 |
| [Fly.io](https://fly.io) | 把容器跑成全球多区域 microVM 的平台，支持持久卷和私有网络；需要长连接、WebSocket 或把服务放到离用户近的区域时选 | Docker | fly mcp server<br>llms.txt: https://fly.io/llms.txt | 付费 |
| [GitHub Actions](https://docs.github.com/actions) | GitHub 内置的 CI/CD，按 YAML 工作流跑测试、构建和部署；代码在 GitHub 上时的默认 CI | YAML |  | 免费+付费 |
| [GitHub Pages](https://pages.github.com) | 从仓库直接发布静态网站，免费；文档站、个人主页和纯静态产物选，⚠ 国内访问较慢 | Static |  | 免费 |
| [Google Cloud Run](https://cloud.google.com/run) | 把任意容器跑成按请求计费、可缩到零的服务，支持 GPU；有容器化后端、要弹性伸缩且不想管 K8s 时选 | Docker, GCP |  | 免费+付费 |
| [Hetzner Cloud](https://www.hetzner.com/cloud) | 性价比极高的欧洲/美国/新加坡云服务器；配合 Coolify、Dokploy 或 Kamal 自托管时最常见的 VPS 选择 | VPS | llms.txt: https://docs.hetzner.com/llms.txt | 付费 |
| [Kamal](https://kamal-deploy.org) | 37signals 出的零停机容器部署工具，用 SSH 把 Docker 应用发到任意服务器；有自己的 VPS/裸金属、不想引入 PaaS 时选 | Docker, Ruby |  | 开源 |
| [Netlify](https://www.netlify.com) | Jamstack 托管平台：Git 部署、预览、函数、表单和 Blob 存储；静态站点和 Astro/Vite 类项目选，框架中立 | Astro, Vite, Next.js | `npm i -g netlify-cli`<br>`npx -y add-mcp https://mcp.netlify.com/mcp`<br>llms.txt: https://www.netlify.com/llms.txt | 免费+付费 |
| [Northflank](https://northflank.com) | 面向生产的容器平台，可跑在自己的云账号（BYOC）上，支持 GPU、预览环境和任务；团队需要 K8s 能力但不想自己运维时选 | Docker, K8s | llms.txt: https://northflank.com/docs/llms.txt | 免费+付费 |
| [OpenTofu](https://opentofu.org) | Linux 基金会维护的 Terraform 开源分支，用 HCL 声明多云基础设施；需要可审计、可复现的基础设施即代码且在意许可证时选 | HCL |  | 开源 |
| [Pulumi](https://www.pulumi.com) | 用 TypeScript/Python/Go 等通用语言写基础设施即代码；团队更想写真实代码而不是 HCL 时选 | TS, Python, Go | `npm i @pulumi/pulumi`<br>`claude mcp add --transport http pulumi https://mcp.ai.pulumi.com/mcp`<br>llms.txt: https://www.pulumi.com/llms.txt | 免费+付费 |
| [Railway](https://railway.com) | 按用量计费的应用托管平台，一键起服务、数据库和定时任务，自动识别构建方式；需要常驻后端进程或带数据库的全栈应用、不想碰 AWS 时选 | Docker, Node, Python | railway mcp install<br>llms.txt: https://railway.com/llms.txt | 付费 |
| [Render](https://render.com) | Heroku 式的托管 PaaS：Web 服务、后台 worker、定时任务、托管 Postgres 和 Redis；想要简单稳定的传统后端托管时选 | Docker, Node, Python | MCP https://mcp.render.com/mcp（需 API Key 请求头）<br>llms.txt: https://render.com/llms.txt | 免费+付费 |
| [SST](https://sst.dev) | 用 TypeScript 定义基础设施并部署到 AWS/Cloudflare 的框架，带本地实时开发；要用 AWS 又不想手写 CloudFormation/Terraform 时选 | TS, AWS | `npm i sst`<br>llms.txt: https://sst.dev/llms.txt | 开源 |

### 后台任务与队列

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Inngest](https://www.inngest.com) | 事件驱动的持久化工作流平台：把函数拆成可重试的步骤，自带并发、限流、定时和 Agent 编排，无需自建队列；Serverless 应用里跑后台任务和 AI 工作流的默认选择 | TS, Python, Go | `npm i inngest`<br>`claude mcp add --transport http inngest-dev http://127.0.0.1:8288/mcp`（本地 dev server）<br>`claude mcp add --transport http inngest-cloud https://api.inngest.com/mcp`<br>llms.txt: https://www.inngest.com/llms.txt | 免费+付费 |
| [BullMQ](https://docs.bullmq.io) | 基于 Redis 的 Node.js 任务队列，支持延迟、重复、优先级、流程依赖和限速；有常驻 Node 进程和 Redis、想完全自己掌控队列时选 | Node, Redis | `npm i bullmq` | 开源 |
| [Cloudflare Queues / Workflows](https://developers.cloudflare.com/queues/) | Workers 平台内置的消息队列和持久化工作流；应用已在 Cloudflare 上时不必再接外部任务系统 | Workers | llms.txt: https://developers.cloudflare.com/queues/llms.txt | 免费+付费 |
| [DBOS Transact](https://www.dbos.dev) | 把持久化工作流做成库：加装饰器即可让函数状态存进 Postgres、崩溃后自动续跑；不想部署独立编排服务时选 | Python, TS, Postgres | `npm i @dbos-inc/dbos-sdk`<br>llms.txt: https://www.dbos.dev/llms.txt | 开源 |
| [Graphile Worker](https://worker.graphile.org) | 基于 Postgres LISTEN/NOTIFY 的高性能 Node.js 任务队列，可在 SQL 触发器里入队；业务逻辑紧贴 Postgres 时选 | Node, Postgres | `npm i graphile-worker`<br>llms.txt: https://worker.graphile.org/llms.txt | 开源 |
| [Hatchet](https://hatchet.run) | 基于 Postgres 的开源任务队列与工作流引擎，强调公平调度和并发控制；Python/TS/Go 后端需要比 Celery 更可靠的任务系统时选 | Python, TS, Go | `npm i @hatchet-dev/typescript-sdk`<br>llms.txt: https://docs.hatchet.run/llms.txt | 开源 |
| [pg-boss](https://github.com/timgit/pg-boss) | 直接用 Postgres 做存储的 Node.js 任务队列（SKIP LOCKED）；已有 Postgres、不想为队列再加一个 Redis 时选 | Node, Postgres | `npm i pg-boss` | 开源 |
| [Restate](https://restate.dev) | 轻量的持久化执行运行时，单二进制部署，提供持久化函数、虚拟对象和工作流；想要 Temporal 式可靠性但更轻、延迟更低时选 | TS, Java, Python, Go, Rust | `npm i @restatedev/restate-sdk`<br>llms.txt: https://restate.dev/llms.txt | 开源 |
| [Temporal](https://temporal.io) | 工业级持久化执行引擎，工作流代码可运行数月并保证恰好一次语义；订单、支付、长流程编排等关键业务选，⚠ 概念多、运维成本高 | Go, TS, Python, Java | `npm i @temporalio/client`<br>llms.txt: https://temporal.io/llms.txt | 开源 |
| [Trigger.dev](https://trigger.dev) | 开源的后台任务与 AI 工作流平台，任务跑在它的托管机器上、没有超时限制，带实时进度推送；需要长时间运行的任务（视频处理、Agent、爬取）时选 | TS | `npx trigger.dev@latest init`<br>`npx trigger.dev@latest install-mcp`<br>llms.txt: https://trigger.dev/llms.txt | 免费+付费 |
| [Upstash QStash / Workflow](https://upstash.com/docs/qstash/overall/getstarted) | 基于 HTTP 的 Serverless 消息队列与定时器，Workflow 在其上提供持久化多步骤流程；只需要延迟、重试、定时回调某个接口时最轻的方案 | TS, HTTP | `npm i @upstash/qstash @upstash/workflow`<br>llms.txt: https://upstash.com/llms.txt | 免费+付费 |
| [Workflow SDK（Vercel，原 Workflow DevKit）](https://workflow-sdk.dev) | 用 "use workflow" / "use step" 指令把普通 TypeScript 异步函数变成可暂停、可恢复的持久化工作流；应用在 Vercel/Next.js 上、想不引入新平台就拥有持久化执行时选 | TS, Next.js | `npm i workflow`<br>llms.txt: https://workflow-sdk.dev/llms.txt | 开源 |

### 实时与协作

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Liveblocks](https://liveblocks.io) | 协作功能的托管平台：在线状态、多人光标、评论、通知、协同文本编辑和 AI Copilot 组件；要给产品加 Figma/Notion 式多人协作时首选 | React, Yjs | `npm i @liveblocks/client @liveblocks/react`<br>`claude mcp add liveblocks -e LIVEBLOCKS_SECRET_KEY="{{SECRET_KEY}}" -- npx -y github:liveblocks/liveblocks-mcp-server`<br>llms.txt: https://liveblocks.io/llms.txt | 免费+付费 |
| [Ably](https://ably.com) | 企业级实时消息平台（发布订阅、在线状态、聊天、LLM 流式推送），保证消息顺序与送达；需要 SLA 和全球规模的实时通道时选 | API, TS | `npm i ably`<br>llms.txt: https://ably.com/llms.txt | 免费+付费 |
| [Automerge](https://automerge.org) | JSON 文档模型的 CRDT 库（Rust 内核），配 automerge-repo 做同步与存储；做本地优先应用、需要完整历史和分支合并时选 | TS, Rust | `npm i @automerge/automerge`<br>llms.txt: https://automerge.org/llms.txt | 开源 |
| [Centrifugo](https://centrifugal.dev) | Go 写的开源自托管实时消息服务器（WebSocket/SSE/HTTP 流），语言无关；后端不是 Node、需要高并发推送且可私有化时选 | Go, Docker | llms.txt: https://centrifugal.dev/llms.txt | 开源 |
| [Hocuspocus](https://tiptap.dev/docs/hocuspocus/getting-started/overview) | Tiptap 团队出的 Yjs WebSocket 后端，带鉴权钩子、持久化和扩展；自托管 Yjs 协同编辑的服务端选它 | Node, Yjs | `npm i @hocuspocus/server`<br>llms.txt: https://tiptap.dev/llms.txt | 开源 |
| [Jazz](https://jazz.tools) | 本地优先的分布式数据库框架：协同数据、权限、文件和离线同步内置；想不写后端就做出多人协作应用时选，⚠ API 仍在演进 | TS, React | `npm i jazz-tools`<br>llms.txt: https://jazz.tools/llms.txt | 开源 |
| [PartyKit / PartyServer](https://www.partykit.io) | 基于 Cloudflare Durable Objects 的实时服务器框架，每个房间一个有状态实例；要自己写多人游戏、协作或 Agent 会话的服务端逻辑时选 | Cloudflare, TS | `npm i partyserver` | 开源 |
| [Pusher Channels](https://pusher.com) | 老牌托管 WebSocket 发布订阅服务，接入最简单；只需要把服务端事件推到浏览器（通知、实时刷新）时选 | API | `npm i pusher pusher-js` | 免费+付费 |
| [Rivet](https://rivet.dev) | 开源的有状态 Actor 平台（RivetKit），每个 Actor 自带持久状态、实时连接和调度；要做有状态 Agent、多人房间且不想绑定 Cloudflare 时选 | TS | `npm i rivetkit`<br>llms.txt: https://rivet.dev/llms.txt | 开源 |
| [Socket.IO](https://socket.io) | 经典的双向实时通信库，带房间、自动重连和降级；有常驻 Node 服务器、要自己写实时逻辑时选 | Node | `npm i socket.io socket.io-client` | 开源 |
| [Stream](https://getstream.io) | 聊天、动态 Feed、音视频通话的托管 API 与 UI 组件；要在应用内快速上线 IM 或社交 Feed 时选 | React, React Native | `npm i stream-chat stream-chat-react`<br>llms.txt: https://getstream.io/llms.txt | 免费+付费 |
| [Yjs](https://yjs.dev) | 最主流的 CRDT 库，为 Tiptap/Lexical/ProseMirror/CodeMirror 等编辑器提供协同编辑；想自托管协同、不依赖托管平台时选 | JS | `npm i yjs`<br>llms.txt: https://docs.yjs.dev/llms.txt | 开源 |

### 搜索

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Meilisearch](https://www.meilisearch.com) | Rust 写的开源搜索引擎，开箱即有容错、分面和混合（关键词+向量）搜索，中文分词可用；站内搜索想自托管且几分钟跑起来时首选 | Rust, Docker | `npm i meilisearch`<br>`claude mcp add --transport http meilisearch https://your-host/mcp --header "Authorization: Bearer YOUR_API_KEY"`<br>llms.txt: https://www.meilisearch.com/llms.txt | 开源 |
| [Algolia](https://www.algolia.com) | 托管搜索服务的标杆，毫秒级响应，InstantSearch 组件、排序规则、分析和 AI 推荐齐全；电商或内容站要最成熟的搜索体验且预算充足时选 | API, React | `npm i algoliasearch react-instantsearch`<br>`claude mcp add --transport http algolia-devex https://mcp.algolia.com/1/snippets/mcp`<br>llms.txt: https://www.algolia.com/llms.txt | 免费+付费 |
| [Algolia DocSearch](https://docsearch.algolia.com) | Algolia 给文档站提供的免费爬取 + 搜索弹窗，现带 AI 问答；开源项目或技术文档站申请即可用 | React | `npm i @docsearch/react` | 免费 |
| [Elasticsearch](https://www.elastic.co/elasticsearch) | 分布式搜索与分析引擎，全文、聚合、向量检索和日志场景通吃；数据量大、查询复杂或已有 ELK 栈时选，⚠ 运维重 | Java, Docker | `npm i @elastic/elasticsearch`<br>llms.txt: https://www.elastic.co/llms.txt | 免费+付费 |
| [Fuse.js](https://www.fusejs.io) | 零依赖的客户端模糊搜索库；数据量小（几千条内）、只需在前端做模糊匹配时选 | JS | `npm i fuse.js` | 开源 |
| [MiniSearch](https://lucaong.github.io/minisearch/) | 小巧的内存全文搜索引擎，支持前缀、模糊和字段加权；要在浏览器或 Node 内做真正的倒排索引搜索时选 | JS | `npm i minisearch` | 开源 |
| [Orama](https://orama.com) | TypeScript 写的全文 + 向量 + 混合搜索引擎，可跑在浏览器、Edge 或服务端；文档站和小数据集要零基础设施的搜索时选 | TS | `npm i @orama/orama`<br>llms.txt: https://orama.com/llms.txt | 开源 |
| [Pagefind](https://pagefind.app) | 构建后对静态 HTML 建索引的纯前端搜索，按需加载分片，支持中文；静态文档站和博客的零成本搜索 | Static | `npx pagefind --site public`<br>llms.txt: https://pagefind.app/llms.txt | 开源 |
| [ParadeDB](https://www.paradedb.com) | 把 BM25 全文检索和分析能力做成 Postgres 扩展（pg_search）；数据已在 Postgres、不想再同步到 Elasticsearch 时选 | Postgres | llms.txt: https://www.paradedb.com/llms.txt | 开源 |
| [Typesense](https://typesense.org) | 开源的内存型搜索引擎，容错、分面、地理与向量搜索，兼容 InstantSearch；想要 Algolia 式体验但自托管或用便宜的云版时选 | C++, Docker | `npm i typesense`<br>llms.txt: https://typesense.org/llms.txt | 开源 |

### 分析 / 监控 / 特性开关

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [PostHog](https://posthog.com) | 开源的一体化产品平台：事件分析、会话回放、特性开关、A/B 实验、错误追踪、问卷和 LLM 可观测性，免费额度大；想用一个 SDK 覆盖产品数据全链路时首选 | TS, Python | `npx -y @posthog/wizard@latest`<br>`npx @posthog/wizard mcp add`<br>llms.txt: https://posthog.com/llms.txt | 免费+付费 |
| ⭐ [Sentry](https://sentry.io) | 错误监控与性能追踪的事实标准，带会话回放、日志和 AI 根因分析（Seer），各语言 SDK 齐全；任何要上线的项目都该接一个，默认选它 | TS, Python, 移动端 | `npx @sentry/wizard@latest -i nextjs`<br>MCP https://mcp.sentry.dev/mcp<br>llms.txt: https://sentry.io/llms.txt | 免费+付费 |
| [Amplitude](https://amplitude.com) | 企业级产品分析与实验平台，行为分群和路径分析强；数据团队成熟、需要治理和大规模分析时选 | 多语言 | `npm i @amplitude/analytics-browser`<br>`claude mcp add --transport http --scope user Amplitude https://mcp.amplitude.com/mcp`<br>llms.txt: https://amplitude.com/llms.txt | 免费+付费 |
| [Axiom](https://axiom.co) | 按量计费的日志、事件与追踪存储，查询快、保留期长、接入 Vercel/Cloudflare 一键完成；Serverless 应用要便宜地存全量日志时选 | API, OTel | `npm i @axiomhq/js`<br>`claude mcp add --transport http --scope user axiom https://mcp.axiom.co/mcp`<br>llms.txt: https://axiom.co/llms.txt | 免费+付费 |
| [Better Stack](https://betterstack.com) | 可用性监控、状态页、值班告警和日志/追踪合一的平台；小团队想用一家服务搞定「挂了要有人知道」时选 | API | MCP https://mcp.betterstack.com | 免费+付费 |
| [Checkly](https://www.checklyhq.com) | 「监控即代码」平台：把 Playwright 脚本和 API 检查作为定时监控跑在全球节点；想复用 E2E 测试来监控线上关键流程时选 | TS, Playwright | `npm i checkly`<br>llms.txt: https://www.checklyhq.com/llms.txt | 免费+付费 |
| [Datadog](https://www.datadoghq.com) | 企业级全栈可观测平台（APM、基础设施、日志、RUM、LLM 观测）；规模大、服务多、需要统一看板和告警时选，⚠ 账单容易失控 | 多语言 | `npm i dd-trace`<br>MCP https://mcp.datadoghq.com/v1/mcp（US1 站点，其他站点见文档）<br>llms.txt: https://www.datadoghq.com/llms.txt | 付费 |
| [Flags SDK（Vercel）](https://flags-sdk.dev) | 开源的服务端特性开关 SDK，开关以函数定义，可接 Statsig/LaunchDarkly/PostHog 等任意提供方；Next.js/SvelteKit 里想无闪烁地在服务端判定开关时选 | Next.js, SvelteKit | `npm i flags`<br>llms.txt: https://flags-sdk.dev/llms.txt | 开源 |
| [Flagsmith](https://www.flagsmith.com) | 开源特性开关与远程配置服务，可自托管或私有云部署；需要把开关服务放在内网或国内环境时选 | 多语言, Docker | `npm i flagsmith`<br>llms.txt: https://www.flagsmith.com/llms.txt | 开源 |
| [Google Analytics 4](https://developers.google.com/analytics) | 免费的网站与应用流量分析，和 Google Ads、Search Console 打通；投放广告或需要与营销团队共用数据时选，⚠ 国内采集不稳定 | Script |  | 免费 |
| [Grafana](https://grafana.com) | 开源可视化与告警平台，配合 Prometheus/Loki/Tempo 构成完整的开源可观测栈，也有带免费档的 Grafana Cloud；想自建监控或基于 OpenTelemetry 时选 | Go, Docker | llms.txt: https://grafana.com/llms.txt | 开源 |
| [GrowthBook](https://www.growthbook.io) | 开源特性开关与 A/B 实验平台，可直接连自己的数据仓库算指标，可自托管；数据已在仓库里、不想把事件再发给第三方时选 | TS, 多语言 | `npm i @growthbook/growthbook-react`<br>`claude mcp add --transport http growthbook https://mcp.growthbook.io/mcp`<br>llms.txt: https://www.growthbook.io/llms.txt | 开源 |
| [LaunchDarkly](https://launchdarkly.com) | 企业级特性管理平台：精细定向、渐进发布、发布护栏与审计；大团队多服务协同发布、对治理要求高时选，⚠ 价格高 | 多语言 | `npm i @launchdarkly/node-server-sdk`<br>MCP https://mcp.launchdarkly.com/mcp<br>llms.txt: https://launchdarkly.com/docs/llms.txt | 免费+付费 |
| [LogRocket](https://logrocket.com) | 会话回放 + 前端错误与性能监控，可回看用户操作时的网络请求和状态；排查难复现的前端问题时选 | JS | `npm i logrocket`<br>llms.txt: https://docs.logrocket.com/llms.txt | 免费+付费 |
| [Microsoft Clarity](https://clarity.microsoft.com) | 完全免费的会话回放与热力图工具，不限流量；只想看用户怎么点、在哪卡住时选 | Script |  | 免费 |
| [Mixpanel](https://mixpanel.com) | 事件型产品分析工具，漏斗、留存、用户分群做得深；产品团队需要自助分析且不需要 PostHog 那样的全家桶时选 | 多语言 | `npm i mixpanel-browser`<br>`claude mcp add --transport http mixpanel https://mcp.mixpanel.com/mcp`<br>llms.txt: https://mixpanel.com/llms.txt | 免费+付费 |
| [OpenPanel](https://openpanel.dev) | 开源的 Mixpanel + Plausible 替代品，网站统计与产品事件分析合一，可自托管；想要比 PostHog 更轻的开源分析时选 | TS | `npm i @openpanel/sdk`<br>llms.txt: https://openpanel.dev/llms.txt | 开源 |
| [OpenStatus](https://www.openstatus.dev) | 开源的全球合成监控与状态页，可用代码定义检查；需要多地区探测 API 延迟并公开状态页时选 | TS | llms.txt: https://www.openstatus.dev/llms.txt | 开源 |
| [OpenTelemetry](https://opentelemetry.io) | CNCF 的可观测性开放标准：统一采集 traces、metrics、logs 并导出到任意后端；想避免被监控厂商锁定、或要给 LLM 调用打点时以它为底座 | 多语言 | `npm i @opentelemetry/api @opentelemetry/sdk-node`<br>llms.txt: https://opentelemetry.io/llms.txt | 开源 |
| [Plausible](https://plausible.io) | 轻量、无 Cookie、符合 GDPR 的网站统计，脚本不到 1KB，云版付费、社区版（AGPL）可自托管；只想看访问量和来源、不要复杂漏斗时选 | Script | `npm i @plausible-analytics/tracker` | 付费 |
| [SigNoz](https://signoz.io) | 基于 OpenTelemetry 和 ClickHouse 的开源 APM（追踪、指标、日志），可自托管；想要开源版 Datadog 时选 | OTel, ClickHouse | llms.txt: https://signoz.io/llms.txt | 开源 |
| [Statsig](https://statsig.com) | 特性开关 + 实验平台 + 产品分析一体，统计引擎强、免费额度高（已被 OpenAI 收购，仍独立运营）；要做严谨 A/B 实验和灰度发布时选 | TS, 多语言 | `npm i @statsig/react-bindings`<br>`claude mcp add --transport http statsig https://api.statsig.com/v3/mcp`<br>llms.txt: https://docs.statsig.com/llms.txt | 免费+付费 |
| [Umami](https://umami.is) | 可自托管的开源隐私友好网站统计，部署只需 Node + Postgres；想免费自托管、数据留在自己服务器（国内也可用）时选 | Next.js, Postgres | llms.txt: https://docs.umami.is/llms.txt | 开源 |
| [Unleash](https://www.getunleash.io) | 老牌开源特性开关平台，发布策略灵活、SDK 覆盖广；企业自托管特性开关的常见选择 | Node, Docker | `npm i unleash-client`<br>llms.txt: https://www.getunleash.io/llms.txt | 开源 |
| [Uptime Kuma](https://github.com/louislam/uptime-kuma) | 自托管的开源可用性监控与状态页，支持微信/钉钉/飞书等 90+ 通知渠道；想免费监控自己的服务是否在线时选 | Node, Docker |  | 开源 |
| [Vercel Web Analytics / Speed Insights](https://vercel.com/docs/analytics) | Vercel 自带的无 Cookie 访问统计和真实用户性能指标（Core Web Vitals）；项目部署在 Vercel、只要基础数据时一行代码搞定 | Next.js, Vercel | `npm i @vercel/analytics @vercel/speed-insights`<br>llms.txt: https://vercel.com/llms.txt | 免费+付费 |

### 国际化

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [next-intl](https://next-intl.dev) | Next.js App Router 的国际化库：ICU 消息、类型安全的 key、本地化路由，原生支持服务端组件；Next.js 项目的默认 i18n 方案 | Next.js, React | `npm i next-intl` | 开源 |
| [Crowdin](https://crowdin.com) | 老牌云端本地化管理平台，对接 GitHub、设计工具和 600+ 集成，开源项目免费；有专职译者或社区协作翻译时选 | SaaS, CLI |  | 免费+付费 |
| [FormatJS / react-intl](https://formatjs.github.io) | 基于 ICU MessageFormat 和 Intl 标准的国际化库集合，react-intl 是其 React 绑定；存量项目或需要严格遵循 ICU 规范时选 | React, JS | `npm i react-intl` | 开源 |
| [General Translation（gt-next）](https://generaltranslation.com) | 面向 React/Next.js 的 AI 国际化库，用 <T> 包住 JSX 即可整段翻译并在开发时热更新；想最少改动地给已有应用加多语言时选 | Next.js, React | `npm i gt-next`<br>llms.txt: https://generaltranslation.com/llms.txt | 免费+付费 |
| [i18next / react-i18next](https://www.i18next.com) | 生态最大的 JavaScript 国际化框架，插件覆盖语言检测、后端加载和各前端框架；非 Next.js 项目、React Native 或需要跨框架共用翻译时选 | JS, React, React Native | `npm i i18next react-i18next`<br>llms.txt: https://www.i18next.com/llms.txt | 开源 |
| [Intlayer](https://intlayer.org) | 把文案声明放在组件旁边的国际化方案，类型安全并带可视化编辑器和 AI 翻译；想按组件而非大 JSON 文件管理翻译时选 | Next.js, React, Vite | `npm i intlayer`<br>`claude mcp add intlayer npx -y @intlayer/mcp`<br>llms.txt: https://intlayer.org/llms.txt | 开源 |
| [Lingo.dev](https://lingo.dev) | 用 LLM 自动翻译的本地化工具链：CLI 批量翻译语言文件、CI 自动补翻、编译器在构建期翻译 React 应用；想把翻译流程完全自动化时选 | React, CLI | `npx lingo.dev@latest init`<br>`claude mcp add lingo --transport http https://mcp.lingo.dev/mcp --scope user`<br>llms.txt: https://lingo.dev/llms.txt | 免费+付费 |
| [Lingui](https://lingui.dev) | 基于宏的国际化库，直接在 JSX 里写原文、编译期抽取成 ICU/PO 目录，包体小；希望源码里保留可读文案并交给译者用 PO 流程时选 | React, TS | `npm i @lingui/core @lingui/react`<br>`npm i -D @lingui/cli`<br>llms.txt: https://lingui.dev/llms.txt | 开源 |
| [Paraglide JS（inlang）](https://paraglidejs.com) | 把翻译编译成可 tree-shake 的类型安全函数，只打包用到的文案；SvelteKit 官方推荐，对包体积敏感的项目选 | SvelteKit, Vite, TS | `npx @inlang/paraglide-js@latest init`<br>llms.txt: https://paraglidejs.com/llms.txt | 开源 |
| [Tolgee](https://tolgee.io) | 开源本地化平台：在页面上按住 Alt 点击即可原位翻译，带机器翻译、翻译记忆和截图上下文，可自托管；需要翻译管理后台而不只是一个库时选 | React, Vue, Docker | `npm i @tolgee/react`<br>llms.txt: https://tolgee.io/llms.txt | 开源 |
| [Vue I18n](https://vue-i18n.intlify.dev) | Vue 官方生态的国际化插件，Nuxt 里对应 @nuxtjs/i18n；Vue/Nuxt 项目的默认选择 | Vue, Nuxt | `npm i vue-i18n`<br>llms.txt: https://vue-i18n.intlify.dev/llms.txt | 开源 |

### 安全与限流

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Upstash Ratelimit](https://upstash.com/docs/redis/sdks/ratelimit-ts/overview) | 基于 Upstash Redis 的无连接限流库（固定窗口、滑动窗口、令牌桶），可在 Edge/Serverless 运行；给 API 路由和 AI 接口加限流的默认做法 | TS, Redis | `npm i @upstash/ratelimit`<br>llms.txt: https://upstash.com/llms.txt | 开源 |
| [Arcjet](https://arcjet.com) | 写在应用代码里的安全 SDK：限流、机器人识别、邮箱校验、敏感信息检测和 Shield WAF；想用几行代码给 Next.js/Node/Python 接口加一整套防护时选 | Next.js, Node, Python | `npm i @arcjet/next`<br>`claude mcp add arcjet --transport http https://api.arcjet.com/mcp`<br>llms.txt: https://arcjet.com/llms.txt | 免费+付费 |
| [Cloudflare Turnstile](https://developers.cloudflare.com/turnstile/) | 免费、无感知的人机验证，替代 reCAPTCHA；保护注册、登录和表单接口时选，⚠ 国内加载偶有失败，面向国内用户请用极验等 | Script | llms.txt: https://developers.cloudflare.com/turnstile/llms.txt | 免费 |
| [Doppler](https://www.doppler.com) | 托管的机密管理服务，把环境变量集中存放并同步到 Vercel/AWS/CI；想要开箱即用、不自托管的密钥管理时选 | CLI | `npx -y @dopplerhq/mcp-server`<br>llms.txt: https://docs.doppler.com/llms.txt | 免费+付费 |
| [Gitleaks](https://gitleaks.io) | 开源的 Git 仓库密钥泄露扫描器，可做 pre-commit 钩子和 CI 检查；防止把 API key 提交进仓库 | Go, CLI |  | 开源 |
| [hCaptcha](https://www.hcaptcha.com) | 注重隐私的人机验证服务，reCAPTCHA 的常见替代；Turnstile 不适用或需要企业级防刷时选 | Script | `npm i @hcaptcha/react-hcaptcha`<br>llms.txt: https://www.hcaptcha.com/llms.txt | 免费+付费 |
| [Hookdeck](https://hookdeck.com) | Webhook 接收网关：排队、重试、过滤、转发到本地开发环境；要可靠地接收 Stripe/GitHub 等第三方 webhook 时选 | API, CLI | `npm i -g hookdeck-cli`<br>llms.txt: https://hookdeck.com/llms.txt | 免费+付费 |
| [Infisical](https://infisical.com) | 开源密钥与机密管理平台：环境变量同步、密钥轮换、动态密钥和泄露扫描，可自托管；团队不想再用 .env 文件互传密钥时选 | CLI, Docker | llms.txt: https://infisical.com/llms.txt | 开源 |
| [Permit.io](https://www.permit.io) | 授权即服务：用界面和 API 管理 RBAC/ABAC/ReBAC 策略，底层基于 OPA/Cedar；不想在业务代码里手写权限判断时选 | API, 多语言 | `npm i permitio`<br>llms.txt: https://www.permit.io/llms.txt | 免费+付费 |
| [Semgrep](https://semgrep.dev) | 开源静态代码扫描（SAST），规则像代码一样好写，另有依赖和密钥扫描；想在 CI 或 Agent 写完代码后自动查安全问题时选 | 多语言, CLI | `pip install semgrep`<br>llms.txt: https://semgrep.dev/llms.txt | 免费+付费 |
| [Socket](https://socket.dev) | 依赖供应链安全工具：在安装和 PR 阶段检测恶意包、安装脚本和可疑行为；Agent 会自动装依赖的项目尤其该接 | npm, PyPI | `npm i -g socket`<br>MCP https://mcp.socket.dev/<br>llms.txt: https://socket.dev/llms.txt | 免费+付费 |
| [Svix](https://www.svix.com) | Webhook 发送即服务：签名、重试、投递日志和给客户的自助门户；自己的产品要向客户推送 webhook 时选，接收端可用其开源校验库 | API, 多语言 | `npm i svix`<br>llms.txt: https://www.svix.com/llms.txt | 免费+付费 |
| [Unkey](https://www.unkey.com) | 开源的 API 密钥管理与限流平台：签发、校验、配额、按密钥统计用量；要对外开放 API 并按 key 计量时选 | TS, API | `npm i @unkey/api`<br>`claude mcp add --transport http unkey-docs "https://www.unkey.com/docs/mcp"`<br>llms.txt: https://www.unkey.com/llms.txt | 免费+付费 |
| [Zuplo](https://zuplo.com) | 可编程的边缘 API 网关：密钥认证、限流、开发者门户和 MCP 服务器托管；要把内部 API 包装成对外产品时选 | TS, OpenAPI | llms.txt: https://zuplo.com/llms.txt | 免费+付费 |

### 国内可用替代

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [腾讯云开发 CloudBase](https://tcb.cloud.tencent.com) | 腾讯云的一体化 Serverless 后端：云函数、云数据库（文档型 + MySQL）、云存储、静态托管、身份认证，原生支持微信小程序；做小程序或面向国内用户的全栈应用时首选，官方提供 MCP 让 Agent 直接部署 | 小程序, Node, React | `npm i @cloudbase/js-sdk`<br>`npx @cloudbase/cloudbase-mcp@latest` | 免费+付费 |
| [1Panel](https://1panel.cn) | 飞致云开源的 Linux 服务器运维面板：容器管理、建站、数据库、证书和应用商店一键装；在国内云服务器上自托管应用时比手敲命令省事 | Docker, Linux | llms.txt: https://1panel.cn/llms.txt | 开源 |
| [Authing](https://www.authing.cn) | 国内的身份云（IDaaS）：支持微信、企业微信、钉钉、飞书扫码登录以及短信登录、SSO 和多因素认证；面向国内用户且不想自建认证时选 | Node, React | `npm i authing-node-sdk` | 免费+付费 |
| [Laf](https://laf.dev) | Sealos 团队开源的云开发平台：在线写云函数，内置数据库和对象存储，可私有化部署；想要国内可用、能自托管的函数式后端时选 | Node, MongoDB |  | 开源 |
| [MemFire Cloud](https://cloud.memfiredb.com) | 国内版 Supabase：托管 Postgres、认证（微信/手机号登录）、存储、实时和云函数，接口与 supabase-js 兼容；想用 Supabase 开发体验但服务器要在国内时选 | Postgres, supabase-js |  | 免费+付费 |
| [Sealos](https://sealos.run) | 基于 Kubernetes 的国产开源云操作系统，提供云开发环境 DevBox、一键数据库、应用托管和对象存储，国内节点可直连；想在国内低成本部署容器化应用时选 | K8s, Docker |  | 免费+付费 |
| [Zeabur](https://zeabur.com) | 华人团队做的一键部署平台，自动识别框架，可选香港/东京等亚洲节点，也能托管到自己的服务器；想要 Railway 式体验且国内访问较好时选 | Docker, Node, Python | `npx @zeabur/mcp-server` | 免费+付费 |
| [七牛云 Kodo](https://www.qiniu.com/products/kodo) | 老牌国内对象存储与 CDN，有免费额度，图片与音视频处理能力成熟；个人或小团队项目存图床、音视频时选 | S3 API | `npm i qiniu`<br>llms.txt: https://www.qiniu.com/llms.txt | 免费+付费 |
| [声网 Agora](https://www.shengwang.cn) | 国内领先的实时音视频（RTC）云服务，另有对话式 AI 引擎；做语音房、视频通话、直播连麦且用户在国内时选 | Web, iOS, Android | `npm i agora-rtc-sdk-ng` | 免费+付费 |
| [微信支付](https://pay.weixin.qq.com/doc/v3/merchant/4012062524) | 国内移动支付必接渠道：JSAPI、小程序、Native 扫码、H5、App 支付；面向国内用户收款时用，⚠ 需企业或个体工商户主体 | API v3 |  | 付费 |
| [支付宝开放平台](https://open.alipay.com) | 支付宝的支付与小程序开放能力：当面付、手机网站、电脑网站、App 支付，官方提供支付 MCP Server；面向国内用户收款时与微信支付搭配接入，⚠ 需签约主体 | API | `npm i alipay-sdk`<br>`npx -y @alipay/mcp-server-alipay`（需配置商户应用密钥） | 付费 |
| [极光推送 JPush](https://www.jiguang.cn/push) | 国内移动推送服务，整合华为/小米/OPPO/vivo 等厂商通道；国内安卓应用要保证推送到达率时选 | Android, iOS, React Native |  | 免费+付费 |
| [极验 GeeTest](https://www.geetest.com) | 国内主流的行为式验证码服务；面向国内用户防刷注册和短信轰炸时选（reCAPTCHA/Turnstile 在国内不稳定） | Script, API | llms.txt: https://www.geetest.com/llms.txt | 付费 |
| [百度统计](https://tongji.baidu.com) | 国内免费网站流量统计，与百度搜索推广打通；面向国内用户的站点替代 Google Analytics | Script |  | 免费 |
| [腾讯云 EdgeOne Pages](https://pages.edgeone.ai) | 腾讯云的边缘全栈部署平台（静态站点 + 边缘函数 + KV），国内外均有节点，对标 Cloudflare Pages/Vercel；前端项目要兼顾国内访问速度时选，⚠ 国内加速需备案域名 | Next.js, Astro, Vite | `npm i -g edgeone`<br>`npx @edgeone/makers-mcp@latest`<br>llms.txt: https://pages.edgeone.ai/llms.txt | 免费+付费 |
| [腾讯云对象存储 COS](https://cloud.tencent.com/product/cos) | 腾讯云对象存储，与数据万象（图片/视频处理）、CDN 和小程序生态打通；业务在腾讯云或微信生态时选 | S3 API | `npm i cos-nodejs-sdk-v5` | 付费 |
| [阿里云 ESA 函数和 Pages](https://www.aliyun.com/product/esa) | 阿里云边缘安全加速 ESA 提供的边缘函数与 Pages 托管，带边缘 KV 存储；已用阿里云、想把前端部署到国内边缘节点时选，⚠ 国内节点需备案 | Static, Edge |  | 免费+付费 |
| [阿里云函数计算 FC](https://www.aliyun.com/product/fc) | 阿里云的 Serverless 计算，支持事件函数、Web 函数和 GPU 实例，配合 Serverless Devs 部署；需要国内节点的 Serverless 后端或 AI 推理服务时选，⚠ 绑定域名需备案 | Node, Python, Docker | `npm i -g @serverless-devs/s` | 免费+付费 |
| [阿里云对象存储 OSS](https://www.aliyun.com/product/oss) | 国内使用最广的对象存储，带图片处理、CDN 回源和 S3 兼容接口；面向国内用户存文件和图片时选 | S3 API | `npm i ali-oss` | 付费 |
| [阿里云短信服务](https://www.aliyun.com/product/sms) | 国内短信验证码与通知短信通道，到达率高；国内手机号登录、验证码场景用，⚠ 需企业认证并报备签名和模板 | API | `npm i @alicloud/dysmsapi20170525` | 付费 |
| [高德开放平台](https://lbs.amap.com) | 国内地图、定位、路线规划与地点搜索 API，官方提供 MCP Server；应用里需要国内地图或让 Agent 查地点路线时选（Google Maps/Mapbox 国内不可用） | JS API, Android, iOS | MCP https://mcp.amap.com/mcp?key=&lt;高德 Key&gt;<br>`npx -y @amap/amap-maps-mcp-server` | 免费+付费 |

<a id="stack-content"></a>

## 文档站 / 博客 / CMS

本类分组：文档站 · API 文档 · 内容层与 MDX · Headless CMS · 博客与发布

### 文档站

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Fumadocs](https://fumadocs.dev) | 基于 Next.js App Router 的文档框架，UI 精致、内置搜索、OpenAPI 页面和 llms.txt 生成，也支持 TanStack Start/React Router；文档要和 Next.js 应用放同一仓库并深度定制时首选 | Next.js, MDX | `npm create fumadocs-app`<br>llms.txt: https://fumadocs.dev/llms.txt | 开源 |
| [Docsify](https://docsify.js.org) | 无需构建、运行时渲染 Markdown 的文档站生成器，一个 index.html 即可；只想把一堆 Markdown 快速变成网站时选，⚠ SEO 较弱 | JS, Markdown | `npm i -g docsify-cli` | 开源 |
| [Docus](https://docus.dev) | 基于 Nuxt Content 和 Nuxt UI 的文档主题，内置 llms.txt 与 MCP 支持；Nuxt/Vue 技术栈写文档时选 | Nuxt, Vue | `npx create-docus my-docs`<br>llms.txt: https://docus.dev/llms.txt | 开源 |
| [Docusaurus](https://docusaurus.io) | Meta 开源的 React 文档站生成器，版本化文档、国际化和插件生态最成熟；大型开源项目需要多版本文档时选 | React, MDX | `npx create-docusaurus@latest my-website classic` | 开源 |
| [GitBook](https://www.gitbook.com) | 所见即所得的托管文档与知识库，支持 Git 同步、AI 搜索并自动提供 llms.txt 和 MCP；非工程师也要一起写文档时选 | SaaS | llms.txt: https://www.gitbook.com/llms.txt | 免费+付费 |
| [Inkeep](https://inkeep.com) | 面向文档与客服的 AI 问答与 Agent 平台，可嵌入文档站搜索框、Slack 和客服系统；想给文档加带引用的 AI 问答时选 | SaaS, React | llms.txt: https://inkeep.com/llms.txt | 付费 |
| [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) | Python 生态最流行的文档主题，YAML 配置 + Markdown 即可出专业文档站；Python 项目或不想碰前端工具链时选 | Python, Markdown | `pip install mkdocs-material` | 开源 |
| [Mintlify](https://www.mintlify.com) | 托管式文档平台：MDX + Git 同步、API Playground、AI 问答，并为每个站点自动生成 llms.txt 和 MCP 服务器；想要最省心、最好看的对外开发者文档且接受付费时选 | MDX, SaaS | `npm i -g mint`<br>`claude mcp add --transport http Mintlify https://mintlify.com/docs/mcp`<br>llms.txt: https://www.mintlify.com/llms.txt | 免费+付费 |
| [Nextra](https://nextra.site) | 基于 Next.js 的 MDX 站点生成器，带文档和博客主题；想用最少配置在 Next.js 里起一个文档站时选 | Next.js, MDX | `npm i next react react-dom nextra nextra-theme-docs` | 开源 |
| [Rspress](https://rspress.rs) | 字节跳动开源、基于 Rspack 的静态站点生成器，构建快、MDX 支持好，有中文文档；Rspack 生态或需要大型文档站快速构建时选 | React, Rspack | `npm create rspress@latest`<br>llms.txt: https://rspress.rs/llms.txt | 开源 |
| [Starlight](https://starlight.astro.build) | Astro 官方文档主题：默认零 JS、自带 Pagefind 搜索、国际化和侧边栏，性能极好；想要一个快速、框架无关的纯文档站时选 | Astro, MDX | `npm create astro@latest -- --template starlight`<br>`claude mcp add --transport http astro-docs https://mcp.docs.astro.build/mcp` | 开源 |
| [VitePress](https://vitepress.dev) | Vite + Vue 驱动的静态文档生成器，启动和热更新极快，中文社区使用广；Vue 生态项目或想要极简 Markdown 文档站时选 | Vue, Vite | `npm add -D vitepress`<br>`npx vitepress init`<br>llms.txt: https://vitepress.dev/llms.txt | 开源 |
| [Vocs](https://vocs.dev) | wevm 团队出的 React + Vite 极简文档框架，viem/wagmi 文档同款；想要轻量、好看的库文档站时选 | React, Vite | `npm i vocs`<br>llms.txt: https://vocs.dev/llms.txt | 开源 |
| [Zensical](https://zensical.org) | Material for MkDocs 原班团队的新一代静态站点生成器（Rust 内核），兼容现有 mkdocs.yml 项目；新建 Python 系文档站或从 MkDocs 迁移时选，⚠ 仍较新 | Python, Rust | `pip install zensical`<br>llms.txt: https://zensical.org/docs/llms.txt | 开源 |

### API 文档

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Scalar](https://scalar.com) | 开源的 OpenAPI 文档与 API 客户端，界面现代、可直接发请求，Hono/FastAPI/NestJS/.NET 等都有官方集成；给后端自动生成交互式 API 文档时首选 | OpenAPI, 多框架 | `npm i @scalar/api-reference`<br>llms.txt: https://scalar.com/llms.txt | 开源 |
| [Apifox](https://apifox.com) | 国产的 API 设计、调试、Mock、自动化测试与文档一体化平台，中文界面，官方提供 MCP Server 让 Agent 读取接口文档；国内团队协作管理接口时选 | Desktop, SaaS |  | 免费+付费 |
| [Bruno](https://www.usebruno.com) | 开源、离线优先的 API 调试客户端，请求集合以纯文本存在 Git 仓库里；想替代 Postman 并让接口用例跟代码一起版本管理时选 | Desktop, CLI | `npm i -g @usebruno/cli`<br>llms.txt: https://docs.usebruno.com/llms.txt | 开源 |
| [Fumadocs OpenAPI](https://fumadocs.dev/docs/integrations/openapi) | Fumadocs 的 OpenAPI 集成：从规范文件生成 MDX 页面和可交互 Playground；文档站已用 Fumadocs、想把 API 参考放在同一站点时选 | Next.js, OpenAPI | `npm i fumadocs-openapi`<br>llms.txt: https://fumadocs.dev/llms.txt | 开源 |
| [Redoc](https://redocly.com/redoc) | 老牌的三栏式 OpenAPI 文档渲染器，单个 HTML 即可部署；只需要把 OpenAPI 文件变成只读参考文档时选 | OpenAPI, React | `npx @redocly/cli build-docs openapi.yaml`<br>llms.txt: https://redocly.com/llms.txt | 开源 |
| [Speakeasy](https://www.speakeasy.com) | OpenAPI 驱动的 SDK、Terraform Provider 和 MCP 服务器生成器，带 CLI 与 CI 工作流；想把 API 自动产出类型安全 SDK 和 Agent 工具时选 | OpenAPI, CLI | llms.txt: https://www.speakeasy.com/llms.txt | 免费+付费 |
| [Stainless](https://www.stainless.com) | 从 OpenAPI 规范生成高质量多语言 SDK、文档和 MCP 服务器的平台（OpenAI、Anthropic 的 SDK 同款）；要对外发布官方 SDK 时选 | OpenAPI, SaaS |  | 免费+付费 |
| [Swagger UI](https://swagger.io/tools/swagger-ui/) | 最广为人知的 OpenAPI 交互式文档界面，多数后端框架默认集成；团队已习惯 Swagger 或框架自带时直接用 | OpenAPI | `npm i swagger-ui-dist` | 开源 |
| [TypeSpec](https://typespec.io) | 微软开源的 API 描述语言，用类似 TypeScript 的语法定义接口再生成 OpenAPI、JSON Schema、客户端和服务端桩；API 规模大、想先设计再实现时选 | TS, OpenAPI | `npm i -g @typespec/compiler`<br>llms.txt: https://typespec.io/docs/llms.txt | 开源 |

### 内容层与 MDX

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Content Collections](https://www.content-collections.dev) | 把 Markdown/MDX 等本地内容转成带校验的类型安全数据集合，适配 Next.js、Vite、Remix 等；Contentlayer 停更后的首选替代 | Next.js, Vite, TS | `npm i @content-collections/core @content-collections/next -D` | 开源 |
| [Markdoc](https://markdoc.dev) | Stripe 开源的 Markdown 扩展与内容创作框架，用标签语法代替任意 JSX，内容可静态校验；作者不是工程师、需要约束内容结构时选 | JS, React | `npm i @markdoc/markdoc` | 开源 |
| [MDX](https://mdxjs.com) | 在 Markdown 里写 JSX 组件的格式与编译器，几乎所有文档/博客框架的底层；内容里需要嵌交互组件时用 | React, Markdown | `npm i @mdx-js/mdx` | 开源 |
| [next-mdx-remote](https://github.com/hashicorp/next-mdx-remote) | 在 Next.js 里渲染来自数据库或 CMS 的远程 MDX 字符串；MDX 内容不在本地文件系统时选 | Next.js | `npm i next-mdx-remote` | 开源 |
| [Notion API（当 CMS 用）](https://developers.notion.com) | 把 Notion 数据库当内容后台，通过官方 API 或 Notion MCP 读取页面；内容作者已习惯 Notion、站点内容量不大时选，⚠ 有速率限制，需缓存 | API, TS | `npm i @notionhq/client`<br>`claude mcp add --transport http notion https://mcp.notion.com/mcp`<br>llms.txt: https://developers.notion.com/llms.txt | 免费+付费 |
| [Nuxt Content](https://content.nuxt.com) | Nuxt 的基于文件的内容层：Markdown/YAML/JSON 进 SQL 可查询集合，MDC 语法可在 Markdown 里用 Vue 组件；Nuxt 项目做博客和文档时选 | Nuxt, Vue | `npx nuxt module add content`<br>llms.txt: https://content.nuxt.com/llms.txt | 开源 |
| [react-markdown](https://github.com/remarkjs/react-markdown) | 把 Markdown 字符串安全渲染成 React 组件，支持 remark/rehype 插件；渲染用户输入或 LLM 输出的 Markdown 时选 | React | `npm i react-markdown` | 开源 |
| [Shiki](https://shiki.style) | 使用 VS Code 语法与主题的代码高亮器，构建期输出带样式 HTML、零运行时；文档和博客里的代码块高亮默认选它 | JS | `npm i shiki` | 开源 |
| [Streamdown](https://streamdown.ai) | Vercel 出的流式 Markdown 渲染组件，能正确处理未闭合的语法块，内置代码高亮、数学公式和 Mermaid；渲染 AI 流式输出时替代 react-markdown | React, Tailwind | `npm i streamdown`<br>llms.txt: https://streamdown.ai/llms.txt | 开源 |
| [unified（remark / rehype）](https://unifiedjs.com) | Markdown/HTML 的语法树处理生态：remark 解析 Markdown、rehype 处理 HTML，上千插件；要自定义 Markdown 渲染管线（目录、代码高亮、数学公式）时用 | JS | `npm i unified remark-parse remark-rehype rehype-stringify` | 开源 |
| [Velite](https://velite.js.org) | 用 Zod schema 把 Markdown/MDX、YAML、JSON 构建成类型安全的数据层，框架无关；想要更轻、配置更自由的 Contentlayer 替代时选 | TS, Zod | `npm i velite` | 开源 |

### Headless CMS

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Sanity](https://www.sanity.io) | 结构化内容平台：schema 即代码、可定制的 Studio、实时协作、GROQ 查询和可视化编辑；内容模型复杂、需要编辑体验和开发灵活性兼得时首选 | React, Next.js | `npm create sanity@latest`<br>`npx sanity@latest mcp configure`<br>llms.txt: https://www.sanity.io/llms.txt | 免费+付费 |
| [BaseHub](https://basehub.com) | 为 Next.js 设计的 AI 原生 Headless CMS，内容像代码一样有分支和提交，类型安全 SDK；营销站和文档内容想要 Git 式工作流又要托管编辑器时选 | Next.js, React | `npm i basehub`<br>llms.txt: https://basehub.com/docs/llms.txt | 免费+付费 |
| [Contentful](https://www.contentful.com) | 企业级托管 Headless CMS，内容建模、多语言、工作流和 CDN API 成熟；大型营销团队和多渠道内容分发选，⚠ 价格高 | API, GraphQL | `npm i contentful`<br>`claude mcp add --transport http contentful https://mcp.contentful.com/mcp` | 免费+付费 |
| [Decap CMS](https://decapcms.org) | 原 Netlify CMS：一个单页应用加配置文件即可给任意静态站点加上 Git 编辑后台；最轻量的 Git CMS，老牌静态站点常用 | Static, React | `npm i decap-cms-app`<br>llms.txt: https://decapcms.org/llms.txt | 开源 |
| [Directus](https://directus.com) | 给任意 SQL 数据库套上即时 REST/GraphQL API 和管理后台的开源数据平台，内置 MCP 服务器；已有数据库、想直接获得后台和接口时选 | Node, Vue, SQL | `npm init directus-project@latest`<br>`claude mcp add --transport http directus https://your-directus-url.com/mcp`<br>llms.txt: https://directus.com/llms.txt | 开源 |
| [EmDash](https://emdashcms.com) | Cloudflare 开源的 TypeScript CMS，定位「WordPress 的精神续作」，基于 Astro 并运行在 Workers 上，插件沙箱隔离；想要 Serverless、AI 原生的 WordPress 式建站时可试，⚠ 仍处早期预览 | Astro, Cloudflare | llms.txt: https://docs.emdashcms.com/llms.txt | 开源 |
| [Ghost](https://ghost.org) | 开源的博客与付费订阅发布平台，内置会员、邮件通讯和付费墙；做独立媒体、Newsletter 或公司博客时选 | Node | `npm install ghost-cli@latest -g`<br>llms.txt: https://ghost.org/docs/llms.txt | 开源 |
| [Hygraph](https://hygraph.com) | GraphQL 原生的托管 Headless CMS，支持内容联邦（把外部 API 拼进同一图）；前端以 GraphQL 为主、需要聚合多数据源时选 | GraphQL | llms.txt: https://hygraph.com/llms.txt | 免费+付费 |
| [Keystatic](https://keystatic.com) | 基于 Git 的 CMS：内容以 Markdown/YAML/JSON 存在仓库里，提供可视化编辑界面，无需数据库；Astro/Next.js 内容站想让非技术同事编辑时选 | Astro, Next.js | `npm create @keystatic@latest` | 开源 |
| [Prismic](https://prismic.io) | 以 Slice（页面区块）为核心的 Headless 页面搭建器，与 Next.js/Nuxt/SvelteKit 集成紧密；营销站要让编辑自己拼页面时选 | Next.js, Nuxt | `npm i @prismicio/client`<br>llms.txt: https://prismic.io/llms.txt | 免费+付费 |
| [Storyblok](https://www.storyblok.com) | 带可视化编辑器的组件化 Headless CMS，营销人员可在真实页面预览上拖拽区块；落地页由市场团队维护时选 | API, React, Vue | `npm i @storyblok/react`<br>llms.txt: https://www.storyblok.com/llms.txt | 免费+付费 |
| [Strapi](https://strapi.io) | 最流行的开源 Node.js Headless CMS，可视化建模并自动生成 REST/GraphQL 接口，可自托管；想要自己掌控数据的传统 CMS 后台时选 | Node, React | `npx create-strapi@latest`<br>llms.txt: https://docs.strapi.io/llms.txt | 开源 |
| [TinaCMS](https://tina.io) | 开源的 Git 驱动 CMS，在页面上所见即所得地编辑 Markdown/MDX，内容提交回仓库；需要可视化实时预览编辑时选 | Next.js, React | `npx create-tina-app@latest`<br>llms.txt: https://tina.io/llms.txt | 开源 |
| [WordPress](https://wordpress.org) | 全球使用最广的开源 CMS，主题和插件生态庞大，也可通过 REST/GraphQL 当 Headless 用；内容团队已熟悉 WordPress 或需要现成插件时选 | PHP, MySQL | llms.txt: https://wordpress.org/llms.txt | 开源 |

### 博客与发布

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [Buttondown](https://buttondown.com) | 面向开发者的 Newsletter 工具，支持 Markdown、API、自定义域名和付费订阅；想用代码友好的方式发邮件通讯时选 | SaaS, API | llms.txt: https://buttondown.com/llms.txt | 免费+付费 |
| [Changesets](https://github.com/changesets/changesets) | 面向 monorepo 的版本管理与 changelog 生成工具，贡献者随 PR 提交变更说明，发版时自动汇总；发布 npm 包时的默认方案 | Node | `npm install @changesets/cli -D && npx changeset init` | 开源 |
| [Eleventy（11ty）](https://www.11ty.dev) | 简单灵活的 JavaScript 静态站点生成器，模板语言自由、默认零客户端 JS；想完全掌控输出 HTML 的小型内容站选 | Node | `npm i @11ty/eleventy` | 开源 |
| [feed](https://github.com/jpmonette/feed) | 生成 RSS 2.0、Atom 和 JSON Feed 的 TypeScript 库；自建博客需要输出订阅源时用 | TS | `npm i feed` | 开源 |
| [git-cliff](https://git-cliff.org) | Rust 写的可高度定制的 changelog 生成器，按 Conventional Commits 或正则解析提交历史；只想从 Git 历史生成一份漂亮的 CHANGELOG 时选 | Rust, CLI | `npx git-cliff@latest` | 开源 |
| [Halo](https://www.halo.run) | 国产开源建站与博客系统（Java），带后台、主题和插件市场，中文文档完善；想要带管理后台、可自托管的中文博客/官网时选 | Java, Docker | llms.txt: https://www.halo.run/llms.txt | 开源 |
| [Hexo](https://hexo.io) | 中文社区最流行的 Node.js 静态博客框架，主题（NexT、Butterfly 等）和中文教程极多；想照着中文教程快速搭个人博客时选 | Node, Markdown | `npm install -g hexo-cli` | 开源 |
| [Hugo](https://gohugo.io) | Go 写的静态站点生成器，构建速度最快、单二进制无依赖，主题丰富；内容量很大的博客或不想引入 Node 工具链时选 | Go, Markdown |  | 开源 |
| [Openchangelog](https://openchangelog.com) | 开源的产品更新日志页：从 GitHub 仓库或本地 Markdown 渲染成可订阅的 changelog 站点；想给用户一个公开的「更新记录」页面时选 | Go, Markdown |  | 开源 |
| [release-please](https://github.com/googleapis/release-please) | Google 的发版自动化：根据 Conventional Commits 自动开发布 PR、更新 CHANGELOG 并打 tag；想让版本号和更新日志全自动时选 | GitHub Actions |  | 开源 |
| [Satori / next/og](https://github.com/vercel/satori) | 把 JSX + CSS 渲染成 SVG/PNG 的库，Next.js 的 ImageResponse 即基于它；给博客文章和分享链接动态生成社交卡片（OG 图）时用 | React, Edge | `npm i satori` | 开源 |
