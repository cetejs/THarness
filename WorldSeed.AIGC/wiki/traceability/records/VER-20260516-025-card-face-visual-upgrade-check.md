# VER-20260516-025-card-face-visual-upgrade-check

## 状态

- status: active
- type: verification
- date: 2026-05-16
- source: `CHG-20260516-024-card-face-visual-upgrade`

## 验证项

| 项目 | 命令或方式 | 结果 |
| --- | --- | --- |
| 资源生成 | `python tools\generate_acceptance_assets.py` | 通过 |
| Godot 资源导入 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --import` | 通过 |
| C# 构建 | `dotnet build WorldSeed.csproj` | 通过 |
| GameSpec 数据 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| Godot 脚本/配置检查 | `python tools\check_gdscript_sanity.py` | 通过 |
| 最小可玩闭环 | `python tools\smoke_playable_loop.py` | 通过 |
| Godot MCP 真实窗口 | `1920x1080` 启动、角色选择截图、斗法截图并点击 `施展` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |

## Godot MCP 验证结果

已完成真实 UI 操作：

1. 主菜单点击 `新开灵契`。
2. 角色选择截图确认新卡面可见。
3. 点击 `开始问道`。
4. 点击 `进入斗法`。
5. 斗法截图确认手牌、己方和敌方卡面使用新视觉。
6. 读取按钮坐标，`施展` 为 `y=928, h=60`。
7. 点击 `施展` 成功，运行输出 `errors` 和 `finalErrors` 为空。

截图证据：

- `.mcp/screenshots/screenshot_1778919579_702.png`
- `.mcp/screenshots/screenshot_1778919649_926.png`
- `.mcp/screenshots/screenshot_1778919739_447.png`

## 结论

验证通过。卡面视觉已升级，运行时可见且不破坏斗法点击流程。
