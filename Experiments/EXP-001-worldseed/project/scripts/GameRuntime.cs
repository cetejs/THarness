using System;
using System.Collections.Generic;
using System.Text.Json.Nodes;

public sealed class GameRuntime
{
    private readonly Random _random = new();
    private GameSpecLoader _spec = new();

    public Dictionary<string, object> Run { get; private set; } = new();
    public Dictionary<string, object> Combat { get; private set; } = new();
    public Dictionary<string, object> PendingReward { get; private set; } = new();
    public string FinalMessage { get; private set; } = "";

    public void Setup(GameSpecLoader spec)
    {
        _spec = spec;
    }

    public void StartNewRun(string characterId)
    {
        var character = _spec.Characters[characterId];
        var chapter = _spec.FirstChapter();
        Run = new Dictionary<string, object>
        {
            ["character_id"] = characterId,
            ["hp"] = GameSpecLoader.GetInt(character, "max_hp", 1),
            ["max_hp"] = GameSpecLoader.GetInt(character, "max_hp", 1),
            ["gold"] = GameSpecLoader.GetInt(GameSpecLoader.GetObject(_spec.Data, "gameplay"), "starting_gold", 0),
            ["deck"] = GameSpecLoader.GetStringList(character, "starting_deck"),
            ["support_inventory"] = new List<string>(),
            ["equipment"] = GameSpecLoader.GetStringList(character, "starting_equipment"),
            ["talents"] = GameSpecLoader.GetStringList(character, "starting_talents"),
            ["talent_points"] = 0,
            ["support_links"] = new Dictionary<string, List<string>>(),
            ["chapter_id"] = GameSpecLoader.GetString(chapter, "id"),
            ["map_node_index"] = 0,
            ["completed_nodes"] = new List<string>(),
            ["stats"] = new Dictionary<string, int>
            {
                ["battles_won"] = 0,
                ["cards_played"] = 0,
                ["damage_dealt"] = 0
            }
        };
        Combat = new Dictionary<string, object>();
        PendingReward = new Dictionary<string, object>();
        FinalMessage = "";
    }

    public JsonObject CurrentChapter()
    {
        return _spec.Chapters.GetValueOrDefault(GetRunString("chapter_id"), new JsonObject());
    }

    public JsonObject CurrentMapProfile()
    {
        return _spec.MapProfiles.GetValueOrDefault(GameSpecLoader.GetString(CurrentChapter(), "map_profile"), new JsonObject());
    }

    public JsonObject CurrentNode()
    {
        var nodes = GameSpecLoader.GetArray(CurrentMapProfile(), "nodes");
        var index = GetRunInt("map_node_index");
        return index < 0 || index >= nodes.Count ? new JsonObject() : GameSpecLoader.AsObject(nodes[index]);
    }

    public void StartCurrentCombat()
    {
        var node = CurrentNode();
        var encounter = _spec.Encounters[GameSpecLoader.GetString(node, "encounter_id")];
        var enemies = new List<Dictionary<string, object>>();
        foreach (var enemyId in GameSpecLoader.GetStringList(encounter, "enemy_ids"))
        {
            var enemy = _spec.Enemies[enemyId];
            enemies.Add(new Dictionary<string, object>
            {
                ["id"] = enemyId,
                ["hp"] = GameSpecLoader.GetInt(enemy, "max_hp", 1),
                ["max_hp"] = GameSpecLoader.GetInt(enemy, "max_hp", 1),
                ["armor"] = 0,
                ["status"] = new Dictionary<string, int>(),
                ["intent_index"] = 0
            });
        }

        var drawPile = new List<string>(GetRunStringList("deck"));
        Shuffle(drawPile);
        Combat = new Dictionary<string, object>
        {
            ["encounter_id"] = GameSpecLoader.GetString(encounter, "id"),
            ["tier"] = GameSpecLoader.GetString(encounter, "tier", "normal"),
            ["reward_pool"] = GameSpecLoader.GetString(encounter, "reward_pool"),
            ["turn"] = 1,
            ["energy"] = GameSpecLoader.GetInt(GameSpecLoader.GetObject(_spec.Data, "gameplay"), "starting_energy", 3),
            ["armor"] = 0,
            ["draw_pile"] = drawPile,
            ["hand"] = new List<string>(),
            ["discard_pile"] = new List<string>(),
            ["exhaust_pile"] = new List<string>(),
            ["enemies"] = enemies,
            ["next_attack_bonus"] = 0,
            ["log"] = new List<string>()
        };
        DrawCards(GameSpecLoader.GetInt(GameSpecLoader.GetObject(_spec.Data, "gameplay"), "cards_drawn_per_turn", 5));
        Log("斗法开始: " + GameSpecLoader.GetString(encounter, "display_name", "遭遇"));
    }

