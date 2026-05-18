# EXP-002-bloomweaver Wiki 入口

默认只读本索引。按任务意图命中 `read_when` 后，再读取对应文件。

| 文件 | read_when |
| --- | --- |
| `SCHEMA.md` | 需要创建、修改或审查项目 wiki 页面格式。 |
| `project.md` | 需要了解项目目标、范围、非目标和产品方向。 |
| `status.md` | 需要了解当前阶段、可执行入口或阻塞状态。 |
| `architecture/INDEX.md` | 需要检索技术路线、模块边界或配置面。 |
| `source-map/INDEX.md` | 需要追溯重要文件、构建测试命令或外部来源。 |
| `design/INDEX.md` | 需要检索 BloomWeaver 策划案、玩法、UI、素材和迁移 GDD。 |
| `development/INDEX.md` | 需要检索开发任务、子任务或接口契约入口。 |
| `traceability/INDEX.md` | 需要追溯新增内容、来源、验证和变更记录。 |
| `decisions/INDEX.md` | 需要查看已确认、废弃或待确认决策。 |
| `workflows/INDEX.md` | 需要查看项目内开发、验证或维护流程约束。 |
| `rules/INDEX.md` | 需要查看项目 wiki 的读取、写入和健康检查规则。 |
| `open-questions.md` | 需要确认未决问题或阻塞。 |

## 写入边界

- 稳定项目事实写入对应 wiki 页面。
- 策划案和功能设计写入 `design/`。
- 实验过程、输入、输出、日志和截图写入 `../../inputs/`、`../../outputs/` 或 `../../validation/`。
- 正式新增内容必须在 `traceability/records/` 中登记。
- 未确认内容写入 `open-questions.md`。
- 通用规则写入 `../../../../AIGC.Framework`，不写入本项目 wiki。
