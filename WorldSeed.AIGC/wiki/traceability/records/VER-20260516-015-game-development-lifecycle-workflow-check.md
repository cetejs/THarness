# VER-20260516-015-game-development-lifecycle-workflow-check

## 状态

- status: active
- source: 本地文档结构检查和编码检查
- updated: 2026-05-16

## 验证目标

验证通用游戏开发生命周期工作流已写入 THarness，索引可发现，且没有把具体项目事实写入通用流程。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| 工作流文件存在 | 检查 `THarness/AIGC/workflows/game-development-lifecycle/WORKFLOW.md` | 通过 |
| 规则索引存在 | 检查 `THarness/AIGC/workflows/game-development-lifecycle/rules/INDEX.md` | 通过 |
| 模板索引存在 | 检查 `THarness/AIGC/workflows/game-development-lifecycle/templates/INDEX.md` | 通过 |
| 通用索引登记 | 检查 `THarness/AIGC/workflows/INDEX.md` | 通过 |
| 通用流程边界 | 检查通用流程未写入 WorldSeed 专属事实 | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |
| THarness 自检 | `python THarness/tools/test_oneharness.py` | 通过 |

## 通过范围

- 新增通用工作流。
- 新增通用规则和模板。
- 新增追溯记录。

## 局限

本次验证只检查文档结构和编码，不验证某个具体游戏项目的执行效果。

## 关联记录

- `CHG-20260516-015-game-development-lifecycle-workflow`
