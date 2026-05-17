# EXP-001-worldseed

实验一用于验证通用游戏 AIGC 流程能否支持 AI 从需求澄清、设计拆分、数据蓝图、Godot 实现、运行验证到复盘沉淀。

## 目录

| 路径 | 职责 |
| --- | --- |
| `project/` | Godot .NET/C# 游戏工程。 |
| `AIGC/` | 实验一项目适配层、wiki、任务、契约和运行记录。 |
| `inputs/` | 需求、参考资料和效果图输入。 |
| `outputs/` | 截图、日志、构建产物和生成素材。 |
| `validation/` | 构建、数据、smoke、视觉、交互和报告验证。 |
| `retro/` | 实验复盘和通用框架候选经验。 |

## 默认读取

```powershell
powershell -ExecutionPolicy Bypass -File ..\..\tools\read_utf8.ps1 -Path AIGC\INDEX.md -Raw
powershell -ExecutionPolicy Bypass -File ..\..\tools\read_utf8.ps1 -Path AIGC\ADAPTER.md -Raw
powershell -ExecutionPolicy Bypass -File ..\..\tools\read_utf8.ps1 -Path AIGC\wiki\INDEX.md -Raw
```

## 项目运行

```powershell
cd Experiments\EXP-001-worldseed\project
dotnet build WorldSeed.csproj
python tools\check_gdscript_sanity.py
python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .
python tools\smoke_playable_loop.py
```
