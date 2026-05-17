# TASK-20260516-003-responsive-combat-layout

## 状态

- status: completed
- source: 用户反馈斗法界面在运行窗口中显示不全
- updated: 2026-05-16

## 目标

修复斗法界面在 1024x576 等运行窗口中显示不全的问题，并让项目以 1280x720 逻辑画布随窗口整体缩放。

## 范围

- 调整 Godot stretch 配置。
- 将斗法页卡牌、面板宽高改为 GameSpec 配置。
- 修复非交互卡牌仍预留按钮高度的问题。
- 更新布局静态检查。

## 禁止范围

- 不新增玩法规则。
- 不改变卡牌、敌人、奖励和章节数据结构。
- 不重新引入全局滚动框。

## 成功标准

1. 运行窗口可按 1280x720 逻辑画布整体缩放。
2. 斗法页上半区和手牌区使用配置化尺寸。
3. 非交互卡牌不再预留按钮高度。
4. 构建、数据、闭环和编码验证通过。

## 验证方式

- `dotnet build WorldSeed.csproj`
- Godot .NET console 构建检查。
- Godot .NET headless 启动检查。
- `python tools\check_gdscript_sanity.py`
- `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .`
- `python tools\smoke_playable_loop.py`
- `python tools\check_text_encoding.py --root .`
