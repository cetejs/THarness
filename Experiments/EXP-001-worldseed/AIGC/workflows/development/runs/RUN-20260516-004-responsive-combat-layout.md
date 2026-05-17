# RUN-20260516-004-responsive-combat-layout

## 状态

- status: completed
- source: 用户反馈斗法界面显示不全
- updated: 2026-05-16

## 目标

修复斗法界面在运行窗口中显示不全的问题，确认窗口缩放策略改为 1280x720 逻辑画布整体缩放。

## 排查结论

- `project.godot` 原配置为 `window/stretch/mode="canvas_items"`，Control UI 会在窗口尺寸变化时重新参与布局。
- 斗法页使用固定的上半区和手牌区高度，且卡牌固定尺寸偏大。
- `AddCardTo` 对非交互卡牌也预留了按钮高度，导致己方和敌方卡牌面板占用额外纵向空间。
- 因此问题不是单一默认分辨率错误，而是窗口缩放策略和斗法页固定布局叠加导致。

## 处理记录

- 将 Godot stretch 改为 `window/stretch/mode="viewport"`，保持 1280x720 逻辑画布随窗口整体缩放。
- 保留 `window/stretch/aspect="expand"`，避免窗口拉伸时重新出现黑边。
- 新增 `ui_visual.combat_*` 布局配置，控制斗法页卡牌、己方面板、记录面板、上半区和手牌区尺寸。
- 斗法页敌阵面板改为占用剩余宽度。
- 非交互卡牌不再预留按钮高度。
- `[WorldSeed/UI]` 日志补充真实窗口尺寸。
- 更新静态检查工具，防止 stretch 和斗法布局配置回退。

## 验证结果

| 验证项 | 命令 | 结果 |
| --- | --- | --- |
| C# 项目构建 | `dotnet build WorldSeed.csproj` | 通过 |
| Godot .NET 构建 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --build-solutions --quit` | 通过 |
| Godot .NET 启动 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --quit-after 3` | 通过，已输出 `[WorldSeed/UI]` 日志 |
| C# 入口结构 | `python tools\check_gdscript_sanity.py` | 通过 |
| GameSpec 数据 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| 最小闭环 smoke | `python tools\smoke_playable_loop.py` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |

## 局限

Headless 仍不能替代真实窗口截图确认。Headless 环境中真实窗口尺寸日志为 `(0, 0)` 属于无窗口运行限制；真实窗口运行后，如果仍有裁切，需要继续依据 `[WorldSeed/UI]` 日志和截图定位。
