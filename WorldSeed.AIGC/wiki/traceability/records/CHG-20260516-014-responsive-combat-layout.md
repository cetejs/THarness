# CHG-20260516-014-responsive-combat-layout

## 状态

- status: active
- source: 用户真实运行截图反馈斗法界面显示不全
- updated: 2026-05-16

## 来源

- 用户反馈斗法界面在运行窗口中下方手牌区显示不全。
- 用户指出屏幕大小应该支持随窗口大小缩放。

## 变更内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| Godot 项目配置 | `project.godot` | 将 stretch 模式改为 `viewport`，让 1280x720 逻辑画布随窗口整体缩放。 |
| GameSpec UI 配置 | `data/game_spec/ascension_forge.prototype.json` | 新增斗法页独立尺寸参数，避免使用通用卡牌尺寸挤压页面。 |
| C# UI 运行时 | `scripts/Main.cs` | 斗法页改用配置化面板和卡牌尺寸，敌阵面板占用剩余宽度，非交互卡牌不预留按钮高度。 |
| 验证工具 | `tools/check_gdscript_sanity.py` | 增加 viewport stretch、斗法布局配置和窗口尺寸日志检查。 |

## 影响范围

- 斗法界面。
- 运行窗口缩放策略。
- UI 布局日志。
- 不改变玩法规则、GameSpec 业务数据或界面跳转。

## 验证方式

- `dotnet build WorldSeed.csproj`
- Godot .NET console 构建检查。
- Godot .NET headless 启动检查。
- `python tools\check_gdscript_sanity.py`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`

## 验证结果

已通过 `VER-20260516-014-responsive-combat-layout-check` 验证。

## 是否晋升为项目事实

是。当前 Godot 运行窗口应使用 viewport stretch，以 1280x720 作为逻辑画布整体缩放。
