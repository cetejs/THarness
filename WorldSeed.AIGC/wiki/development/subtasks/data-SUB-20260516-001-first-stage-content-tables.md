# SUB-20260516-001-first-stage-content-tables

## 状态

- status: draft
- source: TASK-20260516-001-game-data-runtime-prep
- updated: 2026-05-16

## 角色

数据设计。

## 目标

准备第一阶段的样例内容表，使 1 角色、1 章、1 Boss 的完整链路有足够数据可用。

## 允许读取入口

- `WorldSeed.AIGC/wiki/design/game-data-blueprint-v0.1.md`
- `WorldSeed.AIGC/wiki/development/tasks/TASK-20260516-001-game-data-runtime-prep.md`
- `WorldSeed.AIGC/wiki/development/contracts/CONTRACT-20260516-001-gamespec-runtime.md`

## 允许修改范围

后续进入开发后，仅允许修改第一阶段内容数据相关文件或文档。

## 范围

- 1 个角色。
- 初始牌组。
- 第一章卡牌池。
- 辅助卡池。
- 装备池。
- 天赋节点。
- 普通敌人、精英敌人和 Boss。
- 事件、商店、锻造服务和奖励池。

## 禁止范围

- 不扩展到完整 3 章内容。
- 不做平衡性最终结论。
- 不创建运行时代码。

## 验证方式

- 所有样例内容都有 ID。
- 所有引用都能追溯到同一数据集合。
- 内容量能支持至少 1 次从角色选择到 Boss 结算的完整流程。
