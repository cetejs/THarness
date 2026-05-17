# CHG-20260516-002-development-prep-gate

## 状态

- status: active
- source: 用户确认
- updated: 2026-05-16

## 来源

- 用户请求：补充进入开发前所需的主任务、接口契约、子任务和第一阶段范围。
- 关联需求：完整游戏开发前需要任务门控和数据契约。
- 关联决策：当前只补开发前门控文档，不进入代码、schema、配置或 Godot 实现。
- 关联实验：试制 UI 素材包作为第一阶段占位素材候选。
- 关联开发任务：`TASK-20260516-001-game-data-runtime-prep`

## 新增内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 主任务 | `WorldSeed.AIGC/wiki/development/tasks/TASK-20260516-001-game-data-runtime-prep.md` | 定义完整游戏数据层与最小运行闭环开发准备任务。 |
| 接口契约 | `WorldSeed.AIGC/wiki/development/contracts/CONTRACT-20260516-001-gamespec-runtime.md` | 定义 GameSpec 到 Godot 运行时的数据交接契约。 |
| 子任务 | `WorldSeed.AIGC/wiki/development/subtasks/data-SUB-20260516-001-first-stage-content-tables.md` | 拆分第一阶段内容表准备。 |
| 子任务 | `WorldSeed.AIGC/wiki/development/subtasks/gameplay-SUB-20260516-002-combat-build-rules.md` | 拆分战斗和构筑规则准备。 |
| 子任务 | `WorldSeed.AIGC/wiki/development/subtasks/ui-SUB-20260516-003-ui-flow-data.md` | 拆分 UI 流程数据准备。 |
| 子任务 | `WorldSeed.AIGC/wiki/development/subtasks/assets-SUB-20260516-004-asset-reference-plan.md` | 拆分素材引用计划。 |
| 子任务 | `WorldSeed.AIGC/wiki/development/subtasks/qa-SUB-20260516-005-first-stage-verification.md` | 拆分第一阶段验证计划。 |
| 索引更新 | `WorldSeed.AIGC/wiki/development/tasks/INDEX.md` | 登记主任务。 |
| 索引更新 | `WorldSeed.AIGC/wiki/development/contracts/INDEX.md` | 登记接口契约。 |
| 索引更新 | `WorldSeed.AIGC/wiki/development/subtasks/INDEX.md` | 登记子任务。 |
| 追溯索引更新 | `WorldSeed.AIGC/wiki/traceability/records/INDEX.md` | 登记本次变更和验证。 |

## 影响范围

- 影响后续进入开发的任务边界、接口契约和子任务拆分。
- 不影响代码、schema、配置数据、Godot 场景或生成器实现。

## 验证方式

- 检索开发索引是否包含主任务、契约和子任务。
- 检查任务文档是否包含目标、范围、禁止范围和验证方式。
- 检查契约文档是否包含输入、输出、错误处理、验证方式和禁止事项。
- 检查本次没有新增代码、schema 或 GameSpec 配置实现。

## 验证结果

已通过 `VER-20260516-002-development-prep-gate-check` 验证。

## 是否晋升为项目事实

是。作为进入开发前的任务门控文档，但不代表已经开始代码实现。

## 后续事项

- 用户明确确认“进入开发”后，才能创建实际 schema、数据文件、Godot 场景或验证脚本。
