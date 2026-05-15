# CHG-20260515-003 追溯账本体系

## 状态

- status: active
- source: 用户确认
- updated: 2026-05-15

## 来源

- 用户请求：项目开发中每一个新增都要有记录可追寻，并能人为检索。
- 关联决策：无
- 关联实验：无
- 关联开发任务：无

## 新增内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 目录 | `WorldSeed.AIGC/wiki/traceability/` | 保存新增内容追溯体系。 |
| 文档 | `WorldSeed.AIGC/wiki/traceability/INDEX.md` | 追溯分区入口。 |
| 文档 | `WorldSeed.AIGC/wiki/traceability/rules.md` | 追溯登记规则。 |
| 文档 | `WorldSeed.AIGC/wiki/traceability/ids.md` | ID 命名规则。 |
| 目录 | `WorldSeed.AIGC/wiki/traceability/records/` | 保存 `CHG` 和 `VER` 记录。 |
| 目录 | `WorldSeed.AIGC/wiki/traceability/templates/` | 保存追溯记录模板。 |

## 影响范围

- 后续正式新增内容必须先登记或同步更新 `CHG`。
- 验证记录可以通过 `VER` 被人工检索。
- 项目入口和工作流约束新增追溯要求。

## 验证方式

- 检查追溯入口、规则、ID、记录索引和模板存在。
- 检查项目 wiki 能从 `wiki/INDEX.md` 路由到追溯分区。
- 运行 `THarness` 自检确认通用 harness 未受影响。

## 验证结果

见 `VER-20260515-001-doc-entry-check.md`。

## 是否晋升为项目事实

是。追溯规则是当前项目正式开发约束。

## 后续事项

- 后续可补充脚本化检查，自动确认新增文件是否被 `CHG` 覆盖。

