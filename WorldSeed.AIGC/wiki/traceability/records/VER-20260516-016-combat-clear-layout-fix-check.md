# VER-20260516-016-combat-clear-layout-fix-check

## 状态

- status: active
- source: 本地命令验证和 Godot .NET headless 检查
- updated: 2026-05-16

## 验证目标

验证清屏布局累积修复没有破坏 C# 构建、Godot .NET 启动、GameSpec 数据、最小可玩闭环和文本编码。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| C# 项目构建 | `dotnet build WorldSeed.csproj` | 通过 |
| Godot .NET 构建 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --build-solutions --quit` | 通过 |
| Godot .NET 启动 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --quit-after 3` | 通过 |
| 结构和清屏回归 | `python tools\check_gdscript_sanity.py` | 通过 |
| GameSpec 数据和素材引用 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| 最小可玩链路数据闭合 | `python tools\smoke_playable_loop.py` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |

## 通过范围

- `ClearScreen()` 先从父容器移除旧节点，再 `QueueFree()`。
- 静态检查覆盖清屏规则。
- 布局日志包含 `clear children=`。

## 局限

Headless 验证不能替代真实窗口反复刷新斗法界面的人工确认。真实窗口验证重点是 `screen=combat content` 不再随着出牌或回合刷新逐步递增。

## 关联记录

- `CHG-20260516-016-combat-clear-layout-fix`
- `TASK-20260516-004-combat-clear-layout-fix`
- `SUB-20260516-009-combat-clear-layout-fix`
- `RUN-20260516-005-combat-clear-layout-fix`
