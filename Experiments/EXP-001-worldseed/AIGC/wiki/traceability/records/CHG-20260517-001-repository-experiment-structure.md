# CHG-20260517-001-repository-experiment-structure

## 状态

- status: active
- source: 用户确认目录结构调整
- updated: 2026-05-17

## 变更

将仓库从单一 WorldSeed 项目结构调整为“通用 AIGC 框架 + 实验项目 + 报告归档”结构。

## 影响范围

| 类型 | 路径 | 说明 |
| --- | --- | --- |
| 通用框架 | `AIGC.Framework/` | 承接迁移前的通用框架内容和 OneHarness 工具。 |
| 实验入口 | `Experiments/` | 新增实验项目总入口。 |
| 实验一 | `Experiments/EXP-001-worldseed/` | 承接原 WorldSeed 项目事实、Godot 工程和实验产物。 |
| Godot 工程 | `Experiments/EXP-001-worldseed/project/` | 承接原根目录 Godot 工程。 |
| 实验一 AIGC | `Experiments/EXP-001-worldseed/AIGC/` | 承接迁移前的 WorldSeed 项目适配层。 |
| 报告 | `Reports/` | 新增通用框架晋升记录入口。 |
| 归档 | `Archive/` | 新增归档入口。 |

## 边界

- 本次只调整目录结构和入口文档。
- 不改变 Godot 运行时代码逻辑。
- 历史运行记录中的旧路径作为历史证据保留，不逐条改写。

## 验证

- `VER-20260517-001-repository-experiment-structure-check`
