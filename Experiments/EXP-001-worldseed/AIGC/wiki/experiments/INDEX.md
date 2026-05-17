# 实验索引

本目录保存实验规则、实验类型索引和复核后的实验结论摘要。具体实验过程和产物不写入本目录。

| 文件或目录 | read_when |
| --- | --- |
| `rules.md` | 需要判断实验能不能开始、如何命名、如何复核。 |
| `taxonomy.md` | 需要选择实验类型。 |
| `registry.md` | 需要查看实验登记和当前状态。 |
| `findings.md` | 需要查看已复核的实验结论摘要。 |

## 真实实验目录

具体实验写入：

```text
Experiments/EXP-001-worldseed/outputs/legacy-worldseed-experiments/
```

每个实验必须独立成目录，不能把多个目标混在一次实验里。

## 写入边界

- 实验计划、输入、生成工程、日志、截图和原始结果写入 `Experiments/EXP-001-worldseed/outputs/legacy-worldseed-experiments/runs/`。
- 复核后的实验摘要写入 `registry.md` 和 `findings.md`。
- 被采纳为项目事实的结论，再写入对应 `architecture/`、`design/`、`development/` 或 `source-map/` 页面。

