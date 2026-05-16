# VER-20260516-009-runtime-ui-layout-fix-check

## 状态

- status: active
- source: 本地命令验证和静态检查
- updated: 2026-05-16

## 验证目标

验证用户截图反馈的运行时 UI 布局问题已修复：不再把所有界面包进全局滚动框，奖励页和资源条不再由布局压缩导致横向滚动或竖排显示。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| 全局滚动框回归检查 | `python tools\check_gdscript_sanity.py` | 通过 |
| GameSpec 数据和素材引用 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| 最小可玩链路数据闭合 | `python tools\smoke_playable_loop.py` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |
| 脚本高风险模式 | 检索 `scripts/` 中 `ScrollContainer`、`:=`、`.join(`、额外 `class` | 未命中 |

## 局限

当前命令行环境仍未发现 Godot 可执行入口，因此未执行 Godot headless 或实机截图验证。需要使用 Godot 4.6 编辑器运行项目确认视觉表现。

## 关联记录

- `CHG-20260516-009-runtime-ui-layout-fix`
- `ISSUES-20260516-001-playable-loop`
