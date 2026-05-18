# CHG-20260517-005-ui-role-output-protocol

## 状态

- status: active
- source: 用户反馈新会话未按固定文本和详细内容输出
- updated: 2026-05-17

## 来源

- 用户请求：新会话中要求按 UI 策划身份交流时，没有按照固定文本加详细内容的方式输出，需要修正角色定义。
- 关联需求：无独立 REQ，来自本次用户请求。
- 关联决策：UI 开发策划需要明确触发条件和固定输出协议。
- 关联实验：`EXP-002-bloomweaver`
- 关联开发任务：无。本次不进入程序开发。

## 新增内容

| 类型 | 路径 | 原因 |
| --- | --- | --- |
| 角色规则 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/design/ui-development-planner-role.md` | 将“出场固定声明”升级为“角色输出协议”，补充触发条件、固定文本、`【详细内容】` 和新会话启动要求。 |
| 追溯索引 | `Experiments/EXP-002-bloomweaver/AIGC/wiki/traceability/records/INDEX.md` | 登记本次变更和验证记录。 |

## 影响范围

- 只影响实验二 UI 开发策划角色文档。
- 不修改 UI 规格模板字段。
- 不创建程序开发任务。
- 不晋升到 `AIGC.Framework/`。

## 验证方式

- 检查角色文档包含“角色输出协议”。
- 检查角色文档包含 `【详细内容】` 固定标题。
- 检查角色文档包含“新会话启动要求”。
- 检查 CHG、VER 和 `records/INDEX.md` 互相引用。
- 运行 `python tools\check_text_encoding.py`。
- 运行 `git diff --check`。

## 验证结果

见 `VER-20260517-005-ui-role-output-protocol-check`。

## 是否晋升为项目事实

是。该输出协议是实验二 UI 开发策划角色的项目级工作规则。

## 后续事项

- 后续新会话使用 UI 开发策划身份时，先读取角色文档并按固定协议输出。
- 若验证仍不稳定，再考虑将该协议沉淀到更高层入口或通用框架。