    public void DrawCards(int amount)
    {
        for (var i = 0; i < amount; i++)
        {
            var hand = GetCombatStringList("hand");
            if (hand.Count >= GameSpecLoader.GetInt(GameSpecLoader.GetObject(_spec.Data, "gameplay"), "max_hand_size", 10))
            {
                return;
            }

            var drawPile = GetCombatStringList("draw_pile");
            if (drawPile.Count == 0)
            {
                drawPile.AddRange(GetCombatStringList("discard_pile"));
                GetCombatStringList("discard_pile").Clear();
                Shuffle(drawPile);
            }

            if (drawPile.Count == 0)
            {
                return;
            }

            var lastIndex = drawPile.Count - 1;
            hand.Add(drawPile[lastIndex]);
            drawPile.RemoveAt(lastIndex);
        }
    }

    public string PlayCard(int cardIndex, int enemyIndex = 0)
    {
        var hand = GetCombatStringList("hand");
        if (cardIndex < 0 || cardIndex >= hand.Count)
        {
            return "无效法门。";
        }

        var cardId = hand[cardIndex];
        var card = _spec.Cards[cardId];
        var cost = GameSpecLoader.GetInt(card, "cost");
        if (GetCombatInt("energy") < cost)
        {
            return "灵力不足。";
        }

        if (GameSpecLoader.GetString(card, "target_rule", "self") == "single_enemy" && FirstAliveEnemyIndex() == -1)
        {
            return "没有可用目标。";
        }

        Combat["energy"] = GetCombatInt("energy") - cost;
        ApplyCard(card, enemyIndex);
        hand.RemoveAt(cardIndex);
        if (GameSpecLoader.GetString(card, "type") != "curse")
        {
            GetCombatStringList("discard_pile").Add(cardId);
        }

        GetStats()["cards_played"] += 1;
        if (AllEnemiesDead())
        {
            FinishCombat();
        }
        return "";
    }

    public void EndTurn()
    {
        GetCombatStringList("discard_pile").AddRange(GetCombatStringList("hand"));
        GetCombatStringList("hand").Clear();
        foreach (var enemyState in GetCombatEnemies())
        {
            if (GetStateInt(enemyState, "hp") <= 0)
            {
                continue;
            }

            ApplyEnemyStatus(enemyState);
            if (GetStateInt(enemyState, "hp") <= 0)
            {
                continue;
            }

            EnemyAction(enemyState);
        }

        if (GetRunInt("hp") <= 0)
        {
            FinalMessage = "问道失败。";
            return;
        }

        Combat["turn"] = GetCombatInt("turn") + 1;
        Combat["energy"] = GameSpecLoader.GetInt(GameSpecLoader.GetObject(_spec.Data, "gameplay"), "starting_energy", 3);
        if (GameSpecLoader.GetObject(_spec.Data, "gameplay").TryGetPropertyValue("armor_clears_each_turn", out var armorClears) && armorClears != null && armorClears.GetValue<bool>())
        {
            Combat["armor"] = 0;
        }
        DrawCards(GameSpecLoader.GetInt(GameSpecLoader.GetObject(_spec.Data, "gameplay"), "cards_drawn_per_turn", 5));
        Log("第 " + GetCombatInt("turn") + " 回合开始");
        if (AllEnemiesDead())
        {
            FinishCombat();
        }
    }

    public void ClaimCard(string cardId)
    {
        if (string.IsNullOrEmpty(cardId))
        {
            return;
        }

        var card = _spec.Cards.GetValueOrDefault(cardId, new JsonObject());
        if (GameSpecLoader.GetString(card, "type") == "support")
        {
            GetRunStringList("support_inventory").Add(cardId);
        }
        else
        {
            GetRunStringList("deck").Add(cardId);
        }
        ClaimRewardBasics();
    }

    public void ClaimEquipment(string equipmentId)
    {
        var equipment = GetRunStringList("equipment");
        if (!string.IsNullOrEmpty(equipmentId) && !equipment.Contains(equipmentId))
        {
            equipment.Add(equipmentId);
        }
        ClaimRewardBasics();
    }

