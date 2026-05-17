from __future__ import annotations

import math
import random
from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "WorldSeed.AIGC" / "wiki" / "design" / "images" / "ui-screen-mockups-v0.3"
SIZE = (1280, 720)
FONT_KAI = "C:/Windows/Fonts/simkai.ttf"
FONT_REGULAR = "C:/Windows/Fonts/msyh.ttc"
FONT_BOLD = "C:/Windows/Fonts/msyhbd.ttc"

PALETTE = {
    "paper": (232, 224, 207),
    "ink": (48, 45, 39),
    "line": (116, 98, 73),
    "gold": (184, 139, 60),
    "jade": (51, 131, 117),
    "cinnabar": (156, 54, 39),
    "purple": (92, 62, 138),
    "blue": (73, 137, 166),
    "black": (46, 47, 48),
    "cloud": (204, 198, 184),
}


def font(size: int, bold: bool = False, kai: bool = False) -> ImageFont.FreeTypeFont:
    if kai and Path(FONT_KAI).exists():
        return ImageFont.truetype(FONT_KAI, size)
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REGULAR, size)


def canvas(title: str, subtitle: str = "") -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGBA", SIZE, PALETTE["paper"] + (255,))
    draw = ImageDraw.Draw(image)
    paper_texture(draw, 1280, 720)
    bottom_mountains(draw, 520)
    ornament_header(draw, title, subtitle)
    return image, draw


def paper_texture(draw: ImageDraw.ImageDraw, width: int, height: int) -> None:
    random.seed(81)
    for y in range(height):
        shade = 234 - int(y * 0.025)
        draw.line((0, y, width, y), fill=(shade, shade - 9, shade - 25, 255))
    for _i in range(2100):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if random.random() < 0.55:
            color = (117, 101, 75, random.randint(18, 45))
        else:
            color = (255, 250, 230, random.randint(16, 42))
        draw.point((x, y), fill=color)


def bottom_mountains(draw: ImageDraw.ImageDraw, base_y: int) -> None:
    layers = [
        ((120, 135, 129, 70), base_y + 64, 88),
        ((74, 95, 96, 100), base_y + 94, 70),
        ((38, 64, 68, 138), base_y + 130, 52),
    ]
    for color, y_base, amp in layers:
        points = [(0, 720), (0, y_base)]
        for x in range(0, 1320, 90):
            y = y_base - int(abs(math.sin(x / 110)) * amp) - random.randint(0, 22)
            points.append((x, y))
        points.extend([(1280, 720), (0, 720)])
        draw.polygon(points, fill=color)


def ornament_header(draw: ImageDraw.ImageDraw, title: str, subtitle: str) -> None:
    draw.text((28, 20), "❧", fill=PALETTE["ink"] + (210,), font=font(25, False, True))
    draw.text((62, 18), title, fill=PALETTE["ink"] + (255,), font=font(27, True, True))
    draw.line((160, 36, 980, 36), fill=PALETTE["line"] + (140,), width=1)
    draw.text((985, 20), "❧", fill=PALETTE["ink"] + (210,), font=font(25, False, True))
    if subtitle:
        draw.text((1030, 22), subtitle, fill=(91, 82, 65, 255), font=font(15, False, True))


def panel(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], title: str = "") -> None:
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle(xy, radius=8, fill=(239, 231, 211, 236), outline=PALETTE["line"] + (230,), width=2)
    draw.rectangle((x1 + 8, y1 + 8, x2 - 8, y2 - 8), outline=(185, 155, 100, 130), width=1)
    corner(draw, x1 + 12, y1 + 12, "tl")
    corner(draw, x2 - 48, y1 + 12, "tr")
    corner(draw, x1 + 12, y2 - 48, "bl")
    corner(draw, x2 - 48, y2 - 48, "br")
    if title:
        draw.text((x1 + 22, y1 + 15), title, fill=PALETTE["ink"] + (255,), font=font(20, True, True))
        draw.line((x1 + 20, y1 + 48, x2 - 20, y1 + 48), fill=PALETTE["gold"] + (150,), width=1)


