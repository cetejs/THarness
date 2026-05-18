# CHG-20260517-002-ui-development-planner-role

## 状态

- status: active
- source: 用户确认实验二先定义 UI 策划角色
- updated: 2026-05-17

## 来源

- 用户请求：先不讨论具体程序开发，聚焦策划如何写出 UI 案子，并定义一个 UI 策划角色。
- 关联需求：无独立 REQ，来自本次用户请求。
- 关联决策：实验二阶段性目标聚焦 UI 策划案质量验证。
- 关联实验：`EXP-002-bloomweaver`
- 关联开发任务：无。本次不进入程序开发。

## 新增内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 角色定义 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/design/ui-development-planner-role.md` | 定义 UI 开发策划的职责、边界、输入输出和禁用写法。 |
| 规格模板 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/design/ui-screen-development-spec-template.md` | 给后续单界面验证提供可填写的 UI 开发规格案模板。 |
| 验收清单 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/design/ui-planning-validation-checklist.md` | 判断 UI 策划案是否足以交给程序按案开发。 |
| 设计索引 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/design/INDEX.md` | 让新增文档可按 `read_when` 检索。 |

## 影响范围

- 只影响实验二项目 wiki 的设计文档。
- 不创建程序开发任务。
- 不修改工程代码。
- 不晋升到 `AIGC.Framework/`。

## 验证方式

- 检查新增文档存在。
- 检查 `design/INDEX.md` 可检索新增文档。
- 检查 CHG、VER 和 `records/INDEX.md` 互相引用。
- 运行 `python tools\check_text_encoding.py`。
- 运行 `git diff --check`。

## 验证结果

见 `VER-20260517-002-ui-development-planner-role-check`。

## 是否晋升为项目事实

是。UI 开发策划角色作为实验二项目级策划验证规则写入 BloomWeaver 项目 wiki。

## 后续事项

- 用户新开界面验证后，记录 UI 策划案实际缺口。
- 根据验证结果判断是否调整角色定义、模板或验收清单。
- 通过多轮验证后，再讨论是否晋升到通用框架。
