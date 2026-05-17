# GameAIGC

本仓库用于沉淀通用游戏 AIGC 开发流程，并通过实验项目验证这些流程是否能支持 AI 从需求开发到可运行游戏功能。

## 目录

| 路径 | 职责 |
| --- | --- |
| `AIGC.Framework/` | 通用游戏开发流程、规则、模板、适配器和自检工具。 |
| `Experiments/` | 用具体项目验证通用框架。 |
| `Experiments/EXP-001-worldseed/` | 实验一，当前 Godot .NET/C# 游戏项目。 |
| `Reports/` | 实验总结和通用框架晋升记录。 |
| `Archive/` | 废弃或归档资料入口。 |
| `tools/` | 仓库级 UTF-8 读取和文本编码检查工具。 |

## 默认读取

```powershell
powershell -ExecutionPolicy Bypass -File tools\read_utf8.ps1 -Path AIGC.Framework\INDEX.md -Raw
powershell -ExecutionPolicy Bypass -File tools\read_utf8.ps1 -Path Experiments\INDEX.md -Raw
powershell -ExecutionPolicy Bypass -File tools\read_utf8.ps1 -Path Experiments\EXP-001-worldseed\AIGC\INDEX.md -Raw
```

## 验证

仓库级验证：

```powershell
python tools\check_text_encoding.py
```

通用框架验证：

```powershell
cd AIGC.Framework
python tools\oneharness.py gate
python -m unittest tools.test_oneharness
```

实验一 Godot 项目验证：

```powershell
cd Experiments\EXP-001-worldseed\project
dotnet build WorldSeed.csproj
python tools\check_gdscript_sanity.py
python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .
python tools\smoke_playable_loop.py
```
