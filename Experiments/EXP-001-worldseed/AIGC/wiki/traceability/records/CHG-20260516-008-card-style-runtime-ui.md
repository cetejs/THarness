# CHG-20260516-008-card-style-runtime-ui

## 状态

- status: active
- source: 用户确认 v0.3 并要求进入开发
- updated: 2026-05-16

## 来源

- 用户请求：按照已确认的参考卡牌风格开始开发，并交付完整游戏体验内容。
- 关联设计：`WorldSeed.AIGC/wiki/design/ui-screen-visual-spec-v0.3.md`
- 关联开发子任务：`WorldSeed.AIGC/wiki/development/subtasks/ui-SUB-20260516-006-card-style-runtime-ui.md`
- 关联运行记录：`WorldSeed.AIGC/workflows/development/runs/RUN-20260516-002-card-style-runtime-ui.md`

## 变更内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| Godot UI 脚本 | `scripts/Main.gd` | 将第一阶段运行时界面改为 v0.3 卡牌参考风格，覆盖主菜单到结算的完整玩家路径，并补充设置、详情和确认界面入口。 |
| Godot 运行时文案 | `scripts/GameRuntime.gd` | 将战斗、奖励、符箓、悟道等提示文案统一到修仙语境，不改变规则。 |
| GameSpec 数据 | `data/game_spec/ascension_forge.prototype.json` | 补充 `ui_copy` 和卡牌风格布局参数，调整显示名和体验文案。 |
| 说明文档 | `README.md` | 更新当前可玩体验、运行方式和操作术语。 |
| 开发运行记录 | `WorldSeed.AIGC/workflows/development/runs/RUN-20260516-002-card-style-runtime-ui.md` | 记录本次开发进度、验证结果和 Godot 命令行验证局限。 |
| 问题记录 | `WorldSeed.AIGC/workflows/development/runs/ISSUES-20260516-001-playable-loop.md` | 记录并关闭 v0.3 UI 落地时发现的详情按钮和门类标识问题。 |

## 影响范围

- 第一阶段可玩原型从文字占位界面推进为卡牌化修仙 UI。
- 玩家可完成主菜单、角色选择、灵脉图、斗法、奖励、构筑洞府、奇遇、灵市/锻炉、镇守、洞天结算和本局结算。
- 不新增未确认玩法系统，不扩展多章节内容，不实现联机、存档或导出链路。

## 验证方式

- `python tools\check_gdscript_sanity.py`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`
- 检索 `scripts/` 中已知高风险 GDScript 模式。

## 验证结果

已通过 `VER-20260516-008-card-style-runtime-ui-check` 验证。

## 是否晋升为项目事实

是。v0.3 卡牌参考风格已成为当前第一阶段运行时 UI 的实现基线。

## 后续事项

- 在具备 Godot 命令行环境后补充 headless 启动验证。
- 后续可拆分正式美术资产替换、更多卡牌内容和更多章节。
