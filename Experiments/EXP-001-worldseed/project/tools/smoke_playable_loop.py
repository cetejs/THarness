from __future__ import annotations

import json
from pathlib import Path


SPEC_PATH = Path("data/game_spec/ascension_forge.prototype.json")


def by_id(items: list[dict]) -> dict[str, dict]:
    return {item["id"]: item for item in items}


def main() -> int:
    spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    characters = by_id(spec["characters"])
    encounters = by_id(spec["encounters"])
    events = by_id(spec["events"])
    shops = by_id(spec["shops"])
    chapters = by_id(spec["chapters"])
    profiles = by_id(spec["map_generation"]["profiles"])
    rewards = by_id(spec["rewards"]["pools"])

    character = next(iter(characters.values()))
    if not character["starting_deck"]:
        print("失败: 初始牌组为空")
        return 1

    chapter = next(iter(chapters.values()))
    profile = profiles[chapter["map_profile"]]
    required_node_types = {"normal", "event", "shop", "elite", "boss"}
    seen_node_types: set[str] = set()

    for node in profile["nodes"]:
        node_type = node["type"]
        seen_node_types.add(node_type)
        if node_type in {"normal", "elite", "boss"}:
            encounter = encounters[node["encounter_id"]]
            if not encounter["enemy_ids"]:
                print(f"失败: 遭遇 {encounter['id']} 没有敌人")
                return 1
            if encounter["reward_pool"] not in rewards:
                print(f"失败: 遭遇 {encounter['id']} 奖励池不存在")
                return 1
        elif node_type == "event":
            event = events[node["event_id"]]
            if not event["choices"]:
                print(f"失败: 事件 {event['id']} 没有选项")
                return 1
        elif node_type == "shop":
            shop = shops[node["shop_id"]]
            if not shop["services"]:
                print(f"失败: 商店 {shop['id']} 没有服务")
                return 1

    missing = required_node_types - seen_node_types
    if missing:
        print("失败: 地图缺少节点类型 " + ", ".join(sorted(missing)))
        return 1

    print("playable-loop smoke: PASS")
    print(f"character={character['id']} chapter={chapter['id']} nodes={len(profile['nodes'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
