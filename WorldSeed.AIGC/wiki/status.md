# 当前状态

## 状态

- status: active
- source: 代码扫描和用户确认
- updated: 2026-05-16

## 当前阶段

第一阶段最小可玩闭环原型，运行时已迁移为 Godot .NET/C#。

## 已完成

- 已拉取 `https://github.com/cetejs/WorldSeed.git`。
- 已加入 `THarness/` 通用 AIGC 工作流框架。
- 已确认为 WorldSeed 建立独立项目适配层。
- 已确认实验需要独立目录规划，避免污染正式项目事实。
- 已确认正式新增内容需要追溯账本。
- 已完成第一阶段 Godot 最小可玩闭环原型：1 个角色、1 个章节、1 个 Boss，覆盖主菜单到结算。
- 已将占位美术素材接入主菜单、角色选择、地图、战斗、奖励、构筑、事件、商店和结算界面。
- 已将 v0.3 中国风手绘修仙卡牌参考风格落地到 Godot 运行时 UI，覆盖主菜单、角色选择、灵脉图、斗法、奖励、构筑洞府、奇遇、灵市/锻炉、洞天结算、本局结算、设置、详情和确认界面。
- 已确认 `E:\Godot\4.6.2-stable` 为普通 Godot，不作为后续开发入口。
- 已下载并确认 Godot .NET 4.6.2：`E:\Godot\4.6.2-stable-mono\Godot_v4.6.2-stable_mono_win64\`。
- 已将运行时代码迁移到 C#，主场景挂载 `scripts/Main.cs`。
- 已加入 `[WorldSeed/UI]` 布局日志，用于继续排查界面拉伸、错位和卡牌尺寸问题。
- 已将运行窗口缩放策略改为 1920x1080 默认逻辑画布整体缩放，并补充斗法页独立响应式尺寸配置。
- 已替换第一阶段正式验收资源包，覆盖卡牌框、图标、灵脉节点、状态图标、UI 面板和按钮资源。
- 已修复 Godot MCP 验收发现的斗法手牌按钮越界问题，真实 UI 可完成斗法、奖励、构筑并返回灵脉图。
- 已替换运行时背景为低对比水墨远山风格，并完成 Godot MCP 主菜单、斗法和按钮点击验证。
- 已移除地图、斗法和其他界面的空资源徽章占位栏，斗法顶部恢复显示玩家命元、罡气、灵力和灵石。
- 已升级卡面视觉：五类卡框具备不同主体纹样，卡面包含费用灵珠、门类竖签、题签、插画区、规则题签、效果区和底部类型条。
- 已将占位视觉、截图不能替代交互、导入缓存和公共组件复查等问题沉淀到 `THarness/AIGC/workflows/game-development-lifecycle/`。

## 当前事实

- 当前仓库包含 Godot 工程入口 `project.godot`。
- 当前仓库包含第一阶段 GameSpec 样例数据和 Godot .NET/C# 运行时原型。
- 当前运行时入口文件为 `scripts/Main.cs`、`scripts/GameRuntime.cs`、`scripts/GameSpecLoader.cs`。
- 当前 C# 项目文件为 `WorldSeed.csproj`，Godot assembly 名称为 `WorldSeed`。
- 当前运行窗口使用 `viewport + expand` stretch，避免控件按小窗口重新挤压布局。
- 当前默认逻辑分辨率为 `1920x1080`。
- 当前斗法页顶部显示玩家关键数据：命元、罡气、灵力和灵石。
- 当前卡牌内部文字随卡面高度缩放，避免小卡标题和类型被裁剪。
- 当前仓库包含第一阶段卡牌化修仙 UI 运行时实现，关键术语为命元、罡气、灵力、灵石、法门、符箓、灵脉、洞天和斗法。
- 当前仓库已接入第一阶段正式验收资源包，资源预览图位于 `assets/preview/acceptance_asset_pack_preview.png`。
- 当前运行时背景资源为 `assets/ui/background_ink_landscape.png`，由 `data/game_spec/ascension_forge.prototype.json` 的 `assets.ui.background` 配置。
- 当前仓库尚未包含对话到游戏的生成器。
- 当前仓库尚未包含自动导出链路。
- 当前命令行环境已完成 Godot .NET headless 构建和启动验证。

## 下一步入口

继续基于 `TASK-20260516-006-gameplay-ui-alignment-rework` 做完整界面验收，重点检查斗法以外的奖励、构筑、奇遇、商店和结算界面是否仍存在与 v0.3 目标图不一致的布局问题。

## 验证

读取本页面后，应能判断当前第一阶段可玩原型已可使用 Godot .NET 编辑器运行确认；新增业务代码默认使用 C#，不得重新引入 GDScript 运行时入口。
