# VER-20260516-022-combat-button-hitbox-fix-check

## 状态

- status: active
- type: verification
- date: 2026-05-16
- source: `CHG-20260516-021-combat-button-hitbox-fix`

## 验证项

| 项目 | 命令或方式 | 结果 |
| --- | --- | --- |
| C# 构建 | `dotnet build WorldSeed.csproj` | 通过 |
| GameSpec 数据 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| Godot 脚本/配置检查 | `python tools\check_gdscript_sanity.py` | 通过 |
| Godot MCP 真实窗口 | `1920x1080` 启动并点击完整斗法流程 | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |

## Godot MCP 验证结果

斗法初始手牌按钮为 `y=928, h=60`，底部 `988`，在 `1080` 视口内。

已完成真实 UI 操作：

1. `新开灵契`
2. `开始问道`
3. `进入斗法`
4. 多次点击 `施展`
5. 点击 `收势回合`
6. 打赢斗法进入 `斗法奖励`
7. 点击 `收取`
8. 进入 `构筑洞府`
9. 点击 `返回灵脉`

截图证据：

- `.mcp/screenshots/screenshot_1778915233_618.png`

## 结论

验证通过。斗法手牌按钮越界问题已修复，`MCP-ACCEPT-001` 不再阻塞完整流程验收。
