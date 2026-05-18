---
id: bloomweaver-screen-gdd-replacement
title: 上阵替换界面迁移策划案
type: design
status: active
tags: [gdd, migration, screen, replacement]
updated: 2026-05-17
---

# 上阵替换界面迁移策划案

## 定位

上阵替换界面用于在开局阶段替换花灵。它不是战斗内换人系统，首版只服务开局阵容确认。

## 基本信息

| 项 | 内容 |
| --- | --- |
| screen key | `replacement-screen` |
| 参考图 | `images/ui-reference-20260517/replacement.png` |
| 原 Unity Prefab | `Assets/Prefabs/UI/Screens/replacement-screen.prefab` |
| 目标技术 | 新引擎 UI 覆盖层 |
| 显示层级 | 覆盖层 |
| 来源阶段 | 开局界面点击花灵卡位 |
| 退出方向 | 开局界面 |

## 玩家目标

- 选择要替换的上阵槽。
- 浏览候选花灵。
- 对比属性、职业、扫描形状和构筑适配。
- 确认替换或取消。

## 视觉与布局

| 区域 | 内容 |
| --- | --- |
| 左侧 | 当前 5 个上阵槽和小型队伍摘要。 |
| 中央 | 候选花灵详情、属性、扫描形状、替换预览。 |
| 右侧 | 候选花灵列表。 |
| 底部 | 自动推荐、取消、确认替换。 |

## 数据需求

| 字段 | 类型 | 来源 | 用途 |
| --- | --- | --- | --- |
| `partySlots` | list | 阵容系统 | 当前上阵槽。 |
| `selectedSlotIndex` | int | UI 状态 | 替换目标。 |
| `candidateFlowers` | list | 花灵库 | 候选列表。 |
| `selectedCandidateId` | string | UI 状态 | 当前候选。 |
| `replacementPreview` | object | 构筑分析 | 替换后变化。 |
| `canConfirmReplacement` | bool | 阵容规则 | 确认按钮状态。 |

## 交互规格

| 控件 | 操作 | 结果 |
| --- | --- | --- |
| 当前上阵槽 | 点击 | 设置替换目标。 |
| 候选花灵 | 点击 | 设置候选并刷新详情。 |
| 自动推荐 | 点击 | 自动选择合法槽位和候选。 |
| 取消 | 点击 | 不应用更改，回开局。 |
| 确认替换 | 点击 | 更新阵容，回开局并刷新卡位。 |

## 无效输入

- 未选择槽位或候选时确认按钮禁用。
- 不允许重复上阵时，已在队伍中的候选禁用。
- 候选列表为空时显示空状态。

## 迁移实现要点

- 替换前只维护临时选择，确认后才写入阵容系统。
- 开局界面需要订阅阵容变化并刷新。
- 未来若加入锁定花灵，候选项需要支持 locked 状态。

## 迁移验收

- 从开局点击任意花灵槽能打开替换界面。
- 选择候选后详情和预览刷新。
- 取消不改变阵容。
- 确认后开局界面对应槽位更新。
