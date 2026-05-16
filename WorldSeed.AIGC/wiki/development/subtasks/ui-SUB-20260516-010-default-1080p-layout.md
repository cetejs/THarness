# SUB-20260516-010-default-1080p-layout

## 状态

- status: completed
- source: TASK-20260516-005-default-1080p-layout
- updated: 2026-05-16

## 角色

Godot .NET UI 配置修复。

## 目标

将当前默认逻辑分辨率和 UI 尺寸配置切换到 1920x1080 基准。

## 允许读取入口

- `project.godot`
- `data/game_spec/ascension_forge.prototype.json`
- `tools/check_gdscript_sanity.py`
- `README.md`

## 允许修改范围

- `project.godot`
- `data/game_spec/ascension_forge.prototype.json`
- `tools/check_gdscript_sanity.py`
- `README.md`
- 本任务对应运行记录、验证记录和追溯记录

## 禁止范围

- 不改变玩法规则。
- 不改变 C# 运行时代码结构。
- 不新增界面。

## 成功标准

1. 默认 viewport 为 1920x1080。
2. 主要 UI 尺寸配置适配 1080p。
3. 验证命令通过。

## 验证方式

- `dotnet build WorldSeed.csproj`
- Godot .NET console 构建检查。
- Godot .NET headless 启动检查。
- `python tools\check_gdscript_sanity.py`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`
