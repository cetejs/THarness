using System;
using System.Collections.Generic;
using System.Text.Json.Nodes;
using Godot;

public partial class Main : Control
{
    private readonly GameSpecLoader _spec = new();
    private readonly GameRuntime _runtime = new();
    private VBoxContainer _rootBox = new();
    private VBoxContainer _contentBox = new();
    private Label _infoLabel = new();
    private Label _messageLabel = new();
    private ColorRect _flashOverlay = new();
    private string _lastMessage = "";
    private string _returnScreen = "main_menu";
    private bool _debugLayoutLogs = true;
    private int _layoutCardLogs;

    public override void _Ready()
    {
        FitRootToViewport();
        GetViewport().SizeChanged += FitRootToViewport;
        if (!_spec.LoadSpec())
        {
            ShowBootError();
            return;
        }

        _debugLayoutLogs = _spec.UiBool("debug_layout_logs", true);
        _runtime.Setup(_spec);
        BuildBase();
        LogUi("ready viewport=" + GetViewportRect().Size + " window=" + DisplayServer.WindowGetSize() + " root=" + Size);
        ShowMainMenu();
    }

    private void FitRootToViewport()
    {
        SetAnchorsPreset(LayoutPreset.FullRect);
        OffsetLeft = 0;
        OffsetTop = 0;
        OffsetRight = 0;
        OffsetBottom = 0;
        Position = Vector2.Zero;
        LogUi("viewport_changed viewport=" + GetViewportRect().Size + " window=" + DisplayServer.WindowGetSize() + " root=" + Size);
    }

    private void BuildBase()
    {
        AddBackgroundLayer();

        _rootBox = new VBoxContainer();
        _rootBox.SetAnchorsPreset(LayoutPreset.FullRect);
        _rootBox.AddThemeConstantOverride("separation", UiInt("content_spacing"));
        _rootBox.OffsetLeft = UiFloat("window_margin");
        _rootBox.OffsetTop = 14;
        _rootBox.OffsetRight = -UiFloat("window_margin");
        _rootBox.OffsetBottom = -18;
        AddChild(_rootBox);

        _infoLabel = NewLabel("", UiInt("small_font_size"));
        _rootBox.AddChild(_infoLabel);

        _messageLabel = NewLabel("", UiInt("small_font_size"));
        _messageLabel.AddThemeColorOverride("font_color", ColorCinnabar());
        _rootBox.AddChild(_messageLabel);

        _contentBox = new VBoxContainer();
        _contentBox.SizeFlagsHorizontal = SizeFlags.ExpandFill;
        _contentBox.SizeFlagsVertical = SizeFlags.ExpandFill;
        _contentBox.AddThemeConstantOverride("separation", UiInt("content_spacing"));
        _rootBox.AddChild(_contentBox);

        _flashOverlay = new ColorRect();
        _flashOverlay.Color = _spec.UiColor("feedback_flash_color");
        _flashOverlay.SetAnchorsPreset(LayoutPreset.FullRect);
        _flashOverlay.MouseFilter = MouseFilterEnum.Ignore;
        _flashOverlay.Visible = false;
        AddChild(_flashOverlay);
        LogUi("base root_box=" + _rootBox.Size + " content=" + _contentBox.Size);
    }

    private void AddBackgroundLayer()
    {
        var ui = _spec.GetAssetSection("ui");
        var backgroundPath = GameSpecLoader.GetString(ui, "background");
        var texture = LoadBackgroundTexture(backgroundPath);
        if (texture != null)
        {
            var background = new TextureRect();
            background.Texture = texture;
            background.SetAnchorsPreset(LayoutPreset.FullRect);
            background.ExpandMode = TextureRect.ExpandModeEnum.IgnoreSize;
            background.StretchMode = TextureRect.StretchModeEnum.KeepAspectCovered;
            background.MouseFilter = MouseFilterEnum.Ignore;
            AddChild(background);
            return;
        }

        var fallback = new ColorRect();
        fallback.Color = _spec.UiColor("background_color");
        fallback.SetAnchorsPreset(LayoutPreset.FullRect);
        fallback.MouseFilter = MouseFilterEnum.Ignore;
        AddChild(fallback);
    }

    private Texture2D LoadBackgroundTexture(string path)
    {
        if (string.IsNullOrEmpty(path))
        {
            return null;
        }

        if (ResourceLoader.Exists(path, "Texture2D"))
        {
            var imported = ResourceLoader.Load<Texture2D>(path, "Texture2D", ResourceLoader.CacheMode.Replace);
            if (imported != null)
            {
                return imported;
            }
        }

        var image = Godot.Image.LoadFromFile(path);
        return image == null || image.IsEmpty() ? null : ImageTexture.CreateFromImage(image);
    }

    private void ClearScreen()
    {
        var children = _contentBox.GetChildren();
        if (children.Count > 0)
        {
            LogUi("clear children=" + children.Count + " content_before=" + _contentBox.Size);
        }

        foreach (var child in children)
        {
            _contentBox.RemoveChild(child);
            child.QueueFree();
        }

        _layoutCardLogs = 0;
        _messageLabel.Text = _lastMessage;
        if (!string.IsNullOrEmpty(_messageLabel.Text))
        {
            PlayFeedbackFlash();
        }
        _lastMessage = "";
        UpdateInfo();
    }

    private void ShowBootError()
    {
        BuildBase();
        _infoLabel.Text = "GameSpec 加载失败";
        _messageLabel.Text = "请检查 data/game_spec/ascension_forge.prototype.json";
    }

    private void ShowMainMenu()
    {
        ClearScreen();
        _infoLabel.Text = _spec.Copy("game_title", "WorldSeed");
        AddScrollTitle("主菜单", "卡牌修仙 · 灵脉远征 · 法门构筑");
        var row = HBox(_contentBox, UiFloat("content_spacing"));
        var menu = Panel(row, "WorldSeed 山海灵契", new Vector2(360, 450));
        AddText(menu, "一卷山海图，一局问道行。\n\n以法门为牌，以符箓为辅助，在灵脉图中完成一场从入门到镇守的试炼。", UiInt("body_font_size"));
        AddButtonTo(menu, "新开灵契", NewGameRequested);
        AddButtonTo(menu, "续接旧局", ShowMap, _runtime.Run.Count > 0);
        AddButtonTo(menu, "设置", () => OpenSettings("main_menu"));
        AddButtonTo(menu, "退出", QuitGame);

        var recent = Panel(row, "最近远征", new Vector2(520, 450));
        if (_runtime.Run.Count == 0)
        {
            AddEmptyCard(recent, "未有远征", "从新开灵契开始第一局。");
        }
        else
        {
            AddRunSummaryCard(recent);
        }
        LogUi("screen=main_menu content=" + _contentBox.Size);
    }

    private void NewGameRequested()
    {
        if (_runtime.Run.Count == 0)
        {
            ShowCharacterSelect();
        }
        else
        {
            ShowConfirmNewRun();
        }
    }