    public void SkipReward()
    {
        ClaimRewardBasics();
    }

    public void ResolveEvent(int choiceIndex)
    {
        var eventData = _spec.Events[GameSpecLoader.GetString(CurrentNode(), "event_id")];
        var choices = GameSpecLoader.GetArray(eventData, "choices");
        if (choiceIndex < 0 || choiceIndex >= choices.Count)
        {
            return;
        }

        var choice = GameSpecLoader.AsObject(choices[choiceIndex]);
        var cost = GameSpecLoader.GetObject(choice, "cost");
        Run["hp"] = Math.Max(1, GetRunInt("hp") - GameSpecLoader.GetInt(cost, "hp"));
        Run["gold"] = Math.Max(0, GetRunInt("gold") - GameSpecLoader.GetInt(cost, "gold"));
        foreach (var reward in GameSpecLoader.GetArray(choice, "rewards"))
        {
            ApplyDirectReward(GameSpecLoader.AsObject(reward));
        }
        AdvanceMap();
    }

    public string BuyService(int serviceIndex)
    {
        var shop = _spec.Shops[GameSpecLoader.GetString(CurrentNode(), "shop_id")];
        var services = GameSpecLoader.GetArray(shop, "services");
        if (serviceIndex < 0 || serviceIndex >= services.Count)
        {
            return "无效服务。";
        }

        var service = GameSpecLoader.AsObject(services[serviceIndex]);
        var price = GameSpecLoader.GetInt(service, "price");
        if (GetRunInt("gold") < price)
        {
            return "灵石不足。";
        }

        Run["gold"] = GetRunInt("gold") - price;
        ApplyDirectReward(GameSpecLoader.GetObject(service, "reward"));
        return "交易完成。";
    }

    public void LeaveShop()
    {
        AdvanceMap();
    }

    public string LinkFirstSupport()
    {
        var inventory = GetRunStringList("support_inventory");
        if (inventory.Count == 0)
        {
            return "没有可嵌入的符箓。";
        }

        var supportId = inventory[0];
        var support = _spec.Cards[supportId];
        foreach (var cardId in GetRunStringList("deck"))
        {
            var card = _spec.Cards[cardId];
            if (!SupportCompatible(card, support))
            {
                continue;
            }

            var links = GetSupportLinks();
            if (!links.TryGetValue(cardId, out var current))
            {
                current = new List<string>();
                links[cardId] = current;
            }

            if (current.Count >= GameSpecLoader.GetInt(card, "support_slots"))
            {
                continue;
            }

            current.Add(supportId);
            inventory.Remove(supportId);
            return "已把 " + GameSpecLoader.GetString(support, "display_name", supportId) + " 嵌入 " + GameSpecLoader.GetString(card, "display_name", cardId);
        }
        return "没有标签兼容的法门。";
    }

    public string UnlockNextTalent()
    {
        if (GetRunInt("talent_points") <= 0)
        {
            return "没有悟道点。";
        }

        var talents = GetRunStringList("talents");
        foreach (var pair in _spec.Talents)
        {
            if (talents.Contains(pair.Key))
            {
                continue;
            }

            var ready = true;
            foreach (var required in GameSpecLoader.GetStringList(pair.Value, "requires"))
            {
                if (!talents.Contains(required))
                {
                    ready = false;
                }
            }

            if (!ready)
            {
                continue;
            }

            talents.Add(pair.Key);
            Run["talent_points"] = GetRunInt("talent_points") - 1;
            return "已参悟: " + GameSpecLoader.GetString(pair.Value, "display_name", pair.Key);
        }
        return "没有可参悟节点。";
    }

    public void AdvanceMap()
    {
        GetRunStringList("completed_nodes").Add(GameSpecLoader.GetString(CurrentNode(), "id"));
        Run["map_node_index"] = GetRunInt("map_node_index") + 1;
        if (GetRunInt("map_node_index") >= GameSpecLoader.GetArray(CurrentMapProfile(), "nodes").Count)
        {
            FinalMessage = "洞天完成。";
        }
    }

    public void FinishChapter()
    {
        FinalMessage = "你镇压了洞天镇守，问道完成。";
    }

    public int GetRunInt(string key)
    {
        return Run.TryGetValue(key, out var value) ? Convert.ToInt32(value) : 0;
    }

    public string GetRunString(string key)
    {
        return Run.TryGetValue(key, out var value) ? Convert.ToString(value) ?? "" : "";
    }

