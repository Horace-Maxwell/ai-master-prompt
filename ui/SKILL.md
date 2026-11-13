---
name: ui-master
description: UI 路由 Skill。用户要做/改网页或 App 界面、要「好看/高级/有设计感」、要某种动效或视觉风格、要找组件库/图标/字体/配色/灵感/UI 相关 MCP 时使用。根据需求从本文件夹的已核实目录里挑选组件库、风格配方、动效术语和安装命令，再动手实现。
---

# UI Master：做出不像 AI 做的界面

> **路径约定**：本文件在仓库的 `ui/` 目录下，`catalog/` 和 `prompts/` 与它同级，随 Skill 一起走。
> - 在完整仓库里（或通过 `setup.sh --link-skills` 软链接安装的）：先 `realpath` 找到仓库根目录，就能用 `python3 <仓库根>/scripts/find.py <关键词>` 搜索全部模块。
> - 单独安装的（`npx skills add Horace-Maxwell/ai-master-prompt`，只有 `ui/` 这一个文件夹）：没有搜索脚本，直接 grep `catalog/*.md`；脚手架、Skills、工具等其他模块见 <https://github.com/Horace-Maxwell/ai-master-prompt>。

AI 做的 UI 难看，通常不是因为能力不够，而是因为 ① 没用好现成组件库，② 说不出想要的效果叫什么。本 Skill 解决这两件事。

## 工作流程

### 1. 先弄清四件事

- **平台与技术栈**：Web（React/Next？Vue？纯 HTML？）还是 React Native/Expo？已有项目还是新建？
- **页面类型**：落地页 / 仪表盘 / SaaS 应用 / AI 聊天产品 / 移动 App / 作品集…
- **风格**：用户有没有指定风格或参考网站？
- **动效强度**：克制 / 适中 / 炫

**什么时候问、什么时候直接做**：平台和页面类型不清楚才需要问（最多问一轮）。其余用默认值并在回复里说明你选了什么：

| 没说的 | 默认 |
|---|---|
| 技术栈 | 已有项目跟随项目；新建 Web 用 Next.js + Tailwind + shadcn/ui |
| 风格 | 给 2–3 个方向让用户选（见 [prompts/style-recipes.md](prompts/style-recipes.md)）；用户说「你定」就按页面类型选最贴的一个 |
| 动效强度 | 产品界面克制；落地页适中；作品集/活动页可以炫 |

用户说不清效果时，用 [prompts/effect-vocabulary.md](prompts/effect-vocabulary.md) 里的名称跟用户确认（「你说的是不是 *Text Scramble*，字母乱跳后定格成正确文字？」）。

### 2. 按决策表选底座

用户指定了风格时，**风格行优先**：手绘风的落地页用手绘库，不要再叠 Aceternity 这类暗色炫技组件。

| 情况 | 底座 | 加什么 |
|---|---|---|
| React/Next 新项目（默认） | `npx create-next-app@latest`，然后 `npx shadcn@latest init` | 按需从命名空间 registry 加组件 |
| 风格化（手绘/复古/粗野/玻璃/终端） | 对应风格库（见 [style-recipes](prompts/style-recipes.md)） | 多数是 shadcn registry，装进来直接替换同名组件 |
| 落地页 / Hero / 营销页（未指定风格） | shadcn + Magic UI / Aceternity / React Bits | 平滑滚动 Lenis；滚动动画 GSAP ScrollTrigger 或 Motion |
| 仪表盘 / 后台 | shadcn + Tremor 或 shadcn charts | Kibo UI 补高级组件 |
| AI 聊天 / Agent 产品 | shadcn + AI Elements 或 assistant-ui | affectUI 做 Agent 可观测性面板；数据来自 Langfuse / Phoenix；Python 后端用 AG-UI 协议接前端 |
| React Native / Expo | `npx create-expo-app@latest` + React Native Reusables 或 ExpoKit | 液态玻璃用 `expo-glass-effect`，毛玻璃用 `expo-blur`；beUI 做动画 |
| Vue / Nuxt | Nuxt UI 或 shadcn-vue | Inspira UI 做特效；goopUI（液体效果，pre-alpha）；更多见 [catalog/13](catalog/13-other-frameworks.md) |
| Svelte / Angular / Solid / Web Components | 见 [catalog/13](catalog/13-other-frameworks.md) | |
| 国内项目 / 中后台 / 小程序 | Ant Design、Element Plus、TDesign、Vant、Taro、uni-app | 见 [catalog/14](catalog/14-china-ecosystem.md)，图表用 ECharts / AntV |
| Flutter / SwiftUI / Compose | 见 [catalog/05](catalog/05-mobile.md) 的「原生与跨端」 | |
| 纯 HTML / 无框架 | daisyUI 或 Tailwind + 原生 CSS | Animate.css、Hover.css、GSAP |

完整候选清单：

