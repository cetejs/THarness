# VER-20260516-018-ui-design-parity-workflow-gate-check

## 状态

- status: active
- source: 本地文档和工作流检查
- updated: 2026-05-16

## 验证目标

验证斗法界面设计一致性复盘已经写入项目运行记录，并且通用经验已经同步到 THarness 游戏开发生命周期工作流，没有进入代码实现。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| THarness 回归 | `python THarness\tools\test_oneharness.py` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |
| 关键词检查 | `rg -n "设计稿到运行时|设计实现一致性|CHG-20260516-018|VER-20260516-018|RUN-20260516-007" THarness WorldSeed.AIGC` | 通过 |

## 通过范围

- 通用工作流增加设计实现一致性门控。
- 项目运行记录说明本次斗法界面差异原因。
- 本次没有修改 Godot 运行时代码。

## 局限

本记录只验证流程和文档更新，不验证斗法界面视觉修复结果。

## 关联记录

- `CHG-20260516-018-ui-design-parity-workflow-gate`
- `RUN-20260516-007-combat-ui-design-parity-retro`
