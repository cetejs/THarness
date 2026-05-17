# CHG-20260516-022-background-ink-landscape

## 状态

- status: active
- type: change
- date: 2026-05-16
- source: 用户反馈当前背景太 AI，需要替换为更好看的项目背景

## 背景

当前项目背景仍偏纯色或生成感过强，无法支撑中国风、手绘修仙方向的完整验收观感。本次变更将背景替换为低对比宣纸水墨远山图，并修复导入缓存导致运行时可能加载旧背景的问题。

## 变更

| 范围 | 文件 | 说明 |
| --- | --- | --- |
| 背景素材 | `assets/ui/background_ink_landscape.png` | 新增 `1920x1080` 水墨宣纸远山背景。 |
| 资源生成 | `tools/generate_acceptance_assets.py` | 增加背景生成，并降低噪点、线条和远山对比度。 |
| GameSpec | `data/game_spec/ascension_forge.prototype.json` | 增加 `assets.ui.background` 背景资源配置。 |
| 运行时 UI | `scripts/Main.cs` | 背景改为全屏 `TextureRect`，使用导入资源替换式加载和源 PNG 兜底。 |
| 验证脚本 | `tools/check_gdscript_sanity.py` | 增加背景声明、背景层和缓存替换加载检查。 |
| 运行记录 | `WorldSeed.AIGC/workflows/development/runs/RUN-20260516-012-background-ink-landscape.md` | 记录背景替换、缓存根因和 Godot MCP 实测。 |

## 影响

- 主菜单、斗法和其他运行时界面统一使用新的水墨远山背景。
- 背景资源由 `GameSpec` 配置控制，后续替换不需要修改 UI 结构。
- 背景生成后需要执行 Godot `--import` 刷新导入缓存，运行时使用 `ResourceLoader.CacheMode.Replace` 避免复用旧贴图。

## 验证

已通过 `VER-20260516-023-background-ink-landscape-check` 验证。
