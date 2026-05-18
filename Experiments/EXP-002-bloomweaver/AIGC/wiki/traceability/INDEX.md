# 追溯索引

本目录保存 BloomWeaver 正式新增内容的来源、原因、影响范围和验证记录。

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
-> CHG
-> 文件或目录新增
-> VER
-> records/INDEX.md
```
