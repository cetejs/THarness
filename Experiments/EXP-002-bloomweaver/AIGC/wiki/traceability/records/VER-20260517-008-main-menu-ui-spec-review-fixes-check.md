# 主界面 UI 规格案评审修正验证记录

## 状态

- status: active
- source: `CHG-20260517-008-main-menu-ui-spec-review-fixes.md`
- updated: 2026-05-17

## 验证目标

确认主界面 UI 规格案已根据评审反馈补齐施工准入、坐标定义、字体约束、数据绑定、九宫格拉伸和验收口径。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| 施工准入状态 | 检查 `main-menu-ui-spec.md` | 已补充“可评审 / 最终施工阻塞”状态。 |
| 坐标定义 | 检查布局合同说明 | 已明确 `x / y / w / h` 表示最终渲染矩形，不是 anchoredPosition。 |
| 数据绑定修正 | 检查 `main-menu-start-button` 素材或数据来源 | 已由 `title` 修正为 `startLabel`。 |
| 字体施工字段 | 检查文本与字体合同 | 已补充字体资源、字重、行高、字距、描边和阴影字段。 |
| 九宫格拉伸规则 | 检查素材合同 | 已明确 `560x100` 是源图尺寸，运行时按布局矩形九宫格拉伸。 |
| 追溯索引 | 检查 `traceability/records/INDEX.md` | 已登记 `CHG-20260517-008-main-menu-ui-spec-review-fixes` 和 `VER-20260517-008-main-menu-ui-spec-review-fixes-check`。 |
| 文本编码 | 运行 `python tools/check_text_encoding.py` | 通过，扫描 525 个文件。 |

## 局限

本次只修正文档，不确认实际美术素材、字体文件、目标引擎或 UI 系统。

## 关联记录

- `CHG-20260517-008-main-menu-ui-spec-review-fixes.md`