    public int GetCombatInt(string key)
    {
        return Combat.TryGetValue(key, out var value) ? Convert.ToInt32(value) : 0;
    }

    public string GetCombatString(string key)
    {
        return Combat.TryGetValue(key, out var value) ? Convert.ToString(value) ?? "" : "";
    }

    public List<string> GetRunStringList(string key)
    {
        if (!Run.TryGetValue(key, out var value) || value is not List<string> list)
        {
            list = new List<string>();
            Run[key] = list;
        }
        return list;
    }

    public List<string> GetCombatStringList(string key)
    {
        if (!Combat.TryGetValue(key, out var value) || value is not List<string> list)
        {
            list = new List<string>();
            Combat[key] = list;
        }
        return list;
    }

    public List<Dictionary<string, object>> GetCombatEnemies()
    {
        if (!Combat.TryGetValue("enemies", out var value) || value is not List<Dictionary<string, object>> list)
        {
            list = new List<Dictionary<string, object>>();
            Combat["enemies"] = list;
        }
        return list;
    }

    public List<string> PendingCardChoices()
    {
        return PendingReward.TryGetValue("card_choices", out var value) && value is List<string> list ? list : new List<string>();
    }

    public List<string> PendingEquipmentChoices()
    {
        return PendingReward.TryGetValue("equipment_choices", out var value) && value is List<string> list ? list : new List<string>();
    }

    public int PendingInt(string key)
    {
        return PendingReward.TryGetValue(key, out var value) ? Convert.ToInt32(value) : 0;
    }

    public List<string> CombatLog()
    {
        if (!Combat.TryGetValue("log", out var value) || value is not List<string> list)
        {
            list = new List<string>();
            Combat["log"] = list;
        }
        return list;
    }

    public Dictionary<string, List<string>> GetSupportLinks()
    {
        if (!Run.TryGetValue("support_links", out var value) || value is not Dictionary<string, List<string>> links)
        {
            links = new Dictionary<string, List<string>>();
            Run["support_links"] = links;
        }
        return links;
    }

    private void ApplyCard(JsonObject card, int enemyIndex)
    {
        var targetIndex = enemyIndex;
        if (targetIndex < 0 || targetIndex >= GetCombatEnemies().Count || GetStateInt(GetCombatEnemies()[targetIndex], "hp") <= 0)
        {
            targetIndex = FirstAliveEnemyIndex();
        }

        foreach (var effect in GameSpecLoader.GetArray(card, "effects"))
        {
            ApplyEffect(GameSpecLoader.AsObject(effect), card, targetIndex);
        }
        ApplySupports(card, targetIndex);
        Log("施展 " + GameSpecLoader.GetString(card, "display_name", GameSpecLoader.GetString(card, "id")));
    }

    private void ApplySupports(JsonObject card, int targetIndex)
    {
        foreach (var supportId in GetSupportLinks().GetValueOrDefault(GameSpecLoader.GetString(card, "id"), new List<string>()))
        {
            var support = _spec.Cards.GetValueOrDefault(supportId, new JsonObject());
            foreach (var effect in GameSpecLoader.GetArray(support, "effects"))
            {
                ApplyEffect(GameSpecLoader.AsObject(effect), card, targetIndex);
            }
        }
    }

    private void ApplyEffect(JsonObject effect, JsonObject sourceCard, int targetIndex)
    {
        switch (GameSpecLoader.GetString(effect, "type"))
        {
            case "damage":
                DamageEnemy(targetIndex, GameSpecLoader.GetInt(effect, "amount") + CardDamageBonus(sourceCard));
                break;
            case "gain_armor":
                Combat["armor"] = GetCombatInt("armor") + GameSpecLoader.GetInt(effect, "amount") + CardArmorBonus(sourceCard);
                break;
            case "draw_cards":
                DrawCards(GameSpecLoader.GetInt(effect, "amount"));
                break;
            case "apply_status":
                ApplyStatusToEnemy(targetIndex, GameSpecLoader.GetString(effect, "status"), GameSpecLoader.GetInt(effect, "amount"));
                break;
            case "next_attack_bonus":
                Combat["next_attack_bonus"] = GetCombatInt("next_attack_bonus") + GameSpecLoader.GetInt(effect, "amount");
                break;
            case "modify_damage":
                DamageEnemy(targetIndex, GameSpecLoader.GetInt(effect, "amount"));
                break;
            case "gain_armor_after_use":
                Combat["armor"] = GetCombatInt("armor") + GameSpecLoader.GetInt(effect, "amount");
                break;
            case "modify_status_amount":
                ApplyStatusToEnemy(targetIndex, GameSpecLoader.GetString(effect, "status"), GameSpecLoader.GetInt(effect, "amount"));
                break;
        }
    }

