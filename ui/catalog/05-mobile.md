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

<a id="ui-native"></a>

## 原生与跨端（Flutter / SwiftUI / Compose / 桌面）以及 RN 基础库

不走 Web 技术栈、或需要原生手感时用。

本类分组：React Native 基础库 · Flutter · SwiftUI / iOS · Compose / Android · 桌面与跨端

### React Native 基础库

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [React Native Reanimated](https://docs.swmansion.com/react-native-reanimated/) | React Native 动画的事实标准：动画跑在 UI 线程，支持布局动画和 CSS 式动画；几乎所有 RN 动效库的依赖，必装 | React Native, Expo | `npm install react-native-reanimated`<br>llms.txt: https://docs.swmansion.com/react-native-reanimated/llms.txt | 开源 |
| [Bottom Sheet（gorhom）](https://gorhom.dev/react-native-bottom-sheet/) | RN 最常用的底部弹层，吸附点、键盘处理、内嵌滚动都处理好了；要可高度定制的 sheet 时选 | React Native, Expo | yarn add @gorhom/bottom-sheet@^5 | 开源 |
| [CraftReactNative UI](https://github.com/craftreactnative/ui) | shadcn 式 RN 组件：CLI 把基于 Unistyles + Reanimated 的源码复制进项目 ⚠ 项目很小（约 80★），原官网域名已失效，文档看仓库 | React Native, Expo | `npx @craftreactnative/ui init`<br>`npx @craftreactnative/ui add Button` | 开源 |
| [Expo UI](https://docs.expo.dev/versions/latest/sdk/ui/) | 在 Expo 里直接用 SwiftUI 和 Jetpack Compose 的原生控件；要真正原生的列表、选择器、表单外观时选 | Expo, SwiftUI, Jetpack Compose | llms.txt: https://docs.expo.dev/llms.txt | 开源 |
| [FlashList](https://shopify.github.io/flash-list/) | Shopify 的高性能列表，API 兼容 FlatList 但靠视图复用避免白屏；长列表、信息流必选 | React Native, Expo | yarn add @shopify/flash-list | 开源 |
| [Keyboard Controller](https://kirillzyusko.github.io/react-native-keyboard-controller/) | 统一 iOS / Android 的键盘动画与避让，替代不可靠的 KeyboardAvoidingView；聊天输入、表单页必备 | React Native, Expo | yarn add react-native-keyboard-controller | 开源 |
| [Legend List](https://legendapp.com/open-source/list/) | 纯 JS 实现的高性能列表，支持动态高度和双向无限滚动；聊天列表等 FlashList 不顺手的场景选它 | React Native, Expo | `npm install @legendapp/list` | 开源 |
| [Moti](https://moti.fyi) | 基于 Reanimated 的声明式动画组件（写法像 Framer Motion），含骨架屏；想少写动画代码时选 ⚠ 2025-01 后未发新版 | React Native, Expo | yarn add moti | 开源 |
| [NativeBase（legacy）](https://nativebase.io) | 曾经最流行的 RN 组件库 ⚠ 官方 README 已标记 DEPRECATED / 维护模式，新项目请用其继任者 gluestack-ui | React Native |  | 开源 |
| [NativeWind](https://www.nativewind.dev) | 在 React Native 里写 Tailwind 类名，RN Reusables、gluestack 等组件库的样式底座 ⚠ 稳定版 v4 对应 Tailwind v3，v5 仍在预览 | React Native, Expo, Tailwind | `npx rn-new@latest --nativewind`<br>llms.txt: https://www.nativewind.dev/llms.txt | 开源 |
| [React Native Elements](https://reactnativeelements.com) | 老牌跨平台 RN 组件库，API 简单；维护已有项目或做简单 App 时可用，新项目优先 RN Reusables / gluestack | React Native, Expo | `npm install @rneui/themed @rneui/base` | 开源 |
| [React Native Gesture Handler](https://docs.swmansion.com/react-native-gesture-handler/) | 原生手势系统（拖拽、捏合、滑动），与 Reanimated 配套；做任何手势交互都要它 | React Native, Expo | llms.txt: https://docs.swmansion.com/react-native-gesture-handler/llms.txt | 开源 |
| [React Native Screens](https://github.com/software-mansion/react-native-screens) | 把页面栈交给原生导航容器（React Navigation、Expo Router 的底层）；想直接用原生 stack / tabs 时用 | React Native, Expo | `npx expo install react-native-screens` | 开源 |
| [React Native Skia](https://wcandillon.github.io/react-native-skia/) | 把 Skia 2D 图形引擎带到 RN：着色器、路径、模糊、自定义绘制；做图表、特效、画布类界面时选 ⚠ 包名已由 @shopify/react-native-skia 改为 react-native-skia，文档也已迁移 | React Native, Expo | yarn add react-native-skia | 开源 |
| [Restyle](https://shopify.github.io/restyle/) | Shopify 的类型安全主题化工具：用 Box / Text 加主题 token 搭 UI；要严格设计约束的团队项目选它 | React Native, TS | `npm install @shopify/restyle` | 开源 |
| [RNUILib（Wix）](https://wix.github.io/react-native-ui-lib/) | Wix 的 React Native 组件库，组件多并带修饰符式布局写法；要一套久经生产验证的完整组件时选 | React Native | `npm install react-native-ui-lib` | 开源 |
| [sonner-native](https://github.com/gunnartorfis/sonner-native-toasts) | Sonner 的 React Native 版 toast，API 一致、可堆叠可滑动关闭；RN 里要现代 toast 时选 | React Native, Expo | `npx expo install sonner-native` | 开源 |
| [True Sheet](https://sheet.lodev09.com) | 调用系统原生 sheet 的底部弹层，iOS 上是真正的原生表现；想要系统级手感、不需要重度定制时选 | React Native, Expo | `npx expo install @lodev09/react-native-true-sheet`<br>`npx skills add lodev09/react-native-true-sheet`<br>llms.txt: https://sheet.lodev09.com/llms.txt | 开源 |
| [UI Kitten](https://akveo.github.io/react-native-ui-kitten/) | 基于 Eva 设计系统的 RN 组件库，运行时切换主题；要成套主题化组件且接受 Eva 风格时选 | React Native, Expo | `npm install @ui-kitten/components @ui-kitten/eva react-native-svg` | 开源 |
| [Unistyles](https://www.unistyl.es) | C++ 实现的 StyleSheet 超集：主题、断点、变体，切主题不触发重渲染；不想用 Tailwind 又要高性能主题化时选 | React Native, Expo | yarn add react-native-unistyles react-native-nitro-modules<br>`npx skills add jpudysz/react-native-unistyles`<br>llms.txt: https://www.unistyl.es/llms.txt | 开源 |

### Flutter

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Forui](https://forui.dev) | 极简风的 Flutter UI 库，自带 CLI 可把样式源码生成进项目；不想要 Material 观感的 Flutter 应用首选 | Flutter, Dart | flutter pub add forui<br>dart run forui init | 开源 |
| [FlexColorScheme](https://pub.dev/packages/flex_color_scheme) | Flutter Material 主题生成器：一行生成协调的明暗主题并统一各组件样式；想把 Material 调得不像默认时用 | Flutter, Dart | flutter pub add flex_color_scheme | 开源 |
| [fluent_ui](https://bdlukaa.github.io/fluent_ui/) | 用 Flutter 实现的 Windows Fluent Design 组件；做 Windows 桌面应用时选 | Flutter, Dart | flutter pub add fluent_ui | 开源 |
| [Flutter Gems](https://fluttergems.dev) | 按功能分类的 Flutter / Dart 包精选目录；选 Flutter 包之前先来这里比较 | Flutter, Dart |  | 免费 |
| [Flutter Widget catalog（官方）](https://docs.flutter.dev/ui/widgets) | Flutter 官方组件目录（Material 3、Cupertino、布局、动画）；写 Flutter 先查这里，配合官方 Dart / Flutter MCP 使用 | Flutter, Dart | dart mcp-server（官方 MCP，写入客户端配置）<br>llms.txt: https://docs.flutter.dev/llms.txt | 免费 |
| [flutter_animate](https://pub.dev/packages/flutter_animate) | 链式声明动画效果（淡入、滑动、模糊、shader）的 Flutter 库；给现有 widget 快速加动效时选 ⚠ 2024-11 后未发新版 | Flutter, Dart | flutter pub add flutter_animate | 开源 |
| [GetWidget](https://github.com/ionicfirebaseapp/getwidget) | 老牌 Flutter 组件库，预制组件多；快速堆页面可用 ⚠ 官网已转型为 AI 开发工作室，组件库以 GitHub / pub.dev 为准 | Flutter, Dart | flutter pub add getwidget | 开源 |
| [macos_ui](https://macosui.dev) | 用 Flutter 实现的 macOS 原生风格组件与布局；做 Mac 桌面应用时选 | Flutter, Dart | flutter pub add macos_ui | 开源 |
| [Mix](https://fluttermix.com) | Flutter 的样式系统：把样式从 widget 树里抽出来，支持变体和 design token；自建 Flutter 设计系统时选 | Flutter, Dart | flutter pub add mix<br>`npx skills add btwld/mix --skill mix -y` | 开源 |
| [shadcn_flutter](https://sunarya-thito.github.io/shadcn_flutter/) | 另一个 shadcn 风 Flutter 套件：完全独立于 Material / Cupertino 的整套组件；想彻底脱离 Material 时选 | Flutter, Dart | flutter pub add shadcn_flutter | 开源 |
| [shadcn_ui（Flutter）](https://mariuti.com/flutter-shadcn-ui/) | shadcn/ui 的 Flutter 移植，更新活跃，可与 Material 共存；Flutter 里要 shadcn 观感时选 | Flutter, Dart | flutter pub add shadcn_ui<br>`npx skills add nank1ro/flutter-shadcn-ui`<br>llms.txt: https://mariuti.com/flutter-shadcn-ui/llms.txt | 开源 |
| [Syncfusion Flutter Widgets](https://www.syncfusion.com/flutter-widgets) | 图表、DataGrid、日历、PDF 等重型 Flutter 组件 ⚠ 商业授权，仅符合条件的个人和小团队可用免费社区许可 | Flutter, Dart |  | 免费+付费 |
| [Widgetbook](https://www.widgetbook.io) | Flutter 版 Storybook：隔离开发、预览和评审 widget；团队维护组件库时用 ⚠ Cloud 评审功能付费 | Flutter, Dart | flutter pub add widgetbook | 免费+付费 |

### SwiftUI / iOS

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [awesome-swiftui-libraries](https://github.com/Toni77777/awesome-swiftui-libraries) | 按组件类型分类的 SwiftUI 第三方库清单；找某类 SwiftUI 控件时从这里起步 | SwiftUI |  | 免费 |
| [Inferno](https://github.com/twostraws/Inferno) | Paul Hudson 的 SwiftUI Metal 着色器合集（水波、溶解、故障等转场与滤镜）；要 shader 特效又不想自己写 Metal 时选 | SwiftUI, Metal |  | 开源 |
| [Liquid Glass（Apple 文档）](https://developer.apple.com/documentation/technologyoverviews/liquid-glass) | Apple 关于 Liquid Glass 新设计语言的技术概览与适配指南；做 iOS 26 及以后的界面时先读 | SwiftUI, UIKit |  | 免费 |
| [PopupView（Exyte）](https://github.com/exyte/PopupView) | SwiftUI 的 toast / 弹窗 / 浮层库，位置、动画、拖拽关闭都可配；需要系统 sheet 之外的弹出层时选 | SwiftUI, Swift | .package(url: "https://github.com/exyte/PopupView.git") | 开源 |
| [Pow](https://movingparts.io/pow) | SwiftUI 转场与状态变化特效合集（发光、抖动、粒子、翻转），现已开源；想给 iOS 应用加讨喜的动效时选 | SwiftUI, Swift | .package(url: "https://github.com/EmergeTools/Pow", from: Version(1, 0, 0)) | 开源 |
| [Swift Charts](https://developer.apple.com/documentation/charts) | Apple 官方声明式图表框架，与 SwiftUI 无缝集成；iOS 上画图表默认选它 | SwiftUI, Swift |  | 免费 |
| [SwiftUI Introspect](https://github.com/siteline/swiftui-introspect) | 取到 SwiftUI 视图背后的 UIKit / AppKit 对象做微调；SwiftUI 的修饰符不够用时的逃生口 | SwiftUI, Swift | .package(url: "https://github.com/siteline/swiftui-introspect", from: "27.0.0") | 开源 |
| [SwiftUI 官方文档](https://developer.apple.com/documentation/swiftui) | Apple 官方 SwiftUI API 参考与教程；写 iOS / macOS 界面的第一信息源 | SwiftUI, Swift |  | 免费 |
| [SwiftUIX](https://github.com/SwiftUIX/SwiftUIX) | 补齐 SwiftUI 缺失能力的大型扩展库（各类 UIKit / AppKit 桥接视图）；遇到 SwiftUI 做不到的控件时先查它 | SwiftUI, Swift | .package(url: "https://github.com/SwiftUIX/SwiftUIX.git", branch: "master") | 开源 |
| [Vortex](https://github.com/twostraws/Vortex) | SwiftUI 高性能粒子系统（烟花、雨雪、彩带、火焰预设）；需要粒子特效时选 | SwiftUI, Swift |  | 开源 |

### Compose / Android

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| ⭐ [Compose Multiplatform](https://kotlinlang.org/compose-multiplatform/) | JetBrains 的声明式 UI 框架，一套 Kotlin 代码覆盖 Android / iOS / 桌面 / Web；Kotlin 团队做跨端时首选 | Kotlin, Compose |  | 开源 |
| [Composables](https://composables.com) | Jetpack Compose / CMP 的现成界面、组件和 App 模板（Kotlin 源码），与 Compose Unstyled 同团队；想要不像 Material 的成品界面时看 ⚠ 完整 App 模板付费 | Compose, Kotlin | llms.txt: https://composables.com/llms.txt | 免费+付费 |
| [Compose Fluent UI](https://github.com/compose-fluent/compose-fluent-ui) | Compose Multiplatform 上的 Fluent Design 实现；用 Kotlin 做 Windows 风格桌面应用时选 | Compose, Kotlin | implementation("io.github.compose-fluent:fluent:v0.1.0") | 开源 |
| [Compose Unstyled](https://composeunstyled.com) | Compose / Compose Multiplatform 的无样式组件（弹层、菜单、底部 sheet 等）；要脱离 Material 自建设计系统时选 | Compose, Kotlin | llms.txt: https://composeunstyled.com/llms.txt | 开源 |
| [Haze](https://chrisbanes.github.io/haze/) | Compose 的背景模糊 / 毛玻璃效果库，支持多平台；在 Android / CMP 上做玻璃拟态导航栏时选 | Compose, Kotlin | implementation("dev.chrisbanes.haze:haze:&lt;version&gt;") | 开源 |
| [Jetpack Compose Material 3 组件（官方）](https://developer.android.com/develop/ui/compose/components) | Android 官方 Compose 组件文档（Material 3 按钮、导航、弹层等，附示例）；写 Android 界面先查这里 | Jetpack Compose, Kotlin |  | 免费 |
| [Jewel](https://github.com/JetBrains/intellij-community/tree/master/platform/jewel) | JetBrains 官方的 IntelliJ 风格 Compose 桌面组件（现并入 intellij-community 仓库）；做 IDE 插件界面或 IntelliJ 观感的桌面工具时选 | Compose, Kotlin |  | 开源 |
| [Lumo UI](https://www.lumoui.com) | Compose Multiplatform 版 shadcn：Gradle 插件把组件源码生成进项目，不依赖 Material；想完全掌控组件代码时选 | Compose, Kotlin |  | 开源 |
| [Miuix](https://compose-miuix-ui.github.io/miuix/) | 小米 HyperOS 风格的 Compose Multiplatform 组件库；做国内安卓风格界面时选 | Compose, Kotlin | implementation("top.yukonga.miuix.kmp:miuix-ui:&lt;version&gt;") | 开源 |

### 桌面与跨端

| 名称 | 是什么 / 什么时候用 | 技术栈 | AI 接入（安装命令 / MCP / Skill） | 价格 |
|---|---|---|---|---|
| [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/) | 微软的跨平台原生 UI 框架（iOS / Android / macOS / Windows），C# + XAML；.NET 团队做移动和桌面应用时选 | .NET, C# | dotnet new maui -n MyApp --ui csharp（用 C# 写 UI 的模板变体） | 开源 |
| [.NET MAUI Community Toolkit](https://learn.microsoft.com/en-us/dotnet/communitytoolkit/maui/) | MAUI 官方社区工具包：补充控件、行为、转换器、弹窗和动画；MAUI 项目基本必装 | .NET, C# | dotnet add package CommunityToolkit.Maui | 开源 |
| [Avalonia UI](https://avaloniaui.net) | .NET 跨平台 UI 框架，自绘渲染、XAML 写法接近 WPF；把 WPF 应用搬到 macOS / Linux 或新做 .NET 桌面应用时首选 | .NET, C# | dotnet new install Avalonia.Templates<br>dotnet new avalonia.mvvm -o MyApp<br>llms.txt: https://avaloniaui.net/llms.txt | 开源 |
| [Capacitor](https://capacitorjs.com) | 把任意 Web 应用包成 iOS / Android 原生应用的运行时，并提供原生 API 插件；已有 Web 应用要上架商店时选 | Web, iOS, Android | `npm install @capacitor/core @capacitor/cli`<br>`npx cap init` | 开源 |
| [Dioxus](https://dioxuslabs.com) | Rust 的类 React 全栈框架，一套代码出 Web / 桌面 / 移动，支持热重载；Rust 团队想用组件化写法做应用时选 | Rust | cargo install dioxus-cli | 开源 |
| [egui](https://www.egui.rs) | Rust 的即时模式 GUI，上手极快，可编译到 Web 和原生；做工具、调试面板、游戏内 UI 时选 | Rust |  | 开源 |
| [electron-shadcn](https://github.com/LuanRoger/electron-shadcn) | Electron + shadcn/ui + Vite + TypeScript 模板，自带自定义标题栏和主题切换；做 Electron 应用的 UI 起点 | Electron, React, shadcn | `git clone https://github.com/LuanRoger/electron-shadcn.git` | 开源 |
| [Fyne](https://fyne.io) | 纯 Go 的跨平台 GUI 工具包，Material 风格自绘，可出桌面和移动端；不想碰 Web 技术的 Go 项目选它 | Go | `go get fyne.io/fyne/v2@latest` | 开源 |
| [GPUI Kit（原 gpui-component）](https://gpui-kit.com) | 基于 Zed 编辑器 GPUI 的 Rust 桌面组件库（shadcn 风）；要 GPU 加速的高性能原生桌面应用时选 | Rust, GPUI | `npx skills add longbridge/gpui-kit` | 开源 |
| [NativeScript](https://nativescript.org) | 用 JS / TS 直接调用 iOS / Android 原生 API 并渲染原生控件，支持 Angular、Vue、Svelte、Solid；非 React 团队做原生 App 时选 | JS, TS | `npm install -g nativescript` | 开源 |
| [Slint](https://slint.dev) | 声明式原生 GUI 工具包，支持 Rust / C++ / JS / Python，可跑在嵌入式设备上；做嵌入式或轻量原生桌面界面时选 ⚠ GPL / 免版税 / 商业三种许可，闭源商用需确认条款 | Rust, C++ | llms.txt: https://slint.dev/llms.txt | 免费+付费 |
| [Syncfusion .NET MAUI Toolkit](https://github.com/syncfusion/maui-toolkit) | Syncfusion 开源（MIT）的 MAUI 控件包：图表、日历、轮播、底部 sheet 等；不想买商业套件时选 | .NET, C# | dotnet add package Syncfusion.Maui.Toolkit | 开源 |
| [tauri-ui](https://github.com/agmmnn/tauri-ui) | Tauri + shadcn/ui 桌面应用模板，带原生风格标题栏和发布工作流；想要小体积、好看的桌面应用起点时选 | Tauri, React, shadcn | `bunx create-tauri-ui@latest` | 开源 |
| [Uno Platform](https://platform.uno) | 用 WinUI / XAML 一套代码跑 Web（WASM）、移动和桌面的 .NET 平台；团队熟 WinUI 且要覆盖 Web 时选；有官方 MCP | .NET, C# | dotnet new install Uno.Templates<br>llms.txt: https://platform.uno/llms.txt（MCP 见 https://aka.platform.uno/mcp） | 开源 |
| [UraniumUI](https://uraniumui.gh.enisn-projects.io/) | .NET MAUI 的 Material 风 UI 套件（输入框、底部 sheet、表格、校验）并带项目模板；想让 MAUI 开箱好看时选 | .NET, C# | dotnet new install UraniumUI.Templates<br>dotnet new uraniumui-app -n MyMauiApp | 开源 |
| [Wails](https://wails.io) | 用 Go 写后端、Web 技术写界面的桌面应用框架，使用系统 WebView，体积小；Go 团队做桌面应用时选 | Go, Web | `go install github.com/wailsapp/wails/v3/cmd/wails3@v3.0.0`<br>llms.txt: https://wails.io/llms.txt | 开源 |
