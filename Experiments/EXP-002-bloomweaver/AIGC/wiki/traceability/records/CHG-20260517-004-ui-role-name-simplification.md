# CHG-20260517-004-ui-role-name-simplification

## 状态

- status: active
- source: 用户确认角色命名
- updated: 2026-05-17

## 来源

- 用户请求：角色名字叫 `UI 开发策划` 即可。
- 关联需求：无独立 REQ，来自本次用户请求。
- 关联决策：实验二 UI 策划角色统一命名为 `UI 开发策划`。
- 关联实验：`EXP-002-bloomweaver`
- 关联开发任务：无。本次不进入程序开发。

## 新增内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 角色命名 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/design/ui-development-planner-role.md` | 将角色名称统一为 `UI 开发策划`。 |
| 相关文档 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/design/` | 同步模板、索引和说明中的角色名称。 |
| 追溯记录 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/traceability/records/` | 保持正式内容命名一致。 |

## 影响范围

- 只调整实验二项目 wiki 中的角色名称。
- 不改变角色职责、模板字段和验收清单。
- 不修改文件名，避免破坏既有链接。
- 不晋升到 `AIGC.Framework/`。

## 验证方式

- 检查角色文档固定声明为 `【当前角色】UI 开发策划`。
- 检查实验二 wiki 中不再出现旧角色名称。
- 检查 CHG、VER 和 `records/INDEX.md` 互相引用。
- 运行 `python tools\check_text_encoding.py`。
- 运行 `git diff --check`。

## 验证结果

见 `VER-20260517-004-ui-role-name-simplification-check`。

## 是否晋升为项目事实

是。`UI 开发策划` 是实验二当前确认的角色名称。

## 后续事项

- 后续该角色出场时使用 `UI 开发策划`。
