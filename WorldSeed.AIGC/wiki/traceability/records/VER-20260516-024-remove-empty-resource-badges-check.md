# VER-20260516-024-remove-empty-resource-badges-check

## 状态

- status: active
- type: verification
- date: 2026-05-16
- source: `CHG-20260516-023-remove-empty-resource-badges`

## 验证项

| 项目 | 命令或方式 | 结果 |
| --- | --- | --- |
| C# 构建 | `dotnet build WorldSeed.csproj` | 通过 |
| GameSpec 数据 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| Godot 脚本/配置检查 | `python tools\check_gdscript_sanity.py` | 通过 |
| 最小可玩闭环 | `python tools\smoke_playable_loop.py` | 通过 |
| Godot MCP 真实窗口 | `1920x1080` 启动、截图并点击斗法 `施展` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |

## Godot MCP 验证结果

已完成真实 UI 操作：

1. 主菜单点击 `新开灵契`。
2. 角色选择点击 `开始问道`。
3. 灵脉图截图确认空资源徽章栏消失。
4. 点击 `进入斗法`。
5. 斗法截图确认空资源徽章消失，顶部显示玩家数据。
6. 读取按钮坐标，`施展` 为 `y=928, h=60`。
7. 点击 `施展` 成功，斗法刷新无错误。

截图证据：

- `.mcp/screenshots/screenshot_1778917686_903.png`
- `.mcp/screenshots/screenshot_1778917747_869.png`
- `.mcp/screenshots/screenshot_1778917823_75.png`

## 结论

验证通过。占位式空资源徽章栏已移除，斗法玩家数据已恢复清晰展示，手牌按钮仍在可点击区域。
