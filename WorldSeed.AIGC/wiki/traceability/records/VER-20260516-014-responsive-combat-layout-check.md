# VER-20260516-014-responsive-combat-layout-check

## 状态

- status: active
- source: 本地命令验证和 Godot .NET headless 检查
- updated: 2026-05-16

## 验证目标

验证斗法页显示不全修复没有破坏 C# 构建、Godot .NET 启动、GameSpec 数据、最小可玩闭环和文本编码。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| C# 项目构建 | `dotnet build WorldSeed.csproj` | 通过 |
| Godot .NET 构建 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --build-solutions --quit` | 通过 |
| Godot .NET 启动 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --quit-after 3` | 通过，已输出 `[WorldSeed/UI]` 日志 |
| 结构和布局回归 | `python tools\check_gdscript_sanity.py` | 通过 |
| GameSpec 数据和素材引用 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| 最小可玩链路数据闭合 | `python tools\smoke_playable_loop.py` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |

## 通过范围

- `project.godot` 使用 viewport stretch。
- `ui_visual` 包含斗法页独立尺寸配置。
- `scripts/Main.cs` 斗法页使用配置化尺寸。
- `[WorldSeed/UI]` 日志包含真实窗口尺寸。

## 局限

Headless 验证不能替代真实窗口截图确认。Headless 环境中真实窗口尺寸日志为 `(0, 0)` 属于无窗口运行限制；真实窗口仍需由用户运行后确认视觉结果。

## 关联记录

- `CHG-20260516-014-responsive-combat-layout`
- `TASK-20260516-003-responsive-combat-layout`
- `SUB-20260516-008-responsive-combat-layout`
- `RUN-20260516-004-responsive-combat-layout`
