using System.Collections.Generic;
using System.Text.Json.Nodes;
using Godot;

public sealed class GameSpecLoader
{
    private const string SpecPath = "res://data/game_spec/ascension_forge.prototype.json";

    public JsonObject Data { get; private set; } = new();
    public Dictionary<string, JsonObject> Cards { get; private set; } = new();
    public Dictionary<string, JsonObject> Characters { get; private set; } = new();
    public Dictionary<string, JsonObject> Equipment { get; private set; } = new();
    public Dictionary<string, JsonObject> Talents { get; private set; } = new();
    public Dictionary<string, JsonObject> Enemies { get; private set; } = new();
    public Dictionary<string, JsonObject> Encounters { get; private set; } = new();
    public Dictionary<string, JsonObject> Events { get; private set; } = new();
    public Dictionary<string, JsonObject> Shops { get; private set; } = new();
    public Dictionary<string, JsonObject> Chapters { get; private set; } = new();
    public Dictionary<string, JsonObject> RewardPools { get; private set; } = new();
    public Dictionary<string, JsonObject> MapProfiles { get; private set; } = new();

    public bool LoadSpec()
    {
        var text = FileAccess.GetFileAsString(SpecPath);
        if (string.IsNullOrEmpty(text))
        {
            GD.PushError("GameSpec 读取失败: " + SpecPath);
            return false;
        }

        var parsed = JsonNode.Parse(text) as JsonObject;
        if (parsed == null)
        {
            GD.PushError("GameSpec JSON 格式无效");
            return false;
        }

        Data = parsed;
        IndexAll();
        return true;
    }

    public JsonObject FirstCharacter()
    {
        var items = GetArray(Data, "characters");
        return items.Count == 0 ? new JsonObject() : AsObject(items[0]);
    }

    public JsonObject FirstChapter()
    {
        var items = GetArray(Data, "chapters");
        return items.Count == 0 ? new JsonObject() : AsObject(items[0]);
    }

    public string DisplayName(Dictionary<string, JsonObject> section, string itemId)
    {
        return section.TryGetValue(itemId, out var item) ? GetString(item, "display_name", itemId) : itemId;
    }

    public string Copy(string key, string fallback)
    {
        return GetString(GetObject(Data, "ui_copy"), key, fallback);
    }

    public double UiNumber(string key)
    {
        var visual = GetObject(Data, "ui_visual");
        var value = visual[key];
        if (value != null && value.GetValueKind() == System.Text.Json.JsonValueKind.Number)
        {
            return value.GetValue<double>();
        }

        var fallback = new Dictionary<string, double>
        {
            ["window_margin"] = 24,
            ["content_spacing"] = 12,
            ["compact_spacing"] = 6,
            ["title_font_size"] = 26,
            ["body_font_size"] = 18,
            ["small_font_size"] = 15,
            ["tiny_font_size"] = 13,
            ["button_width"] = 240,
            ["button_height"] = 40,
            ["button_texture_margin"] = 12,
            ["panel_texture_margin"] = 24,
            ["card_width"] = 150,
            ["card_height"] = 220,
            ["mini_card_width"] = 132,
            ["mini_card_height"] = 190,
            ["deck_grid_columns"] = 3,
            ["combat_log_visible_lines"] = 4,
            ["feedback_flash_seconds"] = 0.18
        };
        return fallback.GetValueOrDefault(key, 0);
    }

    public bool UiBool(string key, bool fallback)
    {
        var value = GetObject(Data, "ui_visual")[key];
        return value != null && value.GetValueKind() == System.Text.Json.JsonValueKind.True ? true :
            value != null && value.GetValueKind() == System.Text.Json.JsonValueKind.False ? false : fallback;
    }

    public Color UiColor(string key)
    {
        var value = GetArray(GetObject(Data, "ui_visual"), key);
        if (value.Count >= 4)
        {
            return new Color(GetFloat(value[0]), GetFloat(value[1]), GetFloat(value[2]), GetFloat(value[3]));
        }

        return key == "feedback_flash_color"
            ? new Color(0.78f, 0.54f, 0.20f, 0.24f)
            : new Color(0.91f, 0.88f, 0.81f, 1.0f);
    }

    public JsonObject GetAssetSection(string key)
    {
        return GetObject(GetObject(Data, "assets"), key);
    }

    public static JsonObject GetObject(JsonObject obj, string key)
    {
        return obj.TryGetPropertyValue(key, out var value) && value is JsonObject nested ? nested : new JsonObject();
    }

    public static JsonArray GetArray(JsonObject obj, string key)
    {
        return obj.TryGetPropertyValue(key, out var value) && value is JsonArray array ? array : new JsonArray();
    }

    public static JsonObject AsObject(JsonNode node)
    {
        return node as JsonObject ?? new JsonObject();
    }

    public static string GetString(JsonObject obj, string key, string fallback = "")
    {
        var value = obj[key];
        return value == null ? fallback : value.GetValue<string>();
    }

    public static int GetInt(JsonObject obj, string key, int fallback = 0)
    {
        var value = obj[key];
        return value == null ? fallback : value.GetValue<int>();
    }

    public static float GetFloat(JsonNode node)
    {
        return node == null ? 0.0f : node.GetValue<float>();
    }

    public static List<string> GetStringList(JsonObject obj, string key)
    {
        var output = new List<string>();
        foreach (var item in GetArray(obj, key))
        {
            if (item != null)
            {
                output.Add(item.GetValue<string>());
            }
        }
        return output;
    }

    public static bool HasString(JsonObject obj, string key, string value)
    {
        return GetStringList(obj, key).Contains(value);
    }

    private void IndexAll()
    {
        Cards = IndexById(GetArray(Data, "cards"));
        Characters = IndexById(GetArray(Data, "characters"));
        Equipment = IndexById(GetArray(Data, "equipment"));
        Talents = IndexById(GetArray(Data, "talents"));
        Enemies = IndexById(GetArray(Data, "enemies"));
        Encounters = IndexById(GetArray(Data, "encounters"));
        Events = IndexById(GetArray(Data, "events"));
        Shops = IndexById(GetArray(Data, "shops"));
        Chapters = IndexById(GetArray(Data, "chapters"));
        RewardPools = IndexById(GetArray(GetObject(Data, "rewards"), "pools"));
        MapProfiles = IndexById(GetArray(GetObject(Data, "map_generation"), "profiles"));
    }

    private static Dictionary<string, JsonObject> IndexById(JsonArray items)
    {
        var output = new Dictionary<string, JsonObject>();
        foreach (var item in items)
        {
            var obj = AsObject(item);
            var id = GetString(obj, "id");
            if (!string.IsNullOrEmpty(id))
            {
                output[id] = obj;
            }
        }
        return output;
    }
}
