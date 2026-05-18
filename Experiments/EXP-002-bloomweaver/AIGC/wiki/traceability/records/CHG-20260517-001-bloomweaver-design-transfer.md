# CHG-20260517-001-bloomweaver-design-transfer

## 状态

- status: active
- source: 用户请求迁入 BloomWeaver 策划案
- updated: 2026-05-17

## 来源

- 用户请求：阅读仓库启动要求后，开始实验二，并将 `D:\UnityDemo\Project_BloomWeaver\AIGC\projects\Project_BloomWeaver\wiki\design` 中的策划案按规范转移。
- 关联需求：无独立 REQ，来自本次用户请求。
- 关联决策：`DEC-20260517-001`、`DEC-20260517-002`
- 关联实验：`EXP-002-bloomweaver`
- 关联开发任务：无。

## 新增内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 实验登记 | `Experiments/INDEX.md` | 增加实验二入口。 |
| 实验目录 | `Experiments/EXP-002-bloomweaver/` | 承接 BloomWeaver 实验二内容。 |
| 项目适配层 | `Experiments/EXP-002-bloomweaver/AIGC/` | 保存实验二项目上下文、wiki 和追溯。 |
| 策划案 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/design/` | 迁入用户指定的 BloomWeaver 设计文档。 |
| UI 参考图 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/design/images/ui-reference-20260517/` | 保证设计图集引用在实验二目录内可达。 |
| 来源地图 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/source-map/` | 记录旧项目来源和迁入路径。 |
| 追溯账本 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/traceability/` | 登记本次新增内容和验证结果。 |

## 影响范围

- 只新增实验二目录和更新实验总索引。
- 不删除或修改 `D:\UnityDemo\Project_BloomWeaver` 源目录。
- 不修改实验一项目事实。
- 不写入通用 `AIGC.Framework/`。

## 验证方式

- 检查实验二入口文件存在。
- 检查迁入 Markdown 文件数量。
- 检查 `ui-effect-image-gallery.md` 中 19 个图片链接均指向实验二目录内存在文件。
- 运行 `python tools\check_text_encoding.py`。

## 验证结果

见 `VER-20260517-001-bloomweaver-design-transfer-check`。

## 是否晋升为项目事实

是。实验二启动事实、策划案入口和来源地图写入 BloomWeaver 项目 wiki。

## 后续事项

- 确认实验二目标引擎。
- 确认是否迁入旧 BloomWeaver 工程中的开发契约。
