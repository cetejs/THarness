# VER-20260516-007-ui-screen-mockups-card-style-check

## 状态

- status: active
- source: 本地命令验证和人工检查
- updated: 2026-05-16

## 验证目标

验证参考卡牌示例风格后的界面视觉效果图草案已生成、已写入设计文档，并保持文本编码正常。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| 效果图生成 | `python WorldSeed.Experiments\ui-screen-mockups-20260516\render_ui_mockups_card_style.py` | 通过 |
| 效果图数量 | 检查 `ui-screen-mockups-v0.3` 下 15 个 PNG | 通过 |
| 单界面图分辨率 | 检查 13 个界面图均为 1280x720 | 通过 |
| 总览图分辨率 | 检查 `ui-000-overview.png` 为 1280x1232 | 通过 |
| 元素参考图分辨率 | 检查 `ui-014-style-reference.png` 为 1600x1100 | 通过 |
| 文档引用 | 检查 `ui-screen-visual-spec-v0.3.md` 引用 13 个界面图、1 个总览图和 1 个元素参考图 | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |

## 局限

当前效果图是静态视觉草案，不是 Godot 实机截图，也不是最终商业美术资产。用户确认 v0.3 后，后续开发应拆出正式 UI 资产清单，并在 Godot 中实现后补充实机截图验证。

## 关联记录

- `CHG-20260516-007-ui-screen-mockups-card-style`
- `WorldSeed.AIGC/wiki/design/ui-screen-visual-spec-v0.3.md`
