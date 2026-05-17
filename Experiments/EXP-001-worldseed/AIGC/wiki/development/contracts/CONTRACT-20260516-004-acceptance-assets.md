# CONTRACT-20260516-004-acceptance-assets

## 状态

- status: active
- source: TASK-20260516-007-acceptance-asset-replacement
- updated: 2026-05-16

## 目标

定义第一阶段正式验收资源包到 Godot 运行时的交接契约，确保资源路径、尺寸、用途和回退策略明确。

## 输入

| 类别 | 路径 | 尺寸 |
| --- | --- | --- |
| 卡牌框 | `assets/cards/card_attack.png` 等 | `512x736` |
| 资源和符槽图标 | `assets/icons/*.png` | `128x128` |
| 地图节点 | `assets/map/*.png` | `192x192` |
| 状态和意图图标 | `assets/status/*.png` | `128x128` |
| UI 面板 | `assets/ui/panel_large.png` | `960x540` |
| UI 弹窗 | `assets/ui/popup_panel.png` | `640x360` |
| UI 按钮 | `assets/ui/button_*.png` | `480x128` |
| UI 页签 | `assets/ui/tab_*.png` | `240x80` |

## 输出

运行时应能：

- 使用卡牌框纹理渲染卡牌。
- 使用面板纹理渲染主要 UI 容器。
- 使用按钮纹理渲染按钮状态。
- 在资源缺失时保留平面样式回退并输出错误。

## 禁止事项

- 禁止在 UI 代码中写死资源路径，必须通过 GameSpec `assets` 读取。
- 禁止引用实验目录中的图片作为运行时资源。
- 禁止缺少资源时静默显示空白。
- 禁止资源尺寸变更后不更新契约。

## 验证方式

- 资源生成脚本可重复运行。
- GameSpec 资源引用完整性验证通过。
- C# 构建和 Godot .NET 启动通过。
- 手动验收时检查卡牌框、面板和按钮已经显示验收版资源。
