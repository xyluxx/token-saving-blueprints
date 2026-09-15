import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load_validation(test):
    path = ROOT / "scripts" / "validation.py"
    test.assertTrue(path.is_file(), "repository validator is not implemented")
    spec = importlib.util.spec_from_file_location("blueprint_validation", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class LinkTests(unittest.TestCase):
    def test_missing_local_document_is_reported(self):
        validation = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("[Guide](docs/missing.md)\n", encoding="utf-8")
            findings = validation.validate_links(root)
            self.assertEqual(len(findings), 1)
            self.assertIn("missing local link", findings[0])

    def test_valid_document_and_duplicate_heading_anchor(self):
        validation = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("[Guide](guide.md#repeat-1)\n", encoding="utf-8")
            (root / "guide.md").write_text("# Repeat\n## Repeat\n", encoding="utf-8")
            self.assertEqual(validation.validate_links(root), [])

    def test_missing_anchor_is_reported(self):
        validation = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("# Present\n[No](#absent)\n", encoding="utf-8")
            self.assertTrue(any("anchor" in x for x in validation.validate_links(root)))

    def test_code_examples_do_not_create_navigation_links(self):
        validation = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("```md\n[Example](missing.md)\n```\n`[Example](missing.md)`\n", encoding="utf-8")
            self.assertEqual(validation.validate_links(root), [])

    def test_local_links_cannot_escape_repository(self):
        validation = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            root.mkdir()
            (root.parent / "outside.md").write_text("private fixture", encoding="utf-8")
            (root / "README.md").write_text("[No](../outside.md)\n", encoding="utf-8")
            self.assertTrue(any("outside" in x for x in validation.validate_links(root)))

    def test_unsafe_uri_is_rejected(self):
        validation = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("[No](javascript:alert)\n", encoding="utf-8")
            self.assertTrue(any("scheme" in x for x in validation.validate_links(root)))

    def test_reference_style_local_link_is_checked(self):
        validation = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("[Guide][local]\n\n[local]: missing.md\n", encoding="utf-8")
            self.assertTrue(validation.validate_links(root))

    def test_symlinked_document_is_not_read(self):
        validation = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            root.mkdir()
            source = root.parent / "outside.md"
            source.write_text("private fixture", encoding="utf-8")
            try:
                (root / "linked.md").symlink_to(source)
            except OSError:
                self.skipTest("symlink creation unavailable")
            self.assertTrue(any("symlink" in x for x in validation.validate_links(root)))


class RouteTests(unittest.TestCase):
    def make_repo(self, root):
        import json
        guide = root / "docs" / "harnesses" / "example.md"
        guide.parent.mkdir(parents=True)
        guide.write_text("\n".join("## " + h for h in [
            "Who this is for", "Authentication and billing routes", "Conservative recipe",
            "Aggressive recipe", "Verify and roll back", "Limits and evidence", "Sources"
        ]), encoding="utf-8")
        catalog = root / "catalog"
        catalog.mkdir()
        row = {
            "id": "example-native", "harness": "Example", "auth_path": "native login",
            "provider_path": "native", "support_level": "documented", "control": "advisory",
            "guide": "docs/harnesses/example.md", "conservative": "Exact reads",
            "aggressive": "Only explicit context", "caveats": ["Synthetic test fixture"],
            "sources": ["https://example.invalid/docs"], "checked_on": "2000-01-01"
        }
        (catalog / "routes-primary.json").write_text(json.dumps([row]), encoding="utf-8")
        (catalog / "routes-editors.json").write_text("[]", encoding="utf-8")
        (catalog / "harnesses.json").write_text(json.dumps([{
            "id": "example", "name": "Example", "aliases": ["Example"],
            "guide": "docs/harnesses/example.md", "status": "documented-guidance"
        }]), encoding="utf-8")
        return row

    def test_valid_route_is_accepted(self):
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "validate_routes", None)), "route checker is missing")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_repo(root)
            self.assertEqual(v.validate_routes(root, {"example"}), [])

    def test_duplicate_route_id_is_rejected(self):
        import json
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "validate_routes", None)), "route checker is missing")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            row = self.make_repo(root)
            (root / "catalog/routes-editors.json").write_text(json.dumps([row]), encoding="utf-8")
            self.assertTrue(any("duplicate" in x for x in v.validate_routes(root, {"example"})))

    def test_missing_required_harness_is_rejected(self):
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "validate_routes", None)), "route checker is missing")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_repo(root)
            self.assertTrue(any("missing required" in x for x in v.validate_routes(root, {"example", "other"})))

    def test_unknown_control_or_future_check_is_rejected(self):
        import json
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "validate_routes", None)), "route checker is missing")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            row = self.make_repo(root)
            row.update(control="magic", checked_on="9999-12-31")
            (root / "catalog/routes-primary.json").write_text(json.dumps([row]), encoding="utf-8")
            findings = v.validate_routes(root, {"example"})
            self.assertTrue(any("control" in x for x in findings))
            self.assertTrue(any("date" in x for x in findings))

    def test_guide_requires_rollback_and_evidence_sections(self):
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "validate_routes", None)), "route checker is missing")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_repo(root)
            (root / "docs/harnesses/example.md").write_text("# Incomplete", encoding="utf-8")
            self.assertTrue(any("Verify and roll back" in x for x in v.validate_routes(root, {"example"})))

    def test_aliases_are_globally_unambiguous(self):
        import json
        v = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_repo(root)
            registry = json.loads((root / "catalog/harnesses.json").read_text())
            duplicate = dict(registry[0], id="other", name="Other", guide="docs/harnesses/other.md")
            registry.append(duplicate)
            (root / "catalog/harnesses.json").write_text(json.dumps(registry))
            self.assertTrue(any("alias" in finding for finding in v.validate_routes(root, {"example", "other"})))


