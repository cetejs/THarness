# SUB-20260516-007-csharp-runtime-migration

## 状态

- status: completed
- source: TASK-20260516-002-csharp-runtime-migration
- updated: 2026-05-16

## 角色

Godot .NET 运行时迁移。

## 目标

将当前 Godot 原型运行时脚本迁移到 C#，并加入 UI 布局日志。

## 允许读取入口

- `Experiments/EXP-001-worldseed/AIGC/wiki/development/contracts/CONTRACT-20260516-001-gamespec-runtime.md`
- `Experiments/EXP-001-worldseed/AIGC/workflows/development/runs/ISSUES-20260516-001-playable-loop.md`
- `scripts/Main.gd`
- `scripts/GameRuntime.gd`
- `scripts/GameSpecLoader.gd`

## 允许修改范围

- `WorldSeed.csproj`
- `scripts/*.cs`
- `scenes/main.tscn`
- `project.godot`
- `tools/check_gdscript_sanity.py`
- 迁移完成后删除不再作为入口的 `scripts/*.gd`
- 本任务对应运行记录、验证记录和追溯记录

## 禁止范围

- 不改变玩法规则。
- 不改变 GameSpec 格式。
- 不扩展内容规模。

## 成功标准

1. C# 版本可读取 GameSpec。
2. C# 版本可驱动主菜单、角色选择、灵脉图、斗法、奖励、构筑、奇遇、灵市、结算。
3. C# 版本输出 `[WorldSeed/UI]` 布局日志。
4. 验证命令通过。

## 验证方式

- `dotnet build WorldSeed.csproj`
- Godot .NET console 构建检查。
- Godot .NET headless 启动检查。
- `python tools\check_gdscript_sanity.py`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`
