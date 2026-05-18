# VER-20260517-001-bloomweaver-design-transfer-check

## 状态

- status: active
- source: 文件迁入检查
- updated: 2026-05-17

## 验证目标

确认实验二入口、BloomWeaver 策划案、UI 参考图和追溯记录可按规范检索。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| 实验二入口 | 检查 `Experiments/EXP-002-bloomweaver/README.md`、`AIGC/INDEX.md`、`AIGC/ADAPTER.md` 和 `AIGC/wiki/INDEX.md` | 通过，入口文件存在。 |
| 策划案文件 | 统计源目录和目标 `AIGC/wiki/design` 下 Markdown 文件数量 | 通过，源目录 27 个 Markdown，目标目录 27 个 Markdown。 |
| 图片链接 | 检查 `ui-effect-image-gallery.md` 中本地图片链接是否存在 | 通过，19 个图片链接，缺失 0 个。 |
| 旧图片路径残留 | 检查迁入设计目录中是否仍有旧 `Assets/界面` 图片路径 | 通过，未发现残留。 |
| 追溯闭合 | 检查 CHG、VER 和 `records/INDEX.md` 互相引用 | 通过，索引引用 CHG/VER，CHG 引用 VER，VER 反向引用 CHG。 |
| 文本编码 | 运行 `python tools\check_text_encoding.py` | 通过，扫描 506 个文本文件。 |
| 补丁空白 | 运行 `git diff --check` | 通过。 |

## 局限

本次只验证文档和引用迁入，不验证游戏运行时。

## 关联记录

- `CHG-20260517-001-bloomweaver-design-transfer`
