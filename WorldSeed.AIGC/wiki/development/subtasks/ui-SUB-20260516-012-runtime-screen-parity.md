# SUB-20260516-012-runtime-screen-parity

## 状态

- status: draft
- source: TASK-20260516-006-gameplay-ui-alignment-rework
- updated: 2026-05-16

## 角色

Godot .NET UI 实现。

## 目标

按 `1920x1080` 界面合同修正运行时 UI，使主菜单、角色选择、灵脉图、斗法、奖励、构筑、奇遇、灵市、结算、设置、详情和确认界面与 v0.3 目标一致。

## 允许读取入口

- `scripts/Main.cs`
- `data/game_spec/ascension_forge.prototype.json`
- `assets/`
- `WorldSeed.AIGC/wiki/design/gameplay-ui-alignment-v0.1.md`
- `WorldSeed.AIGC/wiki/development/contracts/CONTRACT-20260516-003-screen-runtime-parity.md`

## 允许修改范围

- `scripts/Main.cs`
- `data/game_spec/ascension_forge.prototype.json` 中 UI 配置字段。
- 必要 UI 占位素材。
- 对应运行记录、验证记录和追溯记录。

## 禁止范围

- 不改变战斗规则和构筑规则。
- 不新增非合同内界面。
- 不使用全局滚动框兜底。
- 不把 UI 尺寸散落硬编码到脚本中。

## 成功标准

1. 斗法、奖励、构筑三个 P0 界面优先符合合同。
2. 背景装饰不遮挡操作区。
3. 卡片化展示覆盖角色、敌人、手牌、奖励、商品和结算奖励。
4. 关键界面能输出或保存可对比截图。

## 验证方式

- `dotnet build WorldSeed.csproj`
- Godot .NET console 构建检查。
- Godot .NET headless 启动检查。
- `python tools\check_text_encoding.py --root .`
- 关键界面截图对比。
