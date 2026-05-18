# 主界面 UI 规格案评审修正变更记录

## 状态

- status: active
- source: 用户转述的主界面 UI 规格案评审反馈
- updated: 2026-05-17

## 来源

- 用户请求：针对其他 AI 反馈的问题给出方案并确认无问题后更新文档。
- 关联需求：主界面 UI 开发规格案评审。
- 关联决策：当前主界面为可评审但不可最终施工，背景验收采用可验收一致。
- 关联实验：EXP-002-bloomweaver
- 关联开发任务：无

## 新增内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 修改 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/design/ui-screen-specs/main-menu-ui-spec.md` | 补充施工准入状态、坐标定义、字体施工字段、九宫格拉伸规则，并修正 `startLabel` 数据绑定。 |
| 新增 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/traceability/records/CHG-20260517-008-main-menu-ui-spec-review-fixes.md` | 登记本次评审修正。 |
| 新增 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/traceability/records/VER-20260517-008-main-menu-ui-spec-review-fixes-check.md` | 登记本次修正验证。 |
| 修改 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/traceability/records/INDEX.md` | 登记本次 CHG/VER 记录。 |

## 影响范围

影响主界面 UI 规格案的评审口径、施工准入判断、布局坐标解释、文本字体约束、素材九宫格使用方式和验收口径。

## 验证方式

- 检查主界面 UI 规格案是否包含施工准入状态。
- 检查 `x / y / w / h` 是否明确为最终渲染矩形，不是 anchoredPosition。
- 检查 `main-menu-start-button` 数据来源是否为 `startLabel`。
- 检查文本与字体合同是否包含字体资源、字重、行高、字距、描边和阴影。
- 检查按钮素材是否明确源图尺寸和运行时目标尺寸的关系。
- 运行仓库文本编码检查。

## 验证结果

已通过，见 `VER-20260517-008-main-menu-ui-spec-review-fixes-check.md`。

## 是否晋升为项目事实

是。该修正作为主界面 UI 开发规格案的正式评审修正。

## 后续事项

高阻塞未决问题确认前，主界面规格案只能用于评审和临时原型拆解，不能标记为最终施工就绪。
