# VER-20260515-001 文档入口检查

## 状态

- status: active
- source: 本轮手动命令验证
- updated: 2026-05-15

## 验证目标

检查项目适配层、实验目录规划和追溯账本的关键入口存在，并确认 `THarness` 自检仍通过。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| 项目适配关键入口存在 | PowerShell `Test-Path` 检查 | 通过 |
| 实验关键入口存在 | PowerShell `Test-Path` 检查 | 通过 |
| `THarness` 门控 | `python tools\oneharness.py gate` | 通过 |
| `THarness` 单元测试 | `python -m unittest tools.test_oneharness` | 通过，8 个测试 OK |

## 局限

- 当前只验证文档入口和通用 harness 自检。
- 尚未有 Godot 工程，因此无法验证 Godot 运行链路。

## 关联记录

- `CHG-20260515-001-project-adapter-init`
- `CHG-20260515-002-experiment-planning`
- `CHG-20260515-003-traceability-ledger`

