# 首批生成素材清单

生成日期：2026-05-16

## 输出位置

| 路径 | 内容 |
| --- | --- |
| `Assets/Art/BloomWeaverGenerated/UI/Common` | UGUI 九宫格面板、按钮状态、卡牌状态、列表行、条形素材、槽位框、分割线。 |
| `Assets/Art/BloomWeaverGenerated/UI/Icons` | 五行、资源、属性、操作、状态、职业定位图标。 |
| `Assets/Art/BloomWeaverGenerated/Battle/Backgrounds` | 战斗背景底图、法阵地面叠层、前景植被叠层。 |
| `Assets/Art/BloomWeaverGenerated/Battle/Sprites/Flowers` | 金木水火土五系花灵待机与攻击透明 Sprite。 |
| `Assets/Art/BloomWeaverGenerated/Battle/Sprites/Enemies` | 小怪、重型怪、Boss 占位透明 Sprite。 |
| `Assets/Art/BloomWeaverGenerated/Battle/Projectiles` | 五行弹道透明 Sprite。 |
| `Assets/Art/BloomWeaverGenerated/Battle/Effects` | 命中、治疗、护盾、火焰、生成法阵、连线节点光效。 |

## 生成结果

- PNG 数量：97 张。
- 已生成 Unity `.meta`：是。
- Texture Type：Sprite。
- UI 九宫格素材已写入 `spriteBorder`。
- 战斗角色、敌人、弹道、特效均为透明 PNG。
- 总清单：`Assets/Art/BloomWeaverGenerated/asset_manifest.json`。
- 预览图：`Assets/Art/BloomWeaverGenerated/preview_sheet.png`。

## 风格基准

参考现有素材的风格关键词：

- 暗玉青背景。
- 金线描边。
- 宣纸按钮。
- 莲花与五行法阵。
- 中国奇幻遗迹。
- 战斗画面使用高对比发光 Sprite。

## 可直接用于开发的素材

| 类型 | 可用于 |
| --- | --- |
| `button_*` | 所有 UGUI Button 的 normal、highlighted、pressed、disabled 状态。 |
| `panel_*_9slice` | 弹窗、侧栏、详情框、普通面板。 |
| `card_*` | 奖励卡、商店商品卡、候选花灵卡。 |
| `list_row_*` | 图鉴、候选列表、设置列表。 |
| `bar_*` | HP、护盾、计时、经验、能量条。 |
| `icon_*` | 按钮图标、属性图标、资源图标、状态图标。 |
| `flower_*` | 战斗花灵 Sprite2D 占位表现。 |
| `enemy_*` | 敌人 Sprite2D 占位表现。 |
| `projectile_*` | 五行攻击弹道。 |
| `fx_*` | 战斗命中、治疗、护盾、生成、节点反馈。 |
| `battle_bg_*` | 战斗 Sprite2D 背景分层。 |

## 仍需后续精修

1. 花灵与敌人目前是可开发用的透明 Sprite，不是最终逐帧动画。
2. 弹道与特效是单帧 Sprite，后续可扩展为序列帧或 Animator Clip。
3. UI 通用素材已满足 UGUI 拼装，但具体界面若要完全贴合效果图，还需要按界面做二次尺寸适配。
4. 所有素材为首批生成版，可支撑功能开发；美术终版需要人工或后续 AI 精修。

## 已接入开发流

1. UGUI 通用素材已通过 `Assets/Editor/BloomWeaverGeneratedArtBinder.cs` 批量写入 `Assets/Prefabs/UI/Screens`。
2. 战斗 HUD 顶栏与暂停按钮已由 `BloomWeaverUGUIRuntimeUI` 暴露 sprite 字段，并在 `SceneSetupTool` 自动绑定。
3. 接入细节和验证记录见 `AIGC/projects/Project_BloomWeaver/wiki/development/tasks/ui-generated-art-integration-2026-05-16.md`。
