# EXP-002-bloomweaver 项目适配配置

## 配置

```yaml
project_name: BloomWeaver
experiment_id: EXP-002-bloomweaver
repository_root: D:\UnityDemo\WroldSeed
experiment_root: Experiments/EXP-002-bloomweaver
project_root: Experiments/EXP-002-bloomweaver/project
project_aigc_root: Experiments/EXP-002-bloomweaver/AIGC
project_wiki_root: Experiments/EXP-002-bloomweaver/AIGC/wiki
workflow_runs_root: Experiments/EXP-002-bloomweaver/AIGC/workflows
general_harness_root: AIGC.Framework
active_workflow: project-wiki-maintenance
engine_target: 未确认
source_design_root: D:\UnityDemo\Project_BloomWeaver\AIGC\projects\Project_BloomWeaver\wiki\design
created_at: 2026-05-17
```

## 调用规则

- 需要 BloomWeaver 项目事实时，读取 `Experiments/EXP-002-bloomweaver/AIGC/wiki/INDEX.md` 并按索引命中具体页面。
- 需要通用工作流规则时，读取 `AIGC.Framework/INDEX.md` 并按其工作流路由继续读取。
- 开发任务必须先写入 `Experiments/EXP-002-bloomweaver/AIGC/wiki/development/tasks/`。
- 子任务必须写入 `Experiments/EXP-002-bloomweaver/AIGC/wiki/development/subtasks/`。
- 跨模块接口必须写入 `Experiments/EXP-002-bloomweaver/AIGC/wiki/development/contracts/`。
- 运行记录必须写入 `Experiments/EXP-002-bloomweaver/AIGC/workflows/{workflow_id}/runs/`。

## 路径说明

BloomWeaver 当前只迁入策划案和 UI 参考图。实验二工程目录已预留，目标引擎和工程结构尚未确认。
