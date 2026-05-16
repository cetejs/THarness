# SUB-20260516-008-responsive-combat-layout

## 状态

- status: completed
- source: TASK-20260516-003-responsive-combat-layout
- updated: 2026-05-16

## 角色

Godot .NET UI 布局修复。

## 目标

修复斗法界面显示不全和窗口缩放策略不正确的问题。

## 允许读取入口

- `scripts/Main.cs`
- `project.godot`
- `data/game_spec/ascension_forge.prototype.json`
- `WorldSeed.AIGC/workflows/development/runs/ISSUES-20260516-001-playable-loop.md`

## 允许修改范围

- `scripts/Main.cs`
- `project.godot`
- `data/game_spec/ascension_forge.prototype.json`
- `tools/check_gdscript_sanity.py`
- 本任务对应运行记录、验证记录和追溯记录

## 禁止范围

- 不改变玩法规则。
- 不改变 GameSpec 的业务数据契约。
- 不使用全局 `ScrollContainer` 兜底。

## 成功标准

1. Godot 使用 viewport stretch。
2. 斗法页尺寸参数来自 `ui_visual` 配置。
3. 斗法页日志包含 viewport 和真实 window 尺寸。
4. 验证命令通过。

## 验证方式

- `dotnet build WorldSeed.csproj`
- Godot .NET console 构建检查。
- Godot .NET headless 启动检查。
- `python tools\check_gdscript_sanity.py`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`
