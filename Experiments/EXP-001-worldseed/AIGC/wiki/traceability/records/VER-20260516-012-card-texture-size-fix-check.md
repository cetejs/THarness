# VER-20260516-012-card-texture-size-fix-check

## 状态

- status: active
- source: 本地命令验证和静态检查
- updated: 2026-05-16

## 验证目标

验证卡牌纹理容器固定尺寸修复没有破坏脚本基础约束、GameSpec 数据引用、最小可玩链路和文本编码。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| 卡牌尺寸回归和 GDScript 静态检查 | `python tools\check_gdscript_sanity.py` | 通过 |
| GameSpec 数据和素材引用 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| 最小可玩链路数据闭合 | `python tools\smoke_playable_loop.py` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |

## 通过范围

- `scripts/Main.gd` 中卡牌外层 `box` 使用收缩布局。
- `scripts/Main.gd` 中卡牌画布 `card_panel` 锁定为 `Vector2(width, height)`。
- 卡牌画布开启裁剪，卡面不会越界覆盖父面板内容。

## 局限

当前命令行环境仍未发现 Godot 可执行入口，因此未执行 Godot 实机截图验证。需要使用 Godot 4.6 编辑器重新运行主菜单和斗法界面确认视觉效果。

## 关联记录

- `CHG-20260516-012-card-texture-size-fix`
- `ISSUES-20260516-001-playable-loop`