class ContentTests(unittest.TestCase):
    def checker(self):
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "validate_content", None)), "content checker is missing")
        return v

    def test_valid_json_and_python_pass(self):
        v = self.checker()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "example.json").write_text('{"kind":"synthetic-fixture"}', encoding="utf-8")
            (root / "sample.py").write_text('print("example")\n', encoding="utf-8")
            self.assertEqual(v.validate_content(root), [])

    def test_invalid_json_fence_is_reported(self):
        v = self.checker()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text('```json\n{"broken":}\n```\n', encoding="utf-8")
            self.assertTrue(any("JSON" in x for x in v.validate_content(root)))

    def test_private_home_path_is_reported_without_echoing_it(self):
        v = self.checker()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            private = "/home/" + "private-operator/secret"
            (root / "README.md").write_text(private, encoding="utf-8")
            findings = v.validate_content(root)
            self.assertTrue(any("private path" in x for x in findings))
            self.assertNotIn(private, "\n".join(findings))

    def test_credential_pattern_is_reported_without_echoing_it(self):
        v = self.checker()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            secret = "gh" + "p_" + "A" * 40
            (root / "README.md").write_text(secret, encoding="utf-8")
            findings = v.validate_content(root)
            self.assertTrue(any("credential" in x for x in findings))
            self.assertNotIn(secret, "\n".join(findings))

    def test_private_auth_file_is_rejected(self):
        v = self.checker()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "auth.json").write_text("{}", encoding="utf-8")
            self.assertTrue(any("private file" in x for x in v.validate_content(root)))

    def test_invalid_python_is_reported(self):
        v = self.checker()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "sample.py").write_text("def broken(:", encoding="utf-8")
            self.assertTrue(any("Python" in x for x in v.validate_content(root)))


class LocalGpuRoutingTests(unittest.TestCase):
    def checker(self):
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "validate_local_gpu_routing", None)))
        self.assertTrue(callable(getattr(v, "route_local_gpu", None)))
        return v

    def policy(self):
        import json
        return json.loads((ROOT / "catalog/local-gpu-routing.json").read_text(encoding="utf-8"))

    def request(self, **changes):
        request = {
            "task_class": "general-purpose", "parameters_billions": 8.0,
            "quantization_bits": 4, "context_tokens": 8192,
            "available_memory_gib": 8, "estimated_runtime_memory_gib": 6.5,
            "tools_required": False, "tools_verified": False,
        }
        request.update(changes)
        return request

    def test_repository_policy_and_fixtures_pass(self):
        self.assertEqual(self.checker().validate_local_gpu_routing(ROOT), [])

    def test_tiny_models_are_rejected_for_general_purpose(self):
        v, policy = self.checker(), self.policy()
        for size in (0.512, 1, 2):
            with self.subTest(size=size):
                self.assertEqual(v.route_local_gpu(self.request(parameters_billions=size), policy), {"decision": "reject", "reason": "tiny-general-purpose"})

    def test_q1_is_rejected_for_27b(self):
        v, policy = self.checker(), self.policy()
        result = v.route_local_gpu(self.request(parameters_billions=27, quantization_bits=1, available_memory_gib=24, estimated_runtime_memory_gib=12), policy)
        self.assertEqual(result, {"decision": "reject", "reason": "q1-27b"})

    def test_minimum_good_tier_and_memory_headroom(self):
        v, policy = self.checker(), self.policy()
        self.assertEqual(v.route_local_gpu(self.request(), policy), {"decision": "admit-for-capability-trial", "tier": "minimum-good", "task_eligible": False})
        self.assertEqual(v.route_local_gpu(self.request(estimated_runtime_memory_gib=7.5), policy), {"decision": "reject", "reason": "memory-no-headroom"})

    def test_coarse_gpu_admission_never_claims_task_eligibility(self):
        result = self.checker().route_local_gpu(self.request(), self.policy())
        self.assertEqual(result["decision"], "admit-for-capability-trial")
        self.assertFalse(result["task_eligible"])

    def test_required_tools_must_be_verified(self):
        v, policy = self.checker(), self.policy()
        result = v.route_local_gpu(self.request(tools_required=True), policy)
        self.assertEqual(result, {"decision": "reject", "reason": "unverified-tools"})

    def test_malformed_request_fails_closed(self):
        v, policy = self.checker(), self.policy()
        with self.assertRaises(ValueError):
            v.route_local_gpu({"task_class": "general-purpose"}, policy)


