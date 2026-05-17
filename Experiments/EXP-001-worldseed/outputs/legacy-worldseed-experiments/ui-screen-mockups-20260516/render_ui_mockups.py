from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets"
OUT = ROOT / "WorldSeed.AIGC" / "wiki" / "design" / "images" / "ui-screen-mockups-v0.1"
FONT_REGULAR = "C:/Windows/Fonts/msyh.ttc"
FONT_BOLD = "C:/Windows/Fonts/msyhbd.ttc"
SIZE = (1280, 720)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REGULAR, size)


def asset(*parts: str) -> Image.Image:
    image = Image.open(ASSETS.joinpath(*parts)).convert("RGBA")
    return image


def make_canvas(title: str, subtitle: str = "") -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGBA", SIZE, (18, 21, 26, 255))
    draw = ImageDraw.Draw(image)
    for y in range(SIZE[1]):
        value = int(20 + y * 0.045)
        draw.line((0, y, SIZE[0], y), fill=(12 + value // 4, 16 + value // 5, 24 + value // 3, 255))
    draw.rectangle((0, 0, 1280, 64), fill=(21, 25, 32, 245))
    draw.text((28, 16), title, fill=(236, 231, 214, 255), font=font(28, True))
    if subtitle:
        draw.text((360, 24), subtitle, fill=(162, 170, 178, 255), font=font(16))
    draw.text((1040, 22), "WorldSeed v0.1", fill=(154, 162, 170, 255), font=font(16))
    return image, draw


def panel(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], title: str = "") -> None:
    draw.rounded_rectangle(xy, radius=8, fill=(33, 38, 48, 235), outline=(94, 91, 74, 255), width=2)
    if title:
        draw.text((xy[0] + 18, xy[1] + 14), title, fill=(232, 221, 190, 255), font=font(20, True))


def paste_asset(image: Image.Image, source: Image.Image, xy: tuple[int, int], size: tuple[int, int]) -> None:
    resized = source.resize(size, Image.Resampling.LANCZOS)
    image.alpha_composite(resized, xy)


def draw_button(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, width: int = 250, active: bool = True) -> None:
    x, y = xy
    fill = (75, 71, 56, 255) if active else (51, 53, 58, 255)
    outline = (169, 132, 61, 255) if active else (91, 91, 91, 255)
    draw.rounded_rectangle((x, y, x + width, y + 44), radius=6, fill=fill, outline=outline, width=2)
    draw.text((x + 18, y + 10), text, fill=(245, 236, 205, 255) if active else (130, 130, 130, 255), font=font(17, True))


def draw_icon_text(image: Image.Image, draw: ImageDraw.ImageDraw, icon_name: str, xy: tuple[int, int], text: str) -> None:
    paste_asset(image, asset("icons", icon_name), xy, (30, 30))
    draw.text((xy[0] + 38, xy[1] + 3), text, fill=(225, 226, 221, 255), font=font(17, True))


def draw_card(image: Image.Image, draw: ImageDraw.ImageDraw, xy: tuple[int, int], card_type: str, title: str, cost: str, text: str, scale: float = 1.0) -> None:
    width = int(118 * scale)
    height = int(166 * scale)
    frame = asset("cards", f"card_{card_type}.png")
    paste_asset(image, frame, xy, (width, height))
    x, y = xy
    draw.text((x + 12, y + 15), title, fill=(246, 239, 213, 255), font=font(max(13, int(15 * scale)), True))
    draw.ellipse((x + width - 34, y + 10, x + width - 10, y + 34), fill=(28, 36, 45, 230), outline=(221, 180, 82, 255))
    draw.text((x + width - 27, y + 11), cost, fill=(244, 231, 180, 255), font=font(max(12, int(15 * scale)), True))
    line_y = y + int(78 * scale)
    for line in wrap(text, width=max(6, int(8 * scale))):
        draw.text((x + 12, line_y), line, fill=(224, 222, 208, 255), font=font(max(11, int(12 * scale))))
        line_y += int(18 * scale)


def draw_resource_bar(image: Image.Image, draw: ImageDraw.ImageDraw, x: int = 770, y: int = 78) -> None:
    draw_icon_text(image, draw, "icon_health.png", (x, y), "72/80")
    draw_icon_text(image, draw, "icon_armor.png", (x + 118, y), "6")
    draw_icon_text(image, draw, "icon_energy.png", (x + 185, y), "3/3")
    draw_icon_text(image, draw, "icon_coin.png", (x + 285, y), "84")


def main_menu() -> Image.Image:
    image, draw = make_canvas("主菜单", "进入远征、继续存档、设置和退出")
    paste_asset(image, asset("ui", "panel_large.png"), (560, 110), (560, 315))
    draw.text((86, 142), "WorldSeed:\nAscension Forge", fill=(246, 232, 188, 255), font=font(44, True), spacing=8)
    draw.text((88, 265), "山海：以人力，丈量天地", fill=(170, 178, 180, 255), font=font(20))
    draw_button(draw, (92, 350), "新游戏", 280)
    draw_button(draw, (92, 408), "继续游戏", 280, False)
    draw_button(draw, (92, 466), "设置", 280)
    draw_button(draw, (92, 524), "退出", 280)
    panel(draw, (790, 152, 1145, 385), "最近远征")
    draw.text((820, 205), "角色：铁誓者\n章节：腐化矿脉\n当前位置：node_3 商店\n生命：72/80", fill=(223, 224, 214, 255), font=font(20), spacing=12)
    draw.text((86, 650), "构建版本 0.1.0  /  GameSpec ascension_forge_prototype", fill=(133, 140, 145, 255), font=font(15))
    return image


def character_select() -> Image.Image:
    image, draw = make_canvas("角色选择", "选择角色并查看初始构筑")
    draw_button(draw, (32, 82), "返回", 110)
    panel(draw, (42, 135, 390, 610), "角色卡")
    paste_asset(image, asset("icons", "icon_armor.png"), (85, 205), (96, 96))
    draw.text((200, 206), "铁誓者\n护甲反击\n难度：入门", fill=(236, 234, 220, 255), font=font(22, True), spacing=12)
    draw.rounded_rectangle((70, 185, 360, 330), radius=8, outline=(218, 170, 72, 255), width=3)
    draw.text((88, 366), "星焰术士\n影缝游侠", fill=(130, 137, 143, 255), font=font(21), spacing=22)
    panel(draw, (430, 135, 770, 610), "角色详情")
    draw.text((460, 196), "铁誓者", fill=(247, 234, 192, 255), font=font(32, True))
    draw.text((460, 250), "初始生命：80\n定位：格挡、创伤、重击\n初始装备：誓约刃\n初始天赋：铁誓起点", fill=(222, 223, 213, 255), font=font(19), spacing=14)
    draw_button(draw, (460, 515), "开始远征", 230)
    panel(draw, (810, 135, 1210, 610), "初始牌组预览")
    cards = [("attack", "打击", "1", "造成6伤害"), ("defense", "守备", "1", "获得6护甲"), ("attack", "盾击", "1", "伤害+护甲"), ("skill", "凝神", "0", "抽1张牌")]
    for index, item in enumerate(cards):
        draw_card(image, draw, (835 + index * 90, 230), item[0], item[1], item[2], item[3], 0.72)
    draw.text((842, 460), "核心提示：用护甲抵消伤害，再把护甲转换成反击节奏。", fill=(215, 213, 198, 255), font=font(17))
    return image


def map_screen() -> Image.Image:
    image, draw = make_canvas("地图", "选择下一节点，规划风险和奖励")
    draw_resource_bar(image, draw)
    panel(draw, (36, 120, 300, 610), "章节信息")
    draw.text((62, 175), "腐化矿脉\n地图层数：6\nBoss：活熔炉\n地图词缀：余烬回响", fill=(222, 223, 212, 255), font=font(19), spacing=14)
    panel(draw, (330, 120, 910, 610), "路线")
    nodes = [("node_battle.png", "战斗"), ("node_event.png", "事件"), ("node_shop.png", "商店"), ("node_battle.png", "战斗"), ("node_elite.png", "精英"), ("node_boss.png", "Boss")]
    for index, item in enumerate(nodes):
        x = 375 + index * 86
        y = 360 - (index % 2) * 80
        paste_asset(image, asset("map", item[0]), (x, y), (70, 70))
        draw.text((x + 7, y + 76), item[1], fill=(230, 226, 206, 255), font=font(15, True))
        if index < len(nodes) - 1:
            draw.line((x + 70, y + 35, x + 102, 335 - ((index + 1) % 2) * 80), fill=(146, 122, 74, 255), width=4)
    draw.ellipse((375, 360, 445, 430), outline=(238, 191, 74, 255), width=4)
    panel(draw, (950, 120, 1228, 610), "当前节点")
    paste_asset(image, asset("map", "node_battle.png"), (1040, 185), (96, 96))
    draw.text((982, 310), "node_1 / 普通战斗\n遭遇：锈蚀虫群\n奖励：金币、卡牌三选一", fill=(222, 223, 214, 255), font=font(18), spacing=12)
    draw_button(draw, (985, 505), "进入普通战斗", 210)
    return image


def combat_screen() -> Image.Image:
    image, draw = make_canvas("战斗", "打出手牌、观察敌人意图、结束回合")
    draw_resource_bar(image, draw, 750, 78)
    panel(draw, (36, 120, 300, 470), "玩家")
    paste_asset(image, asset("icons", "icon_armor.png"), (118, 178), (96, 96))
    draw.text((70, 300), "铁誓者\n生命 72/80\n护甲 6\n抽牌堆 12  弃牌堆 3", fill=(225, 224, 211, 255), font=font(18), spacing=11)
    panel(draw, (340, 120, 920, 470), "敌人")
    for x, name, hp, icon in [(430, "锈蚀虫", "20/20", "icon_intent_attack.png"), (650, "锈蚀虫", "14/20", "icon_intent_guard.png")]:
        draw.rounded_rectangle((x, 185, x + 150, 370), radius=8, fill=(42, 45, 52, 255), outline=(122, 95, 62, 255), width=2)
        paste_asset(image, asset("status", icon), (x + 55, 210), (42, 42))
        draw.text((x + 30, 270), name, fill=(242, 232, 202, 255), font=font(18, True))
        draw.text((x + 35, 305), f"HP {hp}\n护甲 3", fill=(222, 223, 212, 255), font=font(16), spacing=8)
    draw.text((560, 408), "伤害数字与攻击连线显示在战场中央", fill=(166, 172, 176, 255), font=font(16))
    panel(draw, (950, 120, 1228, 470), "战斗日志")
    draw.text((980, 178), "战斗开始：锈蚀虫群\n使用 打击：造成 6 伤害\n敌人意图：攻击 5", fill=(222, 223, 214, 255), font=font(17), spacing=14)
    draw_button(draw, (1000, 385), "结束回合", 180)
    panel(draw, (36, 500, 1228, 690), "手牌")
    cards = [("attack", "打击", "1", "造成6伤害"), ("defense", "守备", "1", "获得6护甲"), ("attack", "盾击", "1", "伤害5 护甲3"), ("skill", "铁誓反击", "1", "护甲4 下次攻击+3"), ("attack", "星火弹", "1", "伤害5 燃烧2")]
    for index, item in enumerate(cards):
        draw_card(image, draw, (80 + index * 145, 522), item[0], item[1], item[2], item[3], 0.78)
    return image


def reward_screen() -> Image.Image:
    image, draw = make_canvas("战斗奖励", "选择成长，进入构筑管理")
    draw_resource_bar(image, draw)
    panel(draw, (54, 130, 335, 585), "自动奖励")
    draw_icon_text(image, draw, "icon_coin.png", (90, 200), "+22 金币")
    draw_icon_text(image, draw, "icon_energy.png", (90, 255), "+0 天赋点")
    draw.text((90, 330), "当前牌组：10 张\n辅助库存：0 张\n装备：誓约刃", fill=(222, 223, 214, 255), font=font(18), spacing=12)
    panel(draw, (370, 130, 930, 585), "卡牌三选一")
    cards = [("attack", "盾击", "1", "伤害5 护甲3"), ("skill", "铁誓反击", "1", "护甲4 强化下次攻击"), ("support", "重击辅助", "0", "插入攻击牌 伤害+3")]
    for index, item in enumerate(cards):
        draw_card(image, draw, (410 + index * 165, 220), item[0], item[1], item[2], item[3], 0.95)
    panel(draw, (970, 130, 1220, 585), "操作")
    draw.text((1000, 205), "选中奖励后进入构筑管理。\n辅助卡会进入辅助库存。", fill=(222, 223, 214, 255), font=font(17), spacing=12)
    draw_button(draw, (1000, 405), "确认领取", 180)
    draw_button(draw, (1000, 465), "跳过奖励", 180)
    return image


def build_screen() -> Image.Image:
    image, draw = make_canvas("构筑管理", "管理牌组、辅助连接、装备和天赋")
    draw_resource_bar(image, draw)
    panel(draw, (36, 120, 230, 650), "标签")
    for index, text in enumerate(["牌组", "技能插槽", "装备", "天赋"]):
        draw_button(draw, (62, 180 + index * 62), text, 135, index == 1)
    panel(draw, (265, 120, 835, 650), "技能插槽")
    draw_card(image, draw, (300, 190), "attack", "盾击", "1", "伤害5 护甲3", 0.86)
    paste_asset(image, asset("icons", "socket_attack.png"), (455, 235), (54, 54))
    draw.text((525, 247), "空攻击辅助槽", fill=(222, 223, 214, 255), font=font(18, True))
    draw.line((420, 275, 455, 262), fill=(226, 181, 82, 255), width=4)
    draw_card(image, draw, (300, 410), "attack", "星火弹", "1", "伤害5 燃烧2", 0.86)
    paste_asset(image, asset("icons", "socket_spell.png"), (455, 455), (54, 54))
    draw.text((525, 467), "法术/火焰辅助槽", fill=(222, 223, 214, 255), font=font(18, True))
    panel(draw, (870, 120, 1228, 650), "可用辅助与详情")
    draw_card(image, draw, (910, 180), "support", "重击辅助", "0", "兼容 attack 伤害+3", 0.86)
    draw_card(image, draw, (1060, 180), "support", "护返辅助", "0", "兼容 block 使用后护甲+2", 0.86)
    draw.text((910, 455), "右侧显示兼容提示，插入失败时在底部提示原因。", fill=(222, 223, 214, 255), font=font(17))
    draw_button(draw, (910, 550), "自动推荐", 140)
    draw_button(draw, (1060, 550), "返回地图", 140)
    return image


def event_screen() -> Image.Image:
    image, draw = make_canvas("事件", "非战斗风险收益选择")
    draw_resource_bar(image, draw)
    panel(draw, (70, 140, 470, 585), "事件插画")
    paste_asset(image, asset("map", "node_event.png"), (190, 255), (150, 150))
    panel(draw, (520, 140, 1210, 585), "破损符文炉")
    draw.text((555, 210), "一座仍有余温的符文炉等待代价。", fill=(231, 229, 211, 255), font=font(23, True))
    draw.text((555, 270), "选择会立即结算，并在完成后进入构筑管理。", fill=(174, 181, 181, 255), font=font(17))
    draw_button(draw, (560, 345), "献出 8 生命，获得辅助卡", 360)
    draw_button(draw, (560, 405), "搜刮冷却碎片，获得 35 金币", 360)
    draw_button(draw, (560, 465), "离开", 160)
    return image


def shop_screen() -> Image.Image:
    image, draw = make_canvas("商店/锻造", "购买、恢复、修正构筑")
    draw_resource_bar(image, draw)
    panel(draw, (50, 130, 830, 600), "商品与服务")
    entries = [("support", "重击辅助", "40 金币", "攻击牌伤害+3"), ("defense", "合金外衣", "55 金币", "最大生命+8"), ("skill", "恢复生命", "35 金币", "恢复18生命")]
    for index, item in enumerate(entries):
        x = 95 + index * 230
        draw_card(image, draw, (x, 225), item[0], item[1], "", item[3], 0.9)
        draw.text((x + 18, 395), item[2], fill=(238, 221, 164, 255), font=font(17, True))
        draw_button(draw, (x, 435), "购买", 135)
    panel(draw, (880, 130, 1218, 600), "详情")
    paste_asset(image, asset("map", "node_shop.png"), (995, 185), (96, 96))
    draw.text((920, 315), "金币不足时按钮置灰并在提示栏说明。\n购买完成后商品状态刷新。", fill=(222, 223, 214, 255), font=font(18), spacing=12)
    draw_button(draw, (930, 505), "打开构筑", 130)
    draw_button(draw, (1075, 505), "离开", 100)
    return image


def chapter_result_screen() -> Image.Image:
    image, draw = make_canvas("章节结算", "Boss 胜利后的章节奖励")
    panel(draw, (64, 128, 395, 605), "本章统计")
    paste_asset(image, asset("map", "node_boss.png"), (160, 200), (128, 128))
    draw.text((100, 365), "已击败：活熔炉\n胜利战斗：5\n获得卡牌：4\n造成伤害：286", fill=(222, 223, 214, 255), font=font(19), spacing=12)
    panel(draw, (435, 128, 910, 605), "章节奖励三选一")
    for index, text in enumerate(["升华：护甲反击", "装备：镶孔戒", "天赋点 +1"]):
        draw.rounded_rectangle((480, 215 + index * 105, 865, 285 + index * 105), radius=8, fill=(51, 55, 65, 255), outline=(190, 151, 72, 255), width=2)
        draw.text((510, 235 + index * 105), text, fill=(238, 231, 203, 255), font=font(22, True))
    panel(draw, (950, 128, 1218, 605), "下一步")
    draw.text((980, 210), "MVP 只开放 1 章。\n后续版本这里展示下一章预告。", fill=(222, 223, 214, 255), font=font(18), spacing=12)
    draw_button(draw, (990, 460), "进入本局结算", 180)
    return image


def run_result_screen() -> Image.Image:
    image, draw = make_canvas("本局结算", "失败或通关后的结果页")
    paste_asset(image, asset("ui", "popup_panel.png"), (300, 110), (680, 380))
    draw.text((450, 175), "远征完成", fill=(247, 232, 188, 255), font=font(42, True))
    draw.text((410, 250), "角色：铁誓者\n章节：腐化矿脉\n胜利战斗：5\n打出卡牌：48\n造成伤害：286", fill=(224, 225, 214, 255), font=font(21), spacing=14)
    panel(draw, (86, 535, 515, 660), "最终牌组摘要")
    draw.text((120, 585), "打击 x3、守备 x3、盾击、铁誓反击、星火弹、重击辅助", fill=(222, 223, 214, 255), font=font(17))
    draw_button(draw, (670, 555), "重新开始", 170)
    draw_button(draw, (865, 555), "返回主菜单", 190)
    return image


def settings_popup() -> Image.Image:
    image, draw = make_canvas("设置弹窗", "任意界面上方的居中弹窗")
    draw.rectangle((0, 64, 1280, 720), fill=(0, 0, 0, 112))
    panel(draw, (330, 130, 950, 610), "设置")
    draw.text((370, 190), "音频    画面    游戏    输入", fill=(238, 231, 203, 255), font=font(22, True))
    for index, text in enumerate(["主音量", "音乐", "音效", "战斗速度"]):
        y = 260 + index * 60
        draw.text((380, y), text, fill=(222, 223, 214, 255), font=font(18))
        draw.rounded_rectangle((520, y + 5, 820, y + 21), radius=8, fill=(55, 58, 65, 255), outline=(126, 112, 78, 255), width=1)
        draw.rounded_rectangle((520, y + 5, 700, y + 21), radius=8, fill=(207, 160, 68, 255))
    draw_button(draw, (420, 520), "恢复默认", 150)
    draw_button(draw, (600, 520), "应用", 120)
    draw_button(draw, (750, 520), "关闭", 120)
    return image


def detail_popup() -> Image.Image:
    image, draw = make_canvas("详情弹窗", "卡牌、装备、天赋共用详情层")
    draw.rectangle((0, 64, 1280, 720), fill=(0, 0, 0, 112))
    panel(draw, (255, 105, 1025, 640), "卡牌详情")
    draw_card(image, draw, (320, 190), "attack", "星火弹", "1", "造成5伤害。施加2层燃烧。", 1.35)
    draw.text((560, 185), "星火弹", fill=(247, 232, 188, 255), font=font(34, True))
    draw.text((560, 245), "类型：攻击 / 法术 / 火焰\n费用：1\n目标：单体敌人\n插槽：2", fill=(222, 223, 214, 255), font=font(19), spacing=12)
    draw.text((560, 370), "关键词说明\n燃烧：敌方回合开始时受到层数伤害，然后层数 -1。\n辅助兼容：可插入 attack、spell 或 fire 标签辅助。", fill=(214, 214, 200, 255), font=font(17), spacing=10)
    draw_button(draw, (790, 555), "关闭", 120)
    return image


def confirm_popup() -> Image.Image:
    image, draw = make_canvas("确认弹窗", "防误操作确认层")
    draw.rectangle((0, 64, 1280, 720), fill=(0, 0, 0, 132))
    panel(draw, (405, 220, 875, 500), "确认操作")
    draw.text((450, 290), "开始新局会覆盖当前未完成远征。", fill=(235, 230, 210, 255), font=font(22, True))
    draw.text((450, 340), "该操作确认后不可撤销。", fill=(176, 181, 181, 255), font=font(17))
    draw_button(draw, (485, 425), "确认", 120)
    draw_button(draw, (660, 425), "取消", 120)
    return image


def overview(files: list[tuple[str, str]]) -> Image.Image:
    thumb_w, thumb_h = 320, 180
    rows = (len(files) + 3) // 4
    image = Image.new("RGBA", (1280, 92 + rows * 285), (16, 19, 24, 255))
    draw = ImageDraw.Draw(image)
    draw.text((28, 20), "WorldSeed 界面效果图总览 v0.1", fill=(246, 232, 188, 255), font=font(34, True))
    for index, item in enumerate(files):
        name, filename = item
        x = 28 + index % 4 * 310
        y = 82 + index // 4 * 285
        src = Image.open(OUT / filename).convert("RGBA").resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        image.alpha_composite(src, (x, y))
        draw.rectangle((x, y, x + thumb_w, y + thumb_h), outline=(82, 86, 92, 255), width=1)
        draw.text((x, y + thumb_h + 10), name, fill=(226, 226, 214, 255), font=font(16, True))
    return image


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    screens = [
        ("UI-001 主菜单", "ui-001-main-menu.png", main_menu),
        ("UI-002 角色选择", "ui-002-character-select.png", character_select),
        ("UI-003 地图", "ui-003-map.png", map_screen),
        ("UI-004 战斗", "ui-004-combat.png", combat_screen),
        ("UI-005 战斗奖励", "ui-005-reward.png", reward_screen),
        ("UI-006 构筑管理", "ui-006-build.png", build_screen),
        ("UI-007 事件", "ui-007-event.png", event_screen),
        ("UI-008 商店锻造", "ui-008-shop.png", shop_screen),
        ("UI-009 章节结算", "ui-009-chapter-result.png", chapter_result_screen),
        ("UI-010 本局结算", "ui-010-run-result.png", run_result_screen),
        ("UI-011 设置弹窗", "ui-011-settings.png", settings_popup),
        ("UI-012 详情弹窗", "ui-012-detail.png", detail_popup),
        ("UI-013 确认弹窗", "ui-013-confirm.png", confirm_popup),
    ]
    for name, filename, renderer in screens:
        renderer().convert("RGB").save(OUT / filename, quality=95)
        print(f"rendered {name}: {OUT / filename}")
    overview([(item[0], item[1]) for item in screens]).convert("RGB").save(OUT / "ui-000-overview.png", quality=95)
    print(f"rendered overview: {OUT / 'ui-000-overview.png'}")


if __name__ == "__main__":
    main()