    private void ShowCharacterSelect()
    {
        ClearScreen();
        AddScrollTitle("角色选择", "选择门类与起手法门");
        var character = _spec.FirstCharacter();
        var row = HBox(_contentBox, UiFloat("content_spacing"));
        var rolePanel = Panel(row, "门类卡", new Vector2(300, 530));
        AddCharacterCard(rolePanel, character);
        var detailPanel = Panel(row, "角色详情", new Vector2(330, 530));
        AddText(detailPanel, GameSpecLoader.GetString(character, "display_name"), UiInt("title_font_size"), true);
        AddText(detailPanel,
            "门类: 剑修 / 人族\n定位: " + GameSpecLoader.GetString(character, "archetype") +
            "\n" + _spec.Copy("health", "生命") + ": " + GameSpecLoader.GetInt(character, "max_hp") +
            "\n本命法器: " + Names(_spec.Equipment, GameSpecLoader.GetStringList(character, "starting_equipment")) +
            "\n悟道起点: " + Names(_spec.Talents, GameSpecLoader.GetStringList(character, "starting_talents")),
            UiInt("body_font_size"));
        AddButtonTo(detailPanel, "开始问道", () => StartRun(GameSpecLoader.GetString(character, "id")));
        AddButtonTo(detailPanel, "返回主菜单", ShowMainMenu);
        var deckPanel = Panel(row, "起手法门", new Vector2(470, 530));
        AddCardGridTo(deckPanel, GameSpecLoader.GetStringList(character, "starting_deck"), true, "character_select");
    }

    private void StartRun(string characterId)
    {
        _runtime.StartNewRun(characterId);
        _lastMessage = "灵契已立，问道开始。";
        ShowMap();
    }

    private void ShowMap()
    {
        ClearScreen();
        if (_runtime.Run.Count == 0)
        {
            ShowCharacterSelect();
            return;
        }

        if (!string.IsNullOrEmpty(_runtime.FinalMessage))
        {
            ShowRunResult();
            return;
        }

        AddScrollTitle(_spec.Copy("map", "地图"), "沿灵脉推进，选择下一处风险与奖励");
        var row = HBox(_contentBox, UiFloat("content_spacing"));
        var chapterPanel = Panel(row, "洞天", new Vector2(260, 430));
        var chapter = _runtime.CurrentChapter();
        AddText(chapterPanel,
            GameSpecLoader.GetString(chapter, "display_name") +
            "\n灵脉层数: " + GameSpecLoader.GetArray(_runtime.CurrentMapProfile(), "nodes").Count +
            "\n镇守: " + _spec.DisplayName(_spec.Encounters, GameSpecLoader.GetString(chapter, "boss_encounter_id")) +
            "\n已完成: " + _runtime.GetRunStringList("completed_nodes").Count,
            UiInt("body_font_size"));
        AddButtonTo(chapterPanel, "打开构筑洞府", ShowBuild);
        AddButtonTo(chapterPanel, "设置", () => OpenSettings("map"));

        var mapPanel = Panel(row, "灵脉路线", new Vector2(570, 430));
        AddMapPathTo(mapPanel);
        var nodePanel = Panel(row, "当前节点", new Vector2(300, 430));
        var node = _runtime.CurrentNode();
        AddNodeCard(nodePanel, node);
        AddButtonTo(nodePanel, NodeActionLabel(node), () => EnterNode(node));
    }

    private void EnterNode(JsonObject node)
    {
        var type = GameSpecLoader.GetString(node, "type");
        if (type is "normal" or "elite" or "boss")
        {
            _runtime.StartCurrentCombat();
            _lastMessage = "进入斗法。";
            ShowCombat();
        }
        else if (type == "event")
        {
            ShowEvent();
        }
        else if (type is "shop" or "forge")
        {
            ShowShop();
        }
    }

    private void ShowCombat()
    {
        ClearScreen();
        if (_runtime.GetRunInt("hp") <= 0)
        {
            ShowRunResult();
            return;
        }

        if (_runtime.PendingReward.Count > 0)
        {
            if (_runtime.GetCombatString("tier") == "boss")
            {
                _runtime.FinishChapter();
                ShowChapterResult();
            }
            else
            {
                _lastMessage = "斗法胜利，选择收获。";
                ShowReward();
            }
            return;
        }

        _infoLabel.Text = CombatPlayerStatsText();
        AddCombatHeader();
        AddCombatSummary();
        var row = HBox(_contentBox, UiFloat("content_spacing"));
        var combatTopHeight = UiFloat("combat_top_panel_height");
        var playerPanel = Panel(row, "己方", new Vector2(UiFloat("combat_player_panel_width"), combatTopHeight));
        AddPlayerCard(playerPanel);
        var enemyPanel = Panel(row, "敌阵", new Vector2(0, combatTopHeight));
        AddEnemyBoardTo(enemyPanel);
        var logPanel = Panel(row, "斗法记录", new Vector2(UiFloat("combat_log_panel_width"), combatTopHeight));
        AddLogText(logPanel, _runtime.CombatLog());
        AddButtonTo(logPanel, "收势回合", EndTurn);
        AddButtonTo(logPanel, "设置", () => OpenSettings("combat"));
        var handPanel = Panel(_contentBox, "手牌法门", new Vector2(0, UiFloat("combat_hand_panel_height")));
        AddCardHandTo(handPanel);
        LogUi("screen=combat viewport=" + GetViewportRect().Size + " window=" + DisplayServer.WindowGetSize() + " content=" + _contentBox.Size);
    }

    private void PlayCard(int cardIndex)
    {
        var hand = _runtime.GetCombatStringList("hand");
        var cardName = cardIndex >= 0 && cardIndex < hand.Count ? _spec.DisplayName(_spec.Cards, hand[cardIndex]) : "法门";
        var error = _runtime.PlayCard(cardIndex);
        _lastMessage = string.IsNullOrEmpty(error) ? "施展 " + cardName : error;
        ShowCombat();
    }

    private void EndTurn()
    {
        _runtime.EndTurn();
        _lastMessage = "敌方行动已结算。";
        ShowCombat();
    }

    private void ShowReward()
    {
        ClearScreen();
        AddScrollTitle(_spec.Copy("reward", "奖励"), "择一法门，沉淀构筑");
        var row = HBox(_contentBox, UiFloat("content_spacing"));
        var summary = Panel(row, "自动收获", new Vector2(270, 430));
        AddText(summary,
            _spec.Copy("gold", "金币") + ": +" + _runtime.PendingInt("gold") +
            "\n" + _spec.Copy("talent_points", "天赋点") + ": +" + _runtime.PendingInt("talent_points") +
            "\n当前法门: " + _runtime.GetRunStringList("deck").Count +
            "\n符箓库存: " + _runtime.GetRunStringList("support_inventory").Count,
            UiInt("body_font_size"));
        var cardsPanel = Panel(row, "法门三选一", new Vector2(620, 430));
        AddRewardCardsTo(cardsPanel, _runtime.PendingCardChoices());
        var extraPanel = Panel(row, "操作", new Vector2(240, 430));
        AddRewardEquipmentTo(extraPanel, _runtime.PendingEquipmentChoices());
        AddButtonTo(extraPanel, "略过法门", SkipReward);
    }

    private void ClaimCard(string cardId)
    {
        _runtime.ClaimCard(cardId);
        _lastMessage = "获得法门: " + _spec.DisplayName(_spec.Cards, cardId);
        ShowBuild();
    }

    private void ClaimEquipment(string equipmentId)
    {
        _runtime.ClaimEquipment(equipmentId);
        _lastMessage = "获得法器: " + _spec.DisplayName(_spec.Equipment, equipmentId);
        ShowBuild();
    }

