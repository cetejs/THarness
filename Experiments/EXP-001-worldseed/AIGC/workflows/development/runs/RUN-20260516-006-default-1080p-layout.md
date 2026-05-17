# RUN-20260516-006-default-1080p-layout

## 状态

- status: completed
- source: 用户要求默认使用 1920x1080
- updated: 2026-05-16

## 目标

将当前 Godot .NET 工程默认逻辑画布切换为 1920x1080，并同步 UI 配置基准。

## 处理记录

- `project.godot` 默认 viewport 从 `1280x720` 改为 `1920x1080`。
- 保留 `window/stretch/mode="viewport"` 和 `window/stretch/aspect="expand"`，继续使用逻辑画布整体缩放。
- `ui_visual` 中主要间距、字体、按钮、卡牌、节点、资源徽章和斗法面板尺寸按 1.5 倍同步到 1080p 基准。
- 静态检查改为要求 `1920x1080`。
- README 和项目状态同步更新。

## 验证结果

| 验证项 | 命令 | 结果 |
| --- | --- | --- |
| C# 项目构建 | `dotnet build WorldSeed.csproj` | 通过 |
| Godot .NET 构建 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --build-solutions --quit` | 通过 |
| Godot .NET 启动 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --quit-after 3` | 通过，headless 日志显示 viewport 已进入 1920 基准 |
| C# 入口结构 | `python tools\check_gdscript_sanity.py` | 通过 |
| GameSpec 数据 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| 最小闭环 smoke | `python tools\smoke_playable_loop.py` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |

## 局限

Headless 验证不能替代真实 1920x1080 窗口截图确认。Headless 环境无真实窗口，日志中的 window 为 `(0, 0)` 属于该模式限制；真实窗口仍需用户运行后确认视觉比例。