class UsageTests(unittest.TestCase):
    def checker(self):
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "normalize_usage", None)), "usage normalizer is missing")
        return v

    def test_cached_input_and_reasoning_are_not_double_counted(self):
        v = self.checker()
        result = v.normalize_usage("openai-responses", {
            "input_tokens": 1000, "output_tokens": 200,
            "input_tokens_details": {"cached_tokens": 400},
            "output_tokens_details": {"reasoning_tokens": 80}
        })
        self.assertEqual(result["total"], 1200)
        self.assertEqual(result["cached_input"], 400)
        self.assertEqual(result["reasoning_output"], 80)

    def test_anthropic_cache_fields_are_separate_input(self):
        v = self.checker()
        result = v.normalize_usage("anthropic-messages", {
            "input_tokens": 300, "cache_read_input_tokens": 600,
            "cache_creation_input_tokens": 100, "output_tokens": 200
        })
        self.assertEqual(result["input_total"], 1000)
        self.assertEqual(result["total"], 1200)

    def test_unknown_schema_is_not_guessed(self):
        v = self.checker()
        with self.assertRaises(ValueError):
            v.normalize_usage("unknown", {"total_tokens": 100})

    def test_missing_telemetry_is_not_zero(self):
        v = self.checker()
        with self.assertRaises(ValueError):
            v.normalize_usage("openai-responses", {"output_tokens": 200})

    def test_negative_or_inconsistent_usage_is_rejected(self):
        v = self.checker()
        for usage in [
            {"input_tokens": -1, "output_tokens": 2},
            {"input_tokens": True, "output_tokens": 2},
            {"input_tokens": 1, "output_tokens": 2, "input_tokens_details": {"cached_tokens": 3}},
            {"input_tokens": 1, "output_tokens": 2, "output_tokens_details": {"reasoning_tokens": 3}},
        ]:
            with self.subTest(usage=usage), self.assertRaises(ValueError):
                v.normalize_usage("openai-responses", usage)


class CommandTests(unittest.TestCase):
    def test_command_reports_failure_without_traceback(self):
        import json
        import subprocess
        import sys
        command = ROOT / "scripts" / "validate.py"
        self.assertTrue(command.is_file(), "documented validation command is missing")
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run([sys.executable, str(command), "--root", tmp], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            report = json.loads(result.stdout)
            self.assertEqual(report["status"], "fail")
            self.assertTrue(report["findings"])
            self.assertNotIn("Traceback", result.stderr)


class RegressionTests(unittest.TestCase):
    def test_inline_code_in_heading_keeps_anchor_text(self):
        v = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("## Use `cache`\n[Link](#use-cache)\n", encoding="utf-8")
            self.assertEqual(v.validate_links(root), [])

    def test_windows_private_path_is_detected(self):
        v = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            private = "C:" + chr(92) + "Users" + chr(92) + "operator" + chr(92) + "secret"
            (root / "README.md").write_text(private, encoding="utf-8")
            self.assertTrue(any("private path" in x for x in v.validate_content(root)))

    def test_symlink_directory_is_rejected(self):
        v = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            root.mkdir()
            outside = root.parent / "outside"
            outside.mkdir()
            try:
                (root / "linked").symlink_to(outside, target_is_directory=True)
            except OSError:
                self.skipTest("symlink creation unavailable")
            self.assertTrue(any("symlink" in x for x in v.validate_content(root)))

    def test_malformed_route_fields_report_instead_of_crashing(self):
        import json
        v = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            row = RouteTests().make_repo(root)
            row.update(control=[], support_level={}, sources=["https://["])
            (root / "catalog/routes-primary.json").write_text(json.dumps([row]), encoding="utf-8")
            findings = v.validate_routes(root, {"example"})
            self.assertTrue(any("control" in x for x in findings))
            self.assertTrue(any("source" in x for x in findings))

    def test_required_harness_set_is_closed_world(self):
        v = load_validation(self)
        expected = {
            "claude-code", "codex", "qwen-code", "grok-build", "grokbot", "gemini-cli",
            "hermes", "openclaw", "opencode", "cursor", "copilot", "cline", "windsurf",
            "aider", "junie", "goose", "antigravity", "continue", "kilo-code"
        }
        self.assertEqual(v.REQUIRED_HARNESSES, expected)


class MarketTests(unittest.TestCase):
    def fixture(self, root):
        import json
        (root / "catalog").mkdir()
        source = {"id": "S1", "url": "https://example.invalid/source", "title": "Synthetic fixture", "checked_on": "2000-01-01", "evidence_type": "documentation", "caveat": "Not real research"}
        item = {"id": "example", "name": "Example", "category": "fixture", "url": source["url"], "disposition": "experimental", "rationale": "Synthetic", "license_status": "Not applicable", "evidence_scope": "Fixture only", "overlapping_with": [], "sources": [source["url"]], "checked_on": "2000-01-01"}
        (root / "catalog/sources-market.json").write_text(json.dumps([source]), encoding="utf-8")
        (root / "catalog/market.json").write_text(json.dumps([item]), encoding="utf-8")
        return item

    def test_valid_market_references_pass(self):
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "validate_market", None)), "market checker is missing")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root)
            self.assertEqual(v.validate_market(root), [])

    def test_duplicate_items_and_unknown_references_fail(self):
        import json
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "validate_market", None)), "market checker is missing")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            item = self.fixture(root)
            item.update(sources=["https://example.invalid/absent"], overlapping_with=["missing"])
            (root / "catalog/market.json").write_text(json.dumps([item, item]), encoding="utf-8")
            findings = v.validate_market(root)
            self.assertTrue(any("duplicate" in x for x in findings))
            self.assertTrue(any("source" in x for x in findings))
            self.assertTrue(any("overlap" in x for x in findings))

    def test_empty_catalog_is_not_a_pass(self):
        import json
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "validate_market", None)), "market checker is missing")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root)
            (root / "catalog/market.json").write_text("[]", encoding="utf-8")
            self.assertTrue(v.validate_market(root))


