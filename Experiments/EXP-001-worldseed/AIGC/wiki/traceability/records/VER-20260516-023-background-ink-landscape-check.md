# VER-20260516-023-background-ink-landscape-check

## 状态

- status: active
- type: verification
- date: 2026-05-16
- source: `CHG-20260516-022-background-ink-landscape`

## 验证项

| 项目 | 命令或方式 | 结果 |
| --- | --- | --- |
| 资源生成 | `python tools\generate_acceptance_assets.py` | 通过 |
| Godot 资源导入 | `Godot_v4.6.2-stable_mono_win64_console.exe --headless --path . --import` | 通过 |
| C# 构建 | `dotnet build WorldSeed.csproj` | 通过 |
| GameSpec 数据 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| Godot 脚本/配置检查 | `python tools\check_gdscript_sanity.py` | 通过 |
| 最小可玩闭环 | `python tools\smoke_playable_loop.py` | 通过 |
| Godot MCP 真实窗口 | `1920x1080` 启动、截图并点击斗法 `施展` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |

## Godot MCP 验证结果

背景图层为根节点首个 `TextureRect`，尺寸 `1920x1080`，纹理尺寸 `1920x1080`，拉伸模式为 `KeepAspectCovered`。

已完成真实 UI 操作：

1. 主菜单截图确认背景已显示。
2. 点击 `新开灵契`。
3. 点击 `开始问道`。
4. 点击 `进入斗法`。
5. 斗法界面截图确认手牌按钮完整可见。
6. 点击 `施展`，弃牌数从 `0` 变为 `1`。
7. 读取 Godot 输出，`errors` 和 `finalErrors` 均为空。

截图证据：

- `.mcp/screenshots/screenshot_1778916256_273.png`
- `.mcp/screenshots/screenshot_1778916345_398.png`
- `.mcp/screenshots/screenshot_1778916375_789.png`

## 结论

验证通过。背景资源已替换为低对比水墨远山风格，运行时加载正常，不影响斗法界面布局和按钮点击。
