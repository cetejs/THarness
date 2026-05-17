# CHG-20260516-018-ui-design-parity-workflow-gate

## 状态

- status: active
- source: 用户要求复盘斗法界面差异并同步更新工作流
- updated: 2026-05-16

## 来源

用户指出斗法界面与设计稿差异较大，并要求总结开发流程问题，同时更新可复用游戏开发工作流。

## 变更内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 通用工作流 | `THarness/AIGC/workflows/game-development-lifecycle/WORKFLOW.md` | 增加设计实现一致性门控。 |
| 通用规则 | `THarness/AIGC/workflows/game-development-lifecycle/rules/ui-visual-runtime.md` | 补充设计稿到运行时合同、常见偏差来源和 UI 完成判定。 |
| 通用模板 | `THarness/AIGC/workflows/game-development-lifecycle/templates/screen-contract.md` | 增加设计对齐字段。 |
| 通用模板 | `THarness/AIGC/workflows/game-development-lifecycle/templates/verification-retro.md` | 增加设计一致性复盘字段。 |
| 项目运行记录 | `WorldSeed.AIGC/workflows/development/runs/RUN-20260516-007-combat-ui-design-parity-retro.md` | 记录本次斗法界面差异复盘。 |

## 影响范围

- 影响后续游戏 UI 开发的流程门控和文档模板。
- 不修改 Godot 工程代码、玩法数据、素材和界面实现。
- 不把 WorldSeed 项目事实写入 THarness；THarness 只保留可复用方法。

## 验证方式

- `python THarness\tools\test_oneharness.py`
- `python tools\check_text_encoding.py --root .`
- `rg -n "设计稿到运行时|设计实现一致性|CHG-20260516-018|VER-20260516-018|RUN-20260516-007" THarness WorldSeed.AIGC`

## 验证结果

已通过 `VER-20260516-018-ui-design-parity-workflow-gate-check` 验证。

## 是否晋升为项目事实

是。WorldSeed 后续 UI 实现需要先完成目标设计稿到运行时界面合同，再进入工程修正。
