# RUN-20260516-003-csharp-runtime-migration

## 状态

- status: completed
- source: 用户要求全部使用 C#
- updated: 2026-05-16

## 目标

将当前 Godot 原型运行时迁移到 C#，并确认本机 Godot .NET 环境。

## 环境检查

- 普通 Godot：`E:\Godot\4.6.2-stable\Godot_v4.6.2-stable_win64_console.exe`
- 普通 Godot 版本：`4.6.2.stable.official.71f334935`
- Godot .NET：`E:\Godot\4.6.2-stable-mono\Godot_v4.6.2-stable_mono_win64\Godot_v4.6.2-stable_mono_win64_console.exe`
- Godot .NET 版本：`4.6.2.stable.mono.official.71f334935`
- .NET SDK：本机已安装，可执行 `dotnet build WorldSeed.csproj`。

## 处理记录

- 已确认原 `E:\Godot\4.6.2-stable` 为普通版，不适合作为 C# 开发入口。
- 已下载并解压 Godot .NET 4.6.2 到 `E:\Godot\4.6.2-stable-mono\`。
- 已新增 `WorldSeed.csproj`。
- 已新增 `scripts/GameSpecLoader.cs`、`scripts/GameRuntime.cs`、`scripts/Main.cs`。
- 已将 `scenes/main.tscn` 改为挂载 `res://scripts/Main.cs`。
- 已在 `project.godot` 写入 `[dotnet] project/assembly_name="WorldSeed"`。
- 已删除不再作为运行入口的 `scripts/*.gd`。
- 已在 C# UI 入口加入 `[WorldSeed/UI]` 布局日志。
- 已更新静态检查工具，要求 C# 入口、Godot .NET 项目配置、卡牌固定尺寸和布局日志存在。

## 验证结果

| 验证项 | 命令 | 结果 |
| --- | --- | --- |
| C# 项目构建 | `dotnet build WorldSeed.csproj` | 通过 |
| Godot .NET 构建 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --build-solutions --quit` | 通过，退出码 0 |
| Godot .NET 启动 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --quit-after 3` | 通过 |
| C# 入口结构 | `python tools\check_gdscript_sanity.py` | 通过 |
| GameSpec 数据 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| 最小闭环 smoke | `python tools\smoke_playable_loop.py` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |

## 局限

Godot 构建阶段输出过 Android SDK 编辑器设置读取提示，但命令退出码为 0，未作为构建失败处理。Godot headless 快速退出时可能输出 RID/ObjectDB 资源释放警告，但本次命令退出码为 0，未作为启动失败处理。真实窗口布局仍需要使用 Godot .NET 编辑器运行，并根据 `[WorldSeed/UI]` 日志继续定位。
