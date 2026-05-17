# CHG-20260515-001 项目适配层初始化

## 状态

- status: active
- source: 用户确认
- updated: 2026-05-15

## 来源

- 用户请求：先建立 WorldSeed 项目适配层，使后续 AI 从固定入口开发。
- 关联决策：`D-001`、`D-002`
- 关联实验：无
- 关联开发任务：无

## 新增内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 文档 | `AGENTS.md` | 建立仓库 AI 强制入口和写入边界。 |
| 目录 | `WorldSeed.AIGC/` | 保存 WorldSeed 项目事实、决策、任务和运行记录。 |
| 文档 | `WorldSeed.AIGC/INDEX.md` | 建立项目适配层入口。 |
| 文档 | `WorldSeed.AIGC/ADAPTER.md` | 保存项目适配配置。 |
| 目录 | `WorldSeed.AIGC/wiki/` | 保存项目 wiki。 |
| 目录 | `WorldSeed.AIGC/workflows/` | 保存项目工作流运行记录入口。 |

## 影响范围

- 后续 AI 开发必须先读取项目适配入口。
- 项目事实和通用规则分层保存。

## 验证方式

- 检查关键入口文件存在。
- 运行 `THarness` 自检，确认通用 harness 未受影响。

## 验证结果

见 `VER-20260515-001-doc-entry-check.md`。

## 是否晋升为项目事实

是。该记录对应的目录结构是当前项目正式适配层。

## 后续事项

- 后续新增正式内容必须登记 `CHG` 记录。

