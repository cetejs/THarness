# RUN-20260516-009-acceptance-asset-replacement

## 状态

- status: completed
- source: 用户要求替换正式资源并进行完整验收
- updated: 2026-05-16

## 目标

替换第一阶段原型占位资源，接入 v0.3 中国风手绘卡牌修仙方向的正式验收资源包，并准备用户完整验收。

## 处理记录

- 新增 `TASK-20260516-007-acceptance-asset-replacement`。
- 新增资源契约 `CONTRACT-20260516-004-acceptance-assets`。
- 新增资源设计页 `asset-acceptance-pack-v0.1.md`。
- 新增资源生成脚本 `tools/generate_acceptance_assets.py`。
- 重新生成并覆盖 `assets/cards/`、`assets/icons/`、`assets/map/`、`assets/status/`、`assets/ui/`。
- 新增资源预览图 `assets/preview/acceptance_asset_pack_preview.png`。
- 新增资源清单 `assets/acceptance_asset_manifest.json`。
- `scripts/Main.cs` 中面板和按钮优先使用 GameSpec `assets.ui` 纹理，缺失时回退到原有平面样式。

## 验证结果

| 验证项 | 命令 | 结果 |
| --- | --- | --- |
| 资源生成 | `python tools\generate_acceptance_assets.py` | 通过 |
| C# 构建 | `dotnet build WorldSeed.csproj` | 通过 |
| 资源尺寸 | 内联 PIL 尺寸检查 | 通过 |
| GameSpec 数据 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| 最小闭环 | `python tools\smoke_playable_loop.py` | 通过 |
| C# 入口结构 | `python tools\check_gdscript_sanity.py` | 通过 |
| Godot .NET 构建 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --build-solutions --quit` | 通过 |
| Godot .NET headless 启动 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --quit-after 3` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |

## 局限

- Headless 启动不能替代真实窗口视觉验收。
- Godot headless 退出时输出 RID leak 警告，但命令返回成功；该警告不阻止当前完整验收入口。
- 该资源包是第一阶段验收资源，不是商业发售最终美术。

## 验收入口

使用 Godot .NET 4.6.2 打开工程：

`E:\Godot\4.6.2-stable-mono\Godot_v4.6.2-stable_mono_win64\Godot_v4.6.2-stable_mono_win64.exe --path D:\UnityDemo\WroldSeed`
