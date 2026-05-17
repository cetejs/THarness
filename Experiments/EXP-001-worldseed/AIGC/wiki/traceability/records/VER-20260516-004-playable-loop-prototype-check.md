# VER-20260516-004-playable-loop-prototype-check

## 状态

- status: active
- source: 本地命令验证和静态检查
- updated: 2026-05-16

## 验证目标

验证第一阶段最小可玩闭环原型的数据、素材、主要界面素材接入、项目结构和基础文本编码。

## 验证项

| 验证项 | 方式 | 结果 |
| --- | --- | --- |
| GameSpec 数据和素材引用完整 | `python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .` | 通过 |
| 最小可玩链路数据闭合 | `python tools\smoke_playable_loop.py` | 通过 |
| GDScript 静态风险检查 | `python tools\check_gdscript_sanity.py` | 通过 |
| 文本编码 | `python tools\check_text_encoding.py --root .` | 通过 |
| Godot 主场景存在 | 检查 `project.godot`、`scenes/main.tscn` 和主脚本路径 | 通过 |
| 脚本单类约束 | 检索 `scripts/` 中无额外 `class` 声明 | 通过 |
| 素材导入 | 检查 `assets/` 下 34 个 PNG 素材 | 通过 |
| 主要界面素材接入 | 检查 `scripts/Main.gd` 渲染 UI 面板、按钮纹理、卡框、资源图标、地图节点图标和状态图标 | 通过 |

## 局限

当前命令行环境未发现 Godot 可执行入口，因此未执行 Godot headless 启动测试。工程已配置主场景，可使用 Godot 4.6 编辑器打开 `project.godot` 运行。

## 关联记录

- `CHG-20260516-004-playable-loop-prototype`
- `RUN-20260516-001-playable-loop-development`
- `ISSUES-20260516-001-playable-loop`
