# RUN-20260516-002-card-style-runtime-ui

## 状态

- status: completed
- source: 用户确认 v0.3 并要求进入开发
- updated: 2026-05-16

## 目标

基于已确认的 `ui-screen-visual-spec-v0.3.md`，将当前 Godot 最小可玩闭环改造成参考卡牌风格的完整第一阶段游戏体验。

## 执行边界

- 只实现第一阶段最小可玩闭环的 UI、体验文案和必要视觉配置。
- 不新增未确认玩法系统。
- 不重写战斗和奖励规则。
- 不修改 Godot 引擎源码。

## 验证计划

- GameSpec 数据和素材引用验证。
- 最小可玩链路 smoke 验证。
- GDScript 静态风险检查。
- 文本编码检查。
- 若本地发现 Godot 命令行入口，再补充启动验证；否则记录为局限。

## 当前进度

- 已确认 v0.3 为第一阶段 UI 开发目标。
- 已建立 `SUB-20260516-006-card-style-runtime-ui`。
- 已将运行时界面改为参考卡牌风格：主菜单、角色选择、灵脉图、斗法、奖励、构筑洞府、奇遇、灵市/锻炉、洞天结算、本局结算、设置、详情和确认界面均有可用入口。
- 已将主要术语统一为修仙语境：命元、罡气、灵力、灵石、法门、符箓、灵脉、洞天、斗法。
- 已保留原有战斗、奖励、事件和商店规则，只调整 UI 呈现和体验文案。

## 验证结果

| 验证项 | 命令 | 结果 |
| --- | --- | --- |
| GDScript 静态风险检查 | `python tools\check_gdscript_sanity.py` | 通过 |
| GameSpec 数据和素材引用 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| 最小可玩链路 smoke | `python tools\smoke_playable_loop.py` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |
| 已知高风险脚本模式 | 检索 `:=`、`.join(`、额外 `class` | 未命中 |
| Godot 命令行入口 | `where.exe godot` / `where.exe godot4` / `Get-Command godot` | 未发现，未执行 headless 启动验证 |

## 问题记录

本轮问题记录继续写入：

- `ISSUES-20260516-001-playable-loop.md`
