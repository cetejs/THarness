# VER-20260517-001-repository-experiment-structure-check

## 状态

- status: active
- source: CHG-20260517-001-repository-experiment-structure
- updated: 2026-05-17

## 验证计划

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| 仓库编码 | `python tools\check_text_encoding.py` | 通过，最终扫描 437 个文本文件。 |
| 通用框架门控 | `cd AIGC.Framework; python tools\oneharness.py gate` | 通过。 |
| 通用框架单元测试 | `cd AIGC.Framework; python -m unittest tools.test_oneharness` | 通过，11 个测试。 |
| Godot C# 构建 | `cd Experiments\EXP-001-worldseed\project; dotnet build WorldSeed.csproj` | 通过，0 警告 0 错误。 |
| Godot 项目静态检查 | `python tools\check_gdscript_sanity.py` | 通过。 |
| GameSpec 引用检查 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过。 |
| 最小闭环 smoke | `python tools\smoke_playable_loop.py` | 通过，`character=iron_oath chapter=chapter_1 nodes=6`。 |
| Godot 导入缓存刷新 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --editor --path . --quit` | 通过，重新导入 36 个资源。 |
| Godot headless 启动 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --quit-after 3` | 通过，退出码 0；保留既有 RID/ObjectDB 退出警告风险。 |

## 结论

目录结构迁移通过仓库编码、通用框架、Godot 项目构建、数据、smoke 和 headless 启动验证。Godot 迁移后需要刷新 `.godot/imported` 导入缓存；刷新后未再出现资源缺失错误。
