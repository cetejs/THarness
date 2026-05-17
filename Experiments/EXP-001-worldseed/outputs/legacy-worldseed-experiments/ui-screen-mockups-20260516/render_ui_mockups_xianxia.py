from __future__ import annotations

import math
import random
from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "WorldSeed.AIGC" / "wiki" / "design" / "images" / "ui-screen-mockups-v0.2"
SIZE = (1280, 720)
FONT_KAI = "C:/Windows/Fonts/simkai.ttf"
FONT_REGULAR = "C:/Windows/Fonts/msyh.ttc"
FONT_BOLD = "C:/Windows/Fonts/msyhbd.ttc"


def font(size: int, bold: bool = False, kai: bool = False) -> ImageFont.FreeTypeFont:
    if kai and Path(FONT_KAI).exists():
        return ImageFont.truetype(FONT_KAI, size)
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REGULAR, size)


def canvas(title: str, subtitle: str = "") -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGBA", SIZE, (232, 220, 188, 255))
    draw = ImageDraw.Draw(image)
    draw_paper(draw)
    draw_ink_mountains(draw)
    draw_header(draw, title, subtitle)
    return image, draw


def draw_paper(draw: ImageDraw.ImageDraw) -> None:
    random.seed(42)
    for y in range(SIZE[1]):
        base = 230 - int(y * 0.035)
        draw.line((0, y, SIZE[0], y), fill=(base, base - 12, base - 36, 255))
    for _i in range(1800):
        x = random.randint(0, SIZE[0] - 1)
        y = random.randint(0, SIZE[1] - 1)
        alpha = random.randint(18, 40)
        shade = random.choice([(118, 92, 52), (255, 248, 222), (86, 103, 88)])
        draw.point((x, y), fill=(shade[0], shade[1], shade[2], alpha))


def draw_ink_mountains(draw: ImageDraw.ImageDraw) -> None:
    layers = [
        ((64, 76, 72, 70), 540, 130),
        ((53, 69, 67, 92), 585, 105),
        ((37, 54, 57, 118), 630, 82),
    ]
    for color, base_y, amplitude in layers:
        points = [(0, 720), (0, base_y)]
        for x in range(0, 1320, 80):
            y = base_y - int(math.sin(x / 130) * amplitude * 0.38) - random.randint(0, amplitude)
            points.append((x, y))
        points.extend([(1280, 720), (0, 720)])
        draw.polygon(points, fill=color)
    for x in range(70, 1260, 180):
        draw.arc((x, 95, x + 120, 170), 190, 350, fill=(170, 148, 92, 90), width=2)
        draw.arc((x + 35, 105, x + 170, 180), 190, 350, fill=(170, 148, 92, 72), width=2)


def draw_header(draw: ImageDraw.ImageDraw, title: str, subtitle: str) -> None:
    draw.rectangle((0, 0, 1280, 72), fill=(42, 61, 58, 230))
    draw.rectangle((0, 68, 1280, 72), fill=(159, 42, 34, 230))
    draw.text((30, 16), title, fill=(247, 235, 198, 255), font=font(30, True, True))
    if subtitle:
        draw.text((350, 26), subtitle, fill=(219, 207, 176, 255), font=font(16, False, True))
    draw.text((1062, 24), "山海灵契 v0.2", fill=(219, 207, 176, 255), font=font(16, False, True))


def panel(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], title: str = "") -> None:
    draw.rounded_rectangle(xy, radius=8, fill=(238, 226, 192, 232), outline=(101, 75, 45, 255), width=2)
    draw.rounded_rectangle((xy[0] + 5, xy[1] + 5, xy[2] - 5, xy[3] - 5), radius=6, outline=(190, 153, 78, 155), width=1)
    if title:
        draw.text((xy[0] + 18, xy[1] + 14), title, fill=(55, 63, 55, 255), font=font(21, True, True))
        draw.line((xy[0] + 16, xy[1] + 47, xy[2] - 16, xy[1] + 47), fill=(159, 42, 34, 180), width=2)


def seal(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str = "契") -> None:
    x, y = xy
    draw.rounded_rectangle((x, y, x + 44, y + 44), radius=4, fill=(156, 38, 31, 230), outline=(114, 25, 23, 255), width=2)
    draw.text((x + 10, y + 7), text, fill=(247, 232, 199, 255), font=font(24, True, True))


