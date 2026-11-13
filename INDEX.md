# 资源总索引（自动生成）

共 2528 条资源，49 个分类。点击进入对应分类。
也可以用 `python3 scripts/find.py <关键词>` 搜索，或 `python3 scripts/find.py --list` 列出分类 id。

## 入口与手写指南

- [AGENTS.md](AGENTS.md) — AI 入口：需求 → 文件 路由表与使用规则（先读这个）
- [MASTER_PROMPT.md](MASTER_PROMPT.md) — 可直接粘贴进任何 AI 的总提示词
- [ui/SKILL.md](ui/SKILL.md) — UI 工作流程：选型决策表、MCP、shadcn 命名空间用法、自检清单
- [ui/prompts/effect-vocabulary.md](ui/prompts/effect-vocabulary.md) — 100+ 个动效/特效/镜头/摄影专业名称速查表
- [ui/prompts/style-recipes.md](ui/prompts/style-recipes.md) — 11 种视觉风格配方：特征、推荐库、安装命令、避坑
- [ui/prompts/request-template.md](ui/prompts/request-template.md) — UI 需求描述模板
- [skills/README.md](skills/README.md) — Agent Skills 安装方式与起步包
- [tools/README.md](tools/README.md) — MediaCrawler 等开源工具用法
- [scaffolds/README.md](scaffolds/README.md) — 脚手架快速选型表与已失效项目
- [PICKS.md](PICKS.md) — 全部 ⭐ 精选，一页看完（自动生成）

## ui/

