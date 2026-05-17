# VER-20260516-017-default-1080p-layout-check

## 状态

- status: active
- source: 本地命令验证和 Godot .NET headless 检查
- updated: 2026-05-16

## 验证目标

验证默认 1920x1080 逻辑画布配置没有破坏 C# 构建、Godot .NET 启动、GameSpec 数据、最小可玩闭环和文本编码。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| C# 项目构建 | `dotnet build WorldSeed.csproj` | 通过 |
| Godot .NET 构建 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --build-solutions --quit` | 通过 |
| Godot .NET 启动 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --quit-after 3` | 通过，headless 日志显示 viewport 已进入 1920 基准 |
| 结构和分辨率回归 | `python tools\check_gdscript_sanity.py` | 通过 |
| GameSpec 数据和素材引用 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| 最小可玩链路数据闭合 | `python tools\smoke_playable_loop.py` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |

## 通过范围

- 默认 viewport 为 `1920x1080`。
- `ui_visual` 主要尺寸已同步到 1080p 基准。
- 静态检查覆盖默认分辨率。

## 局限

Headless 验证不能替代真实 1920x1080 窗口截图确认。Headless 环境无真实窗口，日志中的 window 为 `(0, 0)` 属于该模式限制；真实窗口仍需用户运行后确认视觉比例。

## 关联记录

- `CHG-20260516-017-default-1080p-layout`
- `TASK-20260516-005-default-1080p-layout`
- `SUB-20260516-010-default-1080p-layout`
- `RUN-20260516-006-default-1080p-layout`
