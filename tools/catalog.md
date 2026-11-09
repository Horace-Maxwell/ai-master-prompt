# 开源工具

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

## 数据采集 / 爬虫

注意：遵守平台条款与当地法律，只采集公开数据，多数项目禁止商用。

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | 小红书/抖音/快手/B站/微博/贴吧/知乎 的帖子、视频、评论（含二级评论）采集；Playwright 复用登录态免逆向；存 CSV/JSON/Excel/SQLite/MySQL；带 WebUI（约 70k★）。仅供学习，禁止商用 | Python, Playwright | `uv sync && uv run main.py --platform xhs --lt qrcode --type search` | 开源 |
| [Agent Reach](https://github.com/Panniantong/Agent-Reach) | 让 Agent 搜索/阅读 Twitter、Reddit、YouTube、B站、小红书、抖音、微博、公众号等 17 个平台（本机已装为 Skill） |  |  | 开源 |
| [Scrapling](https://github.com/D4Vinci/Scrapling) | 自适应网页抓取，支持隐身浏览器与反爬绕过、爬虫框架（本机已装为 Skill） | Python |  | 开源 |

## 浏览器自动化（给 Agent 用）

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [agent-browser](https://github.com/vercel-labs/agent-browser) | 给 AI Agent 用的浏览器自动化 CLI（也是 Top 5 Skill） |  | `npx skills add vercel-labs/agent-browser` | 开源 |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | 微软官方浏览器自动化 MCP |  | `claude mcp add playwright -- npx @playwright/mcp@latest` | 开源 |