class ReviewRegressionTests(unittest.TestCase):
    def test_route_catalog_symlink_is_rejected_before_read(self):
        from unittest.mock import patch
        v = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            root.mkdir()
            RouteTests().make_repo(root)
            outside = root.parent / "outside.json"
            outside.write_text("[]", encoding="utf-8")
            catalog = root / "catalog/routes-primary.json"
            catalog.unlink()
            try:
                catalog.symlink_to(outside)
            except OSError:
                self.skipTest("symlink creation unavailable")
            reads = []
            original = Path.read_text
            def observed(path, *args, **kwargs):
                if path.resolve() == outside.resolve():
                    reads.append(path)
                return original(path, *args, **kwargs)
            with patch.object(Path, "read_text", observed):
                findings = v.validate_routes(root, {"example"})
            self.assertEqual(reads, [])
            self.assertTrue(findings)

    def test_usage_symlink_does_not_parse_outside_data(self):
        import json
        import subprocess
        import sys
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            (root / "examples").mkdir(parents=True)
            outside = root.parent / "outside.json"
            outside.write_text((ROOT / "examples/usage-normalization.json").read_text(), encoding="utf-8")
            try:
                (root / "examples/usage-normalization.json").symlink_to(outside)
            except OSError:
                self.skipTest("symlink creation unavailable")
            result = subprocess.run([sys.executable, str(ROOT / "scripts/validate.py"), "--root", str(root)], capture_output=True, text=True)
            self.assertEqual(json.loads(result.stdout)["accounting_examples_checked"], 0)

    def test_dotenv_suffix_is_rejected(self):
        v = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".env.production").write_text("EXAMPLE=value", encoding="utf-8")
            self.assertTrue(any("private file" in x for x in v.validate_content(root)))

    def test_private_link_target_is_not_reflected(self):
        v = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            private = "/home/" + "synthetic-person/private-fixture.md"
            (root / "README.md").write_text("[Bad](" + private + ")", encoding="utf-8")
            findings = v.validate_links(root)
            self.assertTrue(findings)
            self.assertNotIn(private, "\n".join(findings))

    def test_malformed_link_returns_structured_failure(self):
        import json
        import subprocess
        import sys
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("[Bad](https://[)", encoding="utf-8")
            result = subprocess.run([sys.executable, str(ROOT / "scripts/validate.py"), "--root", str(root)], capture_output=True, text=True)
            self.assertNotIn("Traceback", result.stderr)
            self.assertEqual(json.loads(result.stdout)["status"], "fail")

    def test_html_and_undefined_reference_links_are_checked(self):
        v = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text('<a href="missing.md">missing</a>\n[Guide][missing]', encoding="utf-8")
            findings = v.validate_links(root)
            self.assertTrue(any("missing local" in x for x in findings))
            self.assertTrue(any("undefined reference" in x for x in findings))

    def test_angle_bracket_destination_is_supported(self):
        v = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "guide.md").write_text("# Guide", encoding="utf-8")
            (root / "README.md").write_text("[Guide](<guide.md>)", encoding="utf-8")
            self.assertEqual(v.validate_links(root), [])

    def test_display_identity_mismatch_is_rejected(self):
        import json
        v = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            row = RouteTests().make_repo(root)
            row["harness"] = "Unrelated Product"
            (root / "catalog/routes-primary.json").write_text(json.dumps([row]), encoding="utf-8")
            self.assertTrue(any("identity" in x for x in v.validate_routes(root, {"example"})))

    def test_route_id_must_be_a_stable_slug(self):
        import json
        v = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            row = RouteTests().make_repo(root)
            row["id"] = "not a stable slug"
            (root / "catalog/routes-primary.json").write_text(json.dumps([row]), encoding="utf-8")
            self.assertTrue(any("slug" in x for x in v.validate_routes(root, {"example"})))


class AddonAssetTests(unittest.TestCase):
    def test_complete_source_inventory_passes(self):
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "validate_addon_inventory", None)), "add-on checker missing")
        self.assertEqual(v.validate_addon_inventory(ROOT), [])

    def test_missing_engine_is_not_hidden_by_changing_declared_count(self):
        import json
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "validate_addon_inventory", None)), "add-on checker missing")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "catalog").mkdir()
            data = json.loads((ROOT / "catalog/omniroute-features.json").read_text())
            removed = data["engines"].pop()["id"]
            data["registered_engine_ids"].remove(removed)
            data["counts"]["registered_engines"] -= 1
            (root / "catalog/omniroute-features.json").write_text(json.dumps(data))
            self.assertTrue(any("engine" in x for x in v.validate_addon_inventory(root)))

    def test_hidden_engine_cannot_be_labeled_normal_config(self):
        import json
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "validate_addon_inventory", None)), "add-on checker missing")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "catalog").mkdir()
            data = json.loads((ROOT / "catalog/omniroute-features.json").read_text())
            row = next(x for x in data["engines"] if x["id"] == "ionizer")
            row["writable_stacked_schema"] = True
            row["in_public_catalog"] = True
            data["public_configurable_engine_ids"].append("ionizer")
            data["counts"]["normal_config_choices"] += 1
            (root / "catalog/omniroute-features.json").write_text(json.dumps(data))
            self.assertTrue(any("config" in x for x in v.validate_addon_inventory(root)))

    def test_navigation_pill_checks_outer_destination(self):
        v = load_validation(self)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "assets").mkdir()
            (root / "assets/pill.svg").write_text("<svg/>")
            (root / "README.md").write_text("[![Guide](assets/pill.svg)](missing-guide.md)")
            self.assertTrue(v.validate_links(root))
            (root / "missing-guide.md").write_text("# Guide")
            self.assertEqual(v.validate_links(root), [])

    def test_malformed_inventory_ids_return_findings(self):
        import json
        v = load_validation(self)
        for field in ("registered_engine_ids", "public_configurable_engine_ids"):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                (root / "catalog").mkdir()
                data = json.loads((ROOT / "catalog/omniroute-features.json").read_text())
                data[field][0] = None
                (root / "catalog/omniroute-features.json").write_text(json.dumps(data))
                try:
                    findings = v.validate_addon_inventory(root)
                except (TypeError, ValueError) as exc:
                    self.fail("malformed IDs raised instead of returning findings: " + type(exc).__name__)
                self.assertTrue(findings)

    def test_supporting_groups_require_reviewed_identity_and_evidence(self):
        import json
        v = load_validation(self)
        for change in ("identity", "source_url", "scope", "caveat"):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                (root / "catalog").mkdir()
                data = json.loads((ROOT / "catalog/omniroute-features.json").read_text())
                group = data["supporting_mechanisms"][0]
                if change == "identity":
                    group["id"] = "invented-unsupported-group"
                else:
                    group.pop(change)
                (root / "catalog/omniroute-features.json").write_text(json.dumps(data))
                self.assertTrue(v.validate_addon_inventory(root))

    def test_basic_svg_passes(self):
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "validate_assets", None)), "asset checker missing")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "assets").mkdir()
            (root / "assets/good.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" width="100" height="30"><rect width="100" height="30" fill="#ffffff"/></svg>')
            self.assertEqual(v.validate_assets(root), [])

    def test_svg_active_and_external_content_is_rejected(self):
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "validate_assets", None)), "asset checker missing")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "assets").mkdir()
            (root / "assets/bad.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"><script>void(0)</script><image href="https://example.invalid/image.png"/></svg>')
            self.assertTrue(v.validate_assets(root))

    def test_svg_entity_declarations_are_rejected(self):
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "validate_assets", None)), "asset checker missing")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "assets").mkdir()
            (root / "assets/bad.svg").write_text('<!DOCTYPE svg [<!ENTITY example "text">]><svg xmlns="http://www.w3.org/2000/svg"><text>&example;</text></svg>')
            self.assertTrue(any("declaration" in x for x in v.validate_assets(root)))


