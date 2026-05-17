# CONTRACT-20260516-002-csharp-runtime-entry

## 状态

- status: active
- source: TASK-20260516-002-csharp-runtime-migration
- updated: 2026-05-16

## 输入

- `data/game_spec/ascension_forge.prototype.json`
- `assets/` 下的 UI、卡牌、地图和状态素材。
- Godot .NET 4.6.2 或兼容版本。

## 输出

- `WorldSeed.csproj`
- `scripts/GameSpecLoader.cs`
- `scripts/GameRuntime.cs`
- `scripts/Main.cs`
- 主场景 `scenes/main.tscn` 挂载 C# 主脚本。

## 错误处理

- GameSpec 读取失败时输出 Godot 错误日志。
- UI 布局调试日志使用 `[WorldSeed/UI]` 前缀。
- 不在运行时吞掉构建错误。

## 禁止事项

- 不允许主场景继续挂载 GDScript 主脚本。
- 不允许同时维护两套运行时入口。
- 不允许在一个 C# 脚本文件中定义多个类。

## 验证方式

- 结构检查确认 C# 入口存在且主场景引用 C#。
- 数据和闭环验证仍通过。
- Godot .NET console 构建检查。
