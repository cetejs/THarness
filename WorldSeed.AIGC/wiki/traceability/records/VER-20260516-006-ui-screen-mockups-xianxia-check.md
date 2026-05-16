# VER-20260516-006-ui-screen-mockups-xianxia-check

## 状态

- status: active
- source: 本地命令验证和人工检查
- updated: 2026-05-16

## 验证目标

验证中国风手绘修仙方向界面视觉效果图草案已生成、已写入设计文档，并保持文本编码正常。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| 效果图生成 | `python WorldSeed.Experiments\ui-screen-mockups-20260516\render_ui_mockups_xianxia.py` | 通过 |
| 效果图数量 | 检查 `ui-screen-mockups-v0.2` 下 14 个 PNG | 通过 |
| 单界面图分辨率 | 检查 13 个界面图均为 1280x720 | 通过 |
| 总览图分辨率 | 检查 `ui-000-overview.png` 为 1280x1232 | 通过 |
| 文档引用 | 检查 `ui-screen-visual-spec-v0.2.md` 引用 13 个界面图和 1 个总览图 | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |

## 局限

当前效果图是静态视觉草案，不是 Godot 实机截图。用户确认 v0.2 后，后续开发应以该草案为目标在 Godot 中实现，并补充实机截图验证。

## 关联记录

- `CHG-20260516-006-ui-screen-mockups-xianxia`
- `WorldSeed.AIGC/wiki/design/ui-screen-visual-spec-v0.2.md`