    private void DamageEnemy(int enemyIndex, int amount)
    {
        if (enemyIndex < 0)
        {
            return;
        }

        var enemyState = GetCombatEnemies()[enemyIndex];
        var blocked = Math.Min(GetStateInt(enemyState, "armor"), amount);
        enemyState["armor"] = GetStateInt(enemyState, "armor") - blocked;
        var finalDamage = amount - blocked + GetCombatInt("next_attack_bonus");
        Combat["next_attack_bonus"] = 0;
        enemyState["hp"] = Math.Max(0, GetStateInt(enemyState, "hp") - finalDamage);
        GetStats()["damage_dealt"] += finalDamage;
    }

    private void ApplyStatusToEnemy(int enemyIndex, string statusId, int amount)
    {
        if (enemyIndex < 0 || string.IsNullOrEmpty(statusId))
        {
            return;
        }

        var status = GetStatus(GetCombatEnemies()[enemyIndex]);
        status[statusId] = status.GetValueOrDefault(statusId) + amount;
    }

    private void ApplyEnemyStatus(Dictionary<string, object> enemyState)
    {
        var status = GetStatus(enemyState);
        var burn = status.GetValueOrDefault("burn");
        if (burn <= 0)
        {
            return;
        }

        enemyState["hp"] = Math.Max(0, GetStateInt(enemyState, "hp") - burn);
        status["burn"] = Math.Max(0, burn - 1);
    }

    private void EnemyAction(Dictionary<string, object> enemyState)
    {
        var enemy = _spec.Enemies[GetStateString(enemyState, "id")];
        var intents = GameSpecLoader.GetArray(enemy, "intents");
        if (intents.Count == 0)
        {
            return;
        }

        var index = GetStateInt(enemyState, "intent_index") % intents.Count;
        var intent = GameSpecLoader.AsObject(intents[index]);
        enemyState["intent_index"] = index + 1;
        switch (GameSpecLoader.GetString(intent, "type"))
        {
            case "damage":
                DamagePlayer(GameSpecLoader.GetInt(intent, "amount"));
                break;
            case "gain_armor":
                enemyState["armor"] = GetStateInt(enemyState, "armor") + GameSpecLoader.GetInt(intent, "amount");
                break;
            case "apply_status":
                DamagePlayer(GameSpecLoader.GetInt(intent, "amount"));
                Log(GameSpecLoader.GetString(enemy, "display_name", "敌人") + " 施加 " + GameSpecLoader.GetString(intent, "status", "状态"));
                break;
        }
    }

    private void DamagePlayer(int amount)
    {
        var blocked = Math.Min(GetCombatInt("armor"), amount);
        Combat["armor"] = GetCombatInt("armor") - blocked;
        Run["hp"] = Math.Max(0, GetRunInt("hp") - (amount - blocked));
    }

    private void FinishCombat()
    {
        GetStats()["battles_won"] += 1;
        PendingReward = BuildReward(GetCombatString("reward_pool"));
        Log("斗法胜利");
    }

    private Dictionary<string, object> BuildReward(string poolId)
    {
        var pool = _spec.RewardPools.GetValueOrDefault(poolId, new JsonObject());
        return new Dictionary<string, object>
        {
            ["pool_id"] = poolId,
            ["gold"] = GameSpecLoader.GetInt(pool, "gold_min"),
            ["card_choices"] = GameSpecLoader.GetStringList(pool, "card_choices"),
            ["equipment_choices"] = GameSpecLoader.GetStringList(pool, "equipment_choices"),
            ["talent_points"] = GameSpecLoader.GetInt(pool, "talent_points")
        };
    }

    private void ClaimRewardBasics()
    {
        Run["gold"] = GetRunInt("gold") + PendingInt("gold");
        Run["talent_points"] = GetRunInt("talent_points") + PendingInt("talent_points");
        PendingReward = new Dictionary<string, object>();
        AdvanceMap();
    }

