# WorldSeed 实验入口

本目录保存 WorldSeed 通用游戏开发流程中的实验计划、输入、输出、日志、截图和报告。

## 默认读取

1. `WorldSeed.AIGC/wiki/experiments/INDEX.md`
2. `registry/INDEX.md`
3. 当前实验目录的 `plan.md`

## 目录职责

| 目录 | 用途 |
| --- | --- |
| `_templates/` | 实验计划、manifest 和结果模板。 |
| `registry/` | 实验目录登记，不保存长结果。 |
| `runs/` | 每次实验的独立目录。 |
| `fixtures/` | 可复用输入样例、小型测试数据和手工构造用例。 |
| `artifacts/` | 需要跨实验引用的小型稳定产物。大型产物只保留路径说明。 |
| `reports/` | 阶段性实验汇总报告。 |

## 单实验结构

```text
runs/
  EXP-YYYYMMDD-001-short-name/
    plan.md
    manifest.md
    result.md
    inputs/
    workspace/
    artifacts/
    logs/
    captures/
```

## 禁止

- 禁止把实验原始产物写入正式 wiki。
- 禁止多个实验共用同一个 `workspace/`。
- 禁止用一次实验结果直接替代产品决策。

