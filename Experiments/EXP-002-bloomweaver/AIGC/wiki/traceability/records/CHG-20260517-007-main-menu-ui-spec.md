# 主界面 UI 开发规格案变更记录

## 状态

- status: active
- source: 用户确认的主界面 UI 开发规格案落地请求
- updated: 2026-05-17

## 来源

- 用户请求：将主界面 UI 开发规格案落成文档，供其他人评审。
- 关联需求：UI 开发策划角色；UI 最小拆分规则。
- 关联决策：主界面按一张背景、Logo、四个按钮和版本号执行最小拆分。
- 关联实验：EXP-002-bloomweaver
- 关联开发任务：无

## 新增内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 新增 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/design/ui-screen-specs/INDEX.md` | 建立单界面 UI 开发规格案索引。 |
| 新增 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/design/ui-screen-specs/main-menu-ui-spec.md` | 保存主界面完整 UI 开发规格案。 |
| 修改 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/design/INDEX.md` | 增加单界面 UI 规格案读取入口。 |
| 修改 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/traceability/records/INDEX.md` | 登记本次 CHG/VER 记录。 |

## 影响范围

影响主界面 UI 后续评审、程序施工、美术切图和 QA 验收。该变更不修改游戏工程代码或素材文件。

## 验证方式

- 检查新增规格案是否包含基本信息、效果图绑定、层级、`1920x1080` 布局、文本、控件、数据、状态、素材、一致性验收和未决问题。
- 检查设计索引和追溯索引是否可达。
- 运行仓库文本编码检查。

## 验证结果

已通过，见 `VER-20260517-007-main-menu-ui-spec-check.md`。

## 是否晋升为项目事实

是。该规格案作为实验二主界面 UI 施工和评审依据。

## 后续事项

需要用户、美术或程序确认未决问题后，才能进入主界面 UI 实际施工。