    private void SkipReward()
    {
        _runtime.SkipReward();
        _lastMessage = "已略过法门。";
        ShowBuild();
    }

    private void ShowBuild()
    {
        ClearScreen();
        AddScrollTitle(_spec.Copy("build", "构筑管理"), "法门、符箓、法器与悟道");
        var row = HBox(_contentBox, UiFloat("content_spacing"));
        var tabs = Panel(row, "页签", new Vector2(190, 540));
        AddButtonTo(tabs, "法门", ShowBuild);
        AddButtonTo(tabs, "符箓槽", ShowBuild);
        AddButtonTo(tabs, "法器", ShowBuild);
        AddButtonTo(tabs, "悟道", ShowBuild);
        AddButtonTo(tabs, "返回灵脉", ShowMap);
        var deckPanel = Panel(row, "法门牌组", new Vector2(520, 540));
        AddCardGridTo(deckPanel, _runtime.GetRunStringList("deck"), true, "build");
        AddSupportLinksTo(deckPanel);
        var side = Panel(row, "符箓 / 法器 / 悟道", new Vector2(420, 540));
        AddText(side, "符箓库存", UiInt("body_font_size"), true);
        AddCardGridTo(side, _runtime.GetRunStringList("support_inventory"), true, "build");
        AddItemListTo(side, _spec.Copy("equipment", "装备"), _runtime.GetRunStringList("equipment"), _spec.Equipment);
        AddItemListTo(side, _spec.Copy("talent", "天赋"), _runtime.GetRunStringList("talents"), _spec.Talents);
        AddText(side, _spec.Copy("talent_points", "天赋点") + ": " + _runtime.GetRunInt("talent_points"), UiInt("body_font_size"));
        AddButtonTo(side, "自动荐符", LinkSupport);
        AddButtonTo(side, "参悟下个节点", UnlockTalent);
    }

    private void LinkSupport()
    {
        _lastMessage = _runtime.LinkFirstSupport();
        ShowBuild();
    }

    private void UnlockTalent()
    {
        _lastMessage = _runtime.UnlockNextTalent();
        ShowBuild();
    }

    private void ShowEvent()
    {
        ClearScreen();
        AddScrollTitle(_spec.Copy("event", "事件"), "山中机缘，取舍有代价");
        var row = HBox(_contentBox, UiFloat("content_spacing"));
        var cardPanel = Panel(row, "奇遇卡", new Vector2(330, 430));
        var eventData = _spec.Events[GameSpecLoader.GetString(_runtime.CurrentNode(), "event_id")];
        AddSimpleCard(cardPanel, GameSpecLoader.GetString(eventData, "display_name"), "?", "奇遇", "余温未散\n可换符箓", true);
        var choicePanel = Panel(row, GameSpecLoader.GetString(eventData, "display_name"), new Vector2(720, 430));
        AddText(choicePanel, GameSpecLoader.GetString(eventData, "description"), UiInt("body_font_size"));
        var choices = GameSpecLoader.GetArray(eventData, "choices");
        for (var index = 0; index < choices.Count; index++)
        {
            var choice = GameSpecLoader.AsObject(choices[index]);
            var captured = index;
            AddButtonTo(choicePanel, GameSpecLoader.GetString(choice, "display_name"), () => ResolveEvent(captured), true, 360);
        }
    }

    private void ResolveEvent(int choiceIndex)
    {
        _runtime.ResolveEvent(choiceIndex);
        _lastMessage = "奇遇已结算。";
        ShowBuild();
    }

    private void ShowShop()
    {
        ClearScreen();
        AddScrollTitle(_spec.Copy("shop", "商店"), "购买法门、法器和温养命元");
        var shop = _spec.Shops[GameSpecLoader.GetString(_runtime.CurrentNode(), "shop_id")];
        var row = HBox(_contentBox, UiFloat("content_spacing"));
        var goods = Panel(row, "货架", new Vector2(780, 470));
        var services = GameSpecLoader.GetArray(shop, "services");
        var goodsRow = HBox(goods, UiFloat("content_spacing"));
        for (var index = 0; index < services.Count; index++)
        {
            var service = GameSpecLoader.AsObject(services[index]);
            var captured = index;
            AddServiceCard(goodsRow, service, () => BuyService(captured));
        }
        var info = Panel(row, "掌柜提示", new Vector2(300, 470));
        AddText(info, GameSpecLoader.GetString(shop, "display_name") + "\n\n灵石不足时按钮会保留，但点击后会在提示栏说明原因。\n交易完成后可继续购买或离开。", UiInt("body_font_size"));
        AddButtonTo(info, "打开构筑", ShowBuild);
        AddButtonTo(info, "离开", LeaveShop);
    }

    private void BuyService(int serviceIndex)
    {
        _lastMessage = _runtime.BuyService(serviceIndex);
        ShowShop();
    }

    private void LeaveShop()
    {
        _runtime.LeaveShop();
        _lastMessage = "离开灵市。";
        ShowBuild();
    }

    private void ShowChapterResult()
    {
        ClearScreen();
        AddScrollTitle(_spec.Copy("chapter_result", "章节结算"), "镇守已破，收束洞天");
        var row = HBox(_contentBox, UiFloat("content_spacing"));
        var result = Panel(row, "战果", new Vector2(330, 430));
        AddSimpleCard(result, "活熔炉", "6", "妖兽", "已镇压", false);
        AddText(result, "胜利斗法: " + Stat("battles_won") + "\n施展法门: " + Stat("cards_played") + "\n造成伤害: " + Stat("damage_dealt"), UiInt("body_font_size"));
        var rewards = Panel(row, "升华三选一", new Vector2(480, 430));
        var rewardRow = HBox(rewards, UiFloat("content_spacing"));
        AddSimpleCard(rewardRow, "罡气反震", "1", "升华", "护体后反击", true);
        AddSimpleCard(rewardRow, "镶孔戒", "2", "法器", "额外符槽", true);
        AddSimpleCard(rewardRow, "悟道点 +1", "3", "悟道", "解锁节点", true);
        var next = Panel(row, "下一步", new Vector2(260, 430));
        AddText(next, "MVP 当前只开放一处洞天。\n后续版本将在这里展示下一章山水图。", UiInt("body_font_size"));
        AddButtonTo(next, "进入本局结算", ShowRunResult);
    }

    private void ShowRunResult()
    {
        ClearScreen();
        AddScrollTitle(_spec.Copy("run_result", "本局结算"), "一局问道的结果");
        var row = HBox(_contentBox, UiFloat("content_spacing"));
        var summary = Panel(row, "远征完成", new Vector2(620, 430));
        AddText(summary, string.IsNullOrEmpty(_runtime.FinalMessage) ? "本局尚未完成。" : _runtime.FinalMessage, UiInt("title_font_size"), true);
        AddText(summary,
            "角色: " + _spec.DisplayName(_spec.Characters, _runtime.GetRunString("character_id")) +
            "\n洞天: " + _spec.DisplayName(_spec.Chapters, _runtime.GetRunString("chapter_id")) +
            "\n胜利斗法: " + Stat("battles_won") +
            "\n施展法门: " + Stat("cards_played") +
            "\n造成伤害: " + Stat("damage_dealt"),
            UiInt("body_font_size"));
        AddButtonTo(summary, "重新问道", ShowCharacterSelect);
        AddButtonTo(summary, "返回主菜单", ShowMainMenu);
        var deck = Panel(row, "最终卡组", new Vector2(520, 430));
        AddCardGridTo(deck, _runtime.GetRunStringList("deck"), true, "run_result", 3);
    }

