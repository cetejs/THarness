# VER-20260516-010-runtime-ui-stretch-fix-check

## 状态

- status: active
- source: 本地命令验证和静态检查
- updated: 2026-05-16

## 验证目标

验证运行窗口放大后游戏画面不再固定居中露出黑边，项目保留 stretch 配置，根 `Control` 在运行时跟随 viewport 尺寸。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| stretch 配置和 GDScript 静态风险检查 | `python tools\check_gdscript_sanity.py` | 通过 |
| GameSpec 数据和素材引用 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| 最小可玩链路数据闭合 | `python tools\smoke_playable_loop.py` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |

## 局限

当前命令行环境仍未发现 Godot 可执行入口，因此未执行 Godot 实机截图验证。需要使用 Godot 4.6 编辑器重新运行项目确认窗口铺满效果。

## 关联记录

- `CHG-20260516-010-runtime-ui-stretch-fix`
- `ISSUES-20260516-001-playable-loop`
