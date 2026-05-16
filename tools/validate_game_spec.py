from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT_KEYS = [
    "meta",
    "gameplay",
    "assets",
    "ui_flow",
    "tags",
    "status_effects",
    "characters",
    "cards",
    "equipment",
    "affixes",
    "talents",
    "enemies",
    "encounters",
    "events",
    "shops",
    "map_generation",
    "chapters",
    "rewards",
    "save_fields",
]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def index_by_id(items: list[dict], section: str, errors: list[str]) -> dict[str, dict]:
    result: dict[str, dict] = {}
    for index, item in enumerate(items):
        item_id = item.get("id")
        if not item_id:
            errors.append(f"{section}[{index}] 缺少 id")
            continue
        if item_id in result:
            errors.append(f"{section} 存在重复 id: {item_id}")
        result[item_id] = item
    return result


def collect_asset_paths(value: object) -> list[str]:
    if isinstance(value, str):
        return [value] if value.startswith("res://") else []
    if isinstance(value, list):
        paths: list[str] = []
        for item in value:
            paths.extend(collect_asset_paths(item))
        return paths
    if isinstance(value, dict):
        paths: list[str] = []
        for item in value.values():
            paths.extend(collect_asset_paths(item))
        return paths
    return []


def validate(spec: dict, project_root: Path) -> list[str]:
    errors: list[str] = []
    for key in ROOT_KEYS:
        if key not in spec:
            errors.append(f"根节点缺少字段: {key}")
    if errors:
        return errors

    tags = index_by_id(spec["tags"], "tags", errors)
    statuses = index_by_id(spec["status_effects"], "status_effects", errors)
    cards = index_by_id(spec["cards"], "cards", errors)
    equipment = index_by_id(spec["equipment"], "equipment", errors)
    talents = index_by_id(spec["talents"], "talents", errors)
    enemies = index_by_id(spec["enemies"], "enemies", errors)
    encounters = index_by_id(spec["encounters"], "encounters", errors)
    events = index_by_id(spec["events"], "events", errors)
    shops = index_by_id(spec["shops"], "shops", errors)
    chapters = index_by_id(spec["chapters"], "chapters", errors)
    profiles = index_by_id(spec["map_generation"].get("profiles", []), "map_profiles", errors)
    reward_pools = index_by_id(spec["rewards"].get("pools", []), "reward_pools", errors)
    screens = index_by_id(spec["ui_flow"].get("screens", []), "ui_screens", errors)

    for transition in spec["ui_flow"].get("transitions", []):
        if transition.get("from") not in screens:
            errors.append(f"UI 跳转来源不存在: {transition}")
        if transition.get("to") not in screens:
            errors.append(f"UI 跳转目标不存在: {transition}")

    for card in cards.values():
        for tag in card.get("tags", []):
            if tag not in tags:
                errors.append(f"卡牌 {card['id']} 引用未知标签: {tag}")
        for tag in card.get("compatible_tags", []):
            if tag not in tags:
                errors.append(f"辅助卡 {card['id']} 引用未知兼容标签: {tag}")
        for effect in card.get("effects", []):
            status = effect.get("status")
            if status and status not in statuses:
                errors.append(f"卡牌 {card['id']} 引用未知状态: {status}")

    for character in spec["characters"]:
        for card_id in character.get("starting_deck", []):
            if card_id not in cards:
                errors.append(f"角色 {character['id']} 初始牌不存在: {card_id}")
        for equipment_id in character.get("starting_equipment", []):
            if equipment_id not in equipment:
                errors.append(f"角色 {character['id']} 初始装备不存在: {equipment_id}")
        for talent_id in character.get("starting_talents", []):
            if talent_id not in talents:
                errors.append(f"角色 {character['id']} 初始天赋不存在: {talent_id}")

    for talent in talents.values():
        for required in talent.get("requires", []):
            if required not in talents:
                errors.append(f"天赋 {talent['id']} 前置不存在: {required}")
        for effect in talent.get("effects", []):
            status = effect.get("status")
            if status and status not in statuses:
                errors.append(f"天赋 {talent['id']} 引用未知状态: {status}")

    for encounter in encounters.values():
        for enemy_id in encounter.get("enemy_ids", []):
            if enemy_id not in enemies:
                errors.append(f"遭遇 {encounter['id']} 敌人不存在: {enemy_id}")
        if encounter.get("reward_pool") not in reward_pools:
            errors.append(f"遭遇 {encounter['id']} 奖励池不存在: {encounter.get('reward_pool')}")

    for profile in profiles.values():
        for node in profile.get("nodes", []):
            if node.get("type") in {"normal", "elite", "boss"} and node.get("encounter_id") not in encounters:
                errors.append(f"地图节点 {node.get('id')} 遭遇不存在: {node.get('encounter_id')}")
            if node.get("type") == "event" and node.get("event_id") not in events:
                errors.append(f"地图节点 {node.get('id')} 事件不存在: {node.get('event_id')}")
            if node.get("type") in {"shop", "forge"} and node.get("shop_id") not in shops:
                errors.append(f"地图节点 {node.get('id')} 商店不存在: {node.get('shop_id')}")

    for chapter in chapters.values():
        if chapter.get("map_profile") not in profiles:
            errors.append(f"章节 {chapter['id']} 地图配置不存在: {chapter.get('map_profile')}")
        if chapter.get("boss_encounter_id") not in encounters:
            errors.append(f"章节 {chapter['id']} Boss 遭遇不存在: {chapter.get('boss_encounter_id')}")

    for pool in reward_pools.values():
        for card_id in pool.get("card_choices", []):
            if card_id not in cards:
                errors.append(f"奖励池 {pool['id']} 卡牌不存在: {card_id}")
        for equipment_id in pool.get("equipment_choices", []):
            if equipment_id not in equipment:
                errors.append(f"奖励池 {pool['id']} 装备不存在: {equipment_id}")

    for asset_path in collect_asset_paths(spec["assets"]):
        local = project_root / asset_path.replace("res://", "")
        if not local.exists():
            errors.append(f"素材不存在: {asset_path}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="验证 WorldSeed GameSpec 数据和素材引用。")
    parser.add_argument("spec", type=Path)
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    try:
        spec = load_json(args.spec)
    except Exception as exc:
        print(f"读取失败: {exc}", file=sys.stderr)
        return 1

    errors = validate(spec, args.project_root)
    if errors:
        print("GameSpec 验证失败:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("GameSpec 验证通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
