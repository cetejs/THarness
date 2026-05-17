# 构建测试运行

## 状态

- status: active
- source: 当前仓库扫描
- updated: 2026-05-15

## 当前可运行验证

```powershell
cd D:\UnityDemo\WroldSeed
python tools\check_text_encoding.py

cd D:\UnityDemo\WroldSeed\AIGC.Framework
python tools\oneharness.py gate
python -m unittest tools.test_oneharness

cd D:\UnityDemo\WroldSeed\Experiments\EXP-001-worldseed\project
dotnet build WorldSeed.csproj
python tools\check_gdscript_sanity.py
python tools\validate_game_spec.py data\game_spec\ascension_forge.prototype.json --project-root .
python tools\smoke_playable_loop.py
```

## Godot 运行入口

```powershell
cd D:\UnityDemo\WroldSeed\Experiments\EXP-001-worldseed\project
& 'E:\Godot\4.6.2-stable-mono\Godot_v4.6.2-stable_mono_win64\Godot_v4.6.2-stable_mono_win64_console.exe' --headless --path . --build-solutions --quit
& 'E:\Godot\4.6.2-stable-mono\Godot_v4.6.2-stable_mono_win64\Godot_v4.6.2-stable_mono_win64_console.exe' --headless --editor --path . --quit
& 'E:\Godot\4.6.2-stable-mono\Godot_v4.6.2-stable_mono_win64\Godot_v4.6.2-stable_mono_win64_console.exe' --headless --path . --quit-after 3
```

目录迁移、资源覆盖或 `.godot/imported` 缓存缺失后，先执行 `--headless --editor --path . --quit` 刷新导入缓存，再执行启动检查。

## 待补充

- 生成器单元测试。
- GameSpec schema 校验命令。
