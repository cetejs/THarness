# VER-20260516-013-csharp-runtime-migration-check

## 状态

- status: active
- source: 本地命令验证和 Godot .NET headless 检查
- updated: 2026-05-16

## 验证目标

验证当前工程已经迁移到 Godot .NET/C# 运行时，主场景不再依赖 GDScript，并且最小可玩闭环、GameSpec 数据和文本编码仍然有效。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| C# 项目构建 | `dotnet build WorldSeed.csproj` | 通过 |
| Godot .NET 构建 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --build-solutions --quit` | 通过，退出码 0 |
| Godot .NET 启动 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --quit-after 3` | 通过 |
| C# 入口和布局日志 | `python tools\check_gdscript_sanity.py` | 通过 |
| GameSpec 数据和素材引用 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| 最小可玩链路数据闭合 | `python tools\smoke_playable_loop.py` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |

## 通过范围

- `scripts/` 下当前运行时脚本为 C#。
- `scenes/main.tscn` 挂载 `res://scripts/Main.cs`。
- `project.godot` 包含 Godot .NET assembly 配置。
- `scripts/Main.cs` 包含 `[WorldSeed/UI]` 布局日志。
- 本机 Godot .NET 4.6.2 路径已确认可执行。

## 局限

Godot 构建阶段输出过 Android SDK 编辑器设置读取提示，但命令退出码为 0，未作为构建失败处理。Headless 启动只能确认项目能加载和输出日志，不能替代用户真实窗口截图确认。真实窗口仍需用 Godot .NET 编辑器运行后，根据 `[WorldSeed/UI]` 日志继续排查界面尺寸和卡牌显示问题。

## 关联记录

- `CHG-20260516-013-csharp-runtime-migration`
- `TASK-20260516-002-csharp-runtime-migration`
- `SUB-20260516-007-csharp-runtime-migration`
- `RUN-20260516-003-csharp-runtime-migration`
