# VER-20260516-029-workflow-knowledge-hardening-check

## 状态

- status: active
- source: `CHG-20260516-028-workflow-knowledge-hardening`
- updated: 2026-05-16

## 验证目标

确认 UI 节点生命周期排查规则、项目 wiki 追溯闭合规则、WorldSeed 追溯规则和 THarness 自检已同步更新。

## 验证项

| 验证项 | 命令 | 结果 |
| --- | --- | --- |
| THarness 自检 | `python THarness\tools\test_oneharness.py` | 通过，11 个测试通过。 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过，扫描 412 个文本文件。 |
| Git 空白检查 | `git diff --check` | 通过，无尾随空白或空白错误；存在 CRLF 将被 Git 归一化的提示。 |

## 验证范围

- 检查 `debug-observability.md` 包含 UI 节点生命周期检查、`RemoveChild` 和 `QueueFree` 规则。
- 检查 `project-wiki-update.md` 包含追溯闭合要求、最大编号、`records/INDEX.md`、CHG 和 VER 检查。
- 检查 WorldSeed 追溯规则和 ID 规则包含编号顺延、索引文件存在性和互相引用要求。
- 未运行 Godot 工程，因为本次只修改通用工作流、项目文档规则、能力索引和 THarness 自检。

## 结论

验证通过。UI 节点生命周期排查规则、项目 wiki 追溯闭合规则、WorldSeed 追溯规则和 THarness 自检已同步更新。
