# SUB-20260516-009-combat-clear-layout-fix

## 状态

- status: completed
- source: TASK-20260516-004-combat-clear-layout-fix
- updated: 2026-05-16

## 角色

Godot .NET UI 布局修复。

## 目标

根据运行日志修复斗法界面刷新时旧节点延迟释放导致的布局高度累积。

## 允许读取入口

- `scripts/Main.cs`
- `tools/check_gdscript_sanity.py`
- `Experiments/EXP-001-worldseed/AIGC/workflows/development/runs/ISSUES-20260516-001-playable-loop.md`

## 允许修改范围

- `scripts/Main.cs`
- `tools/check_gdscript_sanity.py`
- 本任务对应运行记录、验证记录和追溯记录

## 禁止范围

- 不改变斗法规则。
- 不改变卡牌数据。
- 不调整素材风格。

## 成功标准

1. `ClearScreen()` 先 `RemoveChild` 再 `QueueFree`。
2. 静态检查覆盖该清屏规则。
3. 验证命令通过。

## 验证方式

- `dotnet build WorldSeed.csproj`
- Godot .NET console 构建检查。
- Godot .NET headless 启动检查。
- `python tools\check_gdscript_sanity.py`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`
