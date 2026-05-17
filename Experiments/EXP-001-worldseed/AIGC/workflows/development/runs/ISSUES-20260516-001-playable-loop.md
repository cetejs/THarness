# ISSUES-20260516-001-playable-loop

## 状态

- status: active
- source: 开发运行记录
- updated: 2026-05-16

## 记录规则

中途遇到问题时，先记录到本文件，再继续推进。只有阻塞到无法完成可玩闭环时，才在最终交付中说明残余风险。

## 问题

| ID | 状态 | 问题 | 处理 |
| --- | --- | --- | --- |
| DEV-001 | resolved | 试制素材复制到 `assets/` 时使用 `-LiteralPath` 通配符，导致素材未实际导入，GameSpec 素材引用验证失败。 | 改用 `Get-ChildItem` 枚举后逐文件复制，再重跑验证。 |
| DEV-002 | documented | 当前命令行环境未直接发现 Godot 可执行入口，无法立即执行 Godot headless 启动测试。 | 已完成静态验证、数据验证和工程结构检查；交付中说明用户可用 Godot 4.6 编辑器打开 `project.godot` 运行。 |
| DEV-003 | resolved | Godot 编译阶段可能因局部变量使用 `:=` 从 Variant/Dictionary 推断类型而报错。 | 将运行时脚本改为保守动态局部变量写法，移除风险 `:=` 和从 Dictionary 取值后的强类型局部变量。 |
| DEV-004 | resolved | `String.join` 对普通 Array 的兼容性不稳，可能在 Godot 编译或运行时出错。 | 改为 `_join_strings` 显式拼接。 |
| DEV-005 | resolved | 用户运行后反馈原型主要是文字界面，已有 PNG 素材没有充分体现在主要界面，也缺少操作反馈效果。 | 在 `Main.gd` 中接入 UI 面板、按钮纹理、卡框、资源图标、地图节点图标、意图/状态图标和反馈闪烁；在 GameSpec 增加 `ui_visual` 可调布局参数和插槽图标引用。 |
| DEV-006 | resolved | v0.3 卡牌化 UI 落地时，卡组列表的“详情”按钮可能被重复创建，程序化卡片也未展示自定义门类标识。 | 调整 `Main.gd` 的卡牌按钮生成逻辑；为程序化卡片补充 `kind` 字段并优先显示自定义门类首字。 |
| DEV-007 | resolved | 用户实机截图显示所有界面被全局滚动框包裹，奖励页横向溢出，资源条被挤成竖排。 | 移除 `Main.gd` 全局 `ScrollContainer`；奖励卡改为紧凑卡；牌组网格限制首批展示并显示剩余数量；资源徽章增加固定宽高；在 `check_gdscript_sanity.py` 增加全局滚动容器回归检查。 |
| DEV-008 | resolved | 用户实机截图显示运行窗口放大后游戏画面仍按固定 1280x720 居中，周围露出黑边，启动时没有铺满窗口。 | 在 `project.godot` 配置 `canvas_items` + `expand` stretch；在 `Main.gd` 启动和 viewport 尺寸变化时强制根 `Control` 铺满 viewport；在 `check_gdscript_sanity.py` 增加 stretch 配置回归检查。 |
| DEV-009 | resolved | 用户反馈斗法界面仍像普通控件拼接，未接近已确认的卡牌参考图。 | 将斗法页改为专用页眉；清除顶部红字提示；`Main.gd` 卡牌组件改为加载 `assets/cards/*.png` 卡框纹理；重新生成浅色卷轴风格卡框，包含彩色门类边框、黑色竖条、插画区、规则区和底部插槽。 |
| DEV-010 | resolved | 用户实机截图显示主菜单“最近远征”卡框被父容器横向拉伸，巨大卡框覆盖面板内容。 | 在 `Main.gd` 中锁定卡牌纹理容器尺寸，外层卡牌容器和卡牌画布均使用收缩布局，并启用卡牌画布裁剪；在 `check_gdscript_sanity.py` 增加卡牌固定尺寸回归检查。 |

## 2026-05-16 补充

- DEV-011 | resolved | 用户实机截图显示斗法界面在运行窗口中显示不全，手牌区被底部裁切。 | 将 Godot stretch 改为 `viewport + expand`，以 1280x720 作为逻辑画布整体缩放；斗法页新增 `combat_*` 尺寸配置；非交互卡牌不再预留按钮高度；布局日志补充真实窗口尺寸。 |
- DEV-012 | resolved | 用户运行日志显示 `viewport/window/root` 稳定，但斗法界面 `content` 高度从 620 持续累积到 783。 | 定位为 `ClearScreen()` 只 `QueueFree()` 旧节点，同一帧重建时旧节点仍参与布局；已改为先 `_contentBox.RemoveChild(child)` 再 `QueueFree()`，并增加 `clear children=` 回归日志。 |
