# CHG-20260516-023-remove-empty-resource-badges

## 状态

- status: active
- type: change
- date: 2026-05-16
- source: 用户指出地图和斗法顶部红框区域像占位，并反馈斗法缺少玩家数据

## 背景

灵脉图和斗法界面顶部出现四个空圆角框，视觉上像未完成占位。斗法页同时缺少清晰的玩家命元、罡气、灵力和灵石数据展示。

## 变更

| 范围 | 文件 | 说明 |
| --- | --- | --- |
| UI 运行时 | `scripts/Main.cs` | 移除空资源徽章栏，斗法顶部改为显示玩家数据。 |
| GameSpec 默认值 | `scripts/GameSpecLoader.cs` | 删除废弃资源徽章尺寸默认值。 |
| UI 配置 | `data/game_spec/ascension_forge.prototype.json` | 删除废弃资源徽章尺寸配置。 |
| 验证脚本 | `tools/check_gdscript_sanity.py` | 增加禁止空资源徽章栏和斗法玩家数据展示检查。 |
| 运行记录 | `WorldSeed.AIGC/workflows/development/runs/RUN-20260516-013-remove-empty-resource-badges.md` | 记录根因、修复和 Godot MCP 实测。 |

## 影响

- 灵脉图、斗法、奖励、构筑、奇遇和商店界面不再出现空资源徽章占位栏。
- 斗法界面顶部显示玩家关键状态：命元、罡气、灵力、灵石。
- 手牌操作按钮保持在 `1920x1080` 视口内。

## 验证

已通过 `VER-20260516-024-remove-empty-resource-badges-check` 验证。
