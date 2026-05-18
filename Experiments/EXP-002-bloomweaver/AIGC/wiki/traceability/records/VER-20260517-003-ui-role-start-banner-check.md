# VER-20260517-003-ui-role-start-banner-check

## 状态

- status: active
- source: 文件和索引检查
- updated: 2026-05-17

## 验证目标

确认 UI 开发策划角色文档已包含出场固定声明，并且追溯记录闭合。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| 固定声明 | 检查 `ui-development-planner-role.md` 是否包含“出场固定声明”和三行固定文本 | 通过，角色名称、主要职责和工作依据均已写入。 |
| 追溯闭合 | 检查 CHG、VER 和 `records/INDEX.md` 互相引用 | 通过，索引引用 CHG/VER，CHG 引用 VER，VER 反向引用 CHG。 |
| 文本编码 | 运行 `python tools\check_text_encoding.py` | 通过，扫描 513 个文本文件。 |
| 补丁空白 | 运行 `git diff --check` | 通过。 |

## 局限

本次只验证固定声明写入，不验证后续具体界面策划案执行效果。

## 关联记录

- `CHG-20260517-003-ui-role-start-banner`
