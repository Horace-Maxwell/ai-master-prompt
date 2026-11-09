# UI 需求描述模板

> 给人用：照着填，然后贴给任何 AI。给 AI 用：用户需求不清楚时，按这个结构向用户提问。

```markdown
## 我要做什么
- 产品 / 页面：[例：AI 写作工具的落地页]
- 目标用户：[例：独立开发者]
- 页面要达成的一件事：[例：让访客点击「免费试用」]

## 技术
- 平台：[Web / iOS / Android / 跨端]
- 栈：[Next.js + Tailwind + shadcn/ui]（不确定就写「你推荐」）
- 已有项目？[是，路径… / 否，新建]

## 风格
- 风格关键词：[例：编辑杂志风 + 少量暗色科技感]（参考 ui/prompts/style-recipes.md）
- 参考网站 / 截图：[链接或附图]
- 品牌色 / 字体：[有就写，没有写「你来定」]

## 区块（从上到下）
1. 导航栏：[Logo、3 个链接、CTA 按钮]
2. Hero：[大标题 + 副标题 + 两个按钮 + 产品截图]
3. ……

## 动效（用专业名称，参考 ui/prompts/effect-vocabulary.md）
- [例：Hero 标题 Split Text Stagger 入场]
- [例：Logo 墙 Marquee]
- [例：功能区 Sticky Stack Cards]
- 强度：[克制 / 适中 / 炫]

## 必须 / 不要
- 必须：[响应式、暗色模式、可访问性]
- 不要：[紫蓝渐变、emoji 图标、过多玻璃效果]

## 验收
- 完成后截图桌面端和移动端给我看
```

## 举例

> 用 Next.js + shadcn/ui 做一个 AI 播客剪辑工具的落地页。编辑杂志风：标题用 Instrument Serif，正文 Geist，米白背景 #F7F5F0，墨黑文字，强调色砖红 #C2410C。
> 区块：导航 → Hero（大标题 Split Text Stagger 入场、右侧产品视频）→ Logo 墙（Marquee）→ 三个功能（Sticky Stack Cards）→ 用户评价（Infinite Carousel）→ 定价 → FAQ（Accordion）→ 页脚。
> 全站 Lenis 平滑滚动，动效克制，尊重 prefers-reduced-motion。不要紫蓝渐变和 emoji。完成后截图桌面端和 375px 移动端。
