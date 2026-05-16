# VER-20260516-026-game-lifecycle-workflow-hardening-check

## 状态

- status: active
- source: `CHG-20260516-025-game-lifecycle-workflow-hardening`
- updated: 2026-05-16

## 验证目标

确认通用游戏开发生命周期工作流加固后，模板、规则、能力索引和 THarness 自检保持可用。

## 验证项

| 验证项 | 命令 | 结果 |
| --- | --- | --- |
| THarness 自检 | `python THarness\tools\test_oneharness.py` | 通过，10 个测试通过。 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过，扫描 401 个文本文件。 |
| Git 空白检查 | `git diff --check` | 通过，无尾随空白或空白错误。 |

## 验证范围

- 已检查 `game-development-lifecycle` 能从工作流索引和能力索引路由。
- 已检查开发前硬门禁、素材管线合同、UI hitbox、交互验证和关键控件证据字段存在。
- 未运行 Godot 工程，因为本次仅修改通用工作流文档和 THarness 自检，不涉及运行时代码。

## 结论

验证通过。通用游戏开发生命周期工作流已补齐开发前硬门禁、素材管线、UI hitbox 和真实交互验收承接物。
