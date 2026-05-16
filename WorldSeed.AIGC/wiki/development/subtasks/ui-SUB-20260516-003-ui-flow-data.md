# SUB-20260516-003-ui-flow-data

## 状态

- status: draft
- source: TASK-20260516-001-game-data-runtime-prep
- updated: 2026-05-16

## 角色

UI 流程设计。

## 目标

定义第一阶段每个界面的数据来源、按钮动作和跳转关系，确保 UI 不直接硬编码玩法数据。

## 允许读取入口

- `WorldSeed.AIGC/workflows/planning-discussion/runs/RUN-20260515-002-minimum-playable-loop-ui-flow.md`
- `WorldSeed.AIGC/wiki/design/game-data-blueprint-v0.1.md`
- `WorldSeed.AIGC/wiki/development/contracts/CONTRACT-20260516-001-gamespec-runtime.md`

## 允许修改范围

后续进入开发后，仅允许修改 UI 流程、界面数据来源和跳转配置相关文件或文档。

## 范围

- 主菜单。
- 角色选择。
- 地图。
- 战斗。
- 奖励。
- 构筑管理。
- 事件。
- 商店锻造。
- 章节结算。
- 本局结算。
- 设置、详情和确认弹窗。

## 禁止范围

- 不制作最终 UI 美术。
- 不把数值或卡牌效果写在 UI 文案内。
- 不新增未确认界面。

## 验证方式

- 每个界面都有数据来源。
- 每个按钮都有动作和目标。
- 所有跳转目标都存在。
- 失败、取消、返回路径不形成死路。
