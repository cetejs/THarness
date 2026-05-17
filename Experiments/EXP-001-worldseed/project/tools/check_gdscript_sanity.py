from __future__ import annotations

from pathlib import Path


SCRIPT_ROOT = Path("scripts")


def require(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []
    main_scene = Path("scenes/main.tscn")
    project = Path("project.godot")
    main_script = Path("scripts/Main.cs")
    data_file = Path("data/game_spec/ascension_forge.prototype.json")

    require(errors, main_script.exists(), "缺少 scripts/Main.cs")
    require(errors, main_scene.exists(), "缺少 scenes/main.tscn")
    require(errors, project.exists(), "缺少 project.godot")
    require(errors, data_file.exists(), "缺少 GameSpec 数据文件")

    gd_files = list(SCRIPT_ROOT.glob("*.gd"))
    require(errors, not gd_files, "scripts/ 下仍存在 GDScript 运行时文件，C# 迁移后不应保留。")

    if main_script.exists():
        main_text = main_script.read_text(encoding="utf-8")
        require(errors, "ScrollContainer" not in main_text, "scripts/Main.cs 不应使用全局 ScrollContainer，避免所有界面出现滚动框。")
        require(errors, "AddBackgroundLayer()" in main_text, "主界面必须通过背景图层入口加载背景资源。")
        require(errors, "LoadBackgroundTexture" in main_text, "背景图必须具备源码 PNG 兜底加载，避免未导入资源时回退纯色背景。")
        require(errors, "ResourceLoader.CacheMode.Replace" in main_text, "背景图必须替换式加载导入纹理，避免复用旧导入缓存。")
        require(errors, "TextureRect.StretchModeEnum.KeepAspectCovered" in main_text, "背景图必须按覆盖模式铺满窗口。")
        require(errors, "AddResourceBar" not in main_text, "不应保留空资源徽章栏，避免地图和斗法出现占位空框。")
        require(errors, "AddResourceBadge" not in main_text, "不应保留空资源徽章组件，避免出现无文本的占位按钮框。")
        require(errors, "CombatPlayerStatsText()" in main_text, "斗法页必须在顶部显示玩家命元、罡气、灵力和灵石。")
        require(errors, "CardRuleTitle" in main_text, "卡面中部必须使用规则题签，避免重复卡名造成信息层级单薄。")
        require(errors, "CardFontSize" in main_text, "卡牌内部文字必须随卡面高度缩放，避免小卡标题和类型被裁剪。")
        require(errors, "cardPanel.Size = new Vector2(width, height)" in main_text, "卡牌纹理容器必须锁定尺寸，避免被父容器拉伸。")
        require(errors, "box.SizeFlagsHorizontal = SizeFlags.ShrinkBegin" in main_text, "卡牌外层容器必须使用收缩布局。")
        require(errors, "frame.ExpandMode = TextureRect.ExpandModeEnum.IgnoreSize" in main_text, "卡框 TextureRect 必须忽略原始纹理尺寸。")
        require(errors, "frame.Size = new Vector2(width, height)" in main_text, "卡框 TextureRect 必须显式设置绘制尺寸。")
        require(errors, "[WorldSeed/UI]" in main_text, "必须保留 [WorldSeed/UI] 布局日志。")
        require(errors, "DisplayServer.WindowGetSize()" in main_text, "布局日志必须输出真实窗口尺寸。")
        require(errors, "combat_card_width" in main_text, "斗法页卡牌尺寸必须使用独立配置。")
        require(errors, "combat_top_panel_height" in main_text, "斗法页上半区高度必须使用独立配置。")
        require(errors, "height + actionHeight" in main_text, "非交互卡牌不应预留按钮高度。")
        require(errors, "_contentBox.RemoveChild(child)" in main_text, "清屏时必须先从父容器移除旧节点，再 QueueFree，避免同帧重建时布局高度累积。")
        require(errors, "clear children=" in main_text, "清屏必须保留布局排查日志，便于确认旧节点移除数量。")

    if main_scene.exists():
        scene_text = main_scene.read_text(encoding="utf-8")
        require(errors, 'path="res://scripts/Main.cs"' in scene_text, "scenes/main.tscn 未挂载 C# 主脚本。")

    if project.exists():
        project_text = project.read_text(encoding="utf-8")
        require(errors, 'run/main_scene="res://scenes/main.tscn"' in project_text, "project.godot 未配置主场景。")
        require(errors, 'project/assembly_name="WorldSeed"' in project_text, "project.godot 未配置 C# assembly_name。")
        require(errors, 'window/size/viewport_width=1920' in project_text, "project.godot 逻辑宽度必须为 1920。")
        require(errors, 'window/size/viewport_height=1080' in project_text, "project.godot 逻辑高度必须为 1080。")
        require(errors, 'window/stretch/mode="viewport"' in project_text, "project.godot 必须使用 viewport stretch，让 1920x1080 逻辑画布随窗口整体缩放。")
        require(errors, 'window/stretch/aspect="expand"' in project_text, "project.godot 必须使用 expand aspect，避免窗口拉伸时露出黑边。")

    if data_file.exists():
        data_text = data_file.read_text(encoding="utf-8")
        for key in (
            "combat_card_width",
            "combat_card_height",
            "combat_player_panel_width",
            "combat_log_panel_width",
            "combat_top_panel_height",
            "combat_hand_panel_height",
        ):
            require(errors, f'"{key}"' in data_text, f"GameSpec 缺少斗法响应式布局配置: {key}")
        require(errors, '"card_width": 225' in data_text, "GameSpec 1080p 默认 UI 卡牌宽度必须为 225。")
        require(errors, '"combat_card_width": 162' in data_text, "GameSpec 1080p 默认斗法卡牌宽度必须为 162。")
        require(errors, '"background": "res://assets/ui/background_ink_landscape.png"' in data_text, "GameSpec 必须声明正式背景图资源。")
        require(errors, "resource_badge" not in data_text, "GameSpec 不应保留已废弃的资源徽章尺寸配置。")

    asset_generator = Path("tools/generate_acceptance_assets.py")
    if asset_generator.exists():
        asset_text = asset_generator.read_text(encoding="utf-8")
        require(errors, "motif: str" in asset_text, "卡框生成必须按卡牌类型生成不同主体纹样。")
        require(errors, "draw.rounded_rectangle((120, 398" in asset_text, "卡框必须包含规则题签区，避免只剩普通信息块。")

    if errors:
        print("gdscript-sanity: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("gdscript-sanity: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
