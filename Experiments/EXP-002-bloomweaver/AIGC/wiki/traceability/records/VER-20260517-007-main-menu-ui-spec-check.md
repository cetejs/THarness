# 主界面 UI 开发规格案验证记录

## 状态

- status: active
- source: `CHG-20260517-007-main-menu-ui-spec.md`
- updated: 2026-05-17

## 验证目标

确认主界面 UI 开发规格案已落成文档，并可从设计索引和追溯索引检索。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| 规格案存在 | 检查 `design/ui-screen-specs/main-menu-ui-spec.md` | 已存在。 |
| 规格案结构 | 检查基本信息、效果图绑定、层级、布局、文本、控件、数据、状态、素材、一致性验收和未决问题 | 已包含关键章节。 |
| 设计索引 | 检查 `design/INDEX.md` | 已登记 `ui-screen-specs/INDEX.md`。 |
| 追溯索引 | 检查 `traceability/records/INDEX.md` | 已登记 `CHG-20260517-007-main-menu-ui-spec` 和 `VER-20260517-007-main-menu-ui-spec-check`。 |
| 文本编码 | 运行 `python tools/check_text_encoding.py` | 通过，扫描 523 个文件。 |

## 局限

本次只创建 UI 开发规格案文档，不生成实际切图，不修改游戏工程代码。

## 关联记录

- `CHG-20260517-007-main-menu-ui-spec.md`
