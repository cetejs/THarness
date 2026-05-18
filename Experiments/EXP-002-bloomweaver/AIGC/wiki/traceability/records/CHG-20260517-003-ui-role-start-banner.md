# CHG-20260517-003-ui-role-start-banner

## 状态

- status: active
- source: 用户要求角色开始工作时能分辨当前是谁
- updated: 2026-05-17

## 来源

- 用户请求：角色出来时需要固定文本，包含角色名称、主要职责和依据，方便分辨当前是谁在工作。
- 关联需求：无独立 REQ，来自本次用户请求。
- 关联决策：实验二 UI 开发策划角色需要出场固定声明。
- 关联实验：`EXP-002-bloomweaver`
- 关联开发任务：无。本次不进入程序开发。

## 新增内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 角色规则 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/design/ui-development-planner-role.md` | 新增“出场固定声明”，明确角色名称、主要职责和工作依据。 |
| 追溯索引 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/traceability/records/INDEX.md` | 登记本次变更和验证记录。 |

## 影响范围

- 只影响实验二 UI 开发策划角色文档。
- 不修改 UI 规格模板和验收清单。
- 不创建程序开发任务。
- 不晋升到 `AIGC.Framework/`。

## 验证方式

- 检查角色文档包含固定声明。
- 检查 CHG、VER 和 `records/INDEX.md` 互相引用。
- 运行 `python tools\check_text_encoding.py`。
- 运行 `git diff --check`。

## 验证结果

见 `VER-20260517-003-ui-role-start-banner-check`。

## 是否晋升为项目事实

是。出场固定声明作为实验二 UI 开发策划角色的项目级工作规则。

## 后续事项

- 后续使用该角色处理界面策划案时，先输出固定声明。
- 若验证中发现声明信息不足，再按实验二结果修订。
