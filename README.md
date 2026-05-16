# WorldSeed

山海：以人力，丈量天地，AI 一键生成游戏。

## 当前可玩原型

当前工程包含第一阶段最小可玩闭环：

```text
主菜单 -> 角色选择 -> 灵脉图 -> 斗法 -> 斗法奖励 -> 构筑洞府 -> 奇遇/灵市/锻炉 -> 镇守 -> 洞天结算 -> 本局结算
```

主要界面已按 v0.3 中国风手绘修仙卡牌参考风格重做：纸卷背景、墨线面板、卡牌化角色/敌人/手牌/奖励/商品、费用宝珠、门类竖条、规则区、资源条、灵脉节点和操作后的轻量反馈。

## 运行方式

1. 使用 Godot .NET 4.6.2 打开本目录下的 `project.godot`。
2. 本机已确认可用入口：`E:\Godot\4.6.2-stable-mono\Godot_v4.6.2-stable_mono_win64\Godot_v4.6.2-stable_mono_win64.exe`。
3. 不使用 `E:\Godot\4.6.2-stable` 下的普通 Godot 作为开发入口；当前运行时已经迁移为 C#。
4. 当前项目以 1920x1080 作为默认逻辑画布，并随运行窗口整体缩放。
5. 点击运行项目。
6. 在主菜单点击“新开灵契”。
7. 选择“铁誓者”，点击“开始问道”。
8. 按灵脉图节点推进，斗法中点击手牌“施展”，点击“收势回合”让敌方行动。
9. 斗法胜利后选择奖励，在构筑洞府嵌入符箓或参悟节点，再返回灵脉。
10. 处理奇遇、灵市和锻炉节点，击败镇守后进入洞天结算和本局结算。

## UI 排查日志

运行时会输出 `[WorldSeed/UI]` 前缀的布局日志，包含 viewport、根容器、内容区、屏幕名、卡牌目标尺寸、实际尺寸和纹理尺寸。

如果界面继续出现拉伸、错位、滚动框异常或卡牌巨型化，请从 Godot 输出面板复制 `[WorldSeed/UI]` 开头的日志用于定位。

## 验证命令

```powershell
dotnet build WorldSeed.csproj
& 'E:\Godot\4.6.2-stable-mono\Godot_v4.6.2-stable_mono_win64\Godot_v4.6.2-stable_mono_win64_console.exe' --headless --path . --build-solutions --quit
& 'E:\Godot\4.6.2-stable-mono\Godot_v4.6.2-stable_mono_win64\Godot_v4.6.2-stable_mono_win64_console.exe' --headless --path . --quit-after 3
python tools\check_gdscript_sanity.py
python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .
python tools\smoke_playable_loop.py
python tools\check_text_encoding.py --root .
```
