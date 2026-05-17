# CHG-20260516-015-game-development-lifecycle-workflow

## 状态

- status: active
- source: 用户要求把开发过程经验总结为可复用游戏开发工作流
- updated: 2026-05-16

## 来源

- 用户指出本轮开发过程中很多经验可以抽象成开发工作流。
- 本次沉淀对象是跨项目通用方法，不是 WorldSeed 具体玩法事实。

## 变更内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 通用工作流 | `THarness/AIGC/workflows/game-development-lifecycle/WORKFLOW.md` | 新增游戏开发生命周期工作流，覆盖策划、视觉、数据、开发、排查、验证和复盘。 |
| 通用规则 | `THarness/AIGC/workflows/game-development-lifecycle/rules/` | 新增入口、阶段门控、垂直切片、UI 视觉运行时、可观测性和验证复盘规则。 |
| 通用模板 | `THarness/AIGC/workflows/game-development-lifecycle/templates/` | 新增生命周期计划、界面合同、运行时排查记录、验证复盘模板。 |
| 通用索引 | `THarness/AIGC/workflows/INDEX.md` | 增加 `game-development-lifecycle` 工作流入口和选择规则。 |
| 追溯记录 | `WorldSeed.AIGC/wiki/traceability/records/` | 登记本次通用流程沉淀来源和验证结果。 |

## 影响范围

- 影响 THarness 通用工作流索引。
- 不改变 WorldSeed 玩法、数据、UI、运行时或项目事实。
- 后续游戏项目可在准备、开发、排查和复盘时复用该工作流。

## 验证方式

- 检查通用工作流、规则和模板文件存在。
- 检查 `THarness/AIGC/workflows/INDEX.md` 已登记工作流。
- 执行文本编码检查。
- 执行 THarness 自检。

## 验证结果

已通过 `VER-20260516-015-game-development-lifecycle-workflow-check` 验证。

## 是否晋升为项目事实

否。本记录仅说明 WorldSeed 会话中触发了一次通用工作流沉淀；稳定方法本身写入 `THarness/AIGC`。
