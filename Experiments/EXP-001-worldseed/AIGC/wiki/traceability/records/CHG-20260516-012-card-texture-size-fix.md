# CHG-20260516-012-card-texture-size-fix

## 状态

- status: active
- source: 用户实机截图反馈
- updated: 2026-05-16

## 来源

- 用户反馈：主菜单“最近远征”中的卡框巨大化，覆盖面板内容。
- 关联问题：`WorldSeed.AIGC/workflows/development/runs/ISSUES-20260516-001-playable-loop.md` 中 `DEV-010`
- 关联变更：`CHG-20260516-011-combat-card-frame-visual-fix`

## 变更内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| Godot UI 脚本 | `scripts/Main.gd` | 锁定卡牌纹理容器尺寸，卡牌外层和卡牌画布使用收缩布局，避免被父容器拉伸。 |
| 验证工具 | `tools/check_gdscript_sanity.py` | 增加卡牌固定尺寸回归检查。 |
| 问题记录 | `WorldSeed.AIGC/workflows/development/runs/ISSUES-20260516-001-playable-loop.md` | 记录并关闭卡牌纹理拉伸问题。 |

## 影响范围

- 所有复用 `_add_card_to` 的卡牌显示：主菜单最近远征、角色选择、斗法、奖励、构筑和详情。
- 不改变玩法规则、数据结构或界面跳转。

## 验证方式

- `python tools\check_gdscript_sanity.py`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`

## 验证结果

已通过 `VER-20260516-012-card-texture-size-fix-check` 验证。

## 是否晋升为项目事实

是。卡牌纹理容器必须保持固定尺寸，不允许被父布局拉伸。
