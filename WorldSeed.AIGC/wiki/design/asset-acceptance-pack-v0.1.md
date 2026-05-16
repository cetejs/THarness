# 正式验收资源包 v0.1

## 状态

- status: active
- source: 用户要求替换正式资源、v0.3 界面视觉目标、当前 GameSpec 资产引用
- updated: 2026-05-16

## 结论

当前仓库未提供外部商业美术包。本资源包定义为第一阶段“完整验收用正式资源”：它需要替换原型占位图，符合 v0.3 中国风手绘卡牌修仙方向，能够在 Godot 运行时被 GameSpec 引用并通过完整验收。

该资源包不是最终商业发售美术。后续若提供外包或商业美术包，必须按同一资源契约替换。

## 资源范围

| 类别 | 路径 | 数量 | 用途 |
| --- | --- | --- | --- |
| 卡牌框 | `assets/cards/` | 5 | 攻击、护法、法门、符箓、劫咒卡框。 |
| 资源和符槽图标 | `assets/icons/` | 8 | 命元、罡气、灵力、灵石和符槽。 |
| 灵脉节点 | `assets/map/` | 6 | 斗法、强敌、奇遇、灵市、锻炉、镇守。 |
| 状态和意图 | `assets/status/` | 7 | 敌方意图和燃烧、冰冻、雷、毒等状态。 |
| UI 面板按钮 | `assets/ui/` | 8 | 卷轴面板、弹窗、按钮和页签。 |
| 预览图 | `assets/preview/acceptance_asset_pack_preview.png` | 1 | 资源包人工验收预览。 |

## 风格要求

- 宣纸底、墨线、朱砂、青玉、鎏金、玄紫等 v0.3 配色。
- 卡牌框保留左上费用宝珠、左侧门类竖条、插画区、规则题签区、效果宣纸区和底部类型条。
- 攻击、护体、法诀、符箓、劫咒卡框必须有不同主体纹样，不能只靠边框颜色区分。
- 卡牌规则区不使用大面积黑色占位块，避免被误读为遮挡或未完成素材。
- UI 面板和按钮使用卷轴、金线、纸纹和轻微手绘边缘。
- 图标和节点保持清晰剪影，便于小尺寸辨认。

## 验收边界

必须满足：

- 所有 GameSpec 中引用的资源路径存在。
- 所有资源尺寸符合运行时预期。
- Godot 能加载卡框和 UI 纹理。
- 关键界面中可见资源不再是纯色或无风格占位图。

不要求：

- 每张具体卡牌拥有独立插画。
- 每个角色、敌人拥有独立立绘。
- 达到商业发售级最终美术质量。

## 验证

- `python tools\generate_acceptance_assets.py`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `dotnet build WorldSeed.csproj`
- Godot .NET console 构建和 headless 启动。
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`

## 产物

- 资源预览图：`assets/preview/acceptance_asset_pack_preview.png`
- 资源清单：`assets/acceptance_asset_manifest.json`
- 生成脚本：`tools/generate_acceptance_assets.py`