def corner(draw: ImageDraw.ImageDraw, x: int, y: int, side: str) -> None:
    color = PALETTE["gold"] + (160,)
    if side in ["tl", "br"]:
        draw.arc((x, y, x + 36, y + 36), 180, 270, fill=color, width=2)
        draw.arc((x + 9, y + 9, x + 30, y + 30), 180, 270, fill=color, width=1)
    else:
        draw.arc((x, y, x + 36, y + 36), 270, 360, fill=color, width=2)
        draw.arc((x + 6, y + 9, x + 27, y + 30), 270, 360, fill=color, width=1)


def button(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, width: int = 210, active: bool = True) -> None:
    x, y = xy
    fill = (118, 59, 42, 244) if active else (176, 165, 139, 215)
    outline = PALETTE["gold"] + (255,) if active else (119, 107, 84, 210)
    draw.rounded_rectangle((x, y, x + width, y + 40), radius=4, fill=fill, outline=outline, width=2)
    draw.text((x + 14, y + 8), text, fill=(252, 240, 211, 255) if active else (92, 84, 68, 255), font=font(17, True, True))


def resource_bar(draw: ImageDraw.ImageDraw, x: int = 760, y: int = 78) -> None:
    resources = [("命", "72/80", PALETTE["cinnabar"]), ("罡", "6", PALETTE["jade"]), ("灵", "3/3", PALETTE["blue"]), ("石", "84", PALETTE["gold"])]
    for index, item in enumerate(resources):
        cx = x + index * 96
        draw.ellipse((cx, y, cx + 28, y + 28), fill=item[2] + (235,), outline=(64, 49, 35, 255), width=2)
        draw.text((cx + 6, y + 3), item[0], fill=(255, 244, 215, 255), font=font(15, True, True))
        draw.text((cx + 34, y + 3), item[1], fill=PALETTE["ink"] + (255,), font=font(15, True))


def cost_gem(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, color: tuple[int, int, int]) -> None:
    points = [(x + 15, y), (x + 30, y + 9), (x + 27, y + 31), (x + 15, y + 40), (x + 3, y + 31), (x, y + 9)]
    draw.polygon(points, fill=color + (245,), outline=(48, 43, 35, 255))
    draw.text((x + 9, y + 7), text, fill=(255, 244, 215, 255), font=font(18, True))