class CoverageTests(unittest.TestCase):
    def test_oauth_matrix_preserves_mechanisms_and_untested_boundary(self):
        import json
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "validate_auth_matrix", None)))
        self.assertEqual(v.validate_auth_matrix(ROOT), [])
        for change in ("drop", "tested", "source", "mechanism"):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                (root / "catalog").mkdir()
                data = json.loads((ROOT / "catalog/omniroute-auth.json").read_text())
                if change == "drop": data["rows"].pop()
                elif change == "tested": data["runtime_tested"] = True
                elif change == "source": data["rows"][0]["source_urls"] = []
                elif change == "mechanism": data["rows"][0].pop("technical_support")
                (root / "catalog/omniroute-auth.json").write_text(json.dumps(data))
                self.assertTrue(v.validate_auth_matrix(root))

    def test_platform_catalogue_keeps_identity_sources_and_limits(self):
        import json
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "validate_platform_coverage", None)))
        self.assertEqual(v.validate_platform_coverage(ROOT), [])
        for change in ("drop", "identity", "source", "tier", "type"):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                (root / "catalog").mkdir()
                data = json.loads((ROOT / "catalog/coverage.json").read_text())
                if change == "drop": data.pop()
                elif change == "identity": data[0]["id"] = "invented"
                elif change == "source": data[0]["sources"] = []
                elif change == "tier": data[0]["omniroute_interface"]["tier"] = "fully runtime certified"
                elif change == "type": data[0]["upstream_auth"] = None
                (root / "catalog/coverage.json").write_text(json.dumps(data))
                self.assertTrue(v.validate_platform_coverage(root))


class ApiCostScenarioTests(unittest.TestCase):
    def test_scenario_arithmetic_and_nonbenchmark_boundary(self):
        import json
        v = load_validation(self)
        self.assertTrue(callable(getattr(v, "validate_api_cost_scenario", None)))
        self.assertEqual(v.validate_api_cost_scenario(ROOT), [])
        for change in ("label", "cost", "percent", "missing", "duplicate", "assumption", "local-cost", "local-scope"):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                (root / "examples").mkdir()
                data = json.loads((ROOT / "examples/api-cost-scenario.json").read_text())
                if change == "label": data["not_a_benchmark"] = False
                elif change == "cost": data["rows"][0]["cost"] = "1"
                elif change == "percent": data["rows"][0]["rounded_reduction_percent"] += 1
                elif change == "missing": data["rows"].pop()
                elif change == "duplicate": data["rows"][-1] = data["rows"][0]
                elif change == "assumption": data["base_reduction"]["Conservative"] = "-1"
                elif change == "local-cost": data["local_gpu_upper_case"]["cost"] = "1"
                elif change == "local-scope": data["local_gpu_upper_case"]["scope"] = "guaranteed"
                (root / "examples/api-cost-scenario.json").write_text(json.dumps(data))
                self.assertTrue(v.validate_api_cost_scenario(root))


