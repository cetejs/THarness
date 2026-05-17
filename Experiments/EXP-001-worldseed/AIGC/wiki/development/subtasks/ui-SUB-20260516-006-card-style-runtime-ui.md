# SUB-20260516-006-card-style-runtime-ui

## 状态

- status: completed
- source: TASK-20260516-001-game-data-runtime-prep、ui-screen-visual-spec-v0.3、用户确认进入开发
- updated: 2026-05-16

## 角色

Godot UI 实现。

## 目标

将已确认的 `ui-screen-visual-spec-v0.3.md` 卡牌参考风格落实到当前 Godot 最小可玩闭环，让玩家能获得完整的第一阶段游戏体验：

- 主菜单。
- 角色选择。
- 灵脉图。
- 斗法。
- 斗法奖励。
- 构筑洞府。
- 奇遇。
- 灵市/锻炉。
- 洞天结算。
- 本局结算。
- 设置、详情和确认界面。

## 允许读取入口

- `Experiments/EXP-001-worldseed/AIGC/wiki/design/ui-screen-visual-spec-v0.3.md`
- `Experiments/EXP-001-worldseed/AIGC/wiki/development/contracts/CONTRACT-20260516-001-gamespec-runtime.md`
- `Experiments/EXP-001-worldseed/AIGC/workflows/development/runs/RUN-20260516-001-playable-loop-development.md`

## 允许修改范围

- `scripts/Main.gd`
- `scripts/GameRuntime.gd` 中不影响规则的体验文案。
- `data/game_spec/ascension_forge.prototype.json` 中 UI 文案、显示名称、视觉配置和素材引用。
- `README.md`
- 本任务对应运行记录、验证记录和追溯记录。

## 范围

- 将卡牌展示改为费用宝珠、门类竖条、插画区、规则区和底部类型徽章结构。
- 将角色、敌人、商品、事件和奖励尽量卡片化展示。
- 将界面术语替换为修仙语境：命元、罡气、灵力、灵石、法门、符箓、灵脉、洞天、斗法。
- 保留现有最小可玩闭环和数据驱动规则。
- 补充设置、详情和确认界面的最小可用入口。

## 禁止范围

- 不重写战斗、奖励、事件和商店规则。
- 不新增未确认玩法系统。
- 不做联机、存档系统、导出链路或完整多章节内容。
- 不把卡牌数值、敌人数值、奖励内容写死到 UI 脚本。
- 不引入多个类到同一个脚本文件。

## 成功标准

1. 玩家能从主菜单进入新局，完成角色选择、灵脉图、斗法、奖励、构筑、奇遇、灵市、Boss 和结算。
2. 主要界面呈现 v0.3 的卡牌参考风格，而不是纯文字界面。
3. 手牌、奖励、敌人、商品和详情都使用卡片化展示。
4. 设置、详情和确认界面有最小入口且可返回。
5. 已有验证命令通过。

## 完成结果

- 已完成 v0.3 卡牌参考风格运行时 UI。
- 已覆盖主菜单、角色选择、灵脉图、斗法、斗法奖励、构筑洞府、奇遇、灵市/锻炉、洞天结算、本局结算、设置、详情和确认界面。
- 已保留第一阶段最小可玩闭环规则，不新增未确认玩法系统。
- 当前命令行环境未发现 Godot 可执行入口，Godot headless 启动验证未执行。

## 验证方式

- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_gdscript_sanity.py`
- `python tools\check_text_encoding.py --root .`
- 检查 `scripts/Main.gd` 不包含已知高风险 GDScript 模式。
