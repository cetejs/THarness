# CHG-20260516-006-ui-screen-mockups-xianxia

## 状态

- status: active
- source: 用户反馈、v0.1 界面效果图
- updated: 2026-05-16

## 来源

- 用户请求：将界面风格改成中国风、手绘风格，并带修仙元素。
- 关联设计草案：`ui-screen-visual-spec-v0.2.md`
- 被替换草案：`ui-screen-visual-spec-v0.1.md`

## 新增内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 设计文档 | `WorldSeed.AIGC/wiki/design/ui-screen-visual-spec-v0.2.md` | 记录中国风手绘修仙方向的 13 个界面效果图和待确认点。 |
| 效果图 | `WorldSeed.AIGC/wiki/design/images/ui-screen-mockups-v0.2/` | 保存中国风手绘版 13 个界面图和 1 个总览图。 |
| 生成脚本 | `WorldSeed.Experiments/ui-screen-mockups-20260516/render_ui_mockups_xianxia.py` | 使用本地绘制脚本生成可复现的中国风手绘界面草案。 |
| 设计索引 | `WorldSeed.AIGC/wiki/design/INDEX.md` | 登记 v0.2 视觉规格文档入口。 |
| 未确认问题 | `WorldSeed.AIGC/wiki/open-questions.md` | 登记 v0.2 视觉效果图待用户确认。 |

## 影响范围

- 新增视觉确认材料。
- 不修改 Godot 运行时代码。
- 不修改 GameSpec 数据。
- 不把 v0.2 视觉草案标记为已确认开发目标。

## 验证方式

- 检查效果图数量和分辨率。
- 检查设计文档是否引用所有效果图。
- 运行文本编码检查。

## 验证结果

已通过 `VER-20260516-006-ui-screen-mockups-xianxia-check` 验证。

## 是否晋升为项目事实

否。当前仅表示中国风手绘修仙方向视觉草案已产出，等待用户确认。
