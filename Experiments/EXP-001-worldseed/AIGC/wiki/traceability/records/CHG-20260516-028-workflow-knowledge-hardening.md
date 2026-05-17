# CHG-20260516-028-workflow-knowledge-hardening

## 状态

- status: active
- source: 用户要求沉淀本次开发过程中剩余的可复用知识
- updated: 2026-05-16

## 来源

本次来源于 WorldSeed UI 开发与文档沉淀复盘：战斗界面曾因同帧清空重建和延迟释放语义导致布局累积，文档沉淀过程中也暴露出 CHG、VER、记录文件和索引之间需要更明确的闭合检查。

## 变更内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 通用规则 | `THarness/AIGC/workflows/game-development-lifecycle/rules/debug-observability.md` | 补充 UI 同帧重建、延迟销毁和 Godot 节点生命周期检查。 |
| 通用规则 | `THarness/AIGC/projects/rules/project-wiki-update.md` | 补充 CHG、VER 和 `records/INDEX.md` 的追溯闭合要求。 |
| 项目规则 | `WorldSeed.AIGC/wiki/traceability/rules.md` | 将追溯闭合检查写入 WorldSeed 项目规则。 |
| 项目规则 | `WorldSeed.AIGC/wiki/traceability/ids.md` | 明确创建新 ID 前必须查最大编号，禁止复用编号。 |
| 能力索引 | `THarness/AIGC/capabilities/` | 将系统版本升级到 `2.7.0`，并登记 UI 节点生命周期和追溯闭合检查能力。 |
| 自检 | `THarness/tools/test_oneharness.py` | 增加 UI 节点生命周期和项目 wiki 追溯闭合的回归检查。 |
| 追溯记录 | `WorldSeed.AIGC/wiki/traceability/records/` | 登记本次知识沉淀的 CHG、VER 和索引条目。 |

## 影响范围

- 影响后续游戏开发生命周期中的 UI 运行时排查流程。
- 影响后续项目 wiki 更新时的追溯记录创建和检查方式。
- 不修改 WorldSeed 游戏运行时代码、玩法数据或素材。
- 不把 WorldSeed 具体节点路径、运行日志、截图或项目事实写入 THarness。

## 验证方式

- `python THarness\tools\test_oneharness.py`
- `python tools\check_text_encoding.py --root .`
- `git diff --check`

## 验证结果

已通过 `VER-20260516-029-workflow-knowledge-hardening-check` 验证。

## 是否晋升为项目事实

是。WorldSeed 后续处理 UI 同帧刷新、布局累积或追溯记录新增时，应按本次规则执行生命周期检查和 CHG/VER/INDEX 闭合检查。