    private void ShowSettings()
    {
        ClearScreen();
        AddScrollTitle("设置", "卷轴弹层");
        var panel = Panel(_contentBox, "设置", new Vector2(620, 430));
        AddText(panel, "音律    画面    游戏    输入", UiInt("body_font_size"), true);
        AddSliderRow(panel, "总音量", 70);
        AddSliderRow(panel, "乐曲", 62);
        AddSliderRow(panel, "音效", 76);
        AddSliderRow(panel, "斗法速度", 55);
        AddButtonTo(panel, "关闭", ReturnToPrevious);
    }

    private void OpenSettings(string screenName)
    {
        _returnScreen = screenName;
        ShowSettings();
    }

    private void ShowCardDetail(string cardId, string screenName)
    {
        _returnScreen = screenName;
        ClearScreen();
        AddScrollTitle("卡牌详情", "完整法门说明");
        var card = _spec.Cards.GetValueOrDefault(cardId, new JsonObject());
        var row = HBox(_contentBox, UiFloat("content_spacing"));
        var cardPanel = Panel(row, "卡面", new Vector2(320, 480));
        AddCardTo(cardPanel, card, false, null, "", "", false);
        var detailPanel = Panel(row, GameSpecLoader.GetString(card, "display_name", cardId), new Vector2(620, 480));
        AddText(detailPanel, "门类: " + CardKind(card) + "\n费用: " + CardCostText(card) + "\n类型: " + GameSpecLoader.GetString(card, "type") + "\n标签: " + JoinStrings(GameSpecLoader.GetStringList(card, "tags"), "、") + "\n符槽: " + GameSpecLoader.GetInt(card, "support_slots") + "\n效果: " + EffectText(GameSpecLoader.GetArray(card, "effects")), UiInt("body_font_size"));
        AddButtonTo(detailPanel, "关闭", ReturnToPrevious);
    }

    private void ShowConfirmNewRun()
    {
        _returnScreen = "main_menu";
        ClearScreen();
        AddScrollTitle("确认操作", "防止误操作");
        var panel = Panel(_contentBox, "新开灵契", new Vector2(520, 260));
        AddText(panel, "新开灵契会覆盖当前未完成远征。\n确认后将进入角色选择。", UiInt("body_font_size"));
        AddButtonTo(panel, "确认", ShowCharacterSelect);
        AddButtonTo(panel, "取消", ShowMainMenu);
    }

    private void ReturnToPrevious()
    {
        switch (_returnScreen)
        {
            case "main_menu": ShowMainMenu(); break;
            case "character_select": ShowCharacterSelect(); break;
            case "map": ShowMap(); break;
            case "combat": ShowCombat(); break;
            case "reward": ShowReward(); break;
            case "build": ShowBuild(); break;
            case "event": ShowEvent(); break;
            case "shop": ShowShop(); break;
            case "chapter_result": ShowChapterResult(); break;
            case "run_result": ShowRunResult(); break;
            default: ShowMainMenu(); break;
        }
    }

    private void AddScrollTitle(string text, string subtitle)
    {
        var row = new HBoxContainer();
        row.SizeFlagsHorizontal = SizeFlags.ExpandFill;
        row.SizeFlagsVertical = SizeFlags.ShrinkBegin;
        row.AddThemeConstantOverride("separation", 10);
        _contentBox.AddChild(row);
        var title = NewLabel(text, UiInt("title_font_size"), true);
        title.AutowrapMode = TextServer.AutowrapMode.Off;
        title.ClipText = true;
        row.AddChild(title);
        var sub = NewLabel(subtitle, UiInt("small_font_size"));
        sub.AutowrapMode = TextServer.AutowrapMode.Off;
        sub.ClipText = true;
        sub.VerticalAlignment = VerticalAlignment.Center;
        sub.SizeFlagsHorizontal = SizeFlags.ExpandFill;
        row.AddChild(sub);
    }

    private void AddCombatHeader()
    {
        var row = new HBoxContainer();
        row.SizeFlagsHorizontal = SizeFlags.ExpandFill;
        row.SizeFlagsVertical = SizeFlags.ShrinkBegin;
        row.AddThemeConstantOverride("separation", 12);
        _contentBox.AddChild(row);
        var mark = NewLabel("□", UiInt("body_font_size"), true);
        mark.AutowrapMode = TextServer.AutowrapMode.Off;
        mark.ClipText = true;
        row.AddChild(mark);
        var title = NewLabel(_spec.Copy("combat", "斗法"), UiInt("title_font_size"), true);
        title.AutowrapMode = TextServer.AutowrapMode.Off;
        title.ClipText = true;
        row.AddChild(title);
        var line = new ColorRect();
        line.Color = new Color(0.45f, 0.36f, 0.25f, 1.0f);
        line.CustomMinimumSize = new Vector2(0, 1);
        line.SizeFlagsHorizontal = SizeFlags.ExpandFill;
        line.SizeFlagsVertical = SizeFlags.ShrinkCenter;
        row.AddChild(line);
    }

    private VBoxContainer Panel(Node parent, string title, Vector2 minSize)
    {
        var panel = new PanelContainer();
        panel.CustomMinimumSize = minSize;
        panel.SizeFlagsHorizontal = minSize.X <= 0 ? SizeFlags.ExpandFill : SizeFlags.ShrinkBegin;
        panel.SizeFlagsVertical = SizeFlags.ShrinkBegin;
        panel.AddThemeStyleboxOverride("panel", StylePanel());
        parent.AddChild(panel);
        var margin = new MarginContainer();
        margin.AddThemeConstantOverride("margin_left", 14);
        margin.AddThemeConstantOverride("margin_top", 12);
        margin.AddThemeConstantOverride("margin_right", 14);
        margin.AddThemeConstantOverride("margin_bottom", 12);
        panel.AddChild(margin);
        var box = new VBoxContainer();
        box.AddThemeConstantOverride("separation", UiInt("compact_spacing"));
        margin.AddChild(box);
        if (!string.IsNullOrEmpty(title))
        {
            box.AddChild(NewLabel(title, UiInt("body_font_size"), true));
        }
        return box;
    }

    private HBoxContainer HBox(Node parent, float separation)
    {
        var row = new HBoxContainer();
        row.AddThemeConstantOverride("separation", (int)separation);
        row.SizeFlagsHorizontal = SizeFlags.ExpandFill;
        row.SizeFlagsVertical = SizeFlags.ShrinkBegin;
        parent.AddChild(row);
        return row;
    }

    private Label AddText(Node parent, string text, int size, bool bold = false)
    {
        var label = NewLabel(text, size, bold);
        parent.AddChild(label);
        return label;
    }

    private Label NewLabel(string text, int size, bool bold = false)
    {
        var label = new Label();
        label.Text = text;
        label.AutowrapMode = TextServer.AutowrapMode.WordSmart;
        label.AddThemeFontSizeOverride("font_size", size);
        label.AddThemeColorOverride("font_color", bold ? new Color(0.18f, 0.16f, 0.13f, 1.0f) : ColorInk());
        return label;
    }