class TechnicalHardeningTests(unittest.TestCase):
    def checker(self):
        return load_validation(self)

    def policy(self):
        import json
        return json.loads((ROOT / "catalog/task-routing-policy.json").read_text())

    def evidence(self, route="local", **changes):
        value = {
            "schema_version": 1, "worker_id": route + "-worker",
            "requested_model": route + "-alias", "resolved_model": route + "/model-v1",
            "runtime_fingerprint": "sha256:runtime-a", "observed_runtime_fingerprint": "sha256:runtime-a",
            "evidence_status": "verified", "verified_at": "2026-01-01T00:00:00Z",
            "expires_at": "2027-01-01T00:00:00Z", "effective_context_tokens": 8192,
            "task_classes": ["structured-extraction"], "reasoning_levels": ["low", "medium"],
            "verified_tools": ["filesystem-read"], "output_capabilities": ["json"],
            "data_classes": ["public", "internal", "confidential"],
            "verification_methods": ["deterministic", "human"],
            "evidence_reference": "evidence://" + route + "/trial-1", "route_available": True,
            "hard_spend_stop_verified": route == "free"
        }
        value.update(changes)
        return value

    def request(self, **changes):
        value = {
            "schema_version": 2, "task_id": "task-1", "task_class": "structured-extraction",
            "task_shape": "bounded", "operation": "semantic", "reasoning": "low",
            "data_class": "public", "external_effect": "none", "verification": "deterministic",
            "context_tokens": 4096, "required_tools": ["filesystem-read"],
            "required_output_capabilities": ["json"], "evaluation_time": "2026-09-15T00:00:00Z",
            "local_gpu_enabled": True, "free_model_enabled": True, "omniroute_enabled": False,
            "capability_evidence": {"local": self.evidence("local"), "free": self.evidence("free")}
        }
        value.update(changes)
        return value

    def test_valid_policy_precedence_changes_route_without_code_change(self):
        import copy
        v, policy = self.checker(), self.policy()
        self.assertEqual(v.route_task(self.request(), policy)["route"], "local")
        changed = copy.deepcopy(policy)
        changed["route_precedence"] = ["deterministic-code", "free", "local", "main"]
        self.assertEqual(v.route_task(self.request(), changed)["route"], "free")

    def test_capability_matching_fails_closed_with_specific_reasons(self):
        v, policy = self.checker(), self.policy()
        cases = [
            ({"evidence_status": "unknown"}, "CAPABILITY_STATUS_UNKNOWN"),
            ({"expires_at": "2026-01-02T00:00:00Z"}, "CAPABILITY_EXPIRED"),
            ({"observed_runtime_fingerprint": "sha256:changed"}, "RUNTIME_FINGERPRINT_MISMATCH"),
            ({"verified_tools": []}, "TOOLS_UNVERIFIED"),
            ({"task_classes": []}, "TASK_CLASS_UNVERIFIED"),
        ]
        for change, reason in cases:
            with self.subTest(reason=reason):
                evidence = self.evidence("local", **change)
                request = self.request(free_model_enabled=False, capability_evidence={"local": evidence, "free": self.evidence("free")})
                self.assertEqual(v.route_task(request, policy)["reason_code"], reason)

    def test_post_result_contract_correlates_and_rejects_terminal_late_results(self):
        v, policy = self.checker(), self.policy()
        base = {
            "schema_version": 2, "task_id": "task-1", "decision_id": "decision-1",
            "worker_id": "local-worker", "expected_task_id": "task-1",
            "expected_decision_id": "decision-1", "expected_worker_id": "local-worker",
            "worker_route": "local", "evidence_reference": "evidence://local/trial-1",
            "expected_evidence_reference": "evidence://local/trial-1", "verifier_result": "fail",
            "verifier_type": "deterministic", "verifier_identity": "local-deterministic-verifier",
            "verifier_independence": "independent", "expected_verifier_identity": "local-deterministic-verifier",
            "expected_verifier_type": "deterministic", "expected_verifier_independence": "independent",
            "main_fallback_authorized": True,
            "main_fallback_count": 0, "execution_state": "worker-result-pending"
        }
        self.assertEqual(v.resolve_task_result(base, policy)["action"], "fallback-main")
        late = dict(base, execution_state="accepted", verifier_result="pass")
        self.assertEqual(v.resolve_task_result(late, policy)["reason_code"], "LATE_RESULT_REJECTED")
        mismatch = dict(base, worker_id="other")
        self.assertEqual(v.resolve_task_result(mismatch, policy)["reason_code"], "CORRELATION_MISMATCH")

    def test_strict_json_rejects_duplicate_constants_size_and_depth(self):
        v = self.checker()
        for text in ('{"x":1,"x":2}', '{"x":NaN}', '{"x":Infinity}'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                v.loads_strict_json(text)
        with self.assertRaisesRegex(ValueError, "size"):
            v.loads_strict_json('{"x":"' + 'a' * 100 + '"}', max_bytes=16)
        with self.assertRaisesRegex(ValueError, "nesting"):
            v.loads_strict_json("[" * 20 + "0" + "]" * 20, max_depth=8)

    def test_validation_record_detects_stale_policy_metadata(self):
        import json
        v = self.checker()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "validation").mkdir()
            (root / "catalog").mkdir()
            (root / "tests").mkdir()
            record = {"kind": "repository-validation-record", "status": "metadata-only", "forced_task_routing": {"policy_version": 1}, "harness_identities": 0, "declared_test_modules": ["tests/test_validation.py"]}
            (root / "validation/record.json").write_text(json.dumps(record))
            (root / "catalog/task-routing-policy.json").write_text(json.dumps({"version": 2}))
            (root / "catalog/harnesses.json").write_text("[]")
            (root / "tests/test_validation.py").write_text("class T:\n    def test_one(self): pass\n")
            self.assertTrue(any("policy" in x for x in v.validate_validation_record(root)))

    def test_immutable_safety_gate_cannot_be_removed_by_policy(self):
        import copy
        policy = copy.deepcopy(self.policy())
        policy["main_only"]["data_class"].remove("credentials")
        with self.assertRaisesRegex(ValueError, "safety"):
            self.checker().route_task(self.request(), policy)

    def test_reason_code_enum_is_closed(self):
        import copy
        policy = copy.deepcopy(self.policy())
        policy["reason_codes"].append("INVENTED")
        with self.assertRaisesRegex(ValueError, "reason code"):
            self.checker().route_task(self.request(), policy)

    def test_context_and_output_matching_are_compositional(self):
        v, policy = self.checker(), self.policy()
        for change, reason in (({"effective_context_tokens": 100}, "CONTEXT_TOO_LARGE"), ({"output_capabilities": []}, "OUTPUT_CAPABILITY_UNVERIFIED")):
            evidence = self.evidence("local", **change)
            request = self.request(free_model_enabled=False, capability_evidence={"local": evidence, "free": self.evidence("free")})
            self.assertEqual(v.route_task(request, policy)["reason_code"], reason)

    def test_unknown_resolved_model_fails_closed(self):
        evidence = self.evidence("local", resolved_model="unknown")
        request = self.request(free_model_enabled=False, capability_evidence={"local": evidence, "free": self.evidence("free")})
        self.assertEqual(self.checker().route_task(request, self.policy())["reason_code"], "MODEL_IDENTITY_UNKNOWN")

    def test_fallback_requires_explicit_authorization(self):
        base = self._post_request(main_fallback_authorized=False, verifier_result="fail")
        self.assertEqual(self.checker().resolve_task_result(base, self.policy())["reason_code"], "MAIN_FALLBACK_NOT_AUTHORIZED")

    def test_worker_cannot_satisfy_independent_verification(self):
        base = self._post_request(verifier_identity="local-worker", expected_verifier_identity="local-worker")
        self.assertEqual(self.checker().resolve_task_result(base, self.policy())["reason_code"], "VERIFIER_AUTHORIZATION_MISMATCH")

    def test_verifier_must_match_authoritative_route_decision(self):
        v, policy = self.checker(), self.policy()
        decision = v.route_task(self.request(), policy)
        self.assertEqual(decision["expected_verifier_identity"], "local-deterministic-verifier")
        base = self._post_request(
            expected_verifier_identity=decision["expected_verifier_identity"],
            expected_verifier_type=decision["expected_verifier_type"],
            expected_verifier_independence=decision["expected_verifier_independence"],
        )
        self.assertEqual(v.resolve_task_result(base, policy)["action"], "accept")
        arbitrary = dict(base, verifier_identity="arbitrary-self-asserted-verifier")
        self.assertEqual(v.resolve_task_result(arbitrary, policy)["reason_code"], "VERIFIER_AUTHORIZATION_MISMATCH")
        self_asserted = dict(arbitrary, expected_verifier_identity="arbitrary-self-asserted-verifier")
        self.assertEqual(v.resolve_task_result(self_asserted, policy)["reason_code"], "VERIFIER_AUTHORIZATION_MISMATCH")

    def test_fallback_limit_is_read_from_policy(self):
        base = self._post_request(verifier_result="fail", main_fallback_count=1)
        self.assertEqual(self.checker().resolve_task_result(base, self.policy())["reason_code"], "MAIN_FALLBACK_LIMIT_REACHED")

    def test_operational_schemas_are_closed_objects(self):
        import json
        for name in ("task-route", "capability-evidence", "post-result", "task-routing-policy"):
            schema = json.loads((ROOT / "schemas" / (name + ".schema.json")).read_text())
            self.assertFalse(schema["additionalProperties"])
            self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")

    def test_policy_rejects_trigger_corruption_and_unknown_nested_keys(self):
        import copy
        v = self.checker()
        for mutate in (
            lambda p: p.update(enabled_when_any=["task_id"]),
            lambda p: p["routes"]["local"].update(injected=True),
            lambda p: p["post_result"]["actions"].update(injected="accept"),
        ):
            policy = copy.deepcopy(self.policy())
            mutate(policy)
            with self.subTest(policy=policy), self.assertRaises(ValueError):
                v.route_task(self.request(), policy)

    def test_policy_rejects_semantic_gate_and_safety_action_remapping(self):
        import copy
        v = self.checker()
        mutations = (
            lambda p: p["main_gate_reason_mapping"]["data_class"].update(credentials="ROUTE_LOCAL_ELIGIBLE"),
            lambda p: p["post_result"]["actions"].update(fallback_not_authorized="fallback-main"),
            lambda p: p["post_result"]["actions"].update(verifier_not_independent="accept"),
            lambda p: p["post_result"]["actions"].update(correlation_failure="accept"),
        )
        for mutate in mutations:
            policy = copy.deepcopy(self.policy())
            mutate(policy)
            with self.subTest(policy=policy), self.assertRaises(ValueError):
                v.resolve_task_result(self._post_request(), policy)

    def test_post_result_enums_are_closed_and_self_check_never_accepts(self):
        v, policy = self.checker(), self.policy()
        self.assertEqual(v.resolve_task_result(self._post_request(verifier_independence="self-check"), policy)["reason_code"], "VERIFIER_AUTHORIZATION_MISMATCH")
        for field in ("verifier_independence", "execution_state"):
            with self.subTest(field=field), self.assertRaises(ValueError):
                v.resolve_task_result(self._post_request(**{field: "garbage"}), policy)

    def test_capability_timestamps_are_strict_and_ordered(self):
        v, policy = self.checker(), self.policy()
        changes = (
            {"verified_at": "2099-01-01T00:00:00Z"},
            {"verified_at": "2028-01-01T00:00:00Z", "expires_at": "2027-01-01T00:00:00Z"},
            {"verified_at": "2026-01-01 00:00:00Z"},
            {"expires_at": "2027-01-01t00:00:00z"},
        )
        for change in changes:
            evidence = self.evidence("local", **change)
            request = self.request(capability_evidence={"local": evidence, "free": self.evidence("free")})
            with self.subTest(change=change), self.assertRaises(ValueError):
                v.route_task(request, policy)

    def test_inactive_capability_evidence_still_validates_timestamps(self):
        v, policy = self.checker(), self.policy()
        for status in ("unknown", "expired", "unavailable"):
            evidence = self.evidence("local", evidence_status=status, verified_at="not-a-time")
            request = self.request(free_model_enabled=False, capability_evidence={"local": evidence, "free": self.evidence("free")})
            with self.subTest(status=status), self.assertRaises(ValueError):
                v.route_task(request, policy)

    def test_capability_enum_arrays_are_closed(self):
        v, policy = self.checker(), self.policy()
        for field in ("reasoning_levels", "data_classes", "verification_methods"):
            evidence = self.evidence("local", **{field: ["garbage"]})
            request = self.request(capability_evidence={"local": evidence, "free": self.evidence("free")})
            with self.subTest(field=field), self.assertRaises(ValueError):
                v.route_task(request, policy)

    def test_json_file_limit_is_enforced_by_bounded_read(self):
        v = self.checker()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "large.json"
            path.write_bytes(b" " * 17)
            with self.assertRaisesRegex(ValueError, "size"):
                v.read_text_within(root, path, max_bytes=16)

    def test_validation_record_declares_suite_shape_not_executed_pass_count(self):
        import json
        v = self.checker()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "validation").mkdir()
            (root / "catalog").mkdir()
            (root / "tests").mkdir()
            (root / "tests/test_validation.py").write_text("# declared suite module\n")
            record = {"kind": "repository-validation-record", "status": "metadata-only", "forced_task_routing": {"policy_version": 2}, "harness_identities": 0, "declared_test_modules": ["tests/test_validation.py"]}
            (root / "validation/record.json").write_text(json.dumps(record))
            (root / "catalog/task-routing-policy.json").write_text(json.dumps({"version": 2}))
            (root / "catalog/harnesses.json").write_text("[]")
            self.assertEqual(v.validate_validation_record(root), [])

    def test_validation_record_rejects_unknown_and_execution_claim_fields(self):
        import json
        v = self.checker()
        for injected in ({"unit_test_count": 83}, {"repository_command_result": "pass"}, {"invented": True}):
            with self.subTest(injected=injected), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                (root / "validation").mkdir()
                (root / "catalog").mkdir()
                (root / "tests").mkdir()
                (root / "tests/test_validation.py").write_text("# declared suite module\n")
                record = {"kind": "repository-validation-record", "status": "metadata-only", "forced_task_routing": {"policy_version": 2}, "harness_identities": 0, "declared_test_modules": ["tests/test_validation.py"]}
                record.update(injected)
                (root / "validation/record.json").write_text(json.dumps(record))
                (root / "catalog/task-routing-policy.json").write_text(json.dumps({"version": 2}))
                (root / "catalog/harnesses.json").write_text("[]")
                self.assertTrue(v.validate_validation_record(root))

    def test_validation_record_rejects_invalid_status_and_types(self):
        import json
        v = self.checker()
        for change in ({"status": "pass"}, {"harness_identities": True}, {"forced_task_routing": []}):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                (root / "validation").mkdir()
                (root / "catalog").mkdir()
                (root / "tests").mkdir()
                (root / "tests/test_validation.py").write_text("# declared suite module\n")
                record = {"kind": "repository-validation-record", "status": "metadata-only", "forced_task_routing": {"policy_version": 2}, "harness_identities": 0, "declared_test_modules": ["tests/test_validation.py"]}
                record.update(change)
                (root / "validation/record.json").write_text(json.dumps(record))
                (root / "catalog/task-routing-policy.json").write_text(json.dumps({"version": 2}))
                (root / "catalog/harnesses.json").write_text("[]")
                self.assertTrue(v.validate_validation_record(root))

    def test_external_schemas_reject_nested_policy_and_capability_enums(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema is not installed")
        import copy
        import json
        policy_schema = json.loads((ROOT / "schemas/task-routing-policy.schema.json").read_text())
        policy = copy.deepcopy(self.policy())
        policy["routes"]["local"]["injected"] = True
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.Draft202012Validator(policy_schema).validate(policy)
        capability_schema = json.loads((ROOT / "schemas/capability-evidence.schema.json").read_text())
        capability = self.evidence(reasoning_levels=["garbage"])
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.Draft202012Validator(capability_schema).validate(capability)
        for mutation in (
            lambda p: p["allowed_values"].update(reasoning=[]),
            lambda p: p["routes"]["local"]["allowed"].update(reasoning=[]),
        ):
            invalid = copy.deepcopy(self.policy())
            mutation(invalid)
            with self.assertRaises(jsonschema.ValidationError):
                jsonschema.Draft202012Validator(policy_schema).validate(invalid)

    def _post_request(self, **changes):
        value = {
            "schema_version": 2, "task_id": "task-1", "decision_id": "decision-1",
            "worker_id": "local-worker", "expected_task_id": "task-1", "expected_decision_id": "decision-1",
            "expected_worker_id": "local-worker", "worker_route": "local",
            "evidence_reference": "evidence://local/trial-1", "expected_evidence_reference": "evidence://local/trial-1",
            "verifier_result": "pass", "verifier_type": "deterministic", "verifier_identity": "local-deterministic-verifier",
            "verifier_independence": "independent", "expected_verifier_identity": "local-deterministic-verifier",
            "expected_verifier_type": "deterministic", "expected_verifier_independence": "independent",
            "main_fallback_authorized": True,
            "main_fallback_count": 0, "execution_state": "worker-result-pending"
        }
        value.update(changes)
        return value


if __name__ == "__main__":
    unittest.main()
