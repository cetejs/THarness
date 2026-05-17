# VER-20260516-021-godot-mcp-acceptance-check

## 状态

- status: active
- source: Godot MCP 真实运行验收
- updated: 2026-05-16

## 验证目标

验证第一阶段资源替换后的 Godot .NET 运行时是否能够通过真实 UI 完成主菜单到结算的完整最小流程。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| 项目识别 | Godot MCP `list_projects`、`get_project_info` | 通过 |
| Autoload 检查 | Godot MCP `list_autoloads` | 通过，无 autoload 阻塞 |
| 项目启动 | Godot MCP `run_project` | 通过 |
| 主菜单进入角色选择 | `click_element` 点击 `新开灵契` | 通过 |
| 角色选择进入灵脉图 | `click_element` 点击 `开始问道` | 通过 |
| 灵脉图进入斗法 | `click_element` 点击 `进入斗法` | 通过 |
| 斗法出牌 | 检查并点击 `施展` | 不通过，按钮越界 |
| 完整流程到结算 | 真实 UI 操作 | 不通过，斗法阻塞 |
| 运行时错误 | Godot MCP `get_debug_output` | 未发现脚本错误 |

## 验收结果

不通过。

## 阻塞项

斗法手牌按钮全部位于 viewport 外：`y=1114, h=87`，而真实 viewport 高度为 `1080`。玩家无法通过 UI 出牌，因此完整流程无法验收到结算。

## 截图证据

- 主菜单：`.mcp/screenshots/screenshot_1778913866_638.png`
- 斗法：`.mcp/screenshots/screenshot_1778913940_857.png`

## 关联记录

- `RUN-20260516-010-godot-mcp-acceptance`
- `TASK-20260516-006-gameplay-ui-alignment-rework`
- `TASK-20260516-007-acceptance-asset-replacement`
