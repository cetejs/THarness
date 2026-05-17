# VER-20260516-028-game-iteration-ui-ux-spec-check

## 状态

- status: active
- source: `CHG-20260516-027-game-iteration-ui-ux-spec`
- updated: 2026-05-16

## 验证目标

确认游戏迭代工作流已补齐 UI/UX 可开发规格规则、模板、能力索引和自检保护。

## 验证项

| 验证项 | 命令 | 结果 |
| --- | --- | --- |
| THarness 自检 | `python THarness\tools\test_oneharness.py` | 通过，10 个测试通过。 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过，扫描 410 个文本文件。 |
| Git 空白检查 | `git diff --check` | 通过，无尾随空白或空白错误；存在 CRLF 将被 Git 归一化的提示。 |

## 验证范围

- 检查 `game-iteration` 能从规则索引路由到 `ui-ux-development-spec.md`。
- 检查模板索引包含 `ui-ux-development-spec.md`。
- 检查规则和模板包含目标视口、缩放策略、hitbox、素材边界和验收标准。
- 未运行 Godot 工程，因为本次只修改通用工作流文档、模板、能力索引和 THarness 自检。

## 结论

验证通过。游戏迭代工作流已补齐 UI/UX 可开发规格规则和模板，并由 THarness 自检覆盖关键路由和字段。
