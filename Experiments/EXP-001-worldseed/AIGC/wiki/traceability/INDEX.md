# 追溯索引

本目录保存 WorldSeed 正式新增内容的来源、原因、影响范围和验证记录。

## 默认读取

| 文件或目录 | read_when |
| --- | --- |
| `rules.md` | 需要判断什么时候必须登记追溯记录。 |
| `ids.md` | 需要创建需求、决策、实验、任务、变更或验证 ID。 |
| `records/INDEX.md` | 需要查找具体变更、验证或追溯记录。 |
| `templates/change-record.md` | 需要创建 `CHG` 变更记录。 |
| `templates/verification-record.md` | 需要创建 `VER` 验证记录。 |

## 追溯链路

```text
用户请求
-> REQ / TASK / DEC / EXP
-> CHG
-> 文件或目录新增
-> VER
-> records/INDEX.md
```

## 写入边界

- 这里保存追溯摘要，不保存长命令输出。
- 具体实验日志写入 `Experiments/EXP-001-worldseed/outputs/legacy-worldseed-experiments/`。
- 运行过程写入 `Experiments/EXP-001-worldseed/AIGC/workflows/*/runs/`。
- 正式项目事实写入对应 wiki 页面，并在 `CHG` 记录中引用。

