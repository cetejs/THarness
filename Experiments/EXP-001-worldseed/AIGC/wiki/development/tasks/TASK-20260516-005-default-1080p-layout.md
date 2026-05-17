# TASK-20260516-005-default-1080p-layout

## 状态

- status: completed
- source: 用户要求默认使用 1920x1080
- updated: 2026-05-16

## 目标

将 Godot 工程默认逻辑画布调整为 1920x1080，并同步运行时 UI 配置，避免 1080p 下界面显得过小。

## 范围

- 修改 Godot 默认 viewport 宽高。
- 按 1080p 逻辑画布同步 `ui_visual` 尺寸参数。
- 更新静态检查和运行说明。
- 补充追溯和验证记录。

## 禁止范围

- 不改变玩法规则。
- 不改变界面跳转。
- 不新增素材和内容。

## 成功标准

1. `project.godot` 默认 viewport 为 1920x1080。
2. `ui_visual` 的主要 UI 尺寸按 1080p 逻辑画布更新。
3. 静态检查要求 1920x1080。
4. 构建、数据、闭环和编码验证通过。

## 验证方式

- `dotnet build WorldSeed.csproj`
- Godot .NET console 构建检查。
- Godot .NET headless 启动检查。
- `python tools\check_gdscript_sanity.py`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`
