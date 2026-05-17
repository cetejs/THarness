# SUB-20260516-015-acceptance-asset-pack

## 状态

- status: completed
- source: TASK-20260516-007-acceptance-asset-replacement
- updated: 2026-05-16

## 角色

资源生成与替换。

## 目标

生成并替换 `assets/` 下第一阶段验收资源包，覆盖卡牌框、资源图标、符槽、地图节点、状态图标、UI 面板、按钮和页签。

## 允许读取入口

- `Experiments/EXP-001-worldseed/AIGC/wiki/design/ui-screen-visual-spec-v0.3.md`
- `Experiments/EXP-001-worldseed/AIGC/wiki/design/asset-acceptance-pack-v0.1.md`
- `data/game_spec/ascension_forge.prototype.json`
- `assets/`

## 允许修改范围

- `assets/cards/`
- `assets/icons/`
- `assets/map/`
- `assets/status/`
- `assets/ui/`
- `assets/preview/`
- `tools/generate_acceptance_assets.py`
- 对应运行记录、验证记录和追溯记录。

## 禁止范围

- 不修改玩法数据。
- 不引入外部不可追溯图片。
- 不删除 Godot `.import` 文件。

## 成功标准

1. 所有被 GameSpec 引用的 PNG 路径存在。
2. 资源尺寸符合契约。
3. 生成脚本可重复运行。
4. 预览图可人工检查。

## 验证方式

- `python tools\generate_acceptance_assets.py`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\check_text_encoding.py --root .`

## 验证结果

已通过 `VER-20260516-020-acceptance-asset-replacement-check` 验证。
