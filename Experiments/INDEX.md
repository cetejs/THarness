# 实验入口

本目录保存用于验证通用游戏 AIGC 框架的实验项目。实验项目可以包含真实游戏工程、项目 AIGC 适配层、输入材料、输出产物、验证记录和复盘候选经验。

## 实验列表

| 实验 | 状态 | 入口 | 说明 |
| --- | --- | --- | --- |
| `EXP-001-worldseed` | active | `EXP-001-worldseed/README.md` | 第一个 Godot .NET/C# 游戏实验，用于验证通用游戏开发流程。 |
| `EXP-002-bloomweaver` | active | `EXP-002-bloomweaver/README.md` | 第二个游戏实验，用于迁入 BloomWeaver 策划案并准备后续引擎迁移验证。 |

## 写入边界

- 实验项目事实写入对应实验的 `AIGC/`。
- 实验工程代码写入对应实验的 `project/`。
- 实验输入写入对应实验的 `inputs/`。
- 实验输出写入对应实验的 `outputs/`。
- 实验验证写入对应实验的 `validation/`。
- 可晋升为通用框架的候选经验写入对应实验的 `retro/`，复核后再进入 `../AIGC.Framework/`。
