# 开源工具

完整清单见 [catalog.md](catalog.md)。

## MediaCrawler：中文社交平台数据采集

[NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler)（约 70k★）

- **平台**：小红书、抖音、快手、B站、微博、百度贴吧、知乎
- **能力**：关键词搜索、指定帖子 ID、创作者主页、一级与二级评论（默认关闭，`ENABLE_GET_COMMENTS` 开启）；媒体下载（`--get_media true`，贴吧/知乎除外）；IP 代理池；评论词云
- **原理**：Playwright 复用已登录浏览器（默认 CDP 模式接管已有 Chrome），通过 JS 拿签名参数，不需要逆向加密
- **存储**：CSV / JSON / JSONL / Excel / SQLite / MySQL
- **WebUI**：FastAPI + Vite

```bash
git clone https://github.com/NanmiCoder/MediaCrawler && cd MediaCrawler
uv sync
uv run playwright install                                   # 仅标准 Playwright 模式需要
uv run main.py --platform xhs --lt qrcode --type search     # 小红书关键词搜索（扫码登录）
uv run main.py --platform dy --lt qrcode --type detail      # 抖音指定作品
uv run main.py --help
uv run uvicorn api.main:app --port 8080 --reload            # WebUI
```

平台代号：`xhs` 小红书、`dy` 抖音、`ks` 快手、`bili` B站、`wb` 微博、`tieba` 贴吧、`zhihu` 知乎。需要 Python 3.11+ 和 uv；抖音和知乎还需要 Node.js 16+。

> ⚠ **合规**：README 声明仅供学习参考，**禁止商用**，使用者自负责任。只采集公开数据，控制频率，遵守平台条款和当地法律（如《个人信息保护法》）。另有付费版 MediaCrawlerPro。

## 本机已装、可直接调用的相关 Skill

- **agent-reach**：搜索/阅读 Twitter、Reddit、YouTube、B站、小红书、抖音、微博、公众号等 17 个平台
- **scrapling**：带反爬绕过的网页抓取
- **agent-browser**：给 Agent 用的浏览器自动化 CLI
