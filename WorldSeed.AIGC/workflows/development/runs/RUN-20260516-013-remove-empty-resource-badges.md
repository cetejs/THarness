# RUN-20260516-013-remove-empty-resource-badges

## 状态

- status: completed
- source: 用户指出地图和斗法顶部红框区域像占位，并反馈斗法没有显示玩家数据信息
- date: 2026-05-16
- related_task: `TASK-20260516-006-gameplay-ui-alignment-rework`

## 目标

移除地图、斗法和其他界面顶部看起来像占位的空资源徽章栏，并让斗法界面明确显示玩家命元、罡气、灵力和灵石。

## 根因

红框区域来自 `AddResourceBar` 和 `AddCombatHeader` 中复用的资源徽章组件。该组件内部文本没有形成可读布局，运行时只剩四个空圆角框，视觉上像未完成的占位槽。

斗法页还在进入斗法时清空了顶部信息行，玩家数据只出现在小卡牌内部，不够清晰。

## 修复内容

| 文件 | 内容 |
| --- | --- |
| `scripts/Main.cs` | 移除地图、奖励、构筑、奇遇、商店和斗法头部的空资源徽章栏；斗法顶部改为显示 `命元 / 罡气 / 灵力 / 灵石`。 |
| `scripts/GameSpecLoader.cs` | 删除废弃的 `resource_badge_width`、`resource_badge_height` 默认值。 |
| `data/game_spec/ascension_forge.prototype.json` | 删除废弃的 `resource_badge_width`、`resource_badge_height` 配置。 |
| `tools/check_gdscript_sanity.py` | 增加空资源徽章栏禁止项和斗法玩家数据展示检查。 |

## Godot MCP 实测

真实窗口：`1920x1080`

结果：

| 验证点 | 结果 |
| --- | --- |
| 灵脉图红框区域 | 空资源徽章栏已消失。 |
| 斗法红框区域 | 四个空资源徽章已消失。 |
| 斗法玩家数据 | 顶部显示 `命元 80/80  罡气 0  灵力 3/3  灵石 60`。 |
| 手牌按钮位置 | `施展` 按钮为 `y=928, h=60`，底部 `988`，在 `1080` 视口内。 |
| 斗法点击 | 点击 `施展` 成功，斗法刷新无错误。 |

截图：

- 灵脉图：`.mcp/screenshots/screenshot_1778917686_903.png`
- 斗法：`.mcp/screenshots/screenshot_1778917747_869.png`
- 点击施展后：`.mcp/screenshots/screenshot_1778917823_75.png`

## 结论

空资源徽章占位已移除。斗法玩家数据已在顶部明确显示，且没有再次引入手牌按钮越界问题。
