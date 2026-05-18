# EXP-002-bloomweaver

实验二用于迁入 BloomWeaver 策划案，并在后续步骤中验证通用游戏 AIGC 流程对新项目迁移、设计拆解和可玩闭环实现的支持能力。

## 目录

| 路径 | 职责 |
| --- | --- |
| `project/` | 后续实验二游戏工程。当前未初始化。 |
| `AIGC/` | 实验二项目适配层、wiki、任务、契约和运行记录。 |
| `inputs/` | 需求、参考资料和视觉输入。 |
| `outputs/` | 截图、日志、构建产物和生成素材。 |
| `validation/` | 构建、数据、smoke、视觉、交互和报告验证。 |
| `retro/` | 实验复盘和通用框架候选经验。 |

## 默认读取

```powershell
powershell -ExecutionPolicy Bypass -File ..\..\tools\read_utf8.ps1 -Path AIGC\INDEX.md -Raw
powershell -ExecutionPolicy Bypass -File ..\..\tools\read_utf8.ps1 -Path AIGC\ADAPTER.md -Raw
powershell -ExecutionPolicy Bypass -File ..\..\tools\read_utf8.ps1 -Path AIGC\wiki\INDEX.md -Raw
```

## 当前状态

当前只完成 BloomWeaver 策划案迁入。目标引擎、工程结构和构建命令尚未确认。
