---
id: bloomweaver-ui-slicing-layout-asset-map
title: UI 素材拆分与布局关联表
summary: 将每个界面效果图拆解为可生产素材、UGUI 布局区域、控件绑定和运行时使用关系，作为 AI/程序/美术协作开发依据。
type: design
status: active
tags: [ui, ugui, slicing, layout, asset-map, sprite2d]
relates: [bloomweaver-ui-effect-image-gallery, bloomweaver-ui-asset-production-manifest, bloomweaver-ui-control-binding-spec]
read_when: 需要知道每个界面应拆哪些素材、素材用于哪个布局区域、UGUI 控件应绑定哪个素材，或让 AI 根据效果图和策划案自行开发界面。
source: AIGC/projects/Project_BloomWeaver/wiki/design/ui-effect-image-gallery.md; AIGC/projects/Project_BloomWeaver/wiki/design/ui-asset-production-manifest.md; AIGC/projects/Project_BloomWeaver/wiki/development/contracts/ui-control-binding-spec.md; images/ui-reference-20260517/*.png
updated: 2026-05-16
---

# UI 素材拆分与布局关联表

## 结论

正式开发需要在“效果图”和“功能规格”之间增加一层素材映射：

```text
效果图
-> 拆分为背景、面板、按钮、图标、卡片、列表项、动态文本区域
-> 关联到 UGUI 层级和 RectTransform 区域
-> 关联到 Controller 控件名和 ViewModel 字段
-> 进入 Prefab 施工和截图校准
```

当前 `images/ui-reference-20260517/*.png` 多数是完整效果图，不能直接作为唯一 UI 素材使用。它们只作为视觉参考或临时背景。正式 UGUI 开发必须把可交互和动态内容拆成独立素材。

## 拆分状态标记

| 状态 | 含义 |
| --- | --- |
| `existing-reference` | 项目中已有完整效果图，只能参考或临时占位。 |
| `existing-final` | 项目中已有可直接施工的正式素材。 |
| `required-new` | 需要美术或切图流程新增。 |
| `optional-new` | 非首版必须，但建议为动效、质感或后续 polish 准备。 |

## 通用布局区域

| 区域 | 说明 | 常见内容 |
| --- | --- | --- |
| `FullScreenBackground` | 全屏背景层。 | 背景、暗角、氛围。 |
| `TopBar` | 顶部状态栏。 | 波次、资源、计时、帮助、标题。 |
| `LeftPanel` | 左侧面板。 | 花灵状态、分类、难度、列表。 |
| `CenterStage` | 中央主操作区。 | 棋盘、卡片、立绘、节点树、主面板。 |
| `RightPanel` | 右侧详情面板。 | 构筑预览、威胁、详情、推荐。 |
| `BottomBar` | 底部操作区。 | 主操作按钮、确认、返回、刷新。 |
| `ModalCenter` | 居中弹窗区。 | 确认弹窗、提示框。 |
| `OverlayDim` | 覆盖层遮罩。 | 暗色遮罩、阻塞输入。 |

## 通用素材组

这些素材应优先共用，避免每个界面重复制作。

| 素材 ID | 目标文件 | 类型 | 状态 | 用途 |
| --- | --- | --- | --- | --- |
| `bg_dim_overlay` | `ui_common_dim_overlay.png` | Image | `required-new` | 覆盖层和弹窗暗色遮罩。 |
| `panel_large_ornate` | `ui_common_panel_large_ornate.png` | 9-slice | `required-new` | 大型主面板。 |
| `panel_medium_ornate` | `ui_common_panel_medium_ornate.png` | 9-slice | `required-new` | 中型详情面板。 |
| `panel_small_ornate` | `ui_common_panel_small_ornate.png` | 9-slice | `required-new` | 小提示、统计框。 |
| `button_primary` | `ui_common_button_primary_<state>.png` | Button Sprite | `required-new` | 主操作按钮。 |
| `button_secondary` | `ui_common_button_secondary_<state>.png` | Button Sprite | `required-new` | 次级按钮。 |
| `button_danger` | `ui_common_button_danger_<state>.png` | Button Sprite | `required-new` | 返回主界面、重新开始、退出。 |
| `tab_common` | `ui_common_tab_<state>.png` | Toggle Sprite | `required-new` | 图鉴、总览、设置标签。 |
| `list_row_common` | `ui_common_list_row_<state>.png` | 9-slice | `required-new` | 图鉴、候选、分类列表。 |
| `card_common` | `ui_common_card_<state>.png` | 9-slice | `required-new` | 商品、奖励、花灵卡片基础框。 |
| `icon_element_*` | `icon_element_<wood|water|fire|earth|metal>.png` | Icon | `required-new` | 五行。 |
| `icon_resource_*` | `icon_resource_<id>.png` | Icon | `required-new` | 灵砂、灵露、残蕊等资源。 |
| `icon_status_*` | `icon_status_<id>.png` | Icon | `required-new` | 护盾、燃烧、复苏等状态。 |

## 1. 主界面

效果图：`images/ui-reference-20260517/main-menu.png`

### 布局与素材关联

| 布局区域 | UGUI 节点/控件 | 使用素材 | 说明 |
| --- | --- | --- | --- |
| `FullScreenBackground` | `background-raw-image` | `bg_main_menu_clean` | 建议使用无按钮、无文字的干净背景。 |
| `CenterStage` | `logo-root` | `logo_bloomweaver_full` | Logo 应独立素材或 TMP 标题，不建议烘焙在背景。 |
| `CenterStage` | `main-menu-start-button` | `button_main_menu` | 开始守阵。 |
| `CenterStage` | `main-menu-codex-button` | `button_main_menu` | 花灵图鉴。 |
| `CenterStage` | `main-menu-settings-button` | `button_main_menu` | 设置。 |
| `CenterStage` | `main-menu-exit-button` | `button_main_menu` / `button_danger` | 退出。 |
| `LeftPanel/RightPanel` | `element-decor-root` | `decor_main_element_left/right` | 五行侧边装饰。 |
| `BottomBar` | `version-label` | TMP | 版本号动态文本。 |

### 需要拆分/创建的素材

| 素材 ID | 目标文件 | 类型 | 状态 | 来源/说明 |
| --- | --- | --- | --- | --- |
| `bg_main_menu_clean` | `bg_main_menu_clean.png` | Background | `required-new` | 从效果图方向制作无按钮、无 Logo 背景；独立主界面已有 `background_main_scene.png` 可参考。 |
| `logo_bloomweaver_full` | `logo_bloomweaver_full.png` | Image | `existing-final` | 独立主界面已有正式 Logo，可评估复用。 |
| `button_main_menu` | `ui_main_menu_button_<state>.png` | Button Sprite | `required-new` | 需要 normal、pressed、disabled；hover/selected 可选。 |
| `decor_main_element_left` | `ui_main_menu_decor_element_left.png` | Image | `required-new` | 左侧五行装饰。 |
| `decor_main_element_right` | `ui_main_menu_decor_element_right.png` | Image | `required-new` | 右侧五行装饰。 |

## 2. 开局界面

效果图：`images/ui-reference-20260517/opening.png`

### 布局与素材关联

| 布局区域 | UGUI 节点/控件 | 使用素材 | 说明 |
| --- | --- | --- | --- |
| `FullScreenBackground` | `background-raw-image` | `bg_opening_clean` | 无面板和文字的开局背景。 |
| `TopBar` | `opening-title-root` | TMP + `decor_title_flower` | 标题“灵圃启阵”。 |
| `TopBar` | `opening-sand-label` | `icon_resource_spirit_sand` + TMP | 灵砂资源。 |
| `LeftPanel` | `difficulty-panel` | `panel_medium_ornate` | 难度。 |
| `LeftPanel` | `challenge-panel` | `panel_medium_ornate` | 挑战词条。 |
| `CenterStage` | `party-slot-0..4` | `card_party_slot` | 五个花灵卡位。 |
| `RightPanel` | `build-preview-panel` | `panel_medium_ornate` | 构筑预览。 |
| `RightPanel` | `initial-board-card-list` | `card_initial_board` | 初始阵图方案。 |
| `RightPanel` | `initial-blessing-card-list` | `card_initial_blessing` | 初始造化。 |
| `BottomBar` | `opening-back/random/start-button` | `button_secondary` / `button_primary` | 底部操作。 |

### 需要拆分/创建的素材

| 素材 ID | 目标文件 | 类型 | 状态 | 来源/说明 |
| --- | --- | --- | --- | --- |
| `bg_opening_clean` | `bg_opening_clean.png` | Background | `required-new` | 去除所有 UI 面板的庭院背景。 |
| `card_party_slot` | `ui_opening_party_slot_<state>.png` | 9-slice/Card | `required-new` | normal、selected、empty、disabled。 |
| `button_difficulty` | `ui_opening_difficulty_<state>.png` | Toggle Sprite | `required-new` | 清修、标准、劫难共用。 |
| `button_challenge_tag` | `ui_opening_challenge_tag_<state>.png` | Toggle Sprite | `required-new` | 词条共用。 |
| `card_initial_board` | `ui_opening_board_plan_<state>.png` | Card | `required-new` | 阵图方案卡。 |
| `card_initial_blessing` | `ui_opening_blessing_<state>.png` | Card | `required-new` | 初始造化卡。 |
| `icon_difficulty_*` | `icon_difficulty_<id>.png` | Icon | `required-new` | 难度图标。 |
| `icon_challenge_*` | `icon_challenge_<id>.png` | Icon | `required-new` | 挑战词条图标。 |
| `char_*_avatar` | `char_<id>_avatar.png` | Icon | `required-new` | 花灵卡头像。 |

## 3. 布阵界面

效果图：`images/ui-reference-20260517/planning.png`

### 布局与素材关联

| 布局区域 | UGUI 节点/控件 | 使用素材 | 说明 |
| --- | --- | --- | --- |
| `FullScreenBackground` | `background-raw-image` | `bg_planning_clean` | 战场背景。 |
| `TopBar` | `phase/wave/hint/timer/stats-label` | `panel_top_bar` + TMP | 顶部 HUD。 |
| `LeftPanel` | `flower-status-list` | `panel_flower_status` + `list_row_common` | 花灵状态。 |
| `CenterStage` | `planning-grid` | `board_grid_base` + `node_*` + `line_spirit_*` | 棋盘和灵脉。 |
| `RightPanel` | `threat-panel` | `panel_threat_preview` + `icon_enemy_*` | 本波威胁。 |
| `BottomBar` | `undo/clear/start/reweave-button` | `button_secondary` / `button_primary` | 布阵操作。 |

### 需要拆分/创建的素材

| 素材 ID | 目标文件 | 类型 | 状态 | 来源/说明 |
| --- | --- | --- | --- | --- |
| `bg_planning_clean` | `bg_planning_clean.png` | Background | `required-new` | 去除棋盘和 UI 的战场底图。 |
| `panel_top_bar` | `ui_common_top_bar.png` | 9-slice | `required-new` | 顶部状态栏。 |
| `panel_flower_status` | `ui_planning_flower_status_panel.png` | 9-slice | `required-new` | 左侧花灵状态。 |
| `panel_threat_preview` | `ui_planning_threat_panel.png` | 9-slice | `required-new` | 右侧敌潮威胁。 |
| `board_grid_base` | `ui_board_grid_base.png` | Image | `required-new` | 棋盘底板。 |
| `node_*` | `ui_board_node_<state>.png` | Sprite | `required-new` | normal、available、selected、blocked、exhausted、reviving。 |
| `line_spirit_*` | `ui_board_line_<state>.png` | Sprite/Line | `required-new` | 灵脉线段。 |
| `icon_enemy_threat_*` | `icon_enemy_threat_<id>.png` | Icon | `required-new` | 威胁列表小图标。 |

## 4. 战斗界面

效果图：`images/ui-reference-20260517/combat.png`

### 布局与素材关联

| 布局区域 | 节点/控件 | 使用素材 | 说明 |
| --- | --- | --- | --- |
| Sprite2D `BattleBackground` | `bg-far/bg-mid/bg-ground` | `bg_combat_far/mid/ground` | 战斗主体背景分层。 |
| Sprite2D `BattleField` | `path-root/grid-root` | `battle_path_*` / `battle_grid_base` | 敌人路径和棋盘。 |
| Sprite2D `BattleUnit` | `ally-sprites` | `char_*_battle_*` | 花灵战斗 Sprite。 |
| Sprite2D `BattleUnit` | `enemy-sprites` | `enemy_*_*` | 敌人 Sprite。 |
| Sprite2D `BattleEffect` | `effect-sprites` | `projectile_*` / `fx_*` | 投射物和特效。 |
| `TopBar` UGUI | `wave/timer/stats-label` | `hud_combat_top_bar` + TMP | 战斗 HUD。 |
| `RightPanel` UGUI | `pressure-panel` | `hud_combat_pressure_panel` | 战场压力。 |
| `BottomBar` UGUI | `current-line/current-trigger/pause` | `button_pause` + TMP | 当前触发和暂停。 |

### 需要拆分/创建的素材

| 素材 ID | 目标文件 | 类型 | 状态 | 来源/说明 |
| --- | --- | --- | --- | --- |
| `bg_combat_far` | `bg_combat_far.png` | Sprite2D Background | `required-new` | 远景。 |
| `bg_combat_mid` | `bg_combat_mid.png` | Sprite2D Background | `required-new` | 中景。 |
| `bg_combat_ground` | `bg_combat_ground.png` | Sprite2D Background | `required-new` | 地面和路径。 |
| `bg_combat_foreground` | `bg_combat_foreground.png` | Sprite2D Foreground | `optional-new` | 前景遮挡。 |
| `battle_grid_base` | `battle_grid_base.png` | Sprite2D/Image | `required-new` | 战斗棋盘。 |
| `char_*_battle_*` | `char_<id>_battle_<state>_<frame>.png` | Sprite2D | `required-new` | 花灵 Idle、Attack、Hit、Down。 |
| `enemy_*_*` | `enemy_<id>_<state>_<frame>.png` | Sprite2D | `required-new` | 敌人 Move、Hit、Death、Breach。 |
| `projectile_*` | `projectile_<element>_<type>.png` | Sprite2D | `required-new` | 普攻、技能、必杀。 |
| `fx_*` | `fx_<element>_<action>_<frame>.png` | Sprite2D/VFX | `required-new` | 命中、治疗、护盾、燃烧、死亡。 |
| `hud_combat_top_bar` | `ui_combat_top_bar.png` | 9-slice | `required-new` | UGUI HUD 背板。 |
| `button_pause` | `ui_combat_button_pause_<state>.png` | Button Sprite | `required-new` | 暂停按钮。 |

## 5. 暂停界面

效果图：`images/ui-reference-20260517/pause.png`

| 布局区域 | UGUI 节点/控件 | 使用素材 | 说明 |
| --- | --- | --- | --- |
| `OverlayDim` | `pause-dim` | `bg_dim_overlay` | 暗色遮罩。 |
| `ModalCenter` | `pause-panel` | `panel_pause_main` | 暂停主面板。 |
| `CenterStage` | `combat-snapshot` | `panel_small_ornate` + `icon_pause_*` | 当前战况。 |
| `RightPanel` | `pause-button-list` | `button_pause_menu` | 继续、总览、状态、设置、重开、返回。 |

| 素材 ID | 目标文件 | 类型 | 状态 | 来源/说明 |
| --- | --- | --- | --- | --- |
| `panel_pause_main` | `ui_pause_panel_main.png` | 9-slice | `required-new` | 暂停主面板。 |
| `button_pause_menu` | `ui_pause_button_menu_<state>.png` | Button Sprite | `required-new` | 暂停菜单按钮。 |
| `icon_pause_*` | `icon_pause_<wave|kill|breach|alive>.png` | Icon | `required-new` | 战况图标。 |

## 6. 三选一奖励界面

效果图：`images/ui-reference-20260517/reward.png`

| 布局区域 | UGUI 节点/控件 | 使用素材 | 说明 |
| --- | --- | --- | --- |
| `FullScreenBackground` | `background-raw-image` | `bg_reward_clean` | 奖励背景。 |
| `TopBar` | `reward-title/resource` | TMP + `icon_resource_*` | 标题和资源。 |
| `CenterStage` | `reward-card-0..2` | `card_reward_*` | 三张奖励卡。 |
| `BottomBar` | `reward-preview-panel` | `panel_reward_preview` | 选择预览。 |
| `BottomBar` | `skip/confirm/overview-button` | `button_secondary` / `button_primary` | 操作按钮。 |

| 素材 ID | 目标文件 | 类型 | 状态 | 来源/说明 |
| --- | --- | --- | --- | --- |
| `bg_reward_clean` | `bg_reward_clean.png` | Background | `required-new` | 去 UI 的奖励背景。 |
| `card_reward_*` | `ui_reward_card_<element>_<state>.png` | Card | `required-new` | normal、selected、disabled。 |
| `panel_reward_preview` | `ui_reward_preview_panel.png` | 9-slice | `required-new` | 底部构筑预览。 |
| `icon_reward_type_*` | `icon_reward_type_<id>.png` | Icon | `required-new` | 奖励类型。 |
| `fx_reward_confirm` | `fx_ui_reward_confirm_<frame>.png` | UI FX | `optional-new` | 选择成功。 |

## 7. 商店界面

效果图：`images/ui-reference-20260517/shop.png`

| 布局区域 | UGUI 节点/控件 | 使用素材 | 说明 |
| --- | --- | --- | --- |
| `FullScreenBackground` | `background-raw-image` | `bg_shop_clean` | 商店背景。 |
| `TopBar` | `shop-title/resource` | TMP + `icon_resource_*` | 标题和资源。 |
| `CenterStage` | `shop-item-card-0..5` | `card_shop_item` | 商品六宫格。 |
| `RightPanel` | `shop-preview-panel` | `panel_medium_ornate` | 推荐和购买预览。 |
| `BottomBar` | `refresh/continue-button` | `button_secondary` / `button_primary` | 刷新和下一波。 |

| 素材 ID | 目标文件 | 类型 | 状态 | 来源/说明 |
| --- | --- | --- | --- | --- |
| `bg_shop_clean` | `bg_shop_clean.png` | Background | `required-new` | 去 UI 的灵市背景。 |
| `card_shop_item` | `ui_shop_item_card_<state>.png` | Card | `required-new` | normal、selected、disabled、soldout。 |
| `icon_shop_item_*` | `icon_shop_item_<id>.png` | Icon | `required-new` | 商品图标。 |
| `stamp_shop_soldout` | `ui_shop_stamp_soldout.png` | Image | `required-new` | 已购买/售罄标记。 |
| `ribbon_shop_recommended` | `ui_shop_ribbon_recommended.png` | Image | `optional-new` | 推荐购买标记。 |

## 8. 波次结算界面

效果图：`images/ui-reference-20260517/result-wave.png`

| 布局区域 | UGUI 节点/控件 | 使用素材 | 说明 |
| --- | --- | --- | --- |
| `FullScreenBackground` | `background-raw-image` | `bg_result_wave_clean` | 波次结算背景。 |
| `CenterStage` | `result-main-panel` | `panel_result_main` | 主结算面板。 |
| `CenterStage` | `result-kill/breach/alive/grade-label` | `icon_result_*` + TMP | 统计项。 |
| `CenterStage` | `performance-list` | `row_flower_performance` | 花灵表现。 |
| `BottomBar` | `detail/restart/main-menu/continue-button` | `button_secondary` / `button_primary` / `button_danger` | 操作按钮。 |

| 素材 ID | 目标文件 | 类型 | 状态 | 来源/说明 |
| --- | --- | --- | --- | --- |
| `bg_result_wave_clean` | `bg_result_wave_clean.png` | Background | `required-new` | 去 UI 背景。 |
| `panel_result_main` | `ui_result_panel_main.png` | 9-slice | `required-new` | 主面板。 |
| `icon_result_*` | `icon_result_<kill|breach|alive|reward>.png` | Icon | `required-new` | 统计图标。 |
| `badge_grade_*` | `ui_grade_<s|a|b|c>.png` | Image | `required-new` | 评级。 |
| `row_flower_performance` | `ui_result_row_flower_performance.png` | 9-slice | `required-new` | 表现行。 |

## 9. 失败结算界面

效果图：`images/ui-reference-20260517/result-failure.png`

| 布局区域 | UGUI 节点/控件 | 使用素材 | 说明 |
| --- | --- | --- | --- |
| `FullScreenBackground` | `background-raw-image` | `bg_result_failure_clean` | 紫黑失败背景。 |
| `CenterStage` | `failure-main-panel` | `panel_failure_main` | 失败主面板。 |
| `CenterStage` | `failure-reason` | `icon_failure_reason_*` + TMP | 失败原因。 |
| `BottomBar` | `detail/restart/main-menu-button` | `button_secondary` / `button_danger` | 失败操作。 |

| 素材 ID | 目标文件 | 类型 | 状态 | 来源/说明 |
| --- | --- | --- | --- | --- |
| `bg_result_failure_clean` | `bg_result_failure_clean.png` | Background | `required-new` | 去 UI 失败背景。 |
| `panel_failure_main` | `ui_failure_panel_main.png` | 9-slice | `required-new` | 失败结算面板。 |
| `title_failure_lost` | `ui_failure_title_lost.png` | Image/TMP Style | `optional-new` | 失败标题字效。 |
| `icon_failure_reason_*` | `icon_failure_reason_<id>.png` | Icon | `required-new` | 失败原因。 |

## 10. 胜利结算界面

效果图：`images/ui-reference-20260517/victory.png`

| 布局区域 | UGUI 节点/控件 | 使用素材 | 说明 |
| --- | --- | --- | --- |
| `FullScreenBackground` | `background-raw-image` | `bg_victory_clean` | 胜利背景。 |
| `CenterStage` | `victory-main-panel` | `panel_victory_main` | 主面板。 |
| `CenterStage` | `victory-grade/reward-list` | `badge_victory_grade_*` + `icon_victory_reward_*` | 评级和收获。 |
| `BottomBar` | `main-menu/garden/restart-button` | `button_secondary` / `button_primary` | 操作按钮。 |

| 素材 ID | 目标文件 | 类型 | 状态 | 来源/说明 |
| --- | --- | --- | --- | --- |
| `bg_victory_clean` | `bg_victory_clean.png` | Background | `required-new` | 去 UI 胜利背景。 |
| `panel_victory_main` | `ui_victory_panel_main.png` | 9-slice | `required-new` | 胜利主面板。 |
| `badge_victory_grade_*` | `ui_victory_grade_<id>.png` | Image | `required-new` | 最终评级。 |
| `icon_victory_reward_*` | `icon_victory_reward_<id>.png` | Icon | `required-new` | 本局收获。 |
| `fx_victory_light` | `fx_ui_victory_light_<frame>.png` | UI FX | `optional-new` | 胜利光效。 |

## 11. 阵图总览界面

效果图：`images/ui-reference-20260517/overview.png`

| 布局区域 | UGUI 节点/控件 | 使用素材 | 说明 |
| --- | --- | --- | --- |
| `OverlayDim` | `overview-dim` | `bg_dim_overlay` | 遮罩。 |
| `CenterStage` | `overview-main-panel` | `panel_overview_main` | 总览主面板。 |
| `TopBar` | `overview-tabs` | `tab_overview` | 阵图、花灵、造化、敌潮、统计。 |
| `CenterStage` | `overview-board` | `overview_node_*` + `overview_line_*` | 阵图关系。 |
| `LeftPanel/RightPanel` | `summary/risk/status` | `panel_medium_ornate` + `icon_risk_*` | 构筑和风险。 |
| `BottomBar` | `close/back/victory-button` | `button_secondary` / `button_primary` | 操作。 |

| 素材 ID | 目标文件 | 类型 | 状态 | 来源/说明 |
| --- | --- | --- | --- | --- |
| `panel_overview_main` | `ui_overview_panel_main.png` | 9-slice | `required-new` | 总览主面板。 |
| `tab_overview` | `ui_overview_tab_<state>.png` | Toggle Sprite | `required-new` | 标签页。 |
| `overview_node_*` | `ui_overview_node_<state>.png` | Icon | `required-new` | 阵图节点。 |
| `overview_line_*` | `ui_overview_line_<state>.png` | Sprite | `required-new` | 阵图连线。 |
| `icon_risk_*` | `icon_risk_<low|mid|high>.png` | Icon | `required-new` | 风险评级。 |

## 12. 上阵替换界面

效果图：`images/ui-reference-20260517/replacement.png`

| 布局区域 | UGUI 节点/控件 | 使用素材 | 说明 |
| --- | --- | --- | --- |
| `OverlayDim` | `replacement-dim` | `bg_dim_overlay` | 遮罩。 |
| `LeftPanel` | `current-party-list` | `card_current_slot` | 当前上阵槽。 |
| `CenterStage` | `candidate-detail-panel` | `panel_candidate_detail` | 候选详情和预览。 |
| `RightPanel` | `candidate-list` | `row_candidate` | 候选花灵列表。 |
| `BottomBar` | `auto/cancel/confirm-button` | `button_secondary` / `button_primary` | 操作按钮。 |

| 素材 ID | 目标文件 | 类型 | 状态 | 来源/说明 |
| --- | --- | --- | --- | --- |
| `card_current_slot` | `ui_replacement_current_slot_<state>.png` | Card | `required-new` | 当前槽位。 |
| `row_candidate` | `ui_replacement_candidate_row_<state>.png` | 9-slice | `required-new` | 候选行。 |
| `panel_candidate_detail` | `ui_replacement_candidate_detail.png` | 9-slice | `required-new` | 候选详情。 |
| `icon_replacement_diff_*` | `icon_replacement_diff_<up|down|same>.png` | Icon | `required-new` | 替换差异。 |

## 13. 设置界面

效果图：`images/ui-reference-20260517/settings.png`

| 布局区域 | UGUI 节点/控件 | 使用素材 | 说明 |
| --- | --- | --- | --- |
| `OverlayDim/FullScreenBackground` | `settings-bg` | `bg_settings_clean` 或遮罩 | 设置背景。 |
| `CenterStage` | `settings-main-panel` | `panel_settings_main` | 主面板。 |
| `LeftPanel` | `settings-category-list` | `tab_settings_category` | 分类。 |
| `RightPanel` | `setting-control-list` | `slider_*` / `toggle_*` | 设置项。 |
| `BottomBar` | `reset/cancel/apply/confirm-button` | `button_secondary` / `button_primary` | 操作。 |

| 素材 ID | 目标文件 | 类型 | 状态 | 来源/说明 |
| --- | --- | --- | --- | --- |
| `bg_settings_clean` | `bg_settings_clean.png` | Background | `required-new` | 设置背景。 |
| `panel_settings_main` | `ui_settings_panel_main.png` | 9-slice | `required-new` | 设置主面板。 |
| `tab_settings_category` | `ui_settings_category_<state>.png` | Toggle Sprite | `required-new` | 分类标签。 |
| `slider_track/fill/handle` | `ui_settings_slider_<part>.png` | Slider Sprite | `required-new` | 滑条。 |
| `toggle_on/off` | `ui_settings_toggle_<on|off>.png` | Toggle Sprite | `required-new` | 开关。 |

## 14. 花灵图鉴界面

效果图：`images/ui-reference-20260517/codex.png`

| 布局区域 | UGUI 节点/控件 | 使用素材 | 说明 |
| --- | --- | --- | --- |
| `FullScreenBackground` | `background-raw-image` | `bg_codex_flower_clean` | 图鉴背景。 |
| `LeftPanel` | `flower-codex-list` | `row_codex_flower` | 花灵列表。 |
| `CenterStage` | `flower-portrait` | `char_*_portrait` | 立绘。 |
| `RightPanel` | `flower-detail-panel` | `panel_codex_detail` | 详情。 |
| `TopBar/RightPanel` | `codex-tabs` | `tab_codex` | 基础、技能、扫描、灵脉、故事。 |
| `BottomBar` | `close/enemy/garden-button` | `button_secondary` / `button_primary` | 操作。 |

| 素材 ID | 目标文件 | 类型 | 状态 | 来源/说明 |
| --- | --- | --- | --- | --- |
| `bg_codex_flower_clean` | `bg_codex_flower_clean.png` | Background | `required-new` | 花灵图鉴背景。 |
| `row_codex_flower` | `ui_codex_flower_row_<state>.png` | 9-slice | `required-new` | 列表项。 |
| `panel_codex_detail` | `ui_codex_detail_panel.png` | 9-slice | `required-new` | 详情面板。 |
| `tab_codex` | `ui_codex_tab_<state>.png` | Toggle Sprite | `required-new` | 标签。 |
| `char_*_portrait` | `char_<id>_portrait.png` | Image | `required-new` | 花灵立绘。 |
| `char_unknown_silhouette` | `char_unknown_silhouette.png` | Image | `required-new` | 未解锁剪影。 |
| `icon_skill_*` | `icon_skill_<id>.png` | Icon | `required-new` | 技能图标。 |

## 15. 敌人图鉴界面

效果图：`images/ui-reference-20260517/enemy-codex.png`

| 布局区域 | UGUI 节点/控件 | 使用素材 | 说明 |
| --- | --- | --- | --- |
| `FullScreenBackground` | `background-raw-image` | `bg_codex_enemy_clean` | 敌人图鉴背景。 |
| `LeftPanel` | `enemy-codex-list` | `row_codex_enemy` | 敌人列表。 |
| `CenterStage` | `enemy-portrait` | `enemy_*_portrait` | 敌人立绘。 |
| `RightPanel` | `enemy-detail-panel` | `panel_codex_detail` | 详情。 |
| `RightPanel` | `enemy-tabs` | `tab_codex` | 基础、行为、克制、波次、掉落。 |
| `BottomBar` | `close/flower/strategy-button` | `button_secondary` / `button_primary` | 操作。 |

| 素材 ID | 目标文件 | 类型 | 状态 | 来源/说明 |
| --- | --- | --- | --- | --- |
| `bg_codex_enemy_clean` | `bg_codex_enemy_clean.png` | Background | `required-new` | 敌人图鉴背景。 |
| `row_codex_enemy` | `ui_codex_enemy_row_<state>.png` | 9-slice | `required-new` | 敌人列表项。 |
| `enemy_*_portrait` | `enemy_<id>_portrait.png` | Image | `required-new` | 敌人立绘。 |
| `enemy_unknown_silhouette` | `enemy_unknown_silhouette.png` | Image | `required-new` | 未遭遇剪影。 |
| `icon_enemy_type_*` | `icon_enemy_type_<id>.png` | Icon | `required-new` | 敌人类型。 |
| `icon_drop_*` | `icon_drop_<id>.png` | Icon | `required-new` | 掉落。 |

## 16. 局外养成界面

效果图：`images/ui-reference-20260517/garden.png`

| 布局区域 | UGUI 节点/控件 | 使用素材 | 说明 |
| --- | --- | --- | --- |
| `FullScreenBackground` | `background-raw-image` | `bg_garden_clean` | 万花残庭背景。 |
| `LeftPanel` | `garden-category-list` | `button_garden_category` | 分类菜单。 |
| `CenterStage` | `garden-node-tree` | `node_garden_*` + `line_garden_*` | 节点树。 |
| `RightPanel` | `garden-detail-panel` | `panel_garden_detail` | 节点详情。 |
| `BottomBar` | `garden-resource-bar` | `icon_garden_resource_*` + TMP | 资源。 |
| `BottomBar/RightPanel` | `unlock/close-button` | `button_primary` / `button_secondary` | 解锁和返回。 |

| 素材 ID | 目标文件 | 类型 | 状态 | 来源/说明 |
| --- | --- | --- | --- | --- |
| `bg_garden_clean` | `bg_garden_clean.png` | Background | `required-new` | 局外养成背景。 |
| `button_garden_category` | `ui_garden_category_<state>.png` | Toggle Sprite | `required-new` | 左侧分类。 |
| `node_garden_*` | `ui_garden_node_<state>.png` | Icon/Button | `required-new` | locked、available、unlocked、max。 |
| `line_garden_*` | `ui_garden_line_<state>.png` | Sprite | `required-new` | 节点连线。 |
| `panel_garden_detail` | `ui_garden_detail_panel.png` | 9-slice | `required-new` | 详情面板。 |
| `icon_garden_resource_*` | `icon_garden_resource_<id>.png` | Icon | `required-new` | 局外资源。 |

## 17. 确认弹窗

效果图：`images/ui-reference-20260517/confirm.png`

| 布局区域 | UGUI 节点/控件 | 使用素材 | 说明 |
| --- | --- | --- | --- |
| `OverlayDim` | `confirm-dim` | `bg_dim_overlay` | 模态遮罩。 |
| `ModalCenter` | `confirm-panel` | `panel_confirm_normal` / `panel_confirm_danger` | 弹窗面板。 |
| `ModalCenter` | `confirm-title/message/preview` | TMP | 动态文案。 |
| `BottomBar` | `confirm-cancel/accept-button` | `button_secondary` / `button_primary` / `button_danger` | 操作。 |

| 素材 ID | 目标文件 | 类型 | 状态 | 来源/说明 |
| --- | --- | --- | --- | --- |
| `panel_confirm_normal` | `ui_confirm_panel_normal.png` | 9-slice | `required-new` | 普通确认。 |
| `panel_confirm_danger` | `ui_confirm_panel_danger.png` | 9-slice | `required-new` | 危险确认。 |
| `icon_confirm_warning` | `icon_confirm_warning.png` | Icon | `required-new` | 警告图标。 |

## 18. 通用提示框

效果图：`images/ui-reference-20260517/tip.png`

| 布局区域 | UGUI 节点/控件 | 使用素材 | 说明 |
| --- | --- | --- | --- |
| `ModalCenter` 或 `ToastLayer` | `tip-panel` | `panel_tip_toast` / `panel_tip_modal` | 提示容器。 |
| `ModalCenter` | `tip-icon` | `icon_tip_*` | 成功、警告、错误、信息。 |
| `ModalCenter` | `tip-message-label` | TMP | 提示文本。 |
| `ModalCenter` | `tip-close-button` | `button_secondary` | 关闭。 |

| 素材 ID | 目标文件 | 类型 | 状态 | 来源/说明 |
| --- | --- | --- | --- | --- |
| `panel_tip_toast` | `ui_tip_panel_toast.png` | 9-slice | `required-new` | 非阻塞提示。 |
| `panel_tip_modal` | `ui_tip_panel_modal.png` | 9-slice | `required-new` | 模态提示。 |
| `icon_tip_*` | `icon_tip_<success|warning|error|info>.png` | Icon | `required-new` | 提示类型。 |

## 19. 独立主界面

参考效果图：`images/ui-reference-20260517/standalone-main-menu.png`

正式素材：

| 布局区域 | UGUI 节点/控件 | 使用素材 | 状态 | 说明 |
| --- | --- | --- | --- | --- |
| `FullScreenBackground` | `background` | `Assets/StandaloneMainMenu/Sprites/Final/background_main_scene.png` | `existing-final` | 正式背景。 |
| `CenterStage` | `logo` | `Assets/StandaloneMainMenu/Sprites/Final/logo_title_full.png` | `existing-final` | 正式 Logo。 |
| `CenterStage` | `start/codex/settings/exit-button` | `Assets/StandaloneMainMenu/Sprites/Final/button_plate_main.png` | `existing-final` | 四个按钮底板，文字由 TMP 生成。 |

补充建议：

| 素材 ID | 目标文件 | 类型 | 状态 | 说明 |
| --- | --- | --- | --- | --- |
| `button_plate_main_pressed` | `button_plate_main_pressed.png` | Button Sprite | `optional-new` | 按下态。 |
| `button_plate_main_disabled` | `button_plate_main_disabled.png` | Button Sprite | `optional-new` | 禁用态。 |

注意：

- `ReferenceOnly` 目录只能作为视觉参考，不能接入 Prefab、Scene、Config 或 RuntimeConfig。
- 独立主界面文字不烘焙进按钮图，保持 TMP 文本可编辑。

## 开发读取方式

AI 或程序开发某个界面时应读取：

1. 本文对应界面的“布局与素材关联”。
2. `ui-effect-image-gallery.md` 中对应效果图。
3. `ui-interface-detail-spec.md` 中对应界面功能和交互。
4. `ui-control-binding-spec.md` 中对应控件绑定。
5. `ui-functional-acceptance-tests.md` 中对应验收用例。

## 最小完成标准

- 每个可交互按钮都有明确素材 ID 和控件名。
- 每个动态文本区域不烘焙在背景图内。
- 每个列表、卡片、页签都有 normal 和 selected 状态。
- 每个禁用操作都有 disabled 状态或统一 Tint/Scale 方案。
- 战斗界面 Sprite2D 素材与 UGUI HUD 素材分开管理。
- 独立主界面不把 ReferenceOnly 资源接入运行时。