- [聚合站与目录（先从这里找）](ui/catalog/01-aggregators.md#ui-aggregators) — 20 条
- [基础 / 无头组件库](ui/catalog/02-component-libraries.md#ui-core) — 36 条
- [动画与稀有特效组件](ui/catalog/03-animated-components.md#ui-animated) — 35 条
- [风格化主题（手绘 / 复古 / 像素 / 新粗野 / 玻璃）](ui/catalog/04-stylized-themes.md#ui-stylized) — 28 条
- [移动端 / React Native](ui/catalog/05-mobile.md#ui-mobile) — 12 条
- [原生与跨端（Flutter / SwiftUI / Compose / 桌面）以及 RN 基础库](ui/catalog/05-mobile.md#ui-native) — 68 条
- [物理、液体、3D 与 Shader](ui/catalog/06-effects-3d-shaders.md#ui-effects) — 10 条
- [AI 产品 UI（聊天 / Agent / 可观测性）](ui/catalog/07-ai-product-ui.md#ui-ai-product) — 17 条
- [动画引擎 / 滚动 / 3D 底层库](ui/catalog/08-animation-engines.md#ui-animation-engines) — 14 条
- [动效 / 特效词汇与可复制 Prompt](ui/catalog/09-design-vocabulary.md#ui-vocabulary) — 45 条
- [设计风格 / 审美类 Skill 与 DESIGN.md](ui/catalog/09-design-vocabulary.md#ui-design-skills) — 42 条
- [官方 Prompt 指南（v0 / Lovable / Bolt / Stitch / Claude）](ui/catalog/09-design-vocabulary.md#ui-prompt-guides) — 7 条
- [镜头 / 摄影 / 灯光词汇（图像与视频生成）](ui/catalog/09-design-vocabulary.md#ui-camera-photo) — 7 条
- [灵感画廊（带 MCP 的优先）](ui/catalog/10-inspiration.md#ui-inspiration) — 93 条
- [图标、字体、配色、主题生成](ui/catalog/11-assets.md#ui-assets) — 124 条
- [插画、3D、图片视频、样机、背景生成器、音效](ui/catalog/11-assets.md#ui-media-assets) — 167 条
- [UI 相关 MCP 服务器](ui/catalog/12-mcp-registries-llms.md#ui-mcp) — 19 条
- [shadcn 命名空间 Registry](ui/catalog/12-mcp-registries-llms.md#ui-registries) — 2 条
- [shadcn 官方 Registry 索引（全量）](ui/catalog/18-shadcn-registries.md) — 548 个命名空间
- [llms.txt（喂给 AI 的官方文档）](ui/catalog/12-mcp-registries-llms.md#ui-llms-txt) — 18 条
- [其他框架组件库（Vue / Svelte / Angular / Solid / Web Components）](ui/catalog/13-other-frameworks.md#ui-frameworks-other) — 48 条
- [CSS 框架与纯 HTML / Tailwind 组件](ui/catalog/13-other-frameworks.md#ui-css-kits) — 30 条
- [国内生态（Ant Design / Element / TDesign / 小程序 / AntV…）](ui/catalog/14-china-ecosystem.md#ui-china) — 126 条
- [大厂设计系统与官方实现](ui/catalog/15-design-systems.md#ui-design-systems) — 55 条
- [功能型组件](ui/catalog/16-functional-components.md#ui-functional) — 200 条
- [模板、区块、UI Kit](ui/catalog/17-templates-blocks.md#ui-templates) — 65 条

## skills/

- [Skill 目录站与 Awesome 列表](skills/catalog.md#skills-directories) — 6 条
- [全球累计安装量 Top（skills.sh All Time，2026-11-09 实时数据）](skills/catalog.md#skills-top) — 15 条
- [工程 / 工作流类 Skill](skills/catalog.md#skills-engineering) — 54 条
- [前端 / 设计 / 动效类 Skill](skills/catalog.md#skills-ui) — 14 条
- [视频 / 多媒体类 Skill](skills/catalog.md#skills-media) — 8 条
- [其他领域 Skill（写作 / 调研 / 数据 / 文档 / 运维 / 安全 / 产品）](skills/catalog.md#skills-more) — 40 条
- [本文件夹自带的 Skill](skills/catalog.md#skills-local) — 2 条
- [规则 / Prompt / 子 Agent / 规格驱动工作流](skills/02-rules-prompts.md#rules-prompts) — 80 条

## tools/

- [数据采集 / 爬虫](tools/catalog.md#tools-crawl) — 3 条
- [浏览器自动化（给 Agent 用）](tools/catalog.md#tools-browser) — 2 条
- [MCP 目录站](tools/02-mcp.md#mcp-directories) — 22 条
- [常用 MCP 服务器](tools/02-mcp.md#mcp-servers) — 125 条
- [AI 编码 Agent、IDE 与应用生成器](tools/03-ai-builders.md#tools-ai-builders) — 82 条

## scaffolds/

- [全栈 Web Starter](scaffolds/01-starters.md#scaffold-web) — 21 条
- [移动端 / 桌面端 Starter](scaffolds/01-starters.md#scaffold-mobile) — 6 条
- [后端 / API Starter](scaffolds/01-starters.md#scaffold-backend) — 6 条
- [AI 应用 Starter 与 Agent 框架](scaffolds/02-ai-agents.md#scaffold-ai) — 16 条
- [MCP Server 开发模板](scaffolds/02-ai-agents.md#scaffold-mcp) — 4 条
- [架构 / 系统设计参考](scaffolds/03-architecture.md#scaffold-arch) — 17 条
- [服务与基础设施（认证 / 数据库 / 支付 / 邮件 / 部署…）](scaffolds/05-services.md#stack-services) — 219 条
- [文档站 / 博客 / CMS](scaffolds/05-services.md#stack-content) — 59 条
- [AI 基础设施（模型网关 / 向量库 / 评测 / 沙箱 / 语音 / 生成 API）](scaffolds/06-ai-infra.md#stack-ai) — 182 条
- [常用库（状态 / 请求 / 校验 / 测试 / 工具链 / Python）](scaffolds/07-common-libs.md#stack-libs) — 171 条
- [Awesome 元列表 / Prompt 合集](scaffolds/04-awesome-lists.md#meta-lists) — 91 条