    private Button AddButtonTo(Node parent, string text, Action callback, bool enabled = true, int width = 220)
    {
        var button = new Button();
        button.Text = text;
        button.Disabled = !enabled;
        button.CustomMinimumSize = new Vector2(width, UiFloat("button_height"));
        button.SizeFlagsVertical = SizeFlags.ShrinkBegin;
        button.AddThemeStyleboxOverride("normal", StyleButton(false));
        button.AddThemeStyleboxOverride("hover", StyleButton(true));
        button.AddThemeStyleboxOverride("pressed", StyleButton(true));
        button.AddThemeStyleboxOverride("disabled", StyleDisabledButton());
        button.AddThemeColorOverride("font_color", new Color(0.96f, 0.91f, 0.80f, 1.0f));
        button.AddThemeColorOverride("font_disabled_color", new Color(0.35f, 0.32f, 0.27f, 1.0f));
        if (enabled)
        {
            button.Pressed += callback;
        }
        parent.AddChild(button);
        return button;
    }

    private void AddCharacterCard(Node parent, JsonObject character)
    {
        var card = FakeCard(GameSpecLoader.GetString(character, "display_name"), "attack", "5", "剑", "命元 " + GameSpecLoader.GetInt(character, "max_hp"));
        AddCardTo(parent, card, false, null, "", "", false);
    }

    private void AddRunSummaryCard(Node parent)
    {
        var card = FakeCard(_spec.DisplayName(_spec.Characters, _runtime.GetRunString("character_id")), "skill", "?", "法", "未有远征\n不可使用");
        AddCardTo(parent, card, false, null, "", "", true);
        AddText(parent, "从新开灵契开始第一局。", UiInt("body_font_size"));
    }

    private void AddEmptyCard(Node parent, string title, string body)
    {
        var card = FakeCard(title, "skill", "?", "法", "未有远征\n不可使用");
        AddCardTo(parent, card, false, null, "", "", true);
        AddText(parent, body, UiInt("body_font_size"));
    }

    private VBoxContainer AddCardTo(Node parent, JsonObject card, bool clickable, Action callback, string actionText, string screenName, bool compact, float widthOverride = 0, float heightOverride = 0)
    {
        var width = widthOverride > 0 ? widthOverride : UiFloat(compact ? "mini_card_width" : "card_width");
        var height = heightOverride > 0 ? heightOverride : UiFloat(compact ? "mini_card_height" : "card_height");
        var actionHeight = clickable && callback != null ? UiFloat("button_height") + UiFloat("compact_spacing") : 0;
        var box = new VBoxContainer();
        box.CustomMinimumSize = new Vector2(width, height + actionHeight);
        box.SizeFlagsHorizontal = SizeFlags.ShrinkBegin;
        box.SizeFlagsVertical = SizeFlags.ShrinkBegin;
        box.AddThemeConstantOverride("separation", UiInt("compact_spacing"));
        parent.AddChild(box);

        var cardPanel = new Control();
        cardPanel.CustomMinimumSize = new Vector2(width, height);
        cardPanel.Size = new Vector2(width, height);
        cardPanel.SizeFlagsHorizontal = SizeFlags.ShrinkBegin;
        cardPanel.SizeFlagsVertical = SizeFlags.ShrinkBegin;
        cardPanel.ClipContents = true;
        box.AddChild(cardPanel);

        var frame = new TextureRect();
        frame.Texture = GD.Load<Texture2D>(CardFramePath(card));
        frame.ExpandMode = TextureRect.ExpandModeEnum.IgnoreSize;
        frame.StretchMode = TextureRect.StretchModeEnum.Scale;
        frame.Position = Vector2.Zero;
        frame.Size = new Vector2(width, height);
        frame.CustomMinimumSize = Vector2.Zero;
        frame.MouseFilter = MouseFilterEnum.Ignore;
        cardPanel.AddChild(frame);

        var cardBodyFont = CardFontSize(height, "body_font_size");
        var cardSmallFont = CardFontSize(height, "small_font_size");
        var cardTinyFont = CardFontSize(height, "tiny_font_size");
        AddCardLabel(cardPanel, CardCostText(card), new Vector2(width * 0.04f, height * 0.04f), new Vector2(width * 0.15f, height * 0.12f), cardBodyFont, new Color(0.96f, 0.91f, 0.80f, 1.0f), true, HorizontalAlignment.Center);
        AddCardLabel(cardPanel, CardKind(card), new Vector2(width * 0.075f, height * 0.32f), new Vector2(width * 0.11f, height * 0.18f), cardBodyFont, new Color(0.96f, 0.91f, 0.80f, 1.0f), true, HorizontalAlignment.Center);
        AddCardLabel(cardPanel, GameSpecLoader.GetString(card, "display_name"), new Vector2(width * 0.26f, height * 0.045f), new Vector2(width * 0.63f, height * 0.11f), cardTinyFont, new Color(0.18f, 0.14f, 0.10f, 1.0f), true, HorizontalAlignment.Center);
        AddCardLabel(cardPanel, CardArtText(card) + "\n" + CardArtMark(card), new Vector2(width * 0.25f, height * 0.25f), new Vector2(width * 0.57f, height * 0.18f), cardSmallFont, new Color(0.18f, 0.27f, 0.27f, 1.0f), true, HorizontalAlignment.Center);
        AddCardLabel(cardPanel, CardRuleTitle(card), new Vector2(width * 0.24f, height * 0.535f), new Vector2(width * 0.62f, height * 0.10f), cardTinyFont, new Color(0.28f, 0.19f, 0.10f, 1.0f), true, HorizontalAlignment.Center);
        AddCardLabel(cardPanel, EffectText(GameSpecLoader.GetArray(card, "effects")), new Vector2(width * 0.19f, height * 0.675f), new Vector2(width * 0.67f, height * 0.17f), cardTinyFont, new Color(0.22f, 0.17f, 0.12f, 1.0f), false, HorizontalAlignment.Center);
        AddCardLabel(cardPanel, CardTypeLabel(card), new Vector2(width * 0.24f, height * 0.90f), new Vector2(width * 0.52f, height * 0.08f), cardTinyFont, new Color(0.96f, 0.91f, 0.80f, 1.0f), true, HorizontalAlignment.Center);

        if (clickable && callback != null)
        {
            var actions = new HBoxContainer();
            actions.AddThemeConstantOverride("separation", 4);
            box.AddChild(actions);
            AddButtonTo(actions, actionText, callback, true, (int)(width * 0.52f));
            if (actionText != "详情")
            {
                var cardId = GameSpecLoader.GetString(card, "id");
                AddButtonTo(actions, "详情", () => ShowCardDetail(cardId, screenName), true, (int)(width * 0.42f));
            }
        }

        LogCardLayout(GameSpecLoader.GetString(card, "display_name"), width, height, box, cardPanel, frame);
        return box;
    }

    private void AddCardLabel(Node parent, string text, Vector2 pos, Vector2 labelSize, int fontSize, Color color, bool bold, HorizontalAlignment align)
    {
        var label = NewLabel(text, fontSize, bold);
        label.Position = pos;
        label.Size = labelSize;
        label.HorizontalAlignment = align;
        label.VerticalAlignment = VerticalAlignment.Center;
        label.ClipText = true;
        label.AddThemeColorOverride("font_color", color);
        parent.AddChild(label);
    }

    private int CardFontSize(float cardHeight, string key)
    {
        var baseHeight = Math.Max(1.0f, UiFloat("card_height"));
        var scaled = UiInt(key) * cardHeight / baseHeight;
        return Math.Max(11, (int)Math.Round(scaled));
    }