def card_frame(draw: ImageDraw.ImageDraw, xy: tuple[int, int], size: tuple[int, int], color: tuple[int, int, int], title: str, cost: str, kind: str, body: str, art: str) -> None:
    x, y = xy
    w, h = size
    draw.rounded_rectangle((x, y, x + w, y + h), radius=9, fill=(225, 216, 198, 255), outline=(55, 43, 35, 255), width=3)
    draw.rounded_rectangle((x + 7, y + 7, x + w - 7, y + h - 7), radius=7, outline=color + (230,), width=3)
    draw.rectangle((x + 18, y + 16, x + 47, y + h - 18), fill=(32, 33, 31, 235))
    draw.text((x + 23, y + 56), kind, fill=(247, 235, 204, 255), font=font(max(15, w // 9), True, True), spacing=2)
    cost_gem(draw, x + 5, y + 5, cost, color)
    draw.rectangle((x + 56, y + 20, x + w - 18, y + int(h * 0.58)), fill=(210, 205, 190, 255), outline=(98, 82, 58, 180), width=1)
    draw_card_art(draw, (x + 60, y + 24, x + w - 22, y + int(h * 0.58) - 4), color, art)
    draw.rounded_rectangle((x + 56, y + int(h * 0.61), x + w - 18, y + h - 47), radius=5, fill=(222, 216, 202, 245), outline=(130, 110, 80, 180), width=1)
    draw.text((x + 68, y + int(h * 0.63)), title, fill=PALETTE["ink"] + (255,), font=font(max(14, w // 10), True, True))
    text_y = y + int(h * 0.72)
    for line in wrap(body, width=max(7, w // 15)):
        draw.text((x + 67, text_y), line, fill=(64, 59, 50, 255), font=font(max(11, w // 13), False, True))
        text_y += max(15, h // 13)
    draw.rounded_rectangle((x + w // 2 - 32, y + h - 31, x + w // 2 + 32, y + h - 11), radius=4, fill=color + (230,), outline=(68, 50, 34, 255), width=1)
    draw.text((x + w // 2 - 20, y + h - 31), "修士", fill=(255, 241, 210, 255), font=font(max(10, w // 14), True, True))
    ornate_edges(draw, x, y, w, h, color)


def ornate_edges(draw: ImageDraw.ImageDraw, x: int, y: int, w: int, h: int, color: tuple[int, int, int]) -> None:
    for dx, dy, a1, a2 in [(9, 9, 180, 305), (w - 46, 9, 235, 360), (9, h - 46, 55, 180), (w - 46, h - 46, -35, 90)]:
        draw.arc((x + dx, y + dy, x + dx + 38, y + dy + 38), a1, a2, fill=color + (230,), width=2)
        draw.arc((x + dx + 8, y + dy + 8, x + dx + 30, y + dy + 30), a1, a2, fill=PALETTE["gold"] + (185,), width=1)


def draw_card_art(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], color: tuple[int, int, int], art: str) -> None:
    x1, y1, x2, y2 = xy
    if x2 <= x1 + 20 or y2 <= y1 + 20:
        return
    draw.rectangle(xy, fill=(218, 215, 204, 255))
    if art == "sword":
        for offset in [0, 18]:
            draw.line((x1 + 25 + offset, y2 - 18, x2 - 22 + offset, y1 + 20), fill=(84, 137, 166, 230), width=4)
            draw.line((x1 + 32 + offset, y2 - 24, x2 - 15 + offset, y1 + 18), fill=(240, 247, 250, 210), width=1)
        draw.line((x1 + 25, y2 - 18, x1 + 8, y2 - 5), fill=(94, 62, 32, 255), width=5)
    elif art == "fairy":
        draw.ellipse((x1 + 52, y1 + 22, x1 + 88, y1 + 58), fill=(230, 203, 181, 255), outline=(82, 70, 56, 180))
        draw.polygon([(x1 + 70, y1 + 55), (x1 + 35, y2 - 8), (x1 + 110, y2 - 8)], fill=(160, 205, 193, 235), outline=(88, 116, 108, 220))
        draw.arc((x1 + 16, y1 + 55, x2 - 18, y2 - 12), 200, 340, fill=(222, 154, 167, 200), width=4)
    elif art == "beast":
        draw.polygon([(x1 + 42, y2 - 24), (x1 + 65, y1 + 30), (x1 + 92, y2 - 18)], fill=(214, 214, 206, 255), outline=(119, 65, 52, 255))
        draw.arc((x1 + 34, y1 + 22, x1 + 110, y2 - 20), 250, 80, fill=color + (230,), width=5)
        draw.ellipse((x1 + 76, y1 + 60, x1 + 84, y1 + 68), fill=(120, 30, 24, 255))
    elif art == "talisman":
        draw.rounded_rectangle((x1 + 44, y1 + 20, x1 + 100, y2 - 20), radius=4, fill=(218, 176, 92, 240), outline=(111, 71, 38, 230), width=2)
        for i in range(4):
            draw.line((x1 + 55, y1 + 38 + i * 20, x1 + 90, y1 + 45 + i * 15), fill=(105, 47, 35, 220), width=2)
        draw.line((x1 + 12, y2 - 18, x2 - 14, y1 + 16), fill=color + (185,), width=4)
    else:
        for i in range(4):
            yy = y2 - 18 - i * 17
            draw.arc((x1 + 8 + i * 20, yy - 30, x1 + 100 + i * 22, yy + 25), 200, 345, fill=(87, 104, 96, 160), width=3)
    draw.arc((x1 + 8, y2 - 38, x2 - 12, y2 + 15), 185, 350, fill=(80, 98, 92, 130), width=2)


def small_card(draw: ImageDraw.ImageDraw, xy: tuple[int, int], color: tuple[int, int, int], title: str, cost: str = "1", kind: str = "剑", art: str = "sword") -> None:
    card_frame(draw, xy, (108, 154), color, title, cost, kind, "效果摘要", art)


def main_menu() -> Image.Image:
    image, draw = canvas("主菜单", "参考卡牌示例风格")
    draw.text((76, 115), "WorldSeed", fill=PALETTE["ink"] + (255,), font=font(38, True))
    draw.text((76, 163), "山海灵契", fill=PALETTE["ink"] + (255,), font=font(47, True, True))
    draw.text((78, 238), "卡牌修仙 · 灵脉远征 · 法门构筑", fill=(84, 75, 58, 255), font=font(21, False, True))
    for i, text in enumerate(["新开灵契", "续接旧局", "设置", "退出"]):
        button(draw, (82, 330 + i * 55), text, 260, i != 1)
    panel(draw, (690, 105, 1145, 498), "最近远征")
    card_frame(draw, (720, 160), (150, 220), PALETTE["jade"], "铁誓者", "5", "剑修", "命元72/80\n腐化矿脉", "sword")
    draw.text((905, 178), "角色：铁誓者\n境地：腐化矿脉\n节点：灵市\n流派：护体反击", fill=PALETTE["ink"] + (255,), font=font(20, False, True), spacing=14)
    button(draw, (905, 388), "继续此局", 160, False)
    return image


def character_select() -> Image.Image:
    image, draw = canvas("角色选择", "门类卡展示")
    button(draw, (36, 82), "返回", 110)
    panel(draw, (46, 125, 395, 620), "门类")
    card_frame(draw, (78, 180), (145, 220), PALETTE["blue"], "剑渡凌云", "5", "剑修", "对敌方造成3点伤害", "sword")
    draw.rounded_rectangle((68, 170, 233, 410), radius=10, outline=PALETTE["cinnabar"] + (255,), width=3)
    draw.text((255, 205), "铁誓者\n护体反击\n上手难度：低", fill=PALETTE["ink"] + (255,), font=font(22, True, True), spacing=13)
    panel(draw, (430, 125, 760, 620), "角色详情")
    draw.text((465, 188), "铁誓者", fill=PALETTE["ink"] + (255,), font=font(34, True, True))
    draw.text((465, 246), "命元：80\n本命：誓约刃\n门类：剑修 / 人族\n战斗节奏：聚罡、反击、重击", fill=PALETTE["ink"] + (255,), font=font(20, False, True), spacing=14)
    button(draw, (465, 525), "开始问道", 220)
    panel(draw, (800, 125, 1215, 620), "起手卡组")
    examples = [(PALETTE["blue"], "劈山", "剑", "sword"), (PALETTE["jade"], "守势", "护", "land"), (PALETTE["gold"], "凝神", "气", "talisman"), (PALETTE["purple"], "星火符", "术", "talisman")]
    for idx, item in enumerate(examples):
        small_card(draw, (835 + idx * 96, 220), item[0], item[1], "1", item[2], item[3])
    draw.text((840, 485), "选中角色后展示初始法门、法器和天赋起点。", fill=PALETTE["ink"] + (255,), font=font(18, False, True))
    return image


def map_screen() -> Image.Image:
    image, draw = canvas("灵脉图", "山水卷轴路线")
    resource_bar(draw)
    panel(draw, (40, 120, 304, 620), "洞天")
    draw.text((70, 178), "腐化矿脉\n层数：6\n镇守：活熔炉\n异象：余烬回响", fill=PALETTE["ink"] + (255,), font=font(20, False, True), spacing=15)
    panel(draw, (335, 120, 915, 620), "灵脉路线")
    nodes = [("斗", PALETTE["cinnabar"]), ("遇", PALETTE["blue"]), ("市", PALETTE["gold"]), ("斗", PALETTE["cinnabar"]), ("劫", PALETTE["purple"]), ("炉", (187, 83, 43))]
    coords = []
    for i, node in enumerate(nodes):
        x = 385 + i * 84
        y = 360 - (i % 2) * 75
        coords.append((x, y))
        if i:
            px, py = coords[i - 1]
            draw.line((px + 48, py + 28, x, y + 28), fill=(90, 103, 93, 190), width=4)
        draw.ellipse((x, y, x + 56, y + 56), fill=node[1] + (235,), outline=(55, 43, 35, 255), width=3)
        draw.text((x + 16, y + 12), node[0], fill=(255, 242, 211, 255), font=font(24, True, True))
        if i == 0:
            draw.ellipse((x - 7, y - 7, x + 63, y + 63), outline=PALETTE["gold"] + (240,), width=4)
    panel(draw, (950, 120, 1225, 620), "当前节点")
    card_frame(draw, (1010, 175), (135, 200), PALETTE["cinnabar"], "锈蚀虫群", "1", "斗法", "奖励：灵石、法门", "beast")
    button(draw, (1000, 520), "进入斗法", 180)
    return image


def combat_screen() -> Image.Image:
    image, draw = canvas("斗法", "卡牌与敌意")
    resource_bar(draw, 740, 78)
    panel(draw, (38, 120, 300, 470), "己方")
    card_frame(draw, (86, 178), (126, 190), PALETTE["blue"], "铁誓者", "5", "剑修", "命元72/80\n罡气6", "sword")
    panel(draw, (340, 120, 925, 470), "敌阵")
    card_frame(draw, (405, 174), (145, 215), PALETTE["black"], "锈蚀虫", "2", "妖兽", "意图：攻击5", "beast")
    card_frame(draw, (630, 174), (145, 215), PALETTE["black"], "锈蚀虫", "2", "妖兽", "意图：护甲3", "beast")
    panel(draw, (955, 120, 1225, 470), "斗法记录")
    draw.text((985, 178), "施展 劈山：造成6伤害\n敌方准备攻击\n下一步：出牌或收势", fill=PALETTE["ink"] + (255,), font=font(17, False, True), spacing=14)
    button(draw, (1000, 385), "收势回合", 170)
    panel(draw, (38, 498, 1225, 690), "手牌")
    cards = [(PALETTE["blue"], "劈山", "剑", "sword"), (PALETTE["jade"], "守势", "护", "land"), (PALETTE["blue"], "盾击", "剑", "sword"), (PALETTE["gold"], "凝神", "气", "talisman"), (PALETTE["purple"], "星火符", "术", "talisman")]
    for i, item in enumerate(cards):
        small_card(draw, (82 + i * 130, 535), item[0], item[1], "1", item[2], item[3])
    return image


def reward_screen() -> Image.Image:
    image, draw = canvas("斗法奖励", "三选一卡牌")
    resource_bar(draw)
    panel(draw, (55, 125, 335, 600), "收获")
    draw.text((92, 195), "灵石 +22\n悟道点 +0\n当前法门：10\n符箓库存：0", fill=PALETTE["ink"] + (255,), font=font(20, False, True), spacing=16)
    panel(draw, (370, 125, 935, 600), "法门三选一")
    card_frame(draw, (410, 205), (145, 220), PALETTE["blue"], "盾击", "1", "剑修", "伤害5\n获得罡气3", "sword")
    card_frame(draw, (580, 205), (145, 220), PALETTE["jade"], "铁誓反击", "1", "护法", "罡气4\n下次攻击+3", "land")
    card_frame(draw, (750, 205), (145, 220), PALETTE["gold"], "重击符", "0", "符箓", "嵌入攻击\n伤害+3", "talisman")
    panel(draw, (970, 125, 1220, 600), "操作")
    button(draw, (1005, 385), "确认收取", 170)
    button(draw, (1005, 445), "略过法门", 170)
    return image


def build_screen() -> Image.Image:
    image, draw = canvas("构筑洞府", "法门、符箓、法器")
    resource_bar(draw)
    panel(draw, (40, 120, 230, 650), "页签")
    for idx, text in enumerate(["牌组", "符箓槽", "法器", "悟道"]):
        button(draw, (65, 180 + idx * 60), text, 130, idx == 1)
    panel(draw, (265, 120, 830, 650), "符箓连接")
    card_frame(draw, (305, 190), (128, 190), PALETTE["blue"], "盾击", "1", "剑修", "可插攻击符", "sword")
    card_frame(draw, (520, 195), (120, 178), PALETTE["gold"], "重击符", "0", "符箓", "伤害+3", "talisman")
    draw.line((433, 282, 520, 282), fill=PALETTE["cinnabar"] + (220,), width=4)
    card_frame(draw, (305, 420), (128, 190), PALETTE["purple"], "星火符", "1", "法术", "燃烧2", "talisman")
    draw.text((518, 465), "空符槽：火 / 法术", fill=PALETTE["ink"] + (255,), font=font(20, False, True))
    panel(draw, (865, 120, 1225, 650), "可用符箓")
    small_card(draw, (910, 188), PALETTE["gold"], "重击符", "0", "符", "talisman")
    small_card(draw, (1040, 188), PALETTE["jade"], "护返符", "0", "符", "talisman")
    button(draw, (910, 555), "自动荐符", 135)
    button(draw, (1060, 555), "返回灵脉", 135)
    return image


def event_screen() -> Image.Image:
    image, draw = canvas("奇遇", "卷轴事件")
    resource_bar(draw)
    panel(draw, (70, 130, 470, 592), "破损符文炉")
    card_frame(draw, (185, 210), (145, 220), PALETTE["gold"], "符文炉", "?", "奇遇", "余温未散\n可换符箓", "talisman")
    panel(draw, (520, 130, 1210, 592), "选择")
    draw.text((560, 205), "一座仍有余温的符文炉等待代价。", fill=PALETTE["ink"] + (255,), font=font(24, True, True))
    button(draw, (560, 320), "献出 8 命元，获得符箓", 360)
    button(draw, (560, 380), "搜刮灵屑，获得 35 灵石", 360)
    button(draw, (560, 440), "离开", 160)
    return image


def shop_screen() -> Image.Image:
    image, draw = canvas("灵市/锻炉", "商品卡陈列")
    resource_bar(draw)
    panel(draw, (50, 125, 850, 605), "货架")
    goods = [(PALETTE["gold"], "重击符", "40", "符", "talisman"), (PALETTE["jade"], "合金法衣", "55", "器", "land"), (PALETTE["blue"], "温养命元", "35", "丹", "talisman")]
    for idx, item in enumerate(goods):
        x = 95 + idx * 235
        card_frame(draw, (x, 210), (145, 220), item[0], item[1], item[2], item[3], "购买后加入构筑", item[4])
        button(draw, (x + 8, 455), "购买", 128)
    panel(draw, (890, 125, 1220, 605), "掌柜提示")
    draw.text((930, 210), "商品以卡牌形式陈列。\n费用宝珠直接展示价格。\n购买后状态刷新。", fill=PALETTE["ink"] + (255,), font=font(19, False, True), spacing=15)
    button(draw, (940, 500), "打开构筑", 130)
    button(draw, (1085, 500), "离开", 100)
    return image


def chapter_result_screen() -> Image.Image:
    image, draw = canvas("洞天结算", "升华卡选择")
    panel(draw, (65, 125, 395, 608), "战果")
    card_frame(draw, (150, 205), (145, 220), (187, 83, 43), "活熔炉", "6", "妖兽", "已镇压", "beast")
    draw.text((105, 465), "胜利斗法：5\n获得法门：4\n造成伤害：286", fill=PALETTE["ink"] + (255,), font=font(19, False, True), spacing=12)
    panel(draw, (435, 125, 915, 608), "升华三选一")
    for idx, text in enumerate(["罡气反震", "镶孔戒", "悟道点 +1"]):
        card_frame(draw, (475 + idx * 145, 210), (125, 190), [PALETTE["jade"], PALETTE["gold"], PALETTE["purple"]][idx], text, str(idx + 1), "升华", "章节奖励", "land")
    panel(draw, (955, 125, 1220, 608), "下一步")
    draw.text((990, 225), "MVP 当前只开放一处洞天。\n后续这里展示下一章山水图。", fill=PALETTE["ink"] + (255,), font=font(18, False, True), spacing=13)
    button(draw, (998, 500), "进入结算", 165)
    return image


def run_result_screen() -> Image.Image:
    image, draw = canvas("本局结算", "卷轴战报")
    panel(draw, (330, 115, 950, 500), "远征完成")
    draw.text((482, 178), "远征完成", fill=PALETTE["ink"] + (255,), font=font(44, True, True))
    draw.text((430, 260), "角色：铁誓者\n洞天：腐化矿脉\n胜利斗法：5\n施展法门：48\n造成伤害：286", fill=PALETTE["ink"] + (255,), font=font(21, False, True), spacing=14)
    panel(draw, (86, 535, 515, 660), "最终卡组")
    draw.text((118, 585), "劈山 x3、守势 x3、盾击、铁誓反击、星火符、重击符", fill=PALETTE["ink"] + (255,), font=font(17, False, True))
    button(draw, (670, 555), "重新问道", 170)
    button(draw, (865, 555), "返回主菜单", 190)
    return image


def settings_popup() -> Image.Image:
    image, draw = canvas("设置弹窗", "卷轴弹层")
    draw.rectangle((0, 0, 1280, 720), fill=(30, 28, 24, 95))
    panel(draw, (330, 130, 950, 612), "设置")
    draw.text((372, 195), "音律    画面    游戏    输入", fill=PALETTE["ink"] + (255,), font=font(23, True, True))
    for idx, text in enumerate(["总音量", "乐曲", "音效", "斗法速度"]):
        y = 265 + idx * 58
        draw.text((382, y), text, fill=PALETTE["ink"] + (255,), font=font(18, False, True))
        draw.rounded_rectangle((520, y + 6, 820, y + 22), radius=8, fill=(198, 184, 150, 255), outline=PALETTE["line"] + (255,), width=1)
        draw.rounded_rectangle((520, y + 6, 710, y + 22), radius=8, fill=PALETTE["cinnabar"] + (255,))
    button(draw, (420, 522), "恢复默认", 150)
    button(draw, (600, 522), "应用", 120)
    button(draw, (750, 522), "关闭", 120)
    return image


def detail_popup() -> Image.Image:
    image, draw = canvas("详情弹窗", "完整卡牌详情")
    draw.rectangle((0, 0, 1280, 720), fill=(30, 28, 24, 95))
    panel(draw, (255, 100, 1025, 650), "卡牌详情")
    card_frame(draw, (315, 170), (175, 265), PALETTE["purple"], "天雷符", "2", "法术", "对敌方造成4点伤害\n若有导电则+2", "talisman")
    draw.text((555, 170), "天雷符", fill=PALETTE["ink"] + (255,), font=font(36, True, True))
    draw.text((555, 235), "门类：法术 / 雷\n费用：2\n目标：单体敌人\n稀有度：玄品", fill=PALETTE["ink"] + (255,), font=font(20, False, True), spacing=13)
    draw.text((555, 385), "关键词说明\n导电：受到雷属性伤害时额外结算。\n符箓兼容：可插入 spell 或 lightning 标签辅助。", fill=(64, 59, 50, 255), font=font(17, False, True), spacing=11)
    button(draw, (790, 558), "关闭", 120)
    return image


def confirm_popup() -> Image.Image:
    image, draw = canvas("确认弹窗", "小型弹层")
    draw.rectangle((0, 0, 1280, 720), fill=(30, 28, 24, 108))
    panel(draw, (405, 220, 875, 500), "确认操作")
    draw.text((450, 292), "新开灵契会覆盖当前未完成远征。", fill=PALETTE["ink"] + (255,), font=font(23, True, True))
    draw.text((450, 344), "该操作确认后不可撤销。", fill=(91, 82, 65, 255), font=font(18, False, True))
    button(draw, (485, 425), "确认", 120)
    button(draw, (660, 425), "取消", 120)
    return image


def style_reference() -> Image.Image:
    image = Image.new("RGBA", (1600, 1100), PALETTE["paper"] + (255,))
    draw = ImageDraw.Draw(image)
    paper_texture(draw, 1600, 1100)
    draw.text((35, 28), "卡牌与 UI 元素参考 v0.3", fill=PALETTE["ink"] + (255,), font=font(36, True, True))
    draw.line((320, 50, 1040, 50), fill=PALETTE["line"] + (150,), width=2)
    examples = [
        (PALETTE["blue"], "剑渡凌云", "5", "剑修", "对敌方造成3点伤害", "sword"),
        (PALETTE["jade"], "清莲步", "4", "仙子", "恢复2点命元并抽1张牌", "fairy"),
        (PALETTE["cinnabar"], "摄心魅惑", "6", "妖兽", "造成2点伤害并附加魅惑", "beast"),
        (PALETTE["gold"], "玄天青冥剑", "3", "法宝", "装备后攻击+2", "sword"),
        (PALETTE["purple"], "天雷符", "2", "法术", "造成雷伤害", "talisman"),
    ]
    for idx, item in enumerate(examples):
        card_frame(draw, (45 + idx * 250, 95), (210, 320), item[0], item[1], item[2], item[3], item[4], item[5])
    draw.text((45, 470), "卡框设计", fill=PALETTE["ink"] + (255,), font=font(30, True, True))
    frames = [(PALETTE["jade"], "青玉云纹框"), (PALETTE["gold"], "鎏金山水框"), (PALETTE["purple"], "玄紫雷纹框"), (PALETTE["black"], "墨韵水墨框"), (PALETTE["cinnabar"], "朱砂符纹框"), (PALETTE["blue"], "白玉流云框")]
    for idx, item in enumerate(frames):
        x = 45 + idx * 245
        y = 520 if idx < 3 else 760
        if idx >= 3:
            x = 45 + (idx - 3) * 245
        card_frame(draw, (x, y), (150, 210), item[0], "", "", "", "", "land")
        draw.text((x + 8, y + 220), item[1], fill=PALETTE["ink"] + (255,), font=font(18, False, True))
    draw.text((820, 470), "配色与属性", fill=PALETTE["ink"] + (255,), font=font(30, True, True))
    colors = [("青瓷绿", PALETTE["jade"]), ("赭石红", PALETTE["cinnabar"]), ("墨黑", PALETTE["black"]), ("鎏金", PALETTE["gold"]), ("天青蓝", PALETTE["blue"]), ("灵紫", PALETTE["purple"])]
    for idx, item in enumerate(colors):
        x = 830 + idx * 115
        draw.ellipse((x, 540, x + 72, 612), fill=item[1] + (240,), outline=PALETTE["line"] + (255,), width=2)
        draw.text((x, 625), item[0], fill=PALETTE["ink"] + (255,), font=font(16, False, True))
    attrs = [("火", PALETTE["cinnabar"]), ("水", PALETTE["blue"]), ("雷", PALETTE["purple"]), ("木", PALETTE["jade"]), ("剑", PALETTE["black"]), ("灵", PALETTE["gold"])]
    for idx, item in enumerate(attrs):
        x = 835 + idx * 108
        y = 740
        cost_gem(draw, x, y, item[0], item[1])
        draw.text((x - 4, y + 52), item[0] + "系", fill=PALETTE["ink"] + (255,), font=font(16, False, True))
    return image


def overview(files: list[tuple[str, str]]) -> Image.Image:
    thumb_w, thumb_h = 320, 180
    rows = (len(files) + 3) // 4
    image = Image.new("RGBA", (1280, 92 + rows * 285), PALETTE["paper"] + (255,))
    draw = ImageDraw.Draw(image)
    paper_texture(draw, 1280, 92 + rows * 285)
    draw.text((28, 22), "WorldSeed 参考卡牌风格界面总览 v0.3", fill=PALETTE["ink"] + (255,), font=font(34, True))
    for idx, item in enumerate(files):
        name, filename = item
        x = 28 + idx % 4 * 310
        y = 82 + idx // 4 * 285
        source = Image.open(OUT / filename).convert("RGBA").resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        image.alpha_composite(source, (x, y))
        draw.rectangle((x, y, x + thumb_w, y + thumb_h), outline=PALETTE["line"] + (255,), width=1)
        draw.text((x, y + thumb_h + 10), name, fill=PALETTE["ink"] + (255,), font=font(17, True, True))
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
    style_reference().convert("RGB").save(OUT / "ui-014-style-reference.png", quality=95)
    print(f"rendered overview: {OUT / 'ui-000-overview.png'}")
    print(f"rendered style reference: {OUT / 'ui-014-style-reference.png'}")


if __name__ == "__main__":
    main()
