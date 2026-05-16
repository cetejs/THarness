# VER-20260516-011-combat-card-frame-visual-fix-check

## 状态

- status: active
- source: 本地命令验证和静态检查
- updated: 2026-05-16

## 验证目标

验证斗法卡牌视觉修复没有破坏脚本基础约束、GameSpec 数据引用、最小可玩链路和文本编码。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| GDScript 静态风险检查 | `python tools\check_gdscript_sanity.py` | 通过 |
| GameSpec 数据和素材引用 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| 最小可玩链路数据闭合 | `python tools\smoke_playable_loop.py` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |

## 通过范围

- `scripts/Main.gd` 的卡牌组件已使用 `TextureRect` 加载 `assets/cards/*.png` 卡框纹理。
- `assets/cards/` 下五类卡框已替换为浅色卷轴风格。
- 斗法页顶部使用专用页眉和资源徽章，不再显示上一跳红字提示。

## 局限

当前命令行环境仍未发现 Godot 可执行入口，因此未执行 Godot 实机截图验证。需要使用 Godot 4.6 编辑器重新运行斗法节点确认视觉效果。

## 关联记录

- `CHG-20260516-011-combat-card-frame-visual-fix`
- `ISSUES-20260516-001-playable-loop`
