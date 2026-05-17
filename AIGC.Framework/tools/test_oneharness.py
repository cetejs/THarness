from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "tools" / "oneharness.py"


class OneHarnessCliTests(unittest.TestCase):
    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(CLI), *args],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_unknown_command_fails(self) -> None:
        result = self.run_cli("unknown")
        self.assertEqual(result.returncode, 2)
        self.assertIn("未知命令", result.stderr)

    def test_missing_config_fails(self) -> None:
        result = self.run_cli("doctor", "--config", "missing.yaml")
        self.assertEqual(result.returncode, 2)
        self.assertIn("配置文件不存在", result.stderr)

    def test_doctor_passes_current_repo(self) -> None:
        result = self.run_cli("doctor")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("doctor: PASS", result.stdout)

    def test_index_write_passes_current_repo(self) -> None:
        result = self.run_cli("index", "--write")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("index: PASS", result.stdout)
        self.assertIn("索引已写入", result.stdout)

    def test_self_check_requires_path_or_delivery(self) -> None:
        result = self.run_cli("self-check")
        self.assertEqual(result.returncode, 2)
        self.assertIn("至少一个 --path 或 --delivery", result.stderr)

    def test_self_check_plans_wiki_and_delivery_commands(self) -> None:
        result = self.run_cli("self-check", "--path", "wiki\\architecture\\entry-map.md", "--delivery")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("python tools\\oneharness.py index --check", result.stdout)
        self.assertIn("python tools\\oneharness.py gate", result.stdout)

    def test_self_check_plans_tool_commands(self) -> None:
        result = self.run_cli("self-check", "--path", "tools\\oneharness.py")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("python tools\\oneharness.py gate", result.stdout)
        self.assertIn("python -m unittest tools.test_oneharness", result.stdout)

    def test_game_design_methodology_is_routable(self) -> None:
        rules_index = (ROOT / "workflows/planning-discussion/rules/INDEX.md").read_text(encoding="utf-8")
        template_index = (ROOT / "workflows/planning-discussion/templates/INDEX.md").read_text(encoding="utf-8")
        method_index = (ROOT / "workflows/planning-discussion/method-cards/INDEX.md").read_text(encoding="utf-8")

        self.assertIn("game-design-methodology.md", rules_index)
        self.assertIn("game-design-plan.md", template_index)
        self.assertIn("design-and-maintenance.md", method_index)
        self.assertIn("phase-index.md", method_index)
        self.assertIn("trigger-index.md", method_index)

    def test_game_iteration_workflow_is_routable(self) -> None:
        workflow_index = (ROOT / "workflows/INDEX.md").read_text(encoding="utf-8")
        capability_index = (ROOT / "capabilities/INDEX.md").read_text(encoding="utf-8")
        workflow = (ROOT / "workflows/game-iteration/WORKFLOW.md").read_text(encoding="utf-8")
        rules_index = (ROOT / "workflows/game-iteration/rules/INDEX.md").read_text(encoding="utf-8")
        template_index = (ROOT / "workflows/game-iteration/templates/INDEX.md").read_text(encoding="utf-8")

        self.assertIn("game-iteration", workflow_index)
        self.assertIn("../workflows/game-iteration/WORKFLOW.md", capability_index)
        self.assertIn("templates/INDEX.md", workflow)
        self.assertIn("intake.md", rules_index)
        self.assertIn("playable-loop-ui.md", rules_index)
        self.assertIn("ui-ux-development-spec.md", rules_index)
        self.assertIn("data-blueprint.md", rules_index)
        self.assertIn("development-gate.md", rules_index)
        self.assertIn("game-iteration-brief.md", template_index)
        self.assertIn("playable-loop-ui-plan.md", template_index)
        self.assertIn("ui-ux-development-spec.md", template_index)
        self.assertIn("game-data-blueprint.md", template_index)
        self.assertIn("development-gate-plan.md", template_index)

        ui_spec = (ROOT / "workflows/game-iteration/rules/ui-ux-development-spec.md").read_text(encoding="utf-8")
        ui_template = (ROOT / "workflows/game-iteration/templates/ui-ux-development-spec.md").read_text(encoding="utf-8")

        self.assertIn("UI/UX 可开发规格", workflow)
        self.assertIn("hitbox", ui_spec)
        self.assertIn("素材边界", ui_spec)
        self.assertIn("交互和 hitbox 合同", ui_template)
        self.assertIn("验收标准", ui_template)

    def test_game_development_lifecycle_workflow_is_hardened(self) -> None:
        workflow_index = (ROOT / "workflows/INDEX.md").read_text(encoding="utf-8")
        capability_index = (ROOT / "capabilities/INDEX.md").read_text(encoding="utf-8")
        workflow = (ROOT / "workflows/game-development-lifecycle/WORKFLOW.md").read_text(encoding="utf-8")
        stage_gates = (ROOT / "workflows/game-development-lifecycle/rules/stage-gates.md").read_text(encoding="utf-8")
        ui_rules = (ROOT / "workflows/game-development-lifecycle/rules/ui-visual-runtime.md").read_text(encoding="utf-8")
        debug_rules = (ROOT / "workflows/game-development-lifecycle/rules/debug-observability.md").read_text(encoding="utf-8")
        verification_rules = (ROOT / "workflows/game-development-lifecycle/rules/verification-and-retro.md").read_text(encoding="utf-8")
        template_index = (ROOT / "workflows/game-development-lifecycle/templates/INDEX.md").read_text(encoding="utf-8")
        screen_contract = (ROOT / "workflows/game-development-lifecycle/templates/screen-contract.md").read_text(encoding="utf-8")
        verification_template = (ROOT / "workflows/game-development-lifecycle/templates/verification-retro.md").read_text(encoding="utf-8")
        asset_contract = (ROOT / "workflows/game-development-lifecycle/templates/asset-pipeline-contract.md").read_text(encoding="utf-8")
        project_sync = (ROOT / "workflows/game-development-lifecycle/templates/project-execution-sync-check.md").read_text(encoding="utf-8")

        self.assertIn("game-development-lifecycle", workflow_index)
        self.assertIn("../workflows/game-development-lifecycle/WORKFLOW.md", capability_index)
        self.assertIn("开发前硬门禁", workflow)
        self.assertIn("素材管线合同", workflow)
        self.assertIn("开发前硬门禁清单", stage_gates)
        self.assertIn("hitbox", ui_rules)
        self.assertIn("素材管线合同", ui_rules)
        self.assertIn("UI 节点生命周期检查", debug_rules)
        self.assertIn("RemoveChild", debug_rules)
        self.assertIn("QueueFree", debug_rules)
        self.assertIn("交互验证", verification_rules)
        self.assertIn("development-readiness-checklist.md", template_index)
        self.assertIn("asset-pipeline-contract.md", template_index)
        self.assertIn("project-execution-sync-check.md", template_index)
        self.assertIn("交互命中区", screen_contract)
        self.assertIn("关键控件证据", verification_template)
        self.assertIn("引擎导入缓存刷新", asset_contract)
        self.assertIn("项目侧执行同步", workflow)
        self.assertIn("项目侧执行同步门禁", stage_gates)
        self.assertIn("项目侧同步检查", verification_rules)
        self.assertIn("构建测试运行入口", project_sync)

    def test_project_wiki_update_traceability_closure_is_routable(self) -> None:
        projects_index = (ROOT / "projects/INDEX.md").read_text(encoding="utf-8")
        project_rules_index = (ROOT / "projects/rules/INDEX.md").read_text(encoding="utf-8")
        update_rule = (ROOT / "projects/rules/project-wiki-update.md").read_text(encoding="utf-8")
        capability_index = (ROOT / "capabilities/INDEX.md").read_text(encoding="utf-8")

        self.assertIn("rules/project-wiki-update.md", projects_index)
        self.assertIn("project-wiki-update.md", project_rules_index)
        self.assertIn("CHG、VER 和索引追溯闭合", capability_index)
        self.assertIn("追溯闭合要求", update_rule)
        self.assertIn("最大编号", update_rule)
        self.assertIn("records/INDEX.md", update_rule)
        self.assertIn("CHG", update_rule)
        self.assertIn("VER", update_rule)


if __name__ == "__main__":
    unittest.main()
