# VER-20260516-027-game-lifecycle-project-sync-check

## 状态

- status: active
- source: `CHG-20260516-026-game-lifecycle-project-sync`
- updated: 2026-05-16

## 验证目标

确认通用游戏开发生命周期工作流新增的项目侧执行同步门控、模板、能力索引和 THarness 自检保持可用。

## 验证项

| 验证项 | 命令 | 结果 |
| --- | --- | --- |
| THarness 自检 | `python THarness\tools\test_oneharness.py` | 通过，10 个测试通过。 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过，扫描 410 个文本文件。 |
| Git 空白检查 | `git diff --check` | 通过，无尾随空白或空白错误；存在 CRLF 将被 Git 归一化的提示。 |

## 验证范围

- 已检查 `game-development-lifecycle` 工作流包含项目侧执行同步阶段和完成标准。
- 已检查阶段门控包含项目侧执行同步门禁。
- 已检查验证复盘规则包含项目侧同步检查。
- 已检查项目侧执行同步模板已在模板索引登记。
- 已检查能力索引和版本记录包含项目侧执行同步说明。
- 未运行 Godot 工程，因为本次只修改通用工作流文档、模板、能力索引和 THarness 自检。

## 结论

验证通过。通用游戏开发生命周期工作流已补齐项目侧执行同步承接物，后续项目交付不能只停留在运行记录或通用流程更新，需要检查目标项目适配层入口和看板是否一致。