    private void AddSimpleCard(Node parent, string title, string cost, string kind, string body, bool compact)
    {
        AddCardTo(parent, FakeCard(title, "skill", cost, kind, body), false, null, "", "", compact);
    }

    private void AddCardGridTo(Node parent, List<string> cardIds, bool compact, string screenName, int maxCards = 6)
    {
        if (cardIds.Count == 0)
        {
            AddText(parent, "暂无", UiInt("small_font_size"));
            return;
        }

        var grid = new GridContainer();
        grid.Columns = UiInt("deck_grid_columns");
        grid.AddThemeConstantOverride("h_separation", UiInt("content_spacing"));
        grid.AddThemeConstantOverride("v_separation", UiInt("content_spacing"));
        parent.AddChild(grid);
        var shown = Math.Min(cardIds.Count, maxCards);
        for (var index = 0; index < shown; index++)
        {
            var cardId = cardIds[index];
            var card = _spec.Cards.GetValueOrDefault(cardId, new JsonObject());
            AddCardTo(grid, card, true, () => ShowCardDetail(cardId, screenName), "详情", screenName, compact);
        }
        if (cardIds.Count > shown)
        {
            AddText(parent, "另有 " + (cardIds.Count - shown) + " 张法门", UiInt("tiny_font_size"));
        }
    }

    private void AddCardHandTo(Node parent)
    {
        var row = HBox(parent, UiFloat("content_spacing"));
        var hand = _runtime.GetCombatStringList("hand");
        var width = UiFloat("combat_card_width");
        var height = UiFloat("combat_card_height");
        for (var index = 0; index < hand.Count; index++)
        {
            var captured = index;
            AddCardTo(row, _spec.Cards[hand[index]], true, () => PlayCard(captured), "施展", "combat", true, width, height);
        }
    }

    private void AddRewardCardsTo(Node parent, List<string> cardIds)
    {
        var row = HBox(parent, UiFloat("content_spacing"));
        foreach (var cardId in cardIds)
        {
            AddCardTo(row, _spec.Cards.GetValueOrDefault(cardId, new JsonObject()), true, () => ClaimCard(cardId), "收取", "reward", true);
        }
    }

    private void AddRewardEquipmentTo(Node parent, List<string> equipmentIds)
    {
        if (equipmentIds.Count == 0)
        {
            AddText(parent, "本次没有额外法器。", UiInt("small_font_size"));
            return;
        }

        foreach (var equipmentId in equipmentIds)
        {
            AddButtonTo(parent, "收取法器: " + _spec.DisplayName(_spec.Equipment, equipmentId), () => ClaimEquipment(equipmentId));
        }
    }

    private void AddServiceCard(Node parent, JsonObject service, Action callback)
    {
        var reward = GameSpecLoader.GetObject(service, "reward");
        var typeName = GameSpecLoader.GetString(reward, "type") switch
        {
            "equipment" => "器",
            "heal" => "丹",
            _ => "符"
        };
        var card = FakeCard(GameSpecLoader.GetString(service, "display_name"), "support", GameSpecLoader.GetInt(service, "price").ToString(), typeName, typeName + " / 点击购买");
        var box = AddCardTo(parent, card, false, null, "", "", false);
        AddButtonTo(box, "购买", callback, true, 130);
    }

    private void AddMapPathTo(Node parent)
    {
        var nodes = GameSpecLoader.GetArray(_runtime.CurrentMapProfile(), "nodes");
        var currentIndex = _runtime.GetRunInt("map_node_index");
        var row = HBox(parent, 18);
        for (var index = 0; index < nodes.Count; index++)
        {
            var node = GameSpecLoader.AsObject(nodes[index]);
            var nodeBox = new VBoxContainer();
            nodeBox.AddThemeConstantOverride("separation", 4);
            row.AddChild(nodeBox);
            var badge = NewLabel(NodeMark(node), UiInt("body_font_size"), true);
            badge.HorizontalAlignment = HorizontalAlignment.Center;
            badge.CustomMinimumSize = new Vector2(56, 56);
            badge.AddThemeColorOverride("font_color", new Color(0.96f, 0.91f, 0.80f, 1.0f));
            badge.AddThemeStyleboxOverride("normal", StyleBox(NodeColor(node), new Color(0.18f, 0.16f, 0.13f, 1.0f), 28, 3));
            nodeBox.AddChild(badge);
            var state = index < currentIndex ? "完成" : index == currentIndex ? "当前" : "未至";
            nodeBox.AddChild(NewLabel(NodeLabel(node) + "\n" + state, UiInt("tiny_font_size"), true));
        }
    }

    private void AddNodeCard(Node parent, JsonObject node)
    {
        var body = "节点: " + GameSpecLoader.GetString(node, "id") + "\n类型: " + GameSpecLoader.GetString(node, "type");
        if (node.ContainsKey("encounter_id")) body += "\n遭遇: " + _spec.DisplayName(_spec.Encounters, GameSpecLoader.GetString(node, "encounter_id"));
        if (node.ContainsKey("event_id")) body += "\n奇遇: " + _spec.DisplayName(_spec.Events, GameSpecLoader.GetString(node, "event_id"));
        if (node.ContainsKey("shop_id")) body += "\n地点: " + _spec.DisplayName(_spec.Shops, GameSpecLoader.GetString(node, "shop_id"));
        AddSimpleCard(parent, NodeLabel(node), NodeMark(node), "节点", body, false);
    }

    private void AddPlayerCard(Node parent)
    {
        AddCardTo(parent, FakeCard(_spec.DisplayName(_spec.Characters, _runtime.GetRunString("character_id")), "attack", "5", "剑", _spec.Copy("health", "生命") + " " + _runtime.GetRunInt("hp") + "/" + _runtime.GetRunInt("max_hp") + " / " + _spec.Copy("armor", "护甲") + " " + _runtime.GetCombatInt("armor")), false, null, "", "", true, UiFloat("combat_card_width"), UiFloat("combat_card_height"));
    }

    private string CombatPlayerStatsText()
    {
        var maxEnergy = GameSpecLoader.GetInt(GameSpecLoader.GetObject(_spec.Data, "gameplay"), "starting_energy", 3);
        return _spec.Copy("health", "命元") + " " + _runtime.GetRunInt("hp") + "/" + _runtime.GetRunInt("max_hp") +
            "  " + _spec.Copy("armor", "罡气") + " " + _runtime.GetCombatInt("armor") +
            "  " + _spec.Copy("energy", "灵力") + " " + _runtime.GetCombatInt("energy") + "/" + maxEnergy +
            "  " + _spec.Copy("gold", "灵石") + " " + _runtime.GetRunInt("gold");
    }

    private void AddEnemyBoardTo(Node parent)
    {
        var row = HBox(parent, UiFloat("content_spacing"));
        foreach (var enemyState in _runtime.GetCombatEnemies())
        {
            var enemy = _spec.Enemies.GetValueOrDefault(StateString(enemyState, "id"), new JsonObject());
            var body = "命元 " + StateInt(enemyState, "hp") + "/" + StateInt(enemyState, "max_hp") + "\n护甲 " + StateInt(enemyState, "armor") + "\n敌意 " + EnemyIntentText(enemy, enemyState);
            AddCardTo(row, FakeCard(GameSpecLoader.GetString(enemy, "display_name"), "curse", "2", "咒", body), false, null, "", "", true, UiFloat("combat_card_width"), UiFloat("combat_card_height"));
        }
    }

