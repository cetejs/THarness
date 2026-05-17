# SUB-20260516-014-visual-gameplay-verification

## 状态

- status: draft
- source: TASK-20260516-006-gameplay-ui-alignment-rework
- updated: 2026-05-16

## 角色

视觉和玩法验证。

## 目标

建立本轮修正的验证闭环，确保 UI 不是只通过构建，玩法也不是只靠人工点通。

## 允许读取入口

- `tools/`
- `Experiments/EXP-001-worldseed/AIGC/wiki/design/gameplay-ui-alignment-v0.1.md`
- `Experiments/EXP-001-worldseed/AIGC/wiki/development/tasks/TASK-20260516-006-gameplay-ui-alignment-rework.md`
- `Experiments/EXP-001-worldseed/AIGC/wiki/development/contracts/CONTRACT-20260516-003-screen-runtime-parity.md`

## 允许修改范围

- 验证脚本。
- 运行记录、验证记录和截图记录。

## 禁止范围

- 不修改玩法实现。
- 不修改 UI 实现。
- 不用无法复现的口头观察替代验证记录。

## 成功标准

1. 构建、数据、smoke 和编码检查通过。
2. 关键界面截图对比记录存在。
3. P0 不符合项都有对应验证项。
4. 无法自动验证的内容明确记录为人工截图验收。

## 验证方式

- `dotnet build WorldSeed.csproj`
- Godot .NET console 构建和 headless 启动。
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`
- 视觉截图对比记录。
