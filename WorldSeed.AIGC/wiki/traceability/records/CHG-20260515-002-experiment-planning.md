# CHG-20260515-002 实验目录规划

## 状态

- status: active
- source: 用户确认
- updated: 2026-05-15

## 来源

- 用户请求：通用游戏开发流程会有大量实验，需要针对实验进行目录规划。
- 关联决策：无
- 关联实验：无
- 关联开发任务：无

## 新增内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 目录 | `WorldSeed.AIGC/wiki/experiments/` | 保存实验规则、类型、登记和复核结论摘要。 |
| 目录 | `WorldSeed.Experiments/` | 保存具体实验计划、输入、产物、日志、截图和报告。 |
| 文档 | `WorldSeed.Experiments/_templates/experiment-plan.md` | 提供实验计划模板。 |
| 文档 | `WorldSeed.Experiments/_templates/experiment-manifest.md` | 提供实验输入输出登记模板。 |
| 文档 | `WorldSeed.Experiments/_templates/experiment-result.md` | 提供实验结果模板。 |

## 影响范围

- 实验过程与正式项目 wiki 分离。
- 实验结论必须复核后才能晋升为项目事实。

## 验证方式

- 检查实验入口和模板存在。
- 检查项目 wiki 能路由到实验索引。

## 验证结果

见 `VER-20260515-001-doc-entry-check.md`。

## 是否晋升为项目事实

是。实验目录规划是当前项目正式规则。

## 后续事项

- 第一次技术实验开始前，应创建 `EXP` 目录并登记到实验索引。

