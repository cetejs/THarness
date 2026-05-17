# RUN-20260516-012-background-ink-landscape

## 状态

- status: completed
- source: 用户反馈当前项目背景太 AI，需要替换为更好看的背景
- date: 2026-05-16
- related_task: `TASK-20260516-006-gameplay-ui-alignment-rework`

## 目标

替换运行时纯色背景和过重 AI 感背景，接入一张更适合作为 UI 底图的中国风水墨远山背景，并确认主菜单和斗法界面不受背景层影响。

## 处理过程

1. 将背景改为 `GameSpec` 可配置资源：`res://assets/ui/background_ink_landscape.png`。
2. 通过 `tools/generate_acceptance_assets.py` 生成 `1920x1080` 程序化水墨宣纸背景，不使用 AI 图像生成。
3. 第一版背景实际截图后发现噪点、线条和底部暗山过重，继续压低纸纹、远山和云线的对比度。
4. 发现 Godot 导入缓存会优先加载旧图，因此补充 `godot --import` 资源刷新步骤，并让运行时使用 `ResourceLoader.CacheMode.Replace` 加载背景纹理。
5. 保留源 PNG 兜底加载，避免资源未导入时直接回退到纯色背景。

## 变更内容

| 文件 | 内容 |
| --- | --- |
| `assets/ui/background_ink_landscape.png` | 新增水墨宣纸远山背景图，尺寸 `1920x1080`。 |
| `data/game_spec/ascension_forge.prototype.json` | 新增 `assets.ui.background` 背景资源声明。 |
| `scripts/Main.cs` | 背景层改为 `TextureRect` 全屏铺底，使用 `KeepAspectCovered`。 |
| `tools/generate_acceptance_assets.py` | 补充背景生成逻辑，并弱化纸纹、云线和远山对比度。 |
| `tools/check_gdscript_sanity.py` | 补充背景资源声明、背景层和导入缓存替换式加载检查。 |

## Godot MCP 实测

真实窗口：`1920x1080`

结果：

| 验证点 | 结果 |
| --- | --- |
| 背景图层 | 根节点首个子节点为 `TextureRect`，尺寸 `1920x1080`。 |
| 背景纹理 | 纹理尺寸 `1920x1080`，铺满窗口。 |
| 主菜单截图 | 已显示低对比宣纸水墨远山背景。 |
| 斗法截图 | 背景不遮挡斗法 UI，手牌按钮仍完整可见。 |
| 斗法按钮点击 | 点击 `施展` 成功，弃牌数从 `0` 变为 `1`。 |
| 运行输出 | `finalErrors` 为空。 |

截图：

- 主菜单：`.mcp/screenshots/screenshot_1778916256_273.png`
- 斗法：`.mcp/screenshots/screenshot_1778916345_398.png`
- 点击施展后：`.mcp/screenshots/screenshot_1778916375_789.png`

## 结论

背景替换已完成。当前背景不再是纯色或 AI 感强的插画，而是可配置、可重新生成、可导入验证的程序化中国风水墨远山底图。
