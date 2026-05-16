# SUB-20260516-004-asset-reference-plan

## 状态

- status: draft
- source: TASK-20260516-001-game-data-runtime-prep、试制 UI 素材包
- updated: 2026-05-16

## 角色

素材管线设计。

## 目标

定义第一阶段素材引用策略，使 UI、卡牌、图标、地图节点、角色和敌人都能通过数据引用占位素材。

## 允许读取入口

- `WorldSeed.AIGC/wiki/design/game-data-blueprint-v0.1.md`
- `WorldSeed.Experiments/generated-assets/mvp-ui-pack-20260515/`
- `WorldSeed.AIGC/wiki/development/contracts/CONTRACT-20260516-001-gamespec-runtime.md`

## 允许修改范围

后续进入开发后，仅允许修改素材引用清单、占位素材映射和素材导入说明。

## 范围

- UI 面板和按钮。
- 卡框。
- 资源图标。
- 地图节点图标。
- 战斗意图和状态图标。
- 角色与敌人占位策略。
- 素材缺失时的占位回退规则。

## 禁止范围

- 不做最终美术。
- 不删除试制素材。
- 不把素材路径硬编码到 UI 脚本。

## 验证方式

- 每类界面元素都有素材引用来源。
- 缺失素材有明确占位策略。
- 数据层能描述素材路径，不依赖 UI 硬编码。
