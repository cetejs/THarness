---
id: bloomweaver-ui-asset-production-manifest
title: UI 与战斗 Sprite2D 素材生产清单
summary: 定义普通 UGUI 界面、弹窗、图鉴、商店、奖励和战斗 Sprite2D 所需正式素材、状态、尺寸口径和命名规则。
type: design
status: active
tags: [ui, assets, ugui, sprite2d, art-production]
relates: [bloomweaver-ui-interface-detail-spec, bloomweaver-battle-sprite2d-presentation-spec]
read_when: 需要创建 UI 素材、拆分切图、整理美术交付、配置 Unity 导入参数或确认素材缺口。
source: AIGC/projects/Project_BloomWeaver/wiki/design/ui-interface-detail-spec.md; AIGC/projects/Project_BloomWeaver/wiki/development/contracts/battle-sprite2d-presentation-spec.md; images/ui-reference-20260517/*.png; Assets/StandaloneMainMenu/SPRITE_HANDOFF.md
updated: 2026-05-16
---

# UI 与战斗 Sprite2D 素材生产清单

## 结论

当前 `images/ui-reference-20260517/*.png` 是界面完整参考图，不等于正式切片清单。正式生产需要为 UGUI 和 Sprite2D 分别交付：

- UGUI：背景、面板、按钮、页签、卡片、列表项、图标、装饰、字体样式。
- Sprite2D：战场分层、花灵战斗 Sprite、敌人 Sprite、投射物、特效、状态图标、伤害数字样式。

具体到每个界面的素材使用位置、UGUI 节点和控件绑定关系，见 `ui-slicing-layout-asset-map.md`。

## 通用导出规范

| 项 | 规则 |
| --- | --- |
| 色彩 | 透明 PNG，保留 sRGB。 |
| 命名 | 小写英文、下划线分隔，不使用空格和中文。 |
| UGUI 图片 | 边框类素材必须提供九宫格边距。 |
| 按钮 | 至少提供 normal、pressed、disabled；可选 hover、selected。 |
| 图标 | 优先正方形，常用 64x64、128x128、256x256。 |
| 背景 | 可整图，也可分层；若需动效必须分层。 |
| Sprite2D | 需要 Pivot、PPU、排序层建议。 |
| 参考图 | `01.png` 只作为视觉参考，不能直接替代所有切片。 |

## 命名规则

```text
ui_<screen>_<element>_<state>.png
panel_<purpose>_<size>.png
button_<purpose>_<state>.png
icon_<domain>_<name>.png
card_<domain>_<state>.png
char_<id>_<portrait|avatar|battle>_<state>.png
enemy_<id>_<state>_<frame>.png
fx_<element>_<action>_<frame>.png
bg_<screen>_<layer>.png
```

示例：

```text
ui_opening_party_slot_selected.png
button_primary_pressed.png
icon_element_wood.png
card_reward_gold_selected.png
char_qingteng_battle_attack_0001.png
enemy_imp_move_0001.png
fx_wood_hit_0001.png
bg_combat_foreground.png
```

## 通用 UGUI 基础素材

| 素材 | 状态/变体 | 用途 |
| --- | --- | --- |
| 主背景遮罩 | normal | 背景压暗、弹窗遮罩。 |
| 主面板九宫格 | normal | 设置、图鉴、商店、结算大面板。 |
| 小面板九宫格 | normal | 详情框、提示框、统计框。 |
| 主按钮 | normal、hover、pressed、disabled、selected | 主操作按钮。 |
| 次按钮 | normal、hover、pressed、disabled | 次级操作。 |
| 危险按钮 | normal、pressed、disabled | 返回主界面、重新开始、退出。 |
| 页签 | normal、selected、disabled | 图鉴、设置、总览。 |
| 卡片框 | normal、selected、disabled、locked | 花灵、奖励、商品。 |
| 列表条目 | normal、selected、disabled、locked | 图鉴、候选、设置分类。 |
| 分割线 | normal | 面板分区。 |
| 标题装饰 | normal | 页面标题两侧装饰。 |
| 关闭图标 | normal、pressed | 弹窗和覆盖层关闭。 |

## 通用图标

| 图标域 | 必需图标 |
| --- | --- |
| 五行 | 木、水、火、土、金。 |
| 资源 | 灵砂、灵露、残蕊、灵契碎片、妖核。 |
| 职业 | Warrior、Mage、Healer 或对应中文职业。 |
| 状态 | 护盾、燃烧、吸血、溅射、双倍伤害、复苏、枯竭。 |
| 战况 | 击杀、突破、存活、波次、时间、评级。 |
| 功能 | 设置、图鉴、返回、刷新、确认、取消、暂停、继续。 |
| 稀有度 | 普通、稀有、史诗、传说，若奖励系统使用稀有度。 |

## 1. 主界面素材

参考图：`images/ui-reference-20260517/main-menu.png`

| 素材 | 说明 |
| --- | --- |
| `bg_main_menu_base.png` | 幽暗森林和花境入口背景。 |
| `logo_bloomweaver_full.png` | 游戏 Logo，若不烘焙在背景中。 |
| `button_main_menu_normal/pressed/disabled.png` | 四个主菜单按钮底板。 |
| `decor_main_element_left/right.png` | 左右五行装饰。 |
| `decor_main_title_flower.png` | 标题装饰。 |
| `text_style_main_title` | Logo 若使用 TMP 时的字体样式。 |

可选：

- 背景远景、法阵光、雾气分层，用于主界面轻动画。

## 2. 开局界面素材

参考图：`images/ui-reference-20260517/opening.png`

| 素材 | 说明 |
| --- | --- |
| `bg_opening_base.png` | 开局庭院背景。 |
| `panel_opening_left.png` | 难度和挑战词条面板。 |
| `panel_opening_right.png` | 构筑预览和阵图方案面板。 |
| `card_party_slot_normal/selected/empty/disabled.png` | 五个花灵卡位。 |
| `card_initial_board_normal/selected.png` | 初始阵图方案卡。 |
| `card_initial_blessing_normal/selected.png` | 初始造化卡。 |
| `button_difficulty_normal/selected.png` | 难度按钮。 |
| `button_challenge_tag_normal/selected/disabled.png` | 词条按钮。 |
| `icon_build_balance/short/highrisk.png` | 构筑方案图标。 |

还需要：

- 五名默认花灵头像或半身像。
- 难度图标。
- 挑战词条图标。

## 3. 布阵界面素材

参考图：`images/ui-reference-20260517/planning.png`

| 素材 | 说明 |
| --- | --- |
| `bg_planning_base.png` | 布阵战场背景。 |
| `panel_top_bar.png` | 顶部状态栏。 |
| `panel_flower_status.png` | 左侧花灵状态栏。 |
| `panel_threat_preview.png` | 右侧本波威胁。 |
| `board_grid_base.png` | 棋盘底板。 |
| `node_normal/available/selected/blocked/exhausted/reviving.png` | 节点状态。 |
| `line_spirit_normal/active/exhausted.png` | 灵脉连线。 |
| `line_corner.png` | 灵脉拐点。 |
| `button_bottom_action_*` | 撤销、清线、开始演武、重织按钮。 |

还需要：

- 敌人威胁小图标。
- 花灵状态小头像。
- 五行节点图标。

## 4. 战斗界面素材

参考图：`images/ui-reference-20260517/combat.png`

| 素材 | 说明 |
| --- | --- |
| `bg_combat_far.png` | 远景森林。 |
| `bg_combat_mid.png` | 中景战场。 |
| `bg_combat_ground.png` | 地面和路径。 |
| `bg_combat_foreground.png` | 前景遮挡。 |
| `path_warning.png` | 路径预警。 |
| `battle_grid_base.png` | 战斗棋盘底板。 |
| `hud_combat_top_bar.png` | UGUI 顶部 HUD 背板。 |
| `hud_combat_pressure_panel.png` | 战场压力面板。 |
| `button_pause_normal/pressed.png` | 暂停按钮。 |

Sprite2D 必需：

| 素材 | 说明 |
| --- | --- |
| `char_<id>_battle_idle_*` | 花灵待机。 |
| `char_<id>_battle_attack_*` | 花灵普攻。 |
| `char_<id>_battle_skill_*` | 花灵技能。 |
| `char_<id>_battle_hit_*` | 花灵受击。 |
| `char_<id>_battle_down_*` | 花灵倒下。 |
| `enemy_<id>_move_*` | 敌人移动。 |
| `enemy_<id>_hit_*` | 敌人受击。 |
| `enemy_<id>_death_*` | 敌人死亡。 |
| `enemy_<id>_breach_*` | 敌人突破。 |
| `projectile_<element>_<attack_type>.png` | 投射物。 |
| `fx_<element>_hit_*` | 命中特效。 |
| `fx_shield_*` | 护盾特效。 |
| `fx_heal_*` | 治疗特效。 |
| `fx_burn_*` | 燃烧特效。 |

## 5. 暂停界面素材

参考图：`images/ui-reference-20260517/pause.png`

| 素材 | 说明 |
| --- | --- |
| `overlay_dim.png` | 暗色遮罩。 |
| `panel_pause_main.png` | 暂停主面板。 |
| `panel_pause_status.png` | 当前战况面板。 |
| `button_pause_menu_normal/pressed/disabled.png` | 暂停菜单按钮。 |
| `icon_pause_wave/kill/breach/alive.png` | 战况图标。 |

## 6. 三选一奖励界面素材

参考图：`images/ui-reference-20260517/reward.png`

| 素材 | 说明 |
| --- | --- |
| `bg_reward_base.png` | 奖励背景。 |
| `card_reward_normal/selected/disabled.png` | 奖励卡通用底板。 |
| `card_reward_wood/metal/water/fire/earth.png` | 五行奖励卡变体。 |
| `icon_reward_type_*` | 奖励类型图标。 |
| `panel_reward_preview.png` | 底部选择预览。 |
| `fx_reward_confirm_*` | 选择成功反馈。 |

## 7. 商店界面素材

参考图：`images/ui-reference-20260517/shop.png`

| 素材 | 说明 |
| --- | --- |
| `bg_shop_base.png` | 灵市背景。 |
| `panel_shop_goods.png` | 商品区面板。 |
| `card_shop_item_normal/selected/disabled/soldout.png` | 商品卡。 |
| `ribbon_shop_recommended.png` | 推荐标记。 |
| `stamp_shop_soldout.png` | 已购买/售罄标记。 |
| `icon_shop_item_*` | 商品图标。 |
| `icon_price_spirit_sand.png` | 价格资源图标。 |
| `button_shop_buy_*` | 购买按钮。 |
| `button_shop_refresh_*` | 刷新按钮。 |

## 8. 波次结算素材

参考图：`images/ui-reference-20260517/result-wave.png`

| 素材 | 说明 |
| --- | --- |
| `bg_result_wave_base.png` | 结算背景。 |
| `panel_result_main.png` | 结算主面板。 |
| `icon_result_kill/breach/alive/reward.png` | 统计图标。 |
| `badge_grade_a/b/c/s.png` | 评级徽章。 |
| `row_flower_performance.png` | 花灵表现行。 |
| `button_result_continue_*` | 进入造化按钮。 |

## 9. 失败结算素材

参考图：`images/ui-reference-20260517/result-failure.png`

| 素材 | 说明 |
| --- | --- |
| `bg_result_failure_base.png` | 失败背景。 |
| `panel_failure_main.png` | 失败主面板。 |
| `title_failure_lost.png` | 失败标题字效，可选。 |
| `icon_failure_reason_*` | 失败原因图标。 |
| `button_failure_restart_*` | 重新开始强调按钮。 |

## 10. 胜利结算素材

参考图：`images/ui-reference-20260517/victory.png`

| 素材 | 说明 |
| --- | --- |
| `bg_victory_base.png` | 胜利背景。 |
| `panel_victory_main.png` | 胜利主面板。 |
| `title_victory_revival.png` | 胜利标题字效，可选。 |
| `badge_victory_grade_*` | 最终评级徽章。 |
| `icon_victory_reward_*` | 本局收获图标。 |
| `fx_victory_light_*` | 胜利光效。 |

## 11. 阵图总览素材

参考图：`images/ui-reference-20260517/overview.png`

| 素材 | 说明 |
| --- | --- |
| `bg_overview_base.png` | 总览背景。 |
| `panel_overview_main.png` | 总览主面板。 |
| `tab_overview_normal/selected.png` | 标签。 |
| `overview_node_*` | 阵图节点。 |
| `overview_line_*` | 阵图连线。 |
| `icon_risk_low/mid/high.png` | 风险评级。 |

## 12. 上阵替换素材

参考图：`images/ui-reference-20260517/replacement.png`

| 素材 | 说明 |
| --- | --- |
| `bg_replacement_base.png` | 替换界面背景。 |
| `card_current_slot_normal/selected.png` | 当前上阵槽。 |
| `row_candidate_normal/selected/locked/disabled.png` | 候选花灵条目。 |
| `panel_candidate_detail.png` | 候选详情面板。 |
| `icon_replacement_diff_up/down/same.png` | 替换预览差异图标。 |

## 13. 设置界面素材

参考图：`images/ui-reference-20260517/settings.png`

| 素材 | 说明 |
| --- | --- |
| `bg_settings_base.png` | 设置背景。 |
| `panel_settings_main.png` | 设置主面板。 |
| `tab_settings_category_normal/selected.png` | 左侧分类。 |
| `slider_track.png` | 滑条轨道。 |
| `slider_fill.png` | 滑条填充。 |
| `slider_handle.png` | 滑块。 |
| `toggle_on/off.png` | 开关。 |
| `icon_settings_audio/video/control/battle/accessibility/other.png` | 分类图标。 |

## 14. 花灵图鉴素材

参考图：`images/ui-reference-20260517/codex.png`

| 素材 | 说明 |
| --- | --- |
| `bg_codex_flower_base.png` | 花灵图鉴背景。 |
| `row_codex_flower_normal/selected/locked.png` | 花灵列表项。 |
| `panel_codex_detail.png` | 详情面板。 |
| `tab_codex_normal/selected.png` | 标签。 |
| `char_<id>_portrait.png` | 花灵立绘。 |
| `char_<id>_avatar.png` | 花灵头像。 |
| `char_unknown_silhouette.png` | 未解锁剪影。 |
| `icon_skill_<id>.png` | 技能图标。 |

## 15. 敌人图鉴素材

参考图：`images/ui-reference-20260517/enemy-codex.png`

| 素材 | 说明 |
| --- | --- |
| `bg_codex_enemy_base.png` | 敌人图鉴背景。 |
| `row_codex_enemy_normal/selected/locked.png` | 敌人列表项。 |
| `enemy_<id>_portrait.png` | 敌人立绘。 |
| `enemy_<id>_avatar.png` | 敌人头像。 |
| `enemy_unknown_silhouette.png` | 未遭遇剪影。 |
| `icon_enemy_type_*` | 敌人类型图标。 |
| `icon_drop_*` | 掉落图标。 |

## 16. 局外养成素材

参考图：`images/ui-reference-20260517/garden.png`

| 素材 | 说明 |
| --- | --- |
| `bg_garden_base.png` | 万花残庭背景。 |
| `panel_garden_detail.png` | 节点详情面板。 |
| `button_garden_category_normal/selected.png` | 左侧分类。 |
| `node_garden_locked/available/unlocked/max.png` | 养成节点状态。 |
| `line_garden_locked/unlocked.png` | 节点连线。 |
| `icon_garden_resource_*` | 局外资源。 |
| `fx_garden_unlock_*` | 解锁特效。 |

## 17. 确认弹窗素材

参考图：`images/ui-reference-20260517/confirm.png`

| 素材 | 说明 |
| --- | --- |
| `overlay_modal_dim.png` | 模态遮罩。 |
| `panel_confirm_normal.png` | 普通确认弹窗。 |
| `panel_confirm_danger.png` | 危险确认弹窗。 |
| `button_confirm_accept_*` | 确认按钮。 |
| `button_confirm_cancel_*` | 取消按钮。 |
| `icon_confirm_warning.png` | 警告图标。 |

## 18. 通用提示框素材

参考图：`images/ui-reference-20260517/tip.png`

| 素材 | 说明 |
| --- | --- |
| `panel_tip_toast.png` | 非阻塞提示。 |
| `panel_tip_modal.png` | 模态提示。 |
| `icon_tip_success/warning/error/info.png` | 提示类型图标。 |
| `button_tip_close_*` | 关闭按钮。 |

## 19. 独立主界面素材

正式目录：`Assets/StandaloneMainMenu/Sprites/Final`

| 当前正式素材 | 用途 |
| --- | --- |
| `background_main_scene.png` | 独立主界面背景。 |
| `logo_title_full.png` | 独立主界面 Logo。 |
| `button_plate_main.png` | 四个按钮共用底板。 |

仍建议补齐：

- `button_plate_main_pressed.png`
- `button_plate_main_disabled.png`
- 与主工程一致的按钮音效和字体样式。

## Unity 导入设置建议

| 类型 | Texture Type | Sprite Mode | Mesh Type | Filter | Compression |
| --- | --- | --- | --- | --- | --- |
| UGUI 背景 | Sprite (2D and UI) | Single | Full Rect | Bilinear | Normal 或 None |
| UGUI 图标 | Sprite (2D and UI) | Single | Full Rect | Bilinear | None |
| 九宫格面板 | Sprite (2D and UI) | Single | Full Rect | Bilinear | None |
| Sprite2D 序列帧 | Sprite (2D and UI) | Multiple 或 Single | Tight/Full Rect 按需求 | Point 或 Bilinear | None/Low |
| 特效序列帧 | Sprite (2D and UI) | Multiple | Tight | Bilinear | Low/Normal |

## 最小验收

- 每个 UGUI Image 都能在本清单中找到正式素材或明确占位。
- 每个按钮至少有 normal、pressed、disabled 或统一 Tint/Scale 方案。
- 每个列表项都有 normal、selected、locked/disabled 状态。
- 战斗每种花灵和敌人至少有最小动画集。
- 所有素材命名可被脚本、Prefab 和配置稳定引用。
