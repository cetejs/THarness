# WorldSeed Wiki 入口

默认只读本索引。按任务意图命中 `read_when` 后，再读取对应文件。

| 文件 | read_when |
| --- | --- |
| `SCHEMA.md` | 需要创建、修改或审查项目 wiki 页面格式。 |
| `project.md` | 需要了解项目目标、范围、非目标和产品方向。 |
| `status.md` | 需要了解当前阶段、可执行入口或阻塞状态。 |
| `architecture/INDEX.md` | 需要检索 Godot 技术路线、AI 生成链路、模块边界或配置面。 |
| `source-map/INDEX.md` | 需要追溯重要文件、构建测试命令或外部服务。 |
| `design/INDEX.md` | 需要检索玩法、UI、音频、动画、数值或可玩性要求。 |
| `development/INDEX.md` | 需要检索开发任务、子任务、接口契约或验收入口。 |
| `experiments/INDEX.md` | 需要规划、执行、复核或沉淀实验。 |
| `traceability/INDEX.md` | 需要追溯新增内容、来源、验证和变更记录。 |
| `decisions/INDEX.md` | 需要查看已确认、废弃或待确认决策。 |
| `workflows/INDEX.md` | 需要查看项目内开发、验证或维护流程约束。 |
| `rules/INDEX.md` | 需要查看项目 wiki 的读取、写入和健康检查规则。 |
| `open-questions.md` | 需要确认未决问题或阻塞。 |

## 写入边界

- 稳定项目事实写入对应 wiki 页面。
- 实验规则和复核后的实验结论摘要写入 `experiments/`。
- 实验过程、输入、输出、日志和截图写入 `../../WorldSeed.Experiments/`。
- 正式新增内容必须在 `traceability/records/` 中登记。
- 中文项目文档必须按 `rules/encoding.md` 读取和写入。
- 临时过程和命令输出写入 `../workflows/*/runs/`。
- 未确认内容写入 `open-questions.md`。
- 通用规则写入 `THarness/AIGC`，不写入本项目 wiki。
