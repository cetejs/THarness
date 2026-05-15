# 构建测试运行

## 状态

- status: active
- source: 当前仓库扫描
- updated: 2026-05-15

## 当前可运行验证

```powershell
cd D:\UnityDemo\WroldSeed
python tools\check_text_encoding.py

cd D:\UnityDemo\WroldSeed\THarness
python tools\oneharness.py gate
python -m unittest tools.test_oneharness
```

## 待补充

- Godot 可执行文件路径。
- Godot headless 运行命令。
- Godot smoke test。
- 生成器单元测试。
- GameSpec schema 校验命令。
