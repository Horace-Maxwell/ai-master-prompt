---
name: ui-master
description: UI 路由 Skill。用户要做/改网页或 App 界面、要「好看/高级/有设计感」、要某种动效或视觉风格、要找组件库/图标/字体/配色/灵感/UI 相关 MCP 时使用。根据需求从本文件夹的已核实目录里挑选组件库、风格配方、动效术语和安装命令，再动手实现。
---

# UI Master：做出不像 AI 做的界面

> 路径约定：本文件在仓库的 `ui/` 目录下。如果它是通过 `setup.sh --link-skills` 链接到 `~/.claude/skills/ui-master` 的，先解析真实路径（`realpath`）得到仓库根目录；下文的 `scripts/`、`data/` 都相对仓库根目录。

AI 做的 UI 难看，通常不是因为能力不够，而是因为 ① 没用好现成组件库，② 说不出想要的效果叫什么。本 Skill 解决这两件事。

## 工作流程

### 1. 先弄清四件事（缺哪个问哪个，最多问一轮）

- **平台与技术栈**：Web（React/Next？Vue？纯 HTML？）还是 React Native/Expo？已有项目还是新建？
- **页面类型**：落地页 / 仪表盘 / SaaS 应用 / AI 聊天产品 / 移动 App / 作品集…
- **风格**：用户有没有指定风格或参考网站？没有就提 2–3 个方向让用户选（见 [prompts/style-recipes.md](prompts/style-recipes.md)）
- **动效强度**：克制（产品型）/ 适中 / 炫（落地页、作品集）

用户说不清效果时，用 [prompts/effect-vocabulary.md](prompts/effect-vocabulary.md) 里的名称跟用户确认（「你说的是不是 *Text Scramble*，字母乱跳后定格成正确文字？」）。

### 2. 按决策表选底座

| 情况 | 底座 | 加什么 |
|---|---|---|
| React/Next 新项目（默认） | shadcn/ui（`npx shadcn@latest init`） | 按需从命名空间 registry 加组件 |
| 落地页 / Hero / 营销页 | shadcn + Magic UI / Aceternity / React Bits | 平滑滚动 Lenis；滚动动画 GSAP ScrollTrigger 或 Motion |
| 仪表盘 / 后台 | shadcn + Tremor 或 shadcn charts | Kibo UI 补高级组件 |
| AI 聊天 / Agent 产品 | shadcn + AI Elements 或 assistant-ui | affectUI 做 Agent 可观测性（trace、审批、成本） |
| 风格化（手绘/复古/粗野/玻璃） | 对应风格库（见 style-recipes） | 多数可直接 `npx shadcn add @ns/...` 替换 |
| React Native / Expo | React Native Reusables 或 ExpoKit | beUI 做动画；gluestack/Tamagui 做跨端 |
| Vue / Nuxt | Nuxt UI 或 shadcn-vue | Inspira UI 做特效；goopUI（液体效果，pre-alpha） |
| 纯 HTML / 无框架 | daisyUI 或 Tailwind + 原生 CSS | Animate.css、Hover.css、GSAP |

完整候选清单：

- 组件库：[catalog/02](catalog/02-component-libraries.md)、[03 动画](catalog/03-animated-components.md)、[04 风格化](catalog/04-stylized-themes.md)、[05 移动端](catalog/05-mobile.md)、[06 特效/3D](catalog/06-effects-3d-shaders.md)、[07 AI 产品](catalog/07-ai-product-ui.md)
- 找不到时去聚合站：[catalog/01](catalog/01-aggregators.md)（21st.dev、shadcn 官方目录、registry.directory）
- 也可以直接搜索：`python3 scripts/find.py <关键词>`（在仓库根目录运行）

### 3. 给 Agent 装工具（征得用户同意后）

最小组合：

```bash
npx shadcn@latest mcp init --client claude                    # 浏览/安装数百个 registry 的组件
claude mcp add context7 -- npx -y @upstash/context7-mcp        # 任意库的最新文档
npx skills add anthropics/skills --skill frontend-design       # 审美基线，去 AI 味
```

按需再加：Magic UI MCP、21st MCP、Figma MCP（有设计稿时）、Motion AI Kit（`npx motion-ai`）、GSAP skills、Lazyweb MCP（免费找参考截图）。完整列表见 [catalog/12](catalog/12-mcp-registries-llms.md)。

**shadcn 命名空间用法**：官方索引收录的命名空间（548 个）无需配置，直接：

```bash
npx shadcn@latest add @magicui/marquee
npx shadcn@latest search @aceternity --query "spotlight"
npx shadcn@latest view @react-bits/<item>
```

未收录的（如 Looseleaf、Rare UI）在 `components.json` 里加上：

```json
{ "registries": { "@looseleaf": "https://<registry-host>/r/{name}.json" } }
```

（具体 URL 见该库文档。）常用命名空间速查：`@magicui` `@aceternity` `@react-bits` `@animate-ui` `@motion-primitives` `@cult-ui` `@kokonutui` `@coss` `@shadcnblocks` `@tailark` `@kibo-ui` `@8bitcn` `@neobrutalism` `@retroui` `@glasscn` `@ai-elements` `@assistant-ui` `@prompt-kit` `@affectui` `@beui` `@shaderscn` `@threecn` `@lucide-animated` `@svgl`

### 4. 先定设计系统，再写页面

1. **定风格 token**：配色（Realtime Colors / tweakcn 生成）、字体（别默认 Inter：Fontshare、Google Fonts 选一对有性格的）、圆角、阴影、间距。如果用户给了参考品牌，去 [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) 找对应的 DESIGN.md 放进项目根目录。
2. **页面结构**：参考灵感站（[catalog/10](catalog/10-inspiration.md)）里同类页面的区块顺序。
3. **组件优先复用**：能 `shadcn add` 的不手写。
4. **动效有目的**：入场一次、悬停反馈、滚动叙事。尊重 `prefers-reduced-motion`。

### 5. 自检（不要跳过）

- 用浏览器（Playwright / Chrome DevTools MCP / 内置浏览器）打开页面截图，对照下面的「AI 味」清单检查
- 移动端宽度（375px）看一遍
- 控制台无报错；动画不卡（只动 transform/opacity）

**常见 AI 味（避免）**：紫蓝渐变 + Inter + 居中大标题三件套；所有卡片同一圆角同一阴影；emoji 当图标；满屏 glassmorphism；没有层次的灰色文字；每个区块都「淡入上移」。

## 需要动效/风格词汇时

- 速查表：[prompts/effect-vocabulary.md](prompts/effect-vocabulary.md)
- 风格配方：[prompts/style-recipes.md](prompts/style-recipes.md)
- 描述需求的模板（给用户或给其他 AI 用）：[prompts/request-template.md](prompts/request-template.md)
- 有演示的画廊：motion-prompt（192 效果，`npx skills add showheyohtaki/motion-prompt`）、Motion Library（510 效果）、aimotions（195 种文字动效），见 [catalog/09](catalog/09-design-vocabulary.md)
