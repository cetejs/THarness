# CHG-20260516-016-combat-clear-layout-fix

## 状态

- status: active
- source: 用户提供 `[WorldSeed/UI]` 运行日志
- updated: 2026-05-16

## 来源

- 用户提供运行日志，显示窗口尺寸稳定但斗法界面 `content` 高度持续递增。

## 变更内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| C# UI 运行时 | `scripts/Main.cs` | 清屏时先从父容器移除旧节点，再延迟释放，避免旧节点同帧参与布局计算。 |
| 布局日志 | `scripts/Main.cs` | 增加 `clear children=` 日志，确认每次清屏移除数量。 |
| 验证工具 | `tools/check_gdscript_sanity.py` | 增加清屏规则回归检查。 |

## 影响范围

- 所有通过 `ClearScreen()` 切换的界面。
- 重点修复斗法界面多次刷新后的高度累积。
- 不改变玩法规则、数据结构或素材。

## 验证方式

- `dotnet build WorldSeed.csproj`
- Godot .NET console 构建检查。
- Godot .NET headless 启动检查。
- `python tools\check_gdscript_sanity.py`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`

## 验证结果

已通过 `VER-20260516-016-combat-clear-layout-fix-check` 验证。

## 是否晋升为项目事实

是。运行时清屏必须先移除旧 UI 节点，再延迟释放，避免同帧重建时布局累积。