    private void AddSupportLinksTo(Node parent)
    {
        var links = _runtime.GetSupportLinks();
        if (links.Count == 0)
        {
            AddText(parent, "尚未嵌入符箓。", UiInt("small_font_size"));
            return;
        }
        foreach (var pair in links)
        {
            AddText(parent, _spec.DisplayName(_spec.Cards, pair.Key) + " <= " + Names(_spec.Cards, pair.Value), UiInt("small_font_size"));
        }
    }

    private void AddItemListTo(Node parent, string title, List<string> ids, Dictionary<string, JsonObject> section)
    {
        AddText(parent, title, UiInt("body_font_size"), true);
        if (ids.Count == 0)
        {
            AddText(parent, "暂无", UiInt("small_font_size"));
            return;
        }
        foreach (var itemId in ids)
        {
            AddText(parent, "❧ " + _spec.DisplayName(section, itemId), UiInt("small_font_size"));
        }
    }

    private void AddLogText(Node parent, List<string> lines)
    {
        var visibleLines = UiInt("combat_log_visible_lines");
        var start = Math.Max(0, lines.Count - visibleLines);
        var shown = lines.Count == 0 ? new List<string>() : lines.GetRange(start, lines.Count - start);
        var label = AddText(parent, shown.Count == 0 ? "暂无记录。" : JoinStrings(shown, "\n"), UiInt("small_font_size"));
        label.ClipText = true;
    }

    private void AddCombatSummary()
    {
        AddText(_contentBox, "回合 " + _runtime.GetCombatInt("turn") + "    抽牌 " + _runtime.GetCombatStringList("draw_pile").Count + "    弃牌 " + _runtime.GetCombatStringList("discard_pile").Count, UiInt("small_font_size"), true);
    }

    private void AddSliderRow(Node parent, string labelText, int value)
    {
        var row = HBox(parent, 12);
        row.AddChild(NewLabel(labelText, UiInt("small_font_size"), true));
        var slider = new HSlider();
        slider.MinValue = 0;
        slider.MaxValue = 100;
        slider.Value = value;
        slider.CustomMinimumSize = new Vector2(280, 26);
        row.AddChild(slider);
    }

    private JsonObject FakeCard(string title, string type, string cost, string kind, string body)
    {
        return new JsonObject
        {
            ["id"] = "",
            ["display_name"] = title,
            ["kind"] = kind,
            ["type"] = type,
            ["cost"] = cost,
            ["rarity"] = "common",
            ["tags"] = new JsonArray(),
            ["support_slots"] = 0,
            ["effects"] = new JsonArray(new JsonObject { ["type"] = "custom_text", ["text"] = body })
        };
    }

    private string CardCostText(JsonObject card)
    {
        return card["cost"]?.ToString() ?? "0";
    }

    private string CardKind(JsonObject card)
    {
        var customKind = GameSpecLoader.GetString(card, "kind");
        if (!string.IsNullOrEmpty(customKind))
        {
            return customKind[..1];
        }

        return GameSpecLoader.GetString(card, "type") switch
        {
            "attack" => GameSpecLoader.GetStringList(card, "tags").Contains("fire") || GameSpecLoader.GetStringList(card, "tags").Contains("spell") ? "术" : "剑",
            "defense" => "护",
            "skill" => "法",
            "support" => "符",
            "curse" => "咒",
            _ => "卡"
        };
    }

    private string CardTypeLabel(JsonObject card)
    {
        return GameSpecLoader.GetString(card, "type") switch
        {
            "attack" => "修士",
            "defense" => "护法",
            "skill" => "法门",
            "support" => "符箓",
            "curse" => "劫咒",
            _ => "卡牌"
        };
    }

    private string CardRuleTitle(JsonObject card)
    {
        return CardKind(card) switch
        {
            "剑" => "剑诀",
            "护" => "护体",
            "术" => "符术",
            "法" => "法诀",
            "符" => "符箓",
            "咒" => "劫气",
            _ => "规则"
        };
    }

    private string CardFramePath(JsonObject card)
    {
        var frames = _spec.GetAssetSection("card_frames");
        var type = GameSpecLoader.GetString(card, "type", "skill");
        return GameSpecLoader.GetString(frames, type, GameSpecLoader.GetString(frames, "skill", "res://assets/cards/card_skill.png"));
    }

    private string CardArtText(JsonObject card)
    {
        return CardKind(card) switch
        {
            "剑" => "剑气纵横",
            "护" => "罡气护体",
            "术" => "雷火符术",
            "法" => "古卷法诀",
            "符" => "朱砂符箓",
            "咒" => "劫气成形",
            _ => "山水云纹"
        };
    }

    private string CardArtMark(JsonObject card)
    {
        return CardKind(card) switch
        {
            "剑" => "╱╲",
            "护" => "◯",
            "术" => "✦",
            "法" => "▧",
            "符" => "☷",
            "咒" => "☄",
            _ => "〰"
        };
    }

    private string EnemyIntentText(JsonObject enemy, Dictionary<string, object> enemyState)
    {
        var intents = GameSpecLoader.GetArray(enemy, "intents");
        if (intents.Count == 0)
        {
            return "未知";
        }
        var intent = GameSpecLoader.AsObject(intents[StateInt(enemyState, "intent_index") % intents.Count]);
        return GameSpecLoader.GetString(intent, "type") switch
        {
            "damage" => "攻击 " + GameSpecLoader.GetInt(intent, "amount"),
            "gain_armor" => "护体 " + GameSpecLoader.GetInt(intent, "amount"),
            "apply_status" => "异常 " + GameSpecLoader.GetString(intent, "status"),
            _ => "未知"
        };
    }

    private string EffectText(JsonArray effects)
    {
        var parts = new List<string>();
        foreach (var effect in effects)
        {
            var obj = GameSpecLoader.AsObject(effect);
            switch (GameSpecLoader.GetString(obj, "type"))
            {
                case "damage": parts.Add("伤害 " + GameSpecLoader.GetInt(obj, "amount")); break;
                case "gain_armor": parts.Add("罡气 " + GameSpecLoader.GetInt(obj, "amount")); break;
                case "draw_cards": parts.Add("抽牌 " + GameSpecLoader.GetInt(obj, "amount")); break;
                case "apply_status": parts.Add(GameSpecLoader.GetString(obj, "status") + " " + GameSpecLoader.GetInt(obj, "amount")); break;
                case "next_attack_bonus": parts.Add("下次攻击 +" + GameSpecLoader.GetInt(obj, "amount")); break;
                case "modify_damage": parts.Add("连接伤害 +" + GameSpecLoader.GetInt(obj, "amount")); break;
                case "gain_armor_after_use": parts.Add("施展后罡气 +" + GameSpecLoader.GetInt(obj, "amount")); break;
                case "modify_status_amount": parts.Add("状态 +" + GameSpecLoader.GetInt(obj, "amount")); break;
                case "custom_text": parts.Add(GameSpecLoader.GetString(obj, "text")); break;
                case "dead_card": parts.Add("不可使用"); break;
            }
        }
        return JoinStrings(parts, "，");
    }