def button(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, width: int = 240, active: bool = True) -> None:
    x, y = xy
    fill = (151, 47, 36, 245) if active else (150, 139, 112, 205)
    outline = (94, 42, 30, 255) if active else (104, 96, 78, 255)
    draw.rounded_rectangle((x, y, x + width, y + 44), radius=5, fill=fill, outline=outline, width=2)
    draw.text((x + 18, y + 9), text, fill=(252, 238, 203, 255) if active else (89, 87, 76, 255), font=font(18, True, True))


def icon_value(draw: ImageDraw.ImageDraw, xy: tuple[int, int], mark: str, text: str, color: tuple[int, int, int]) -> None:
    x, y = xy
    draw.ellipse((x, y, x + 30, y + 30), fill=color + (230,), outline=(80, 61, 38, 255), width=2)
    draw.text((x + 7, y + 3), mark, fill=(255, 246, 214, 255), font=font(17, True, True))
    draw.text((x + 38, y + 3), text, fill=(57, 62, 54, 255), font=font(17, True, True))


def resource_bar(draw: ImageDraw.ImageDraw, x: int = 736, y: int = 88) -> None:
    icon_value(draw, (x, y), "命", "72/80", (150, 43, 38))
    icon_value(draw, (x + 126, y), "罡", "6", (62, 104, 111))
    icon_value(draw, (x + 204, y), "灵", "3/3", (58, 119, 92))
    icon_value(draw, (x + 310, y), "石", "84", (178, 128, 42))


