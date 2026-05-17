# TASK-20260516-002-csharp-runtime-migration

## 状态

- status: completed
- source: 用户要求后续开发内容全部使用 C#
- updated: 2026-05-16

## 目标

将当前 Godot 第一阶段可玩原型从 GDScript 运行时迁移到 Godot .NET/C#，后续运行时开发默认使用 C#。

## 范围

- 检查并安装可用的 Godot .NET 版本。
- 新增 C# 项目文件。
- 将 GameSpec 读取、局内运行时和主 UI 迁移到 C#。
- 主场景改挂 C# 脚本。
- 加入 UI 布局日志，便于用户提供运行日志后继续定位问题。
- 更新验证工具，检查 C# 入口和项目配置。

## 禁止范围

- 不扩展玩法系统。
- 不改动 GameSpec 数据契约。
- 不新增未确认角色、卡牌、敌人或章节。
- 不保留两套并行运行时代码入口。

## 成功标准

1. `scenes/main.tscn` 使用 C# 主脚本。
2. 当前运行时入口不再依赖 `scripts/*.gd`。
3. Godot .NET 版本路径已确认。
4. C# 代码包含 `[WorldSeed/UI]` 布局日志。
5. 数据、闭环、编码和结构验证通过。

## 验证方式

- `dotnet build WorldSeed.csproj`
- Godot .NET console 执行项目构建检查。
- Godot .NET headless 启动检查。
- `python tools\check_gdscript_sanity.py`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`
