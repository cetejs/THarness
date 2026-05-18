# VER-20260517-005-ui-role-output-protocol-check

## 状态

- status: active
- source: 文件和索引检查
- updated: 2026-05-17

## 验证目标

确认 UI 开发策划角色文档已明确新会话触发条件、固定文本和 `【详细内容】` 输出结构。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| 输出协议 | 检查 `ui-development-planner-role.md` 是否包含“角色输出协议” | 通过。 |
| 详细内容标题 | 检查固定格式是否包含 `【详细内容】` | 通过。 |
| 新会话要求 | 检查角色文档是否包含“新会话启动要求” | 通过。 |
| 追溯闭合 | 检查 CHG、VER 和 `records/INDEX.md` 互相引用 | 通过，索引引用 CHG/VER，CHG 引用 VER，VER 反向引用 CHG。 |
| 文本编码 | 运行 `python tools\check_text_encoding.py` | 通过，扫描 517 个文本文件。 |
| 补丁空白 | 运行 `git diff --check` | 通过。 |

## 局限

本次只验证角色文档规则写入，不验证另一个新会话是否实际遵循。

## 关联记录

- `CHG-20260517-005-ui-role-output-protocol`
