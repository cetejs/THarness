# VER-20260516-008-card-style-runtime-ui-check

## 状态

- status: active
- source: 本地命令验证和静态检查
- updated: 2026-05-16

## 验证目标

验证 v0.3 卡牌参考风格运行时 UI 已落地到第一阶段 Godot 可玩原型，且没有破坏 GameSpec 数据契约、最小可玩链路、GDScript 基础约束和文本编码。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| GDScript 静态风险检查 | `python tools\check_gdscript_sanity.py` | 通过 |
| GameSpec 数据和素材引用 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| 最小可玩链路数据闭合 | `python tools\smoke_playable_loop.py` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |
| 禁止/高风险脚本模式 | 检索 `scripts/` 中 `:=`、`.join(`、额外 `class` | 未命中 |
| Godot 命令行入口 | `where.exe godot`、`where.exe godot4`、`Get-Command godot` | 未发现 |

## 通过范围

- 数据配置可被验证工具读取并通过素材引用检查。
- 最小可玩闭环数据路径可完成 1 个角色、1 个章节和 6 个节点。
- `scripts/Main.gd` 已覆盖主菜单、角色选择、灵脉图、斗法、斗法奖励、构筑洞府、奇遇、灵市/锻炉、洞天结算、本局结算、设置、详情和确认界面。
- `scripts/GameRuntime.gd` 文案已进入修仙语境，规则逻辑未在本次扩展。

## 局限

当前命令行环境未发现 Godot 可执行入口，因此未执行 Godot headless 启动测试。需要使用 Godot 4.6 编辑器打开 `project.godot` 做实机运行确认。

## 关联记录

- `CHG-20260516-008-card-style-runtime-ui`
- `RUN-20260516-002-card-style-runtime-ui`
- `SUB-20260516-006-card-style-runtime-ui`
- `ISSUES-20260516-001-playable-loop`
