# CHG-20260516-003 game-iteration 路由和测试补充

## 状态

- status: active
- source: 用户确认和本轮 review 发现
- updated: 2026-05-16

## 来源

- 用户请求：补充 `THarness` 新增游戏开发工作流验证中发现的缺口。
- 关联需求：无
- 关联决策：无
- 关联实验：无
- 关联开发任务：无

## 新增内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 文档 | `THarness/AIGC/README.md` | 让通用入口能路由到 `game-iteration`。 |
| 文档 | `THarness/AIGC/workflows/game-iteration/WORKFLOW.md` | 让工作流默认读取链能到达模板索引。 |
| 测试 | `THarness/tools/test_oneharness.py` | 增加 `game-iteration` 工作流、规则和模板可达性回归测试。 |
| 追溯 | `WorldSeed.AIGC/wiki/traceability/records/VER-20260516-003-game-iteration-route-test.md` | 记录本次验证结果。 |

## 影响范围

- `game-iteration` 从通用 README、工作流索引、能力索引、规则索引和模板索引均可被检索。
- 后续修改 `game-iteration` 入口、规则或模板时，单元测试能覆盖最小可达性。

## 验证方式

- `python tools\oneharness.py doctor`
- `python tools\oneharness.py gate`
- `python -m unittest tools.test_oneharness`
- `python ..\tools\check_text_encoding.py`

## 验证结果

见 `VER-20260516-003-game-iteration-route-test.md`。

## 是否晋升为项目事实

是。本次补充是当前通用游戏迭代工作流的正式路由和测试约束。

## 后续事项

- 后续可考虑把 `game-iteration` 自检覆盖扩展到模板字段完整性。