def talisman_card(draw: ImageDraw.ImageDraw, xy: tuple[int, int], ctype: str, title: str, cost: str, body: str, scale: float = 1.0) -> None:
    x, y = xy
    w = int(116 * scale)
    h = int(166 * scale)
    colors = {
        "attack": (178, 82, 51),
        "defense": (67, 107, 105),
        "skill": (82, 93, 132),
        "support": (97, 132, 78),
        "curse": (75, 58, 82),
    }
    accent = colors.get(ctype, (97, 132, 78))
    draw.rounded_rectangle((x, y, x + w, y + h), radius=7, fill=(244, 230, 192, 255), outline=(92, 63, 39, 255), width=2)
    draw.rectangle((x + 8, y + 8, x + w - 8, y + 38), fill=accent + (230,))
    draw.text((x + 13, y + 12), title, fill=(255, 244, 211, 255), font=font(max(13, int(15 * scale)), True, True))
    if cost:
        draw.ellipse((x + w - 32, y + 9, x + w - 10, y + 31), fill=(216, 174, 80, 255), outline=(91, 61, 38, 255))
        draw.text((x + w - 25, y + 9), cost, fill=(62, 52, 36, 255), font=font(max(12, int(14 * scale)), True))
    draw.line((x + 17, y + 48, x + w - 17, y + 48), fill=accent + (180,), width=2)
    draw.arc((x + 22, y + 55, x + w - 22, y + 104), 200, 340, fill=accent + (190,), width=2)
    draw.line((x + w // 2, y + 54, x + w // 2, y + 105), fill=accent + (150,), width=1)
    line_y = y + int(112 * scale)
    for line in wrap(body, width=max(6, int(8 * scale))):
        draw.text((x + 13, line_y), line, fill=(66, 60, 47, 255), font=font(max(11, int(12 * scale)), False, True))
        line_y += int(18 * scale)


def spirit_node(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, color: tuple[int, int, int], active: bool = False) -> None:
    x, y = xy
    r = 33
    draw.ellipse((x, y, x + r * 2, y + r * 2), fill=color + (230,), outline=(84, 62, 39, 255), width=3)
    if active:
        draw.ellipse((x - 6, y - 6, x + r * 2 + 6, y + r * 2 + 6), outline=(186, 45, 35, 230), width=4)
    draw.arc((x + 12, y + 15, x + 52, y + 48), 210, 330, fill=(255, 239, 205, 230), width=2)
    draw.text((x + 6, y + 72), text, fill=(57, 62, 54, 255), font=font(15, True, True))


def main_menu() -> Image.Image:
    image, draw = canvas("主菜单", "水墨仙途、灵契远征")
    draw.text((88, 126), "WorldSeed", fill=(68, 56, 40, 255), font=font(42, True))
    draw.text((88, 178), "山海灵契", fill=(68, 56, 40, 255), font=font(50, True, True))
    draw.text((92, 270), "一卷山海图，一局问道行。", fill=(96, 84, 64, 255), font=font(22, False, True))
    seal(draw, (355, 175), "山")
    for index, text in enumerate(["新开灵契", "续接旧局", "设置", "退出"]):
        button(draw, (92, 350 + index * 58), text, 282, index != 1)
    panel(draw, (650, 138, 1138, 425), "最近远征")
    draw.text((690, 205), "角色：铁誓者\n境地：腐化矿脉\n所在：灵市\n命元：72/80", fill=(57, 62, 54, 255), font=font(22, False, True), spacing=14)
    draw.arc((800, 295, 1020, 530), 205, 336, fill=(83, 100, 91, 130), width=5)
    draw.text((90, 650), "GameSpec ascension_forge_prototype  /  视觉草案 v0.2", fill=(101, 94, 78, 255), font=font(15))
    return image


def character_select() -> Image.Image:
    image, draw = canvas("角色选择", "选择修行流派与起手法门")
    button(draw, (32, 86), "返回", 110)
    panel(draw, (42, 138, 392, 612), "流派")
    draw.rounded_rectangle((72, 190, 360, 335), radius=8, fill=(226, 207, 163, 210), outline=(156, 39, 31, 255), width=3)
    seal(draw, (92, 218), "罡")
    draw.text((158, 213), "铁誓者\n护体反击\n入门", fill=(55, 63, 55, 255), font=font(23, True, True), spacing=10)
    draw.text((92, 382), "星焰术士\n影缝游侠", fill=(96, 88, 70, 205), font=font(22, False, True), spacing=24)
    panel(draw, (432, 138, 772, 612), "角色详情")
    draw.text((465, 198), "铁誓者", fill=(65, 54, 38, 255), font=font(36, True, True))
    draw.text((465, 258), "命元：80\n流派：护体、创伤、重击\n本命法器：誓约刃\n天赋起点：铁誓起点", fill=(57, 62, 54, 255), font=font(20, False, True), spacing=14)
    button(draw, (465, 520), "开始问道", 230)
    panel(draw, (812, 138, 1212, 612), "起手法门")
    cards = [("attack", "劈山", "1", "造成6伤害"), ("defense", "守势", "1", "获得6罡气"), ("attack", "盾击", "1", "伤害+罡气"), ("skill", "凝神", "0", "抽1张牌")]
    for index, item in enumerate(cards):
        talisman_card(draw, (838 + index * 88, 230), item[0], item[1], item[2], item[3], 0.72)
    draw.text((840, 470), "定位：先聚罡气，再以重击反制。", fill=(57, 62, 54, 255), font=font(18, False, True))
    return image


def map_screen() -> Image.Image:
    image, draw = canvas("灵脉图", "选择下一处灵脉节点")
    resource_bar(draw)
    panel(draw, (36, 126, 302, 612), "洞天信息")
    draw.text((64, 184), "腐化矿脉\n灵脉层数：6\n镇守：活熔炉\n地脉异象：余烬回响", fill=(57, 62, 54, 255), font=font(20, False, True), spacing=14)
    panel(draw, (332, 126, 912, 612), "灵脉路线")
    nodes = [("斗法", (155, 45, 35)), ("奇遇", (88, 104, 119)), ("灵市", (170, 126, 44)), ("斗法", (155, 45, 35)), ("强敌", (107, 74, 118)), ("炉心", (190, 76, 36))]
    coords = []
    for index, item in enumerate(nodes):
        x = 382 + index * 84
        y = 366 - (index % 2) * 82
        coords.append((x, y))
        if index > 0:
            prev = coords[index - 1]
            draw.line((prev[0] + 66, prev[1] + 33, x, y + 33), fill=(96, 114, 96, 170), width=4)
        spirit_node(draw, (x, y), item[0], item[1], index == 0)
    panel(draw, (950, 126, 1228, 612), "当前灵脉")
    spirit_node(draw, (1058, 190), "斗法", (155, 45, 35), True)
    draw.text((985, 323), "node_1 / 普通斗法\n遭遇：锈蚀虫群\n奖励：灵石、法门三选一", fill=(57, 62, 54, 255), font=font(18, False, True), spacing=12)
    button(draw, (990, 510), "进入斗法", 190)
    return image


def combat_screen() -> Image.Image:
    image, draw = canvas("斗法", "以法门出招，观敌意图")
    resource_bar(draw, 742, 88)
    panel(draw, (36, 126, 300, 475), "修士")
    seal(draw, (138, 190), "罡")
    draw.text((72, 305), "铁誓者\n命元 72/80\n护体罡气 6\n抽牌 12  弃牌 3", fill=(57, 62, 54, 255), font=font(18, False, True), spacing=11)
    panel(draw, (340, 126, 922, 475), "敌阵")
    for x, name, hp, mark in [(430, "锈蚀虫", "20/20", "攻"), (650, "锈蚀虫", "14/20", "守")]:
        draw.rounded_rectangle((x, 188, x + 152, 372), radius=8, fill=(231, 213, 175, 235), outline=(96, 70, 42, 255), width=2)
        seal(draw, (x + 54, 213), mark)
        draw.text((x + 34, 278), name, fill=(60, 58, 45, 255), font=font(18, True, True))
        draw.text((x + 34, 313), f"命元 {hp}\n护甲 3", fill=(57, 62, 54, 255), font=font(16, False, True), spacing=8)
    draw.text((548, 410), "术法轨迹、伤害字和状态墨痕显示在战场中央", fill=(96, 88, 70, 255), font=font(16, False, True))
    panel(draw, (950, 126, 1228, 475), "斗法记录")
    draw.text((980, 184), "斗法开始：锈蚀虫群\n施展 劈山：造成 6 伤害\n敌意：攻击 5", fill=(57, 62, 54, 255), font=font(17, False, True), spacing=14)
    button(draw, (1000, 390), "收势回合", 180)
    panel(draw, (36, 505, 1228, 692), "手牌法门")
    cards = [("attack", "劈山", "1", "造成6伤害"), ("defense", "守势", "1", "获得6罡气"), ("attack", "盾击", "1", "伤害5 罡气3"), ("skill", "铁誓反击", "1", "罡气4 下击+3"), ("attack", "星火符", "1", "伤害5 燃烧2")]
    for index, item in enumerate(cards):
        talisman_card(draw, (80 + index * 145, 525), item[0], item[1], item[2], item[3], 0.78)
    return image


def reward_screen() -> Image.Image:
    image, draw = canvas("斗法奖励", "择一法门，沉淀构筑")
    resource_bar(draw)
    panel(draw, (54, 134, 335, 586), "自动收获")
    icon_value(draw, (92, 205), "石", "+22 灵石", (178, 128, 42))
    icon_value(draw, (92, 260), "悟", "+0 悟道点", (83, 122, 92))
    draw.text((92, 338), "牌组：10 张\n辅助：0 张\n法器：誓约刃", fill=(57, 62, 54, 255), font=font(18, False, True), spacing=12)
    panel(draw, (370, 134, 932, 586), "法门三选一")
    cards = [("attack", "盾击", "1", "伤害5 罡气3"), ("skill", "铁誓反击", "1", "罡气4 强化下击"), ("support", "重击符", "0", "嵌入攻击 伤害+3")]
    for index, item in enumerate(cards):
        talisman_card(draw, (412 + index * 165, 222), item[0], item[1], item[2], item[3], 0.95)
    panel(draw, (970, 134, 1220, 586), "操作")
    draw.text((1000, 210), "选择法门后进入构筑。\n符箓辅助会进入库存。", fill=(57, 62, 54, 255), font=font(18, False, True), spacing=12)
    button(draw, (1000, 410), "确认收取", 180)
    button(draw, (1000, 470), "略过法门", 180)
    return image


def build_screen() -> Image.Image:
    image, draw = canvas("构筑洞府", "镶符、换器、悟道")
    resource_bar(draw)
    panel(draw, (36, 126, 230, 650), "页签")
    for index, text in enumerate(["牌组", "符箓插槽", "法器", "天赋"]):
        button(draw, (62, 186 + index * 62), text, 135, index == 1)
    panel(draw, (265, 126, 835, 650), "符箓插槽")
    talisman_card(draw, (300, 196), "attack", "盾击", "1", "伤害5 罡气3", 0.86)
    seal(draw, (462, 246), "空")
    draw.text((528, 255), "攻击符槽", fill=(57, 62, 54, 255), font=font(19, True, True))
    draw.line((420, 280, 462, 268), fill=(159, 42, 34, 190), width=4)
    talisman_card(draw, (300, 418), "attack", "星火符", "1", "伤害5 燃烧2", 0.86)
    seal(draw, (462, 468), "火")
    draw.text((528, 477), "火法符槽", fill=(57, 62, 54, 255), font=font(19, True, True))
    panel(draw, (870, 126, 1228, 650), "可用符箓")
    talisman_card(draw, (910, 188), "support", "重击符", "0", "攻击牌伤害+3", 0.86)
    talisman_card(draw, (1060, 188), "support", "护返符", "0", "使用后罡气+2", 0.86)
    draw.text((912, 463), "右侧显示符箓兼容规则，失败时给出原因。", fill=(57, 62, 54, 255), font=font(17, False, True))
    button(draw, (910, 555), "自动荐符", 140)
    button(draw, (1060, 555), "返回灵脉", 140)
    return image


def event_screen() -> Image.Image:
    image, draw = canvas("奇遇", "山中机缘，取舍有代价")
    resource_bar(draw)
    panel(draw, (70, 142, 470, 586), "奇遇画面")
    draw.arc((180, 248, 350, 430), 205, 335, fill=(64, 79, 72, 220), width=6)
    draw.arc((205, 275, 330, 410), 205, 335, fill=(132, 51, 39, 210), width=4)
    seal(draw, (236, 314), "炉")
    panel(draw, (520, 142, 1210, 586), "破损符文炉")
    draw.text((555, 212), "一座仍有余温的符文炉等待代价。", fill=(57, 62, 54, 255), font=font(24, True, True))
    draw.text((555, 274), "选择会立即结算，并在完成后进入构筑洞府。", fill=(96, 88, 70, 255), font=font(17, False, True))
    button(draw, (560, 350), "献出 8 命元，获得符箓", 360)
    button(draw, (560, 410), "搜刮冷却灵屑，获得 35 灵石", 360)
    button(draw, (560, 470), "离开", 160)
    return image


def shop_screen() -> Image.Image:
    image, draw = canvas("灵市/锻炉", "购买法门、法器和修复命元")
    resource_bar(draw)
    panel(draw, (50, 134, 830, 602), "货架与服务")
    entries = [("support", "重击符", "40 灵石", "攻击法门伤害+3"), ("defense", "合金法衣", "55 灵石", "命元上限+8"), ("skill", "温养命元", "35 灵石", "恢复18命元")]
    for index, item in enumerate(entries):
        x = 96 + index * 230
        talisman_card(draw, (x, 226), item[0], item[1], "", item[3], 0.9)
        draw.text((x + 18, 397), item[2], fill=(86, 62, 35, 255), font=font(17, True, True))
        button(draw, (x, 438), "购买", 135)
    panel(draw, (880, 134, 1218, 602), "掌柜提示")
    seal(draw, (1026, 190), "市")
    draw.text((920, 320), "灵石不足时按钮置灰并提示。\n购买完成后货架刷新状态。", fill=(57, 62, 54, 255), font=font(18, False, True), spacing=12)
    button(draw, (930, 510), "打开构筑", 130)
    button(draw, (1075, 510), "离开", 100)
    return image


def chapter_result_screen() -> Image.Image:
    image, draw = canvas("洞天结算", "镇守已破，择升华奖励")
    panel(draw, (64, 132, 395, 607), "本章战果")
    seal(draw, (180, 210), "胜")
    draw.text((100, 370), "已击败：活熔炉\n胜利斗法：5\n获得法门：4\n造成伤害：286", fill=(57, 62, 54, 255), font=font(19, False, True), spacing=12)
    panel(draw, (435, 132, 910, 607), "升华三选一")
    for index, text in enumerate(["升华：罡气反震", "法器：镶孔戒", "悟道点 +1"]):
        draw.rounded_rectangle((480, 220 + index * 105, 865, 290 + index * 105), radius=8, fill=(227, 205, 161, 235), outline=(154, 42, 34, 255), width=2)
        draw.text((510, 240 + index * 105), text, fill=(57, 62, 54, 255), font=font(23, True, True))
    panel(draw, (950, 132, 1218, 607), "下一步")
    draw.text((980, 214), "MVP 只开放一处洞天。\n后续版本展示下一章地脉预告。", fill=(57, 62, 54, 255), font=font(18, False, True), spacing=12)
    button(draw, (990, 466), "进入结算", 180)
    return image


def run_result_screen() -> Image.Image:
    image, draw = canvas("本局结算", "一局问道的结果")
    panel(draw, (330, 118, 950, 492), "远征完成")
    draw.text((482, 176), "远征完成", fill=(65, 54, 38, 255), font=font(44, True, True))
    draw.text((432, 258), "角色：铁誓者\n洞天：腐化矿脉\n胜利斗法：5\n施展法门：48\n造成伤害：286", fill=(57, 62, 54, 255), font=font(21, False, True), spacing=14)
    panel(draw, (86, 535, 515, 660), "最终牌组摘要")
    draw.text((120, 586), "劈山 x3、守势 x3、盾击、铁誓反击、星火符、重击符", fill=(57, 62, 54, 255), font=font(17, False, True))
    button(draw, (670, 555), "重新问道", 170)
    button(draw, (865, 555), "返回主菜单", 190)
    return image


def settings_popup() -> Image.Image:
    image, draw = canvas("设置弹窗", "覆盖当前界面的竹简弹窗")
    draw.rectangle((0, 72, 1280, 720), fill=(35, 42, 37, 116))
    panel(draw, (330, 130, 950, 612), "设置")
    draw.text((372, 192), "音律    画面    游戏    输入", fill=(57, 62, 54, 255), font=font(23, True, True))
    for index, text in enumerate(["总音量", "乐曲", "音效", "斗法速度"]):
        y = 262 + index * 60
        draw.text((382, y), text, fill=(57, 62, 54, 255), font=font(18, False, True))
        draw.rounded_rectangle((520, y + 6, 820, y + 22), radius=8, fill=(206, 189, 145, 255), outline=(101, 75, 45, 255), width=1)
        draw.rounded_rectangle((520, y + 6, 704, y + 22), radius=8, fill=(154, 42, 34, 255))
    button(draw, (420, 522), "恢复默认", 150)
    button(draw, (600, 522), "应用", 120)
    button(draw, (750, 522), "关闭", 120)
    return image


def detail_popup() -> Image.Image:
    image, draw = canvas("详情弹窗", "法门、法器、天赋共用详情")
    draw.rectangle((0, 72, 1280, 720), fill=(35, 42, 37, 116))
    panel(draw, (255, 106, 1025, 642), "法门详情")
    talisman_card(draw, (320, 190), "attack", "星火符", "1", "造成5伤害。施加2层燃烧。", 1.35)
    draw.text((560, 186), "星火符", fill=(65, 54, 38, 255), font=font(36, True, True))
    draw.text((560, 248), "类型：攻击 / 法术 / 火焰\n费用：1\n目标：单体敌人\n符槽：2", fill=(57, 62, 54, 255), font=font(19, False, True), spacing=12)
    draw.text((560, 374), "关键词说明\n燃烧：敌方回合开始时受到层数伤害，然后层数 -1。\n符箓兼容：可插入 attack、spell 或 fire 标签辅助。", fill=(67, 66, 55, 255), font=font(17, False, True), spacing=10)
    button(draw, (790, 558), "关闭", 120)
    return image


def confirm_popup() -> Image.Image:
    image, draw = canvas("确认弹窗", "防止误操作")
    draw.rectangle((0, 72, 1280, 720), fill=(35, 42, 37, 132))
    panel(draw, (405, 220, 875, 500), "确认操作")
    draw.text((450, 292), "新开灵契会覆盖当前未完成远征。", fill=(57, 62, 54, 255), font=font(23, True, True))
    draw.text((450, 344), "该操作确认后不可撤销。", fill=(96, 88, 70, 255), font=font(18, False, True))
    button(draw, (485, 425), "确认", 120)
    button(draw, (660, 425), "取消", 120)
    return image


def overview(files: list[tuple[str, str]]) -> Image.Image:
    thumb_w, thumb_h = 320, 180
    rows = (len(files) + 3) // 4
    image = Image.new("RGBA", (1280, 92 + rows * 285), (232, 220, 188, 255))
    draw = ImageDraw.Draw(image)
    draw_paper(draw)
    draw.text((28, 22), "WorldSeed 中国风手绘界面总览 v0.2", fill=(65, 54, 38, 255), font=font(34, True))
    seal(draw, (650, 22), "修")
    for index, item in enumerate(files):
        name, filename = item
        x = 28 + index % 4 * 310
        y = 82 + index // 4 * 285
        src = Image.open(OUT / filename).convert("RGBA").resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        image.alpha_composite(src, (x, y))
        draw.rectangle((x, y, x + thumb_w, y + thumb_h), outline=(101, 75, 45, 255), width=1)
        draw.text((x, y + thumb_h + 10), name, fill=(57, 62, 54, 255), font=font(17, True, True))
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
