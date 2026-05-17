# CHG-20260516-013-csharp-runtime-migration

## 状态

- status: active
- source: 用户要求全部使用 C#，并要求不要再靠猜测排查界面问题
- updated: 2026-05-16

## 来源

- 用户要求检查 `E:\Godot` 下现有版本，如果不是合适版本则下载对应安装包。
- 用户要求后续开发内容全部使用 C#。
- 用户要求反复出现的 UI 问题改为通过日志定位。

## 变更内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| Godot .NET 环境 | `E:\Godot\4.6.2-stable-mono\` | 当前 `E:\Godot\4.6.2-stable` 为普通 Godot，不能作为 C# 开发入口。 |
| C# 项目 | `WorldSeed.csproj` | 为 Godot .NET 运行时建立 C# 项目入口。 |
| 运行时脚本 | `scripts/GameSpecLoader.cs` | 将 GameSpec 读取入口迁移到 C#。 |
| 运行时脚本 | `scripts/GameRuntime.cs` | 将局内运行时逻辑迁移到 C#。 |
| UI 脚本 | `scripts/Main.cs` | 将主 UI 和界面跳转迁移到 C#，并加入 `[WorldSeed/UI]` 布局日志。 |
| 场景入口 | `scenes/main.tscn` | 主场景改挂 `res://scripts/Main.cs`。 |
| 项目配置 | `project.godot` | 增加 Godot .NET assembly 配置。 |
| 验证工具 | `tools/check_gdscript_sanity.py` | 增加 C# 入口、项目配置、卡牌尺寸和 UI 日志检查。 |
| 文档 | `README.md` | 明确 Godot .NET 运行入口和 UI 日志获取方式。 |

## 影响范围

- 后续 WorldSeed 运行时代码默认使用 C#。
- 当前主场景不再依赖 `scripts/*.gd`。
- 真实窗口 UI 问题后续优先依据 `[WorldSeed/UI]` 日志定位。
- 不改变 GameSpec 数据格式、玩法规则和当前内容规模。

## 验证方式

- `dotnet build WorldSeed.csproj`
- Godot .NET console 构建检查。
- Godot .NET headless 启动检查。
- `python tools\check_gdscript_sanity.py`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`

## 验证结果

已通过 `VER-20260516-013-csharp-runtime-migration-check` 验证。

## 是否晋升为项目事实

是。后续运行时代码默认使用 Godot .NET/C#，普通 Godot 不再作为开发入口。
