# SUB-20260516-002-combat-build-rules

## 状态

- status: draft
- source: TASK-20260516-001-game-data-runtime-prep
- updated: 2026-05-16

## 角色

玩法系统设计。

## 目标

定义第一阶段战斗和构筑规则，使卡牌、辅助、装备、天赋和状态效果能以统一数据规则驱动。

## 允许读取入口

- `Experiments/EXP-001-worldseed/AIGC/wiki/design/game-data-blueprint-v0.1.md`
- `Experiments/EXP-001-worldseed/AIGC/wiki/design/playable-game-requirements.md`
- `Experiments/EXP-001-worldseed/AIGC/wiki/development/contracts/CONTRACT-20260516-001-gamespec-runtime.md`

## 允许修改范围

后续进入开发后，仅允许修改战斗规则、效果规则和构筑规则相关文件或文档。

## 范围

- 回合流程。
- 能量、抽牌、手牌上限。
- 卡牌目标规则。
- 效果类型。
- 辅助卡标签兼容。
- 装备效果作用范围。
- 天赋节点效果。
- 状态效果结算时机。

## 禁止范围

- 不做复杂 AI。
- 不做最终数值平衡。
- 不做后期地图词缀。

## 验证方式

- 每种卡牌类型都有可解释行为。
- 每种构筑来源都能落到效果规则。
- 无效输入有明确反馈规则。
