# TASK-20260516-006-gameplay-ui-alignment-rework

## 状态

- status: draft
- source: 用户要求、整体功能与界面玩法对齐 v0.1、设计一致性门控复盘
- updated: 2026-05-16

## 目标

基于已确认的 v0.3 中国风手绘卡牌修仙 UI 目标，重新对齐第一阶段原型的整体功能、玩家界面和核心玩法方式，解决当前运行时中明显不符合设计目标和玩法目标的部分。

## 范围

允许后续开发修正：

- 13 个玩家可见界面的 `1920x1080` 运行时界面合同。
- 斗法、奖励、构筑洞府三个 P0 核心界面。
- 奖励三选一规则。
- 手动符箓嵌入和单卡槽位表达。
- 章节结算、奖励和商店中的硬编码展示。
- 必要的 GameSpec 字段补充、运行时状态补充和验证脚本补充。
- 实机截图对比记录。

## 禁止范围

- 不扩展完整内容量。
- 不新增未确认角色、章节或大规模卡牌池。
- 不切换引擎或重新引入 GDScript 运行时入口。
- 不把卡牌、敌人、奖励、装备、天赋或素材路径硬编码到 UI 脚本。
- 不用全局滚动框掩盖布局错误。
- 不把构建通过当成视觉完成。

## 成功标准

1. 每个玩家可见界面都有 `1920x1080` 合同、目标图、跳转、按钮、状态和截图验收规则。
2. 斗法界面构图、卡牌尺寸、敌我区域、手牌区、记录区和背景层级符合 v0.3 目标。
3. 奖励界面真正执行三选一，法器和额外奖励也以卡片化方式展示。
4. 构筑洞府支持玩家选择法门、符箓和槽位，不再只依赖自动荐符。
5. 重复卡可以拥有独立符箓链接状态。
6. 章节结算和商店展示从 GameSpec 或运行状态读取，不使用固定文案伪装。
7. 构建、数据、smoke、编码和关键界面截图对比验证通过。

## 验证方式

- `dotnet build WorldSeed.csproj`
- Godot .NET console 构建检查。
- Godot .NET headless 启动检查。
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`
- 关键界面截图对比记录。

## 子任务

- `SUB-20260516-011-screen-contracts-1080p`
- `SUB-20260516-012-runtime-screen-parity`
- `SUB-20260516-013-runtime-rule-parity`
- `SUB-20260516-014-visual-gameplay-verification`
