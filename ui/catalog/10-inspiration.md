# 设计灵感画廊

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="ui-inspiration"></a>

## 灵感画廊（带 MCP 的优先）

找参考图、截图给 AI 看。Mobbin / Refero / Lazyweb 有 MCP，Agent 可直接检索（都需要账号，Mobbin 和 Refero 要付费套餐）。

| 名称 | 是什么 / 什么时候用 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|
| ⭐ [Mobbin](https://mobbin.com) | 60 万+ 真实 App/Web 截图、流程、页面区块 | `claude mcp add --transport http mobbin https://api.mobbin.com/mcp` | 付费 |
| ⭐ [Refero](https://refero.design) | 12.5 万+ Web/iOS 截图、8000+ 流程；配套 refero_skill 做「先调研再设计」 | `claude mcp add --transport http refero https://api.refero.design/mcp` | 付费 |
| [Awwwards](https://www.awwwards.com) | 获奖网站；有 llms.txt 和只读 OpenAPI | llms.txt: https://www.awwwards.com/llms.txt | 免费 |
| [Cosmos](https://www.cosmos.so) | 视觉情绪板与灵感发现 |  | 免费 |
| [Curated Design](https://www.curated.design) | 精选网页设计 |  | 免费 |
| [Dark Design](https://dark.design) | 暗色模式网站合集 |  | 免费 |
| [Footer Design](https://www.footer.design) | 页脚模式 |  | 免费 |
| [Httpster](https://httpster.net) | 网页设计画廊 |  | 免费 |
| [Land-book](https://land-book.com) | 每日精选落地页，可按区块/颜色浏览 | llms.txt: https://land-book.com/llms.txt | 免费+付费 |
| [Landingfolio](https://www.landingfolio.com) | 落地页与组件 |  | 免费+付费 |
| [Lapa Ninja](https://www.lapa.ninja) | 落地页画廊 |  | 免费 |
| [Lazyweb](https://design.lazyweb.com) | 28 万+ 真实 App/营销页截图与流程，2 万+ 移动端 A/B 测试；MCP 需注册账号（OAuth 登录），免费账号只能拿到部分结果 | `claude mcp add --transport http lazyweb https://www.lazyweb.com/mcp`（首次连接要 OAuth 登录） | 免费+付费 |
| [Minimal Gallery](https://minimal.gallery) | 极简风网站 |  | 免费 |
| [Navbar Gallery](https://www.navbar.gallery) | 导航栏模式 |  | 免费 |
| [One Page Love](https://onepagelove.com) | 单页网站与模板 |  | 免费 |
| [Page Flows](https://pageflows.com) | 真实用户流程录屏（注册、引导、支付…） |  | 付费 |
| [SaaS Landing Page](https://saaslandingpage.com) | SaaS 落地页，按区块分类 |  | 免费 |
| [SaaSFrame](https://www.saasframe.io) | SaaS UI 与邮件示例 |  | 免费+付费 |
| [UIland](https://uiland.design) | 移动端 UI 截图 |  | 免费+付费 |
