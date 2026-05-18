---
id: bloomweaver-screen-gdd-tip
title: 通用提示框迁移策划案
type: design
status: active
tags: [gdd, migration, screen, tip]
updated: 2026-05-17
---

# 通用提示框迁移策划案

## 定位

通用提示框用于展示成功、失败、警告和信息提示。它分为非阻塞 Toast 和阻塞式提示两种。

## 基本信息

| 项 | 内容 |
| --- | --- |
| screen key | `tip-screen` |
| 参考图 | `images/ui-reference-20260517/tip.png` |
| 原 Unity Prefab | `Assets/Prefabs/UI/Screens/tip-screen.prefab` |
| 目标技术 | 新引擎 UI 弹窗或 Toast |
| 显示层级 | 提示层 |
| 来源阶段 | 任意界面 |
| 退出方向 | 来源界面 |

## 玩家目标

- 快速理解操作结果。
- 在必要时关闭提示。
- 不被轻量提示打断主要流程。

## 视觉与布局

| 类型 | 布局 |
| --- | --- |
| Toast | 屏幕上方或右侧短暂出现，自动消失。 |
| Modal Tip | 居中弹窗，带关闭按钮。 |

## 数据需求

| 字段 | 类型 | 来源 | 用途 |
| --- | --- | --- | --- |
| `message` | string | 调用方 | 提示内容。 |
| `title` | string | 调用方 | 可选标题。 |
| `tipType` | enum | 调用方 | 成功、警告、错误、信息。 |
| `mode` | enum | 调用方 | Toast 或 Modal。 |
| `duration` | float | 调用方/配置 | 自动消失时间。 |

## 交互规格

| 控件 | 操作 | 结果 |
| --- | --- | --- |
| 关闭 | 点击 | 关闭提示。 |
| 自动消失 | 计时结束 | 关闭 Toast。 |

## 无效输入

- 提示消息为空时不创建提示。
- 连续触发多个提示时按队列或合并规则显示，不能重叠不可读。
- Modal Tip 打开时下层输入按配置决定是否阻断。

## 迁移实现要点

- 提示框应作为全局服务，不挂在具体界面控制器里。
- Toast 和 Modal 共用数据结构，但不同显示容器。
- 错误提示要保留足够时间，成功提示可以较短。

## 迁移验收

- 成功、警告、错误、信息四类样式可区分。
- 连续触发提示不会互相遮挡。
- Toast 能自动关闭。
- Modal Tip 能手动关闭并回来源界面。
