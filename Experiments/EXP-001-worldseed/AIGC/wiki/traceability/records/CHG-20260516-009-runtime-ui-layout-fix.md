# CHG-20260516-009-runtime-ui-layout-fix

## 状态

- status: active
- source: 用户实机截图反馈
- updated: 2026-05-16

## 来源

- 用户反馈：界面和确认截图不一致，所有界面都带滚动框，奖励页内容横向溢出。
- 关联问题：`WorldSeed.AIGC/workflows/development/runs/ISSUES-20260516-001-playable-loop.md` 中 `DEV-007`
- 关联变更基线：`CHG-20260516-008-card-style-runtime-ui`

## 变更内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| Godot UI 脚本 | `scripts/Main.gd` | 移除全局 `ScrollContainer`，修复所有界面都出现滚动框的问题；压缩斗法、奖励和牌组展示，避免 1280x720 视口横向溢出。 |
| GameSpec 数据 | `data/game_spec/ascension_forge.prototype.json` | 调整标题字号、牌组列数和资源徽章尺寸，使布局参数可配置。 |
| 验证工具 | `tools/check_gdscript_sanity.py` | 增加全局滚动容器回归检查，避免再次把全部界面包入滚动框。 |
| 问题记录 | `WorldSeed.AIGC/workflows/development/runs/ISSUES-20260516-001-playable-loop.md` | 记录并关闭本次实机布局反馈。 |

## 影响范围

- 主菜单到结算的运行时 UI 布局。
- 不改变战斗、奖励、事件、商店、构筑等玩法规则。
- 不新增界面流程。

## 验证方式

- `python tools\check_gdscript_sanity.py`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`
- 检索 `scripts/` 中无 `ScrollContainer`、`:=`、`.join(`、额外 `class`

## 验证结果

已通过 `VER-20260516-009-runtime-ui-layout-fix-check` 验证。

## 是否晋升为项目事实

是。当前运行时 UI 不再使用全局滚动容器，第一阶段界面应优先在 1280x720 视口内固定布局。
