# CHG-20260516-017-default-1080p-layout

## 状态

- status: active
- source: 用户要求默认使用 1920x1080
- updated: 2026-05-16

## 来源

- 用户要求后续默认以 `1920x1080` 进行。

## 变更内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| Godot 项目配置 | `project.godot` | 将默认 viewport 调整为 `1920x1080`。 |
| GameSpec UI 配置 | `data/game_spec/ascension_forge.prototype.json` | 将主要 UI 尺寸配置同步到 1080p 基准。 |
| 验证工具 | `tools/check_gdscript_sanity.py` | 将默认分辨率回归检查改为 `1920x1080`。 |
| 文档 | `README.md`、`WorldSeed.AIGC/wiki/status.md` | 同步默认逻辑画布说明。 |

## 影响范围

- 默认运行窗口和逻辑画布。
- UI 配置尺寸。
- 不改变玩法规则、界面跳转、素材内容或 C# 运行时结构。

## 验证方式

- `dotnet build WorldSeed.csproj`
- Godot .NET console 构建检查。
- Godot .NET headless 启动检查。
- `python tools\check_gdscript_sanity.py`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`

## 验证结果

已通过 `VER-20260516-017-default-1080p-layout-check` 验证。

## 是否晋升为项目事实

是。当前默认逻辑分辨率为 `1920x1080`。
