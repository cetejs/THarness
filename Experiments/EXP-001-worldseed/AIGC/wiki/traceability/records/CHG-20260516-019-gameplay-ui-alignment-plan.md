# CHG-20260516-019-gameplay-ui-alignment-plan

## 状态

- status: active
- source: 用户要求重新梳理整体功能并解决不符合的界面和游戏方式
- updated: 2026-05-16

## 来源

用户要求基于已更新的设计一致性工作流，对游戏整体功能进行重新梳理，并处理不符合的界面和游戏方式。

## 变更内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 设计结论 | `WorldSeed.AIGC/wiki/design/gameplay-ui-alignment-v0.1.md` | 记录整体功能、界面和玩法方式对齐结论。 |
| 开发任务 | `WorldSeed.AIGC/wiki/development/tasks/TASK-20260516-006-gameplay-ui-alignment-rework.md` | 建立后续修正任务边界。 |
| 子任务 | `WorldSeed.AIGC/wiki/development/subtasks/ui-SUB-20260516-011-screen-contracts-1080p.md` | 拆分 1080p 界面合同工作。 |
| 子任务 | `WorldSeed.AIGC/wiki/development/subtasks/ui-SUB-20260516-012-runtime-screen-parity.md` | 拆分运行时界面一致性修正。 |
| 子任务 | `WorldSeed.AIGC/wiki/development/subtasks/gameplay-SUB-20260516-013-runtime-rule-parity.md` | 拆分玩法规则一致性修正。 |
| 子任务 | `WorldSeed.AIGC/wiki/development/subtasks/qa-SUB-20260516-014-visual-gameplay-verification.md` | 拆分视觉和玩法验证。 |
| 接口契约 | `WorldSeed.AIGC/wiki/development/contracts/CONTRACT-20260516-003-screen-runtime-parity.md` | 定义 v0.3 设计稿到运行时界面的交接契约。 |
| 运行记录 | `WorldSeed.AIGC/workflows/development/runs/RUN-20260516-008-overall-feature-ui-alignment.md` | 记录本次梳理过程。 |

## 影响范围

- 影响后续 UI 和玩法修正的任务边界。
- 不修改 Godot 工程代码。
- 不修改 GameSpec 样例数据。

## 验证方式

- `python tools\check_text_encoding.py --root .`
- `rg -n "gameplay-ui-alignment|TASK-20260516-006|CONTRACT-20260516-003|SUB-20260516-011|SUB-20260516-012|SUB-20260516-013|SUB-20260516-014|RUN-20260516-008|CHG-20260516-019|VER-20260516-019" WorldSeed.AIGC`

## 验证结果

已通过 `VER-20260516-019-gameplay-ui-alignment-plan-check` 验证。

## 是否晋升为项目事实

是。后续修正应先处理 P0 对齐项，再继续扩展内容量。
