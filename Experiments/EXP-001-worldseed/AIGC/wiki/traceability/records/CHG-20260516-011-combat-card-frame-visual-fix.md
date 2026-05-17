# CHG-20260516-011-combat-card-frame-visual-fix

## 状态

- status: active
- source: 用户实机截图反馈
- updated: 2026-05-16

## 来源

- 用户反馈：斗法界面仍像普通控件拼接，没有贴近已确认的参考卡牌素材图。
- 关联问题：`WorldSeed.AIGC/workflows/development/runs/ISSUES-20260516-001-playable-loop.md` 中 `DEV-009`
- 关联设计：`WorldSeed.AIGC/wiki/design/ui-screen-visual-spec-v0.3.md`

## 变更内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| Godot UI 脚本 | `scripts/Main.gd` | 斗法页改为专用页眉；清除顶部红字提示；卡牌组件改为加载卡框纹理并按费用、门类、标题、插画、规则、类型区布局。 |
| 卡牌素材 | `assets/cards/card_attack.png` | 替换为浅色卷轴风格攻击卡框。 |
| 卡牌素材 | `assets/cards/card_defense.png` | 替换为浅色卷轴风格防御卡框。 |
| 卡牌素材 | `assets/cards/card_skill.png` | 替换为浅色卷轴风格技能卡框。 |
| 卡牌素材 | `assets/cards/card_support.png` | 替换为浅色卷轴风格符箓卡框。 |
| 卡牌素材 | `assets/cards/card_curse.png` | 替换为浅色卷轴风格劫咒卡框。 |
| GameSpec 数据 | `data/game_spec/ascension_forge.prototype.json` | 调整紧凑卡尺寸，使手牌和敌阵更接近参考图比例。 |
| 问题记录 | `WorldSeed.AIGC/workflows/development/runs/ISSUES-20260516-001-playable-loop.md` | 记录并关闭斗法卡牌视觉反馈。 |

## 影响范围

- 斗法界面、奖励界面、构筑界面、详情界面中复用的卡牌视觉。
- 不改变战斗规则、卡牌效果、奖励逻辑或数据契约。

## 验证方式

- `python tools\check_gdscript_sanity.py`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`

## 验证结果

已通过 `VER-20260516-011-combat-card-frame-visual-fix-check` 验证。

## 是否晋升为项目事实

是。当前卡牌视觉基线改为浅色卷轴卡框，运行时卡牌组件必须使用卡框纹理承载卡面结构。
