# UI 最小拆分规则验证记录

## 状态

- status: active
- source: `CHG-20260517-006-ui-minimal-slicing-rule.md`
- updated: 2026-05-17

## 验证目标

确认 UI 开发策划角色已沉淀主界面测试中确认的最小拆分、精确布局和素材规格规则。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| 角色职责更新 | 检查 `ui-development-planner-role.md` 的“职责”段落 | 已补充最小开发量、交互逻辑、精确布局和素材规格职责。 |
| 拆解原则新增 | 检查 `ui-development-planner-role.md` 的“UI 拆解原则”段落 | 已新增 `1920x1080`、`x/y/w/h`、背景合并、按钮文本分离和素材规格规则。 |
| 追溯索引 | 检查 `traceability/records/INDEX.md` | 已登记 `CHG-20260517-006-ui-minimal-slicing-rule` 和 `VER-20260517-006-ui-minimal-slicing-rule-check`。 |
| 文本编码 | 运行 `python tools/check_text_encoding.py` | 通过，扫描 519 个文件。 |

## 局限

本次只更新 UI 开发策划角色职责，不生成具体界面规格案，不修改工程代码或素材。

## 关联记录

- `CHG-20260517-006-ui-minimal-slicing-rule.md`