- 组件库：[catalog/02 基础](catalog/02-component-libraries.md)、[03 动画](catalog/03-animated-components.md)、[04 风格化](catalog/04-stylized-themes.md)、[05 移动端](catalog/05-mobile.md)、[06 特效/3D](catalog/06-effects-3d-shaders.md)、[07 AI 产品](catalog/07-ai-product-ui.md)
- 要某个具体功能（图表、表格、富文本编辑器、日历、拖拽、流程图、地图、上传、播放器）：[catalog/16](catalog/16-functional-components.md)，每个子类有一个 ⭐ 默认选择，不要自己造
- 模板与整页区块：[catalog/17](catalog/17-templates-blocks.md)；对齐平台规范：[catalog/15 大厂设计系统](catalog/15-design-systems.md)
- 插画、3D、样机、背景生成器等素材：[catalog/11](catalog/11-assets.md)
- 还找不到：[catalog/18](catalog/18-shadcn-registries.md) 是 shadcn 官方索引的全部 548 个 registry（文件很大，用 grep 搜关键词）；再不行去聚合站 [catalog/01](catalog/01-aggregators.md)

### 3. 安装组件：shadcn 命名空间用法

官方索引收录的命名空间（548 个）**无需任何配置**：

```bash
npx shadcn@latest add @magicui/marquee
npx shadcn@latest add @aceternity/spotlight
npx shadcn@latest search @aceternity --query "card"     # 不知道条目名：先搜
npx shadcn@latest list @magicui                    # 或列出该命名空间的全部条目
npx shadcn@latest view @magicui/border-beam        # 装之前看代码
```

三个容易踩的坑：

1. **条目名不能猜。** 目录里的 `<item>` 是占位符，各库命名不一样。先 `search` 或 `list`。
2. **React Bits 的条目名带变体后缀**：`<组件名>-<TS|JS>-<TW|CSS>`，例如 `npx shadcn@latest add @react-bits/DecryptedText-TS-TW`。不带后缀会 404。
3. **没进官方索引的库**（Looseleaf、Rare UI 等）有两种装法：
   - 直接给完整 URL 或 GitHub 路径，零配置：`npx shadcn@latest add https://kevintngo.github.io/looseleaf/r/button.json`、`npx shadcn@latest add swamimalode07/rare-ui/fluid-orb`
   - 或在 `components.json` 里登记一次，之后就能用 `@looseleaf/button`：

     ```json
     { "registries": { "@looseleaf": "https://kevintngo.github.io/looseleaf/r/{name}.json" } }
     ```

常用命名空间速查（均在官方索引内）：`@magicui` `@aceternity` `@react-bits` `@animate-ui` `@motion-primitives` `@cult-ui` `@kokonutui` `@coss` `@shadcnblocks` `@tailark` `@kibo-ui` `@8bitcn` `@neobrutalism` `@retroui` `@glasscn` `@glassyui` `@ai-elements` `@assistant-ui` `@prompt-kit` `@affectui` `@beui` `@shaderscn` `@threecn` `@lucide-animated` `@svgl`

### 4. 给 Agent 装工具（征得用户同意后）

最小组合（以 Claude Code 为例；其他 Agent 把 `--` 后面同样的 `npx …` 写进自己的 MCP 配置，对照表见仓库根目录 `AGENTS.md`）：

```bash
npx shadcn@latest mcp init --client claude                    # 浏览/安装数百个 registry 的组件（也支持 --client cursor / vscode）
claude mcp add context7 -- npx -y @upstash/context7-mcp        # 任意库的最新文档
npx skills add anthropics/skills --skill frontend-design       # 审美基线，去 AI 味
```

按需再加：Magic UI MCP、21st MCP、Figma MCP（有设计稿时）、Motion AI Kit（`npx motion-ai`）、GSAP skills、找参考截图的 Mobbin / Refero / Lazyweb MCP（都要账号）。完整列表见 [catalog/12](catalog/12-mcp-registries-llms.md)。

### 5. 先定设计系统，再写页面

1. **定风格 token**：配色（Realtime Colors / tweakcn 生成）、字体（别默认 Inter：Fontshare、Google Fonts 选一对有性格的）、圆角、阴影、间距。如果用户给了参考品牌，去 [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) 找对应的 DESIGN.md 放进项目根目录。
2. **页面结构**：参考灵感站（[catalog/10](catalog/10-inspiration.md)）里同类页面的区块顺序。
3. **组件优先复用**：能 `npx shadcn@latest add` 的不手写。
4. **动效有目的**：入场一次、悬停反馈、滚动叙事。尊重 `prefers-reduced-motion`。

### 6. 自检（不要跳过）

- 用浏览器（Playwright / Chrome DevTools MCP / 内置浏览器）打开页面截图，对照下面的「AI 味」清单检查
- 移动端宽度（375px）看一遍
- 控制台无报错；动画不卡（只动 transform/opacity）

**常见 AI 味（避免）**：紫蓝渐变 + Inter + 居中大标题三件套；所有卡片同一圆角同一阴影；emoji 当图标；满屏 glassmorphism；没有层次的灰色文字；每个区块都「淡入上移」。

## 需要动效/风格词汇时

- 速查表：[prompts/effect-vocabulary.md](prompts/effect-vocabulary.md)（带可直接安装的条目名）
- 风格配方：[prompts/style-recipes.md](prompts/style-recipes.md)
- 描述需求的模板（给用户或给其他 AI 用）：[prompts/request-template.md](prompts/request-template.md)
- 有演示的画廊：motion-prompt（192 效果，`npx skills add showheyohtaki/motion-prompt`）、Motion Library（510 效果）、aimotions（195 种文字动效），见 [catalog/09](catalog/09-design-vocabulary.md)
