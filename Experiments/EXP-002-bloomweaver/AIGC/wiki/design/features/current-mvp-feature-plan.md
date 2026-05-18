---
id: bloomweaver-current-mvp-feature-plan
title: 当前 MVP 功能设计
summary: 汇总当前可确认的 MVP 玩法闭环和后续设计缺口。
type: design
status: active
tags: [design, mvp]
relates: [bloomweaver-status, bloomweaver-implemented-feature-inventory]
read_when: 需要了解当前 MVP 玩法闭环、已完成体验和后续设计方向。
source: Assets/BloomWeaver_ProjectDoc.md; Assets/BloomWeaver_Progress.md; Assets/BloomWeaver_DevPlan.md; Assets/Scripts
updated: 2026-05-15
---

# 当前 MVP 功能设计

## 结论

当前 MVP 的核心体验是“观阵划线积累灵脉，演武阶段花灵自动扫描命中并触发攻击，波间通过造化和商店成长，持续抵御敌潮”。

## 已确认闭环

```text
MainMenu -> 开局/花灵上阵 -> Init -> Planning -> Combat -> Reward -> Shop -> Planning
                                                   -> Result / GameOver
```

## 核心规则

- 灵枢盘是 12x6 网格。
- 玩家在 Planning 阶段拖拽连接四向相邻、充盈且未被占用的节点。
- 连线禁止穿过已确认灵脉，并防止当前线自交。
- Combat 阶段花灵按攻速异步扫描棋盘。
- 命中灵脉后由 `CombatEngine` 按三定律结算。
- 有效节点数 1-3 为普攻，4-7 为技能，8+ 为必杀。
- 波间奖励包含三选一造化和商店购买。

## 后续设计缺口

- 音效、粒子和 UI 动效的风格标准。
- 新手如何理解三定律、灵蕊类型、五行和职业差异。
- 敌人和奖励的数值平衡目标。
- 独立主界面是否并入主流程。
