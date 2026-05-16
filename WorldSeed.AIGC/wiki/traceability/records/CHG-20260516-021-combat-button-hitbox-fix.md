# CHG-20260516-021-combat-button-hitbox-fix

## 状态

- status: active
- type: change
- date: 2026-05-16
- source: 用户反馈斗法 `施展` 按钮不可点击、Godot MCP 验收失败记录

## 背景

`VER-20260516-021-godot-mcp-acceptance-check` 记录了斗法手牌按钮位于 `y=1114, h=87`，超过 `1920x1080` 视口，导致玩家无法出牌。本次变更修复该阻塞问题。

## 变更

| 范围 | 文件 | 说明 |
| --- | --- | --- |
| UI 运行时 | `scripts/Main.cs` | 修复斗法标题自动换行、资源徽章拉伸、按钮高度、面板边距和斗法记录增长导致的布局越界。 |
| GameSpec 默认值 | `scripts/GameSpecLoader.cs` | 增加按钮纹理边距、面板纹理边距、斗法记录可见行数默认配置。 |
| UI 配置 | `data/game_spec/ascension_forge.prototype.json` | 增加 `button_texture_margin`、`panel_texture_margin`、`combat_log_visible_lines`。 |
| 运行记录 | `WorldSeed.AIGC/workflows/development/runs/RUN-20260516-011-combat-button-hitbox-fix.md` | 记录根因、修复和 Godot MCP 实测结果。 |

## 影响

- 斗法页手牌操作按钮保持在 `1920x1080` 视口内。
- 多次出牌、斗法记录增长和回合刷新后，手牌按钮仍可点击。
- 主流程可从斗法推进到奖励、构筑洞府并返回灵脉图。

## 验证

已通过 `VER-20260516-022-combat-button-hitbox-fix-check` 验证。
