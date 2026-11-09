# 移动端 / React Native 组件库

> 本文件由 `scripts/build.py` 从 `data/resources/*.json` 自动生成，请勿手改；要增删条目请改 JSON 后重新运行脚本。⭐ = 同类首选。

<a id="ui-mobile"></a>

## 移动端 / React Native

Expo / React Native 项目用。

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [beUI](https://beui.dev) | 同时覆盖 Web 和 React Native 的动画组件（Motion/Tailwind/Reanimated），带 MCP 和 Skill | React, React Native | `npx shadcn@latest add @beui/<item>`<br>`npx beui-native add <item>`（React Native）<br>`claude mcp add --transport http beui https://mcp.beui.dev/mcp`<br>`npx skills add starc007/ui-components --skill beui` | 免费 |
| ⭐ [expo-glass-effect](https://docs.expo.dev/versions/latest/sdk/glass-effect/) | Expo 官方液态玻璃视图（iOS 26 Liquid Glass 原生效果）。React Native 里要真·液态玻璃用它 | React Native, Expo | `npx expo install expo-glass-effect` | 免费 |
| ⭐ [ExpoKit](https://expokit.in) | Expo 复制粘贴组件库：73 组件（340+ 变体）、12 屏、44 图表、液态玻璃与 3D 效果；iOS/Android/Web/Expo Go | React Native, Expo | `npx @expokit/cli@latest init`<br>`npx @expokit/cli@latest add <component>`<br>`npx @expokit/cli@latest mcp init --client claude` | 免费+付费 |
| ⭐ [React Native Reusables](https://reactnativereusables.com) | shadcn/ui 的标准 RN 移植（NativeWind / Uniwind） | React Native | `npx @react-native-reusables/cli@latest init`<br>`npx @react-native-reusables/cli@latest add button` | 免费 |
| [expo-blur](https://docs.expo.dev/versions/latest/sdk/blur-view/) | Expo 官方毛玻璃模糊视图（BlurView），跨 iOS/Android 的玻璃拟态基础 | React Native, Expo | `npx expo install expo-blur` | 免费 |
| [gluestack-ui](https://gluestack.io) | 通用 React + RN 复制组件（NativeBase 继任者），带 MCP | React, React Native | MCP / llms.txt: https://gluestack.io/llms.txt | 免费 |
| [HeroUI Native](https://heroui.com/en/docs/native/getting-started) | HeroUI v3 的 React Native 版 | React Native |  | 免费 |
| [NativewindUI](https://nativewindui.com) | 原生 iOS/Android 手感的组件与页面 | React Native | llms.txt: https://nativewindui.com/llms.txt | 免费+付费 |
| [React Native Paper](https://reactnativepaper.com) | RN 的 Material Design | React Native |  | 免费 |
| [Reacticx](https://www.reacticx.com) | 60+ 动画组件（Reanimated、Skia） | React Native |  | 免费 |
| [Tamagui](https://tamagui.dev) | 类型安全的跨端样式与 UI + 优化编译器 | React, React Native | llms.txt: https://tamagui.dev/llms.txt | 免费 |
| [Uniwind](https://uniwind.dev) | RN 的 Tailwind 样式引擎 | React Native |  | 免费 |
