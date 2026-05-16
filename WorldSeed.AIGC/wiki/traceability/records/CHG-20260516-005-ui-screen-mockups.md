# CHG-20260516-005-ui-screen-mockups

## 状态

- status: active
- source: 用户请求、第一阶段占位素材
- updated: 2026-05-16

## 来源

- 用户请求：在继续开发前，先绘制每个界面的效果图，并补充到界面文档中供确认。
- 关联设计草案：`ui-screen-visual-spec-v0.1.md`
- 关联素材：`assets/`

## 新增内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 设计文档 | `WorldSeed.AIGC/wiki/design/ui-screen-visual-spec-v0.1.md` | 记录 13 个玩家可见界面的视觉效果图和待确认点。 |
| 效果图 | `WorldSeed.AIGC/wiki/design/images/ui-screen-mockups-v0.1/` | 保存 13 个界面图和 1 个总览图。 |
| 生成脚本 | `WorldSeed.Experiments/ui-screen-mockups-20260516/render_ui_mockups.py` | 使用现有占位素材合成界面效果图，保留生成过程。 |
| 设计索引 | `WorldSeed.AIGC/wiki/design/INDEX.md` | 登记界面视觉规格文档入口。 |
| 未确认问题 | `WorldSeed.AIGC/wiki/open-questions.md` | 登记视觉效果图待用户确认。 |

## 影响范围

- 新增视觉确认材料。
- 不修改 Godot 运行时代码。
- 不把本视觉草案标记为已确认开发目标。

## 验证方式

- 检查效果图数量和分辨率。
- 检查设计文档是否引用所有效果图。
- 运行文本编码检查。

## 验证结果

已通过 `VER-20260516-005-ui-screen-mockups-check` 验证。

## 是否晋升为项目事实

否。当前仅表示视觉草案已产出，具体 UI 方案等待用户确认。