    private void ApplyDirectReward(JsonObject reward)
    {
        switch (GameSpecLoader.GetString(reward, "type"))
        {
            case "card":
                var cardId = GameSpecLoader.GetString(reward, "card_id");
                var card = _spec.Cards.GetValueOrDefault(cardId, new JsonObject());
                if (GameSpecLoader.GetString(card, "type") == "support")
                {
                    GetRunStringList("support_inventory").Add(cardId);
                }
                else if (!string.IsNullOrEmpty(cardId))
                {
                    GetRunStringList("deck").Add(cardId);
                }
                break;
            case "equipment":
                var equipmentId = GameSpecLoader.GetString(reward, "equipment_id");
                var equipment = GetRunStringList("equipment");
                if (!string.IsNullOrEmpty(equipmentId) && !equipment.Contains(equipmentId))
                {
                    equipment.Add(equipmentId);
                }
                break;
            case "gold":
                Run["gold"] = GetRunInt("gold") + GameSpecLoader.GetInt(reward, "amount");
                break;
            case "heal":
                Run["hp"] = Math.Min(GetRunInt("max_hp"), GetRunInt("hp") + GameSpecLoader.GetInt(reward, "amount"));
                break;
        }
    }

    private bool SupportCompatible(JsonObject card, JsonObject support)
    {
        foreach (var tag in GameSpecLoader.GetStringList(support, "compatible_tags"))
        {
            if (GameSpecLoader.GetStringList(card, "tags").Contains(tag))
            {
                return true;
            }
        }
        return false;
    }

    private int CardDamageBonus(JsonObject card)
    {
        var bonus = 0;
        foreach (var equipmentId in GetRunStringList("equipment"))
        {
            var item = _spec.Equipment.GetValueOrDefault(equipmentId, new JsonObject());
            foreach (var effect in GameSpecLoader.GetArray(item, "effects"))
            {
                var obj = GameSpecLoader.AsObject(effect);
                if (GameSpecLoader.GetString(obj, "type") == "tag_damage_bonus" && GameSpecLoader.GetStringList(card, "tags").Contains(GameSpecLoader.GetString(obj, "tag")))
                {
                    bonus += GameSpecLoader.GetInt(obj, "amount");
                }
            }
        }
        return bonus;
    }

    private int CardArmorBonus(JsonObject card)
    {
        var bonus = 0;
        foreach (var talentId in GetRunStringList("talents"))
        {
            var talent = _spec.Talents.GetValueOrDefault(talentId, new JsonObject());
            foreach (var effect in GameSpecLoader.GetArray(talent, "effects"))
            {
                var obj = GameSpecLoader.AsObject(effect);
                if (GameSpecLoader.GetString(obj, "type") == "tag_armor_bonus" && GameSpecLoader.GetStringList(card, "tags").Contains(GameSpecLoader.GetString(obj, "tag")))
                {
                    bonus += GameSpecLoader.GetInt(obj, "amount");
                }
            }
        }
        return bonus;
    }

    private int FirstAliveEnemyIndex()
    {
        for (var index = 0; index < GetCombatEnemies().Count; index++)
        {
            if (GetStateInt(GetCombatEnemies()[index], "hp") > 0)
            {
                return index;
            }
        }
        return -1;
    }

    private bool AllEnemiesDead()
    {
        return FirstAliveEnemyIndex() == -1;
    }

    private void Log(string message)
    {
        var log = CombatLog();
        log.Add(message);
        if (log.Count > 8)
        {
            log.RemoveAt(0);
        }
    }

    private Dictionary<string, int> GetStats()
    {
        return Run.TryGetValue("stats", out var value) && value is Dictionary<string, int> stats ? stats : new Dictionary<string, int>();
    }

    private static int GetStateInt(Dictionary<string, object> state, string key)
    {
        return state.TryGetValue(key, out var value) ? Convert.ToInt32(value) : 0;
    }

    private static string GetStateString(Dictionary<string, object> state, string key)
    {
        return state.TryGetValue(key, out var value) ? Convert.ToString(value) ?? "" : "";
    }

    private static Dictionary<string, int> GetStatus(Dictionary<string, object> state)
    {
        if (!state.TryGetValue("status", out var value) || value is not Dictionary<string, int> status)
        {
            status = new Dictionary<string, int>();
            state["status"] = status;
        }
        return status;
    }

    private void Shuffle(List<string> items)
    {
        for (var index = items.Count - 1; index > 0; index--)
        {
            var other = _random.Next(index + 1);
            (items[index], items[other]) = (items[other], items[index]);
        }
    }
}
