# RUN-20260516-005-combat-clear-layout-fix

## 状态

- status: completed
- source: 用户提供 `[WorldSeed/UI]` 运行日志
- updated: 2026-05-16

## 目标

根据日志定位并修复斗法界面刷新后内容高度持续累积的问题。

## 日志证据

- `viewport=(1280, 720)`、`window=(1280, 720)`、`root=(1280, 720)` 一直稳定。
- `root_box=(1232, 688)` 稳定。
- 多次进入或刷新斗法后，`screen=combat content` 从 `620` 递增到 `783`。
- 卡牌目标尺寸和实际尺寸稳定，说明卡牌纹理本身没有继续拉伸。

## 排查结论

问题来源不是默认分辨率，而是清屏逻辑只调用 `QueueFree()`。Godot 会延迟释放 queued 节点；同一帧立刻重建界面时，旧节点仍留在父容器中参与 VBox 布局计算，导致内容高度逐次累积。

## 处理记录

- `ClearScreen()` 改为先获取子节点列表。
- 对每个旧节点先调用 `_contentBox.RemoveChild(child)`，再调用 `child.QueueFree()`。
- 增加 `clear children=` 布局日志，用于确认每次清屏移除的旧节点数量。
- 更新 `tools/check_gdscript_sanity.py`，要求保留先移除再释放的清屏规则。

## 验证结果

| 验证项 | 命令 | 结果 |
| --- | --- | --- |
| C# 项目构建 | `dotnet build WorldSeed.csproj` | 通过 |
| Godot .NET 构建 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --build-solutions --quit` | 通过 |
| Godot .NET 启动 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --quit-after 3` | 通过 |
| C# 入口结构 | `python tools\check_gdscript_sanity.py` | 通过 |
| GameSpec 数据 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| 最小闭环 smoke | `python tools\smoke_playable_loop.py` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |

## 局限

Headless 验证不能模拟用户完整斗法操作路径；真实窗口仍需用户重新运行后确认 `screen=combat content` 不再随刷新递增。
