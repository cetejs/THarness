---
id: bloomweaver-screen-gdd-standalone-main-menu
title: 独立主界面模块迁移策划案
type: design
status: active
tags: [gdd, migration, screen, standalone-main-menu]
updated: 2026-05-17
---

# 独立主界面模块迁移策划案

## 定位

独立主界面模块是当前项目中额外存在的一套主菜单实现。迁移时可以作为主界面的参考实现或备用模块，但不能和主流程主界面同时启用。

## 基本信息

| 项 | 内容 |
| --- | --- |
| 模块路径 | `Assets/StandaloneMainMenu` |
| 参考图 | `images/ui-reference-20260517/standalone-main-menu.png` |
| 正式素材 | `Assets/StandaloneMainMenu/Sprites/Final/background_main_scene.png`，`logo_title_full.png`，`button_plate_main.png` |
| 原 Unity Prefab | `Assets/StandaloneMainMenu/Prefabs/StandaloneMainMenu.prefab` |
| 目标技术 | 新引擎 UI 模块 |
| 显示层级 | 主页面或独立场景 |

## 玩家目标

- 从独立主界面开始守阵。
- 打开图鉴。
- 打开设置。
- 退出游戏。

## 视觉与布局

| 区域 | 内容 |
| --- | --- |
| 全屏 | 正式背景图。 |
| 顶部中心 | 正式 Logo。 |
| 中央 | 四个按钮，使用同一按钮底板和动态文本。 |
| 边角 | 装饰角和五行元素。 |

按钮顺序：

1. 开始守阵。
2. 花灵图鉴。
3. 设置。
4. 退出。

## 数据需求

| 字段 | 类型 | 来源 | 用途 |
| --- | --- | --- | --- |
| `backgroundSprite` | asset | 模块配置 | 背景。 |
| `logoSprite` | asset | 模块配置 | Logo。 |
| `buttonSprite` | asset | 模块配置 | 按钮底板。 |
| `onStartClicked` | callback | 接入方 | 开始按钮。 |
| `onCodexClicked` | callback | 接入方 | 图鉴按钮。 |
| `onSettingsClicked` | callback | 接入方 | 设置按钮。 |
| `onExitClicked` | callback | 接入方 | 退出按钮。 |

## 交互规格

| 控件 | 操作 | 结果 |
| --- | --- | --- |
| 开始守阵 | 点击 | 派发开始事件，由接入方进入开局界面。 |
| 花灵图鉴 | 点击 | 派发图鉴事件。 |
| 设置 | 点击 | 派发设置事件。 |
| 退出 | 点击 | 派发退出事件。 |

## 无效输入

- 未绑定事件时点击按钮不能报错。
- 该模块与主流程主界面不能同时显示。
- `ReferenceOnly` 目录资源只能做文档参考，不接入运行时。

## 迁移实现要点

- 如果新引擎重做主界面，应优先复用正式背景、Logo 和按钮底板的视觉方向。
- 如果保留独立模块，应把它做成纯 UI 模块，所有按钮只派发事件。
- 文字必须是动态文本，不能烘焙进按钮图。

## 迁移验收

- 独立主界面打开后背景、Logo、四个按钮显示正确。
- 四个按钮均能派发事件。
- 未绑定事件时无异常。
- 与正式主界面不会重复叠加。
