# VER-20260516-020-acceptance-asset-replacement-check

## 状态

- status: active
- source: 本地命令验证和 Godot .NET headless 检查
- updated: 2026-05-16

## 验证目标

验证第一阶段正式验收资源包已经生成、接入并可被 Godot .NET 工程加载，且没有破坏数据、构建和最小可玩闭环。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| 资源生成 | `python tools\generate_acceptance_assets.py` | 通过 |
| C# 构建 | `dotnet build WorldSeed.csproj` | 通过 |
| 资源尺寸 | 内联 PIL 尺寸检查 | 通过 |
| GameSpec 数据和素材引用 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| 最小闭环 | `python tools\smoke_playable_loop.py` | 通过 |
| C# 入口结构 | `python tools\check_gdscript_sanity.py` | 通过 |
| Godot .NET 构建 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --build-solutions --quit` | 通过 |
| Godot .NET 启动 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --quit-after 3` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |

## 通过范围

- 验收资源包已生成并覆盖 `assets/`。
- GameSpec 引用资源存在。
- 面板和按钮已接入运行时纹理优先加载。
- 工程可构建，最小闭环数据验证通过。

## 局限

- Headless 启动不能替代真实窗口视觉验收。
- Godot headless 退出时输出 RID leak 警告，但命令返回成功。
- 该资源包是第一阶段验收资源，不是商业发售最终美术。

## 关联记录

- `CHG-20260516-020-acceptance-asset-replacement`
- `TASK-20260516-007-acceptance-asset-replacement`
- `RUN-20260516-009-acceptance-asset-replacement`