    private string Names(Dictionary<string, JsonObject> section, List<string> ids)
    {
        var parts = new List<string>();
        foreach (var id in ids)
        {
            parts.Add(_spec.DisplayName(section, id));
        }
        return JoinStrings(parts, "、");
    }

    private string JoinStrings(List<string> items, string separator)
    {
        var text = "";
        for (var index = 0; index < items.Count; index++)
        {
            if (index > 0) text += separator;
            text += items[index];
        }
        return text;
    }

    private string NodeActionLabel(JsonObject node)
    {
        return GameSpecLoader.GetString(node, "type") switch
        {
            "normal" => "进入斗法",
            "elite" => "挑战强敌",
            "event" => "进入奇遇",
            "shop" => "进入灵市",
            "forge" => "进入锻炉",
            "boss" => "挑战镇守",
            _ => "进入节点"
        };
    }

    private string NodeLabel(JsonObject node)
    {
        return GameSpecLoader.GetString(node, "type") switch
        {
            "normal" => "斗法",
            "elite" => "强敌",
            "event" => "奇遇",
            "shop" => "灵市",
            "forge" => "锻炉",
            "boss" => "炉心",
            _ => "节点"
        };
    }

    private string NodeMark(JsonObject node)
    {
        return GameSpecLoader.GetString(node, "type") switch
        {
            "normal" => "斗",
            "elite" => "劫",
            "event" => "遇",
            "shop" => "市",
            "forge" => "炉",
            "boss" => "镇",
            _ => "?"
        };
    }

    private Color NodeColor(JsonObject node)
    {
        return GameSpecLoader.GetString(node, "type") switch
        {
            "normal" => ColorCinnabar(),
            "elite" => ColorPurple(),
            "event" => ColorBlue(),
            "shop" or "forge" => ColorGold(),
            "boss" => new Color(0.73f, 0.30f, 0.14f, 1.0f),
            _ => ColorJade()
        };
    }

    private void UpdateInfo()
    {
        _infoLabel.Text = _runtime.Run.Count == 0
            ? _spec.Copy("game_title", GameSpecLoader.GetString(GameSpecLoader.GetObject(_spec.Data, "meta"), "display_name", "WorldSeed"))
            : _spec.Copy("health", "生命") + " " + _runtime.GetRunInt("hp") + "/" + _runtime.GetRunInt("max_hp") + "  " + _spec.Copy("gold", "金币") + " " + _runtime.GetRunInt("gold");
    }

    private void PlayFeedbackFlash()
    {
        _flashOverlay.Visible = true;
        _flashOverlay.Modulate = Colors.White;
        var tween = CreateTween();
        tween.TweenProperty(_flashOverlay, "modulate:a", 0.0, _spec.UiNumber("feedback_flash_seconds"));
        tween.Finished += HideFeedbackFlash;
    }

    private void HideFeedbackFlash()
    {
        _flashOverlay.Visible = false;
    }

    private void QuitGame()
    {
        GetTree().Quit();
    }

    private void LogCardLayout(string cardName, float width, float height, Control box, Control cardPanel, TextureRect frame)
    {
        if (_layoutCardLogs >= 20)
        {
            return;
        }
        _layoutCardLogs += 1;
        LogUi("card name=" + cardName + " target=" + new Vector2(width, height) + " box_min=" + box.CustomMinimumSize + " box_size=" + box.Size + " panel_min=" + cardPanel.CustomMinimumSize + " panel_size=" + cardPanel.Size + " frame_size=" + frame.Size + " texture_size=" + (frame.Texture == null ? Vector2.Zero : frame.Texture.GetSize()));
    }

    private void LogUi(string message)
    {
        if (_debugLayoutLogs)
        {
            GD.Print("[WorldSeed/UI] " + message);
        }
    }

    private int Stat(string key)
    {
        return _runtime.Run.TryGetValue("stats", out var value) && value is Dictionary<string, int> stats && stats.TryGetValue(key, out var number) ? number : 0;
    }

    private int StateInt(Dictionary<string, object> state, string key)
    {
        return state.TryGetValue(key, out var value) ? Convert.ToInt32(value) : 0;
    }

    private string StateString(Dictionary<string, object> state, string key)
    {
        return state.TryGetValue(key, out var value) ? Convert.ToString(value) ?? "" : "";
    }

    private StyleBox StylePanel()
    {
        var ui = _spec.GetAssetSection("ui");
        return StyleTexture(
            GameSpecLoader.GetString(ui, "panel"),
            UiInt("panel_texture_margin"),
            StyleBox(new Color(0.93f, 0.89f, 0.79f, 0.94f), new Color(0.45f, 0.36f, 0.25f, 1.0f), 8, 2)
        );
    }

    private StyleBox StyleButton(bool hover)
    {
        var ui = _spec.GetAssetSection("ui");
        return StyleTexture(
            GameSpecLoader.GetString(ui, hover ? "button_hover" : "button_normal"),
            UiInt("button_texture_margin"),
            StyleBox(hover ? new Color(0.62f, 0.27f, 0.19f, 1.0f) : new Color(0.46f, 0.22f, 0.15f, 1.0f), ColorGold(), 4, 2)
        );
    }

    private StyleBox StyleDisabledButton()
    {
        var ui = _spec.GetAssetSection("ui");
        return StyleTexture(
            GameSpecLoader.GetString(ui, "button_disabled"),
            UiInt("button_texture_margin"),
            StyleBox(new Color(0.64f, 0.60f, 0.50f, 0.85f), new Color(0.45f, 0.40f, 0.32f, 0.85f), 4, 1)
        );
    }

    private StyleBox StyleTexture(string path, int margin, StyleBoxFlat fallback)
    {
        if (string.IsNullOrEmpty(path))
        {
            return fallback;
        }

        var texture = GD.Load<Texture2D>(path);
        if (texture == null)
        {
            GD.PushWarning("UI texture missing: " + path);
            return fallback;
        }

        var style = new StyleBoxTexture();
        style.Texture = texture;
        style.TextureMarginLeft = margin;
        style.TextureMarginTop = margin;
        style.TextureMarginRight = margin;
        style.TextureMarginBottom = margin;
        style.AxisStretchHorizontal = StyleBoxTexture.AxisStretchMode.Stretch;
        style.AxisStretchVertical = StyleBoxTexture.AxisStretchMode.Stretch;
        return style;
    }

    private StyleBoxFlat StyleBox(Color bg, Color border, int radius, int borderWidth)
    {
        var style = new StyleBoxFlat();
        style.BgColor = bg;
        style.BorderColor = border;
        style.SetCornerRadiusAll(radius);
        style.SetBorderWidthAll(borderWidth);
        return style;
    }

    private int UiInt(string key)
    {
        return (int)_spec.UiNumber(key);
    }

    private float UiFloat(string key)
    {
        return (float)_spec.UiNumber(key);
    }

    private Color ColorInk() => new(0.19f, 0.17f, 0.14f, 1.0f);
    private Color ColorGold() => new(0.72f, 0.55f, 0.24f, 1.0f);
    private Color ColorJade() => new(0.20f, 0.51f, 0.46f, 1.0f);
    private Color ColorCinnabar() => new(0.61f, 0.21f, 0.15f, 1.0f);
    private Color ColorBlue() => new(0.29f, 0.54f, 0.65f, 1.0f);
    private Color ColorPurple() => new(0.36f, 0.24f, 0.54f, 1.0f);
}
