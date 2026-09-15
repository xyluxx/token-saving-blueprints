"""Dependency-free checks for this documentation repository, not an AI runtime."""
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

MAX_JSON_BYTES = 1_000_000
MAX_JSON_DEPTH = 64


def loads_strict_json(text, max_bytes=MAX_JSON_BYTES, max_depth=MAX_JSON_DEPTH):
    """Parse bounded RFC 8259 JSON; reject ambiguous/non-finite input."""
    import json
    if not isinstance(text, str):
        raise ValueError("JSON input must be text")
    if len(text.encode("utf-8")) > max_bytes:
        raise ValueError("JSON size limit exceeded")

    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError("duplicate JSON object key")
            result[key] = value
        return result

    def constant(_value):
        raise ValueError("non-finite JSON number")

    try:
        value = json.loads(text, object_pairs_hook=pairs, parse_constant=constant)
    except (json.JSONDecodeError, RecursionError) as exc:
        raise ValueError("invalid or excessively nested JSON") from exc
    stack = [(value, 1)]
    while stack:
        node, depth = stack.pop()
        if depth > max_depth:
            raise ValueError("JSON nesting limit exceeded")
        if isinstance(node, dict):
            stack.extend((item, depth + 1) for item in node.values())
        elif isinstance(node, list):
            stack.extend((item, depth + 1) for item in node)
    return value


def _body(text, remove_inline=True):
    text = re.sub(r"(?ms)^\s*(```|~~~)[^\n]*\n.*?^\s*\1\s*$", "", text)
    return re.sub(r"`[^`\n]*`", "", text) if remove_inline else text


def _anchors(text):
    found, counts = set(), {}
    for heading in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", _body(text, False)):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        occurrence = counts.get(slug, 0)
        counts[slug] = occurrence + 1
        found.add(slug if occurrence == 0 else f"{slug}-{occurrence}")
    found.update(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', text))
    return found


def read_text_within(root, path, max_bytes=None):
    root, path = Path(root).resolve(), Path(path)
    if not path.is_absolute():
        path = root / path
    if not path.resolve().is_relative_to(root):
        raise ValueError("path outside repository")
    probe = root
    for part in path.relative_to(root).parts:
        probe = probe / part
        if probe.is_symlink():
            raise ValueError("symlinked input is not allowed")
    with path.open("rb") as handle:
        data = handle.read(max_bytes + 1) if max_bytes is not None else handle.read()
    if max_bytes is not None and len(data) > max_bytes:
        raise ValueError("text size limit exceeded")
    return data.decode("utf-8")


def load_json_within(root, path):
    return loads_strict_json(read_text_within(root, path, max_bytes=MAX_JSON_BYTES))


def validate_links(root):
    from html.parser import HTMLParser
    root = Path(root).resolve()
    findings = []
    class Links(HTMLParser):
        def __init__(self):
            super().__init__()
            self.targets = []
        def handle_starttag(self, tag, attrs):
            self.targets.extend(value for key, value in attrs if key in {"href", "src"} and value)
    for document in root.rglob("*.md"):
        if ".git" in document.relative_to(root).parts:
            continue
        label = document.relative_to(root)
        try:
            text = _body(read_text_within(root, document))
        except (OSError, UnicodeError, ValueError):
            findings.append(f"{label}: unreadable or symlinked document")
            continue
        targets = re.findall(r'!?\[[^\]]*\]\((<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\)', text)
        targets.extend(re.findall(r'\[!\[[^\]]*\]\([^\n)]+\)\]\((<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\)', text))
        definitions = re.findall(r'(?m)^\s{0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)', text)
        defined = {" ".join(name.lower().split()) for name, _ in definitions}
        numeric_citations = set(re.findall(r'(?m)^\[(\d+)\]\s+https?://', text))
        for number, match in enumerate(re.finditer(r'!?\[([^\]\n]+)\]\[([^\]\n]*)\]', text), 1):
            first, second = match.groups()
            if first in numeric_citations and second in numeric_citations:
                continue
            reference = " ".join((second or first).lower().split())
            if reference not in defined:
                findings.append(f"{label}: undefined reference link {number}")
        targets.extend(value for _, value in definitions)
        html = Links()
        html.feed(text)
        targets.extend(html.targets)
        for number, target in enumerate(targets, 1):
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            location = f"{label}: link {number}"
            try:
                parsed = urlsplit(target)
            except ValueError:
                findings.append(f"{location}: malformed URL (value withheld)")
                continue
            if parsed.scheme in {"http", "https", "mailto"}:
                continue
            if parsed.scheme or parsed.netloc:
                findings.append(f"{location}: unsupported link scheme (value withheld)")
                continue
            destination = document.parent / unquote(parsed.path) if parsed.path else document
            if not destination.resolve().is_relative_to(root):
                findings.append(f"{location}: points outside repository (value withheld)")
                continue
            if not destination.exists():
                findings.append(f"{location}: missing local link")
                continue
            if parsed.fragment and destination.suffix == ".md":
                try:
                    found = _anchors(read_text_within(root, destination))
                except (OSError, UnicodeError, ValueError):
                    findings.append(f"{location}: unreadable anchor target")
                    continue
                if unquote(parsed.fragment) not in found:
                    findings.append(f"{location}: missing anchor")
    return findings

REQUIRED_HARNESSES = {
    "claude-code", "codex", "qwen-code", "grok-build", "grokbot", "gemini-cli",
    "hermes", "openclaw", "opencode", "cursor", "copilot", "cline", "windsurf",
    "aider", "junie", "goose", "antigravity", "continue", "kilo-code",
}
GUIDE_HEADINGS = {
    "Who this is for", "Authentication and billing routes", "Conservative recipe",
    "Aggressive recipe", "Verify and roll back", "Limits and evidence", "Sources",
}
SUPPORT_LEVELS = {
    "documented", "source-inspected", "local-fixture-verified", "native-smoke-tested",
    "limited", "unresolved",
}
CONTROLS = {"advisory", "native-supported", "explicit-tool-only", "gateway-supported", "unresolved"}


def _http_url(value):
    if not isinstance(value, str):
        return False
    try:
        parsed = urlsplit(value)
        return parsed.scheme in {"http", "https"} and bool(parsed.netloc)
    except ValueError:
        return False


def validate_routes(root, required_harnesses=None):
    import json
    from datetime import date, datetime, timezone
    root = Path(root).resolve()
    required = REQUIRED_HARNESSES if required_harnesses is None else set(required_harnesses)
    findings, identifiers, represented = [], set(), set()
    identity_map, alias_owner = {}, {}
    try:
        registry = load_json_within(root, root / "catalog/harnesses.json")
        if not isinstance(registry, list):
            raise ValueError("identity registry must be an array")
        for entry in registry:
            if not isinstance(entry, dict) or not isinstance(entry.get("id"), str):
                raise ValueError("invalid identity registry")
            aliases = entry.get("aliases")
            if not isinstance(aliases, list) or not aliases or not all(isinstance(x, str) and x for x in aliases):
                raise ValueError("identity aliases required")
            if entry["id"] in identity_map:
                raise ValueError("duplicate identity")
            identity_map[entry["id"]] = entry
            for alias in aliases:
                folded = alias.casefold()
                if folded in alias_owner and alias_owner[folded] != entry["id"]:
                    findings.append("harness alias resolves to multiple canonical identities")
                alias_owner[folded] = entry["id"]
            if entry.get("guide") != f"docs/harnesses/{entry['id']}.md":
                findings.append("harness canonical identity/guide mismatch")
        if set(identity_map) != required:
            findings.append("identity registry does not match declared harness scope")
    except (OSError, UnicodeError, ValueError):
        findings.append("missing or invalid harness identity registry")
    for name in ("routes-primary.json", "routes-editors.json"):
        path = root / "catalog" / name
        try:
            rows = load_json_within(root, path)
        except (OSError, ValueError) as exc:
            findings.append(f"{name}: unreadable route catalog ({type(exc).__name__})")
            continue
        if not isinstance(rows, list):
            findings.append(f"{name}: catalog must be an array")
            continue
        for number, row in enumerate(rows, 1):
            label = f"{name} row {number}"
            if not isinstance(row, dict):
                findings.append(f"{label}: route must be an object")
                continue
            for key in ("id", "harness", "auth_path", "provider_path", "guide", "conservative", "aggressive"):
                if not isinstance(row.get(key), str) or not row[key].strip():
                    findings.append(f"{label}: missing nonempty {key}")
            identifier = row.get("id")
            if isinstance(identifier, str):
                if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", identifier):
                    findings.append(f"{label}: route id must be a stable slug")
                if identifier in identifiers:
                    findings.append(f"{label}: duplicate route id")
                identifiers.add(identifier)
            if not isinstance(row.get("support_level"), str) or row["support_level"] not in SUPPORT_LEVELS:
                findings.append(f"{label}: invalid support_level")
            if not isinstance(row.get("control"), str) or row["control"] not in CONTROLS:
                findings.append(f"{label}: invalid control")
            if not isinstance(row.get("caveats"), list) or not all(isinstance(x, str) for x in row["caveats"]):
                findings.append(f"{label}: caveats must be an array of strings")
            sources = row.get("sources")
            if not isinstance(sources, list) or not sources or not all(
                _http_url(x) for x in sources
            ):
                findings.append(f"{label}: nonempty HTTP source URLs required")
            try:
                checked = date.fromisoformat(row.get("checked_on", ""))
                if checked > datetime.now(timezone.utc).date():
                    findings.append(f"{label}: check date is in the future")
            except (TypeError, ValueError):
                findings.append(f"{label}: invalid check date")
            guide_value = row.get("guide", "")
            if not isinstance(guide_value, str) or not guide_value:
                continue
            guide = (root / guide_value).resolve()
            if not guide.is_relative_to(root / "docs" / "harnesses") or guide.suffix != ".md":
                findings.append(f"{label}: guide must be inside docs/harnesses")
                continue
            represented.add(guide.stem)
            identity = identity_map.get(guide.stem)
            if identity is None or row.get("harness") not in identity["aliases"] or row.get("guide") != identity.get("guide"):
                findings.append(f"{label}: harness identity/guide mismatch")
            if identity and identity.get("status") == "identity-only" and (row.get("support_level") != "unresolved" or row.get("control") != "unresolved"):
                findings.append(f"{label}: unresolved identity cannot claim an approved route")
            if not guide.is_file():
                findings.append(f"{label}: guide file missing: {guide_value}")
                continue
            try:
                guide_text = read_text_within(root, root / guide_value)
            except (OSError, UnicodeError, ValueError):
                findings.append(f"{label}: unreadable or unsafe guide")
                continue
            headings = set(re.findall(r"(?m)^## (.+?)\s*$", guide_text))
            for heading in sorted(GUIDE_HEADINGS - headings):
                findings.append(f"{label}: guide missing section {heading}")
    for harness in sorted(required - represented):
        findings.append(f"missing required harness: {harness}")
    for harness in sorted(represented - required):
        findings.append(f"unexpected harness outside declared scope: {harness}")
    return findings


def validate_content(root):
    import ast
    import json
    import os
    root = Path(root).resolve()
    findings = []
    private_names = {".env", "auth.json", "credentials.json", ".credentials.json"}
    patterns = {
        "private path": re.compile(r"/(?:home|Users)/[A-Za-z0-9_.-]+/|[A-Za-z]:[/\\]Users[/\\][^/\\\s]+[/\\]"),
        "credential-like text": re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9_-]{24,}|xai-[A-Za-z0-9]{30,})\b"),
        "private key material": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    }
    for directory, dirs, names in os.walk(root, followlinks=False):
        dirs[:] = [d for d in dirs if d not in {".git", "__pycache__", ".pytest_cache"}]
        for name in list(dirs):
            candidate = Path(directory) / name
            if candidate.is_symlink():
                findings.append(f"{candidate.relative_to(root)}: symlinked directory is not allowed")
                dirs.remove(name)
        for name in names:
            path = Path(directory) / name
            label = path.relative_to(root)
            if path.is_symlink():
                findings.append(f"{label}: symlinked file is not allowed")
                continue
            if name in private_names or name.startswith(".env.") or name == ".envrc" or path.suffix in {".pem", ".key"}:
                findings.append(f"{label}: private file must not be distributed")
            if path.suffix not in {".md", ".json", ".py", ".yml", ".yaml", ".toml", ".csv", ".txt", ".svg"} and name != "LICENSE":
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError):
                findings.append(f"{label}: unreadable text file")
                continue
            for description, pattern in patterns.items():
                if pattern.search(text):
                    findings.append(f"{label}: {description} detected (value withheld)")
            if path.suffix == ".json":
                try:
                    loads_strict_json(text)
                except ValueError:
                    findings.append(f"{label}: invalid JSON")
            if path.suffix == ".py":
                try:
                    ast.parse(text)
                except SyntaxError:
                    findings.append(f"{label}: invalid Python")
            if path.suffix == ".md":
                for number, block in enumerate(re.findall(r"(?ms)^\s*```json\s*\n(.*?)^\s*```\s*$", text), 1):
                    try:
                        loads_strict_json(block)
                    except ValueError:
                        findings.append(f"{label}: invalid JSON code fence {number}")
    return findings


REASON_CODES = frozenset({
    "ADDONS_DISABLED", "DETERMINISTIC_OPERATION", "ROUTE_LOCAL_ELIGIBLE",
    "ROUTE_FREE_ELIGIBLE", "NO_VERIFIED_WORKER_ROUTE", "UNKNOWN_TASK_SHAPE",
    "UNKNOWN_OPERATION", "HIGH_REASONING_REQUIRED", "CREDENTIAL_DATA",
    "UNKNOWN_DATA_CLASS", "IRREVERSIBLE_EFFECT", "UNKNOWN_EXTERNAL_EFFECT",
    "VERIFIER_MISSING", "VERIFICATION_UNKNOWN", "ROUTE_UNAVAILABLE",
    "CAPABILITY_STATUS_UNKNOWN", "CAPABILITY_EXPIRED", "RUNTIME_FINGERPRINT_MISMATCH",
    "MODEL_IDENTITY_UNKNOWN", "TASK_CLASS_UNVERIFIED", "REASONING_UNSUPPORTED",
    "DATA_CLASS_UNSUPPORTED", "CONTEXT_TOO_LARGE", "TOOLS_UNVERIFIED",
    "OUTPUT_CAPABILITY_UNVERIFIED", "VERIFICATION_METHOD_UNSUPPORTED",
    "HARD_SPEND_STOP_UNVERIFIED", "VERIFIED_WORKER_RESULT", "WORKER_VERIFICATION_FAILED",
    "MAIN_FALLBACK_NOT_AUTHORIZED", "MAIN_FALLBACK_LIMIT_REACHED", "CORRELATION_MISMATCH",
    "VERIFIER_NOT_INDEPENDENT", "VERIFIER_AUTHORIZATION_MISMATCH", "LATE_RESULT_REJECTED",
})
ROUTES = ("deterministic-code", "local", "free", "main")
# These are code-level safety invariants; policy may order eligible routes but cannot weaken them.
IMMUTABLE_MAIN_GATES = {
    "task_shape": {"open-ended", "unknown"}, "reasoning": {"high", "unknown"},
    "data_class": {"credentials", "unknown"}, "external_effect": {"irreversible", "unknown"},
    "verification": {"none", "unknown"},
}
ENABLED_SWITCHES = {"local_gpu_enabled", "free_model_enabled", "omniroute_enabled"}
POLICY_VALUE_ENUMS = {
    "task_shape": {"bounded", "open-ended", "unknown"},
    "operation": {"deterministic", "semantic", "mixed", "unknown"},
    "reasoning": {"low", "medium", "high", "unknown"},
    "data_class": {"public", "internal", "confidential", "credentials", "unknown"},
    "external_effect": {"none", "reversible", "irreversible", "unknown"},
    "verification": {"deterministic", "human", "none", "unknown"},
}
MAIN_GATE_REASON_MAPPING = {
    "task_shape": {"open-ended": "UNKNOWN_TASK_SHAPE", "unknown": "UNKNOWN_TASK_SHAPE"},
    "reasoning": {"high": "HIGH_REASONING_REQUIRED", "unknown": "HIGH_REASONING_REQUIRED"},
    "data_class": {"credentials": "CREDENTIAL_DATA", "unknown": "UNKNOWN_DATA_CLASS"},
    "external_effect": {"irreversible": "IRREVERSIBLE_EFFECT", "unknown": "UNKNOWN_EXTERNAL_EFFECT"},
    "verification": {"none": "VERIFIER_MISSING", "unknown": "VERIFICATION_UNKNOWN"},
}
POST_RESULT_ENUMS = {
    "worker_routes": {"local", "free"}, "verifier_results": {"pass", "fail", "unknown"},
    "verifier_types": {"deterministic", "human", "independent-model"},
    "terminal_states": {"accepted", "stopped", "cancelled", "timed-out", "main-fallback-failed"},
}
POST_RESULT_ACTIONS = {
    "pass": "accept", "failed_first": "fallback-main", "fallback_not_authorized": "stop",
    "fallback_limit": "stop", "correlation_failure": "reject", "verifier_not_independent": "stop",
    "terminal_late_result": "reject",
    "verifier_authorization_failure": "reject",
}


def _timestamp(value, field):
    from datetime import datetime, timezone
    if not isinstance(value, str) or not re.fullmatch(
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})", value
    ):
        raise ValueError(field + " must be an RFC 3339 timestamp")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("invalid " + field) from exc
    return result.astimezone(timezone.utc)


def _validate_policy(policy):
    required = {"kind", "version", "default_route", "enabled_when_any", "route_precedence",
                "allowed_values", "main_only", "main_gate_reason_mapping", "routes", "post_result",
                "reason_codes", "failure_behavior", "evidence_limit"}
    if not isinstance(policy, dict) or set(policy) != required:
        raise ValueError("task routing policy fields do not match schema")
    if policy["kind"] != "forced-task-routing-policy" or policy["version"] != 2:
        raise ValueError("unsupported task routing policy")
    if set(policy["enabled_when_any"]) != ENABLED_SWITCHES or len(policy["enabled_when_any"]) != len(ENABLED_SWITCHES):
        raise ValueError("enabled_when_any must contain the exact add-on switches")
    if policy["default_route"] != "main" or set(policy["route_precedence"]) != set(ROUTES) or len(policy["route_precedence"]) != 4:
        raise ValueError("route precedence must contain each route exactly once")
    if set(policy["reason_codes"]) != REASON_CODES or len(policy["reason_codes"]) != len(REASON_CODES):
        raise ValueError("reason code enum is not the closed stable set")
    if not all(isinstance(policy.get(name), dict) for name in ("allowed_values", "main_only", "main_gate_reason_mapping", "routes", "post_result", "failure_behavior")):
        raise ValueError("nested policy sections must be objects")
    if set(policy["allowed_values"]) != set(POLICY_VALUE_ENUMS) or any(
        not isinstance(policy["allowed_values"][field], list)
        or set(policy["allowed_values"][field]) != values
        or len(policy["allowed_values"][field]) != len(values)
        for field, values in POLICY_VALUE_ENUMS.items()
    ):
        raise ValueError("allowed value enums do not match the closed contract")
    if set(policy["main_only"]) != set(IMMUTABLE_MAIN_GATES) or set(policy["main_gate_reason_mapping"]) != set(MAIN_GATE_REASON_MAPPING):
        raise ValueError("main gate fields do not match the closed contract")
    for field, invariant in IMMUTABLE_MAIN_GATES.items():
        if not isinstance(policy["main_only"][field], list) or set(policy["main_only"][field]) != invariant or len(policy["main_only"][field]) != len(invariant):
            raise ValueError("immutable main-only safety gate weakened")
        if policy["main_gate_reason_mapping"].get(field) != MAIN_GATE_REASON_MAPPING[field]:
            raise ValueError("main gate reason mapping semantics changed")
    if set(policy["routes"]) != {"local", "free"}:
        raise ValueError("route policy keys do not match schema")
    for route in ("local", "free"):
        config = policy["routes"][route]
        if not isinstance(config, dict) or set(config) != {"allowed", "policy_mismatch_reason", "expected_verifier"} or not isinstance(config["allowed"], dict) or set(config["allowed"]) != set(POLICY_VALUE_ENUMS):
            raise ValueError("nested route policy keys do not match schema")
        for field, values in config["allowed"].items():
            if not isinstance(values, list) or not values or len(values) != len(set(values)) or not set(values).issubset(POLICY_VALUE_ENUMS[field]):
                raise ValueError("route allowed values are invalid")
        if config["policy_mismatch_reason"] != "NO_VERIFIED_WORKER_ROUTE":
            raise ValueError("route mismatch reason semantics changed")
        verifier = config["expected_verifier"]
        if (not isinstance(verifier, dict) or set(verifier) != {"identity", "type", "independence"}
                or not isinstance(verifier["identity"], str) or not verifier["identity"]
                or verifier["type"] not in POST_RESULT_ENUMS["verifier_types"]
                or verifier["independence"] != "independent"):
            raise ValueError("route expected verifier authorization is invalid")
    post = policy["post_result"]
    if set(post) != set(POST_RESULT_ENUMS) | {"maximum_main_fallbacks", "actions"}:
        raise ValueError("post-result policy keys do not match schema")
    if any(not isinstance(post[field], list) or set(post[field]) != values or len(post[field]) != len(values) for field, values in POST_RESULT_ENUMS.items()):
        raise ValueError("post-result enum changed")
    if post.get("maximum_main_fallbacks") != 1:
        raise ValueError("immutable one-fallback safety bound weakened")
    if post.get("actions") != POST_RESULT_ACTIONS:
        raise ValueError("immutable post-result actions changed")
    if set(policy["failure_behavior"]) != {"pre_dispatch", "post_dispatch", "enforcement"} or not all(isinstance(value, str) and value for value in policy["failure_behavior"].values()):
        raise ValueError("failure behavior fields do not match schema")
    if not isinstance(policy["evidence_limit"], str) or not policy["evidence_limit"]:
        raise ValueError("evidence limit required")
    return policy


def _validate_task_request(request, policy):
    required = {"schema_version", "task_id", "task_class", "task_shape", "operation", "reasoning",
                "data_class", "external_effect", "verification", "context_tokens", "required_tools",
                "required_output_capabilities", "evaluation_time", "local_gpu_enabled",
                "free_model_enabled", "omniroute_enabled", "capability_evidence"}
    if not isinstance(request, dict) or set(request) != required or request["schema_version"] != 2:
        raise ValueError("task route request fields do not match schema")
    if not isinstance(request["task_id"], str) or not request["task_id"].strip() or not isinstance(request["task_class"], str) or not request["task_class"]:
        raise ValueError("task and class identity required")
    for field in ("local_gpu_enabled", "free_model_enabled", "omniroute_enabled"):
        if type(request[field]) is not bool:
            raise ValueError(field + " must be boolean")
    if type(request["context_tokens"]) is not int or request["context_tokens"] <= 0:
        raise ValueError("context_tokens must be a positive integer")
    for field in ("required_tools", "required_output_capabilities"):
        value = request[field]
        if not isinstance(value, list) or len(value) != len(set(value)) or not all(isinstance(x, str) and x for x in value):
            raise ValueError(field + " must be a unique string array")
    for field, values in policy["allowed_values"].items():
        if request[field] not in values:
            raise ValueError("invalid " + field)
    _timestamp(request["evaluation_time"], "evaluation_time")
    if not isinstance(request["capability_evidence"], dict) or set(request["capability_evidence"]) != {"local", "free"}:
        raise ValueError("both route evidence slots are required")


def _match_capability(task, evidence, route, config):
    fields = {"schema_version", "worker_id", "requested_model", "resolved_model", "runtime_fingerprint",
              "observed_runtime_fingerprint", "evidence_status", "verified_at", "expires_at",
              "effective_context_tokens", "task_classes", "reasoning_levels", "verified_tools",
              "output_capabilities", "data_classes", "verification_methods", "evidence_reference",
              "route_available", "hard_spend_stop_verified"}
    if not isinstance(evidence, dict) or set(evidence) != fields or evidence["schema_version"] != 1:
        raise ValueError(route + " capability evidence fields do not match schema")
    scalar_strings = ("worker_id", "requested_model", "resolved_model", "runtime_fingerprint",
                      "observed_runtime_fingerprint", "evidence_reference")
    if any(not isinstance(evidence[x], str) or not evidence[x] for x in scalar_strings):
        raise ValueError("capability evidence identity fields required")
    for field in ("route_available", "hard_spend_stop_verified"):
        if type(evidence[field]) is not bool:
            raise ValueError("capability evidence booleans required")
    for field in ("task_classes", "reasoning_levels", "verified_tools", "output_capabilities", "data_classes", "verification_methods"):
        value = evidence[field]
        if not isinstance(value, list) or len(value) != len(set(value)) or not all(isinstance(x, str) and x for x in value):
            raise ValueError("invalid capability array")
    if evidence["evidence_status"] not in {"verified", "expired", "unknown", "unavailable"}:
        raise ValueError("invalid evidence status")
    capability_enums = {
        "reasoning_levels": POLICY_VALUE_ENUMS["reasoning"],
        "data_classes": POLICY_VALUE_ENUMS["data_class"],
        "verification_methods": POLICY_VALUE_ENUMS["verification"],
    }
    if any(not set(evidence[field]).issubset(values) for field, values in capability_enums.items()):
        raise ValueError("invalid capability enum")
    if type(evidence["effective_context_tokens"]) is not int or evidence["effective_context_tokens"] <= 0:
        raise ValueError("invalid effective context size")
    verified_at = _timestamp(evidence["verified_at"], "verified_at")
    evaluation_time = _timestamp(task["evaluation_time"], "evaluation_time")
    expires_at = _timestamp(evidence["expires_at"], "expires_at")
    if not verified_at < expires_at:
        raise ValueError("capability evidence timestamps are inconsistent")
    if evidence["evidence_status"] != "verified":
        return "CAPABILITY_STATUS_UNKNOWN"
    if not verified_at <= evaluation_time < expires_at or not verified_at < expires_at:
        if expires_at <= evaluation_time and verified_at < expires_at:
            return "CAPABILITY_EXPIRED"
        raise ValueError("capability evidence timestamps are inconsistent")
    if evidence["runtime_fingerprint"] != evidence["observed_runtime_fingerprint"]:
        return "RUNTIME_FINGERPRINT_MISMATCH"
    if evidence["resolved_model"] == "unknown":
        return "MODEL_IDENTITY_UNKNOWN"
    if not evidence["route_available"]:
        return "ROUTE_UNAVAILABLE"
    checks = (
        (task["task_class"] in evidence["task_classes"], "TASK_CLASS_UNVERIFIED"),
        (task["reasoning"] in evidence["reasoning_levels"], "REASONING_UNSUPPORTED"),
        (task["data_class"] in evidence["data_classes"], "DATA_CLASS_UNSUPPORTED"),
        (task["context_tokens"] <= evidence["effective_context_tokens"], "CONTEXT_TOO_LARGE"),
        (set(task["required_tools"]).issubset(evidence["verified_tools"]), "TOOLS_UNVERIFIED"),
        (set(task["required_output_capabilities"]).issubset(evidence["output_capabilities"]), "OUTPUT_CAPABILITY_UNVERIFIED"),
        (task["verification"] in evidence["verification_methods"], "VERIFICATION_METHOD_UNSUPPORTED"),
    )
    for passed, reason in checks:
        if not passed:
            return reason
    allowed = config["allowed"]
    for field in ("task_shape", "operation", "reasoning", "data_class", "external_effect", "verification"):
        if task[field] not in allowed[field]:
            return config["policy_mismatch_reason"]
    if route == "free" and not evidence["hard_spend_stop_verified"]:
        return "HARD_SPEND_STOP_UNVERIFIED"
    return None


def route_task(request, policy):
    """Pure reference reducer: interpret explicit task, policy and evidence."""
    _validate_policy(policy)
    _validate_task_request(request, policy)
    enabled = any(request[name] for name in policy["enabled_when_any"])
    if not enabled:
        return {"route": "main", "reason_code": "ADDONS_DISABLED", "forced": False}
    for field in policy["main_only"]:
        if request[field] in policy["main_only"][field]:
            code = policy["main_gate_reason_mapping"][field][request[field]]
            return {"route": "main", "reason_code": code, "forced": True}
    failures = []
    for route in policy["route_precedence"]:
        if route == "deterministic-code" and request["operation"] == "deterministic":
            return {"route": route, "reason_code": "DETERMINISTIC_OPERATION", "forced": True}
        if route in {"local", "free"}:
            switch = "local_gpu_enabled" if route == "local" else "free_model_enabled"
            if not request[switch]:
                continue
            reason = _match_capability(request, request["capability_evidence"][route], route, policy["routes"][route])
            if reason is None:
                verifier = policy["routes"][route]["expected_verifier"]
                return {"route": route, "reason_code": "ROUTE_" + route.upper() + "_ELIGIBLE", "forced": True,
                        "worker_id": request["capability_evidence"][route]["worker_id"],
                        "evidence_reference": request["capability_evidence"][route]["evidence_reference"],
                        "expected_verifier_identity": verifier["identity"],
                        "expected_verifier_type": verifier["type"],
                        "expected_verifier_independence": verifier["independence"]}
            failures.append(reason)
        if route == "main":
            return {"route": "main", "reason_code": failures[0] if failures else "NO_VERIFIED_WORKER_ROUTE", "forced": True}
    raise ValueError("policy precedence produced no route")


def resolve_task_result(request, policy):
    """Pure post-result reducer; it never executes acceptance or fallback."""
    _validate_policy(policy)
    required = {"schema_version", "task_id", "decision_id", "worker_id", "expected_task_id",
                "expected_decision_id", "expected_worker_id", "worker_route", "evidence_reference",
                "expected_evidence_reference", "verifier_result", "verifier_type", "verifier_identity",
                "verifier_independence", "expected_verifier_identity", "expected_verifier_type",
                "expected_verifier_independence", "main_fallback_authorized", "main_fallback_count", "execution_state"}
    if not isinstance(request, dict) or set(request) != required or request["schema_version"] != 2:
        raise ValueError("post-result fields do not match schema")
    post = policy["post_result"]
    if request["execution_state"] not in set(post["terminal_states"]) | {"worker-result-pending"} or request["verifier_independence"] not in {"independent", "self-check", "required"}:
        raise ValueError("invalid post-result enum")
    if request["execution_state"] in post["terminal_states"]:
        return {"action": post["actions"]["terminal_late_result"], "reason_code": "LATE_RESULT_REJECTED"}
    correlated = all(request[a] == request[b] for a, b in (("task_id", "expected_task_id"),
        ("decision_id", "expected_decision_id"), ("worker_id", "expected_worker_id"),
        ("evidence_reference", "expected_evidence_reference")))
    if not correlated:
        return {"action": post["actions"]["correlation_failure"], "reason_code": "CORRELATION_MISMATCH"}
    if request["worker_route"] not in post["worker_routes"] or request["verifier_result"] not in post["verifier_results"]:
        raise ValueError("invalid post-result enum")
    if request["verifier_type"] not in post["verifier_types"] or not request["verifier_identity"]:
        raise ValueError("invalid verifier identity/type")
    expected = (request["expected_verifier_identity"], request["expected_verifier_type"], request["expected_verifier_independence"])
    if (not isinstance(expected[0], str) or not expected[0] or expected[1] not in post["verifier_types"]
            or expected[2] != "independent"):
        raise ValueError("invalid expected verifier authorization")
    authorized = policy["routes"][request["worker_route"]]["expected_verifier"]
    authorized_tuple = (authorized["identity"], authorized["type"], authorized["independence"])
    if expected != authorized_tuple:
        return {"action": post["actions"]["verifier_authorization_failure"], "reason_code": "VERIFIER_AUTHORIZATION_MISMATCH"}
    actual = (request["verifier_identity"], request["verifier_type"], request["verifier_independence"])
    if actual != expected:
        return {"action": post["actions"]["verifier_authorization_failure"], "reason_code": "VERIFIER_AUTHORIZATION_MISMATCH"}
    if request["verifier_independence"] != "independent" or request["verifier_identity"] == request["worker_id"]:
        return {"action": post["actions"]["verifier_not_independent"], "reason_code": "VERIFIER_NOT_INDEPENDENT"}
    if type(request["main_fallback_authorized"]) is not bool or type(request["main_fallback_count"]) is not int or request["main_fallback_count"] < 0:
        raise ValueError("invalid fallback state")
    if request["verifier_result"] == "pass":
        return {"action": post["actions"]["pass"], "reason_code": "VERIFIED_WORKER_RESULT"}
    if not request["main_fallback_authorized"]:
        return {"action": post["actions"]["fallback_not_authorized"], "reason_code": "MAIN_FALLBACK_NOT_AUTHORIZED"}
    if request["main_fallback_count"] >= post["maximum_main_fallbacks"]:
        return {"action": post["actions"]["fallback_limit"], "reason_code": "MAIN_FALLBACK_LIMIT_REACHED"}
    return {"action": post["actions"]["failed_first"], "reason_code": "WORKER_VERIFICATION_FAILED"}


def validate_task_routing(root):
    """Validate policy and shipped operational examples with manual validators."""
    root = Path(root).resolve()
    findings = []
    try:
        policy = _validate_policy(load_json_within(root, root / "catalog/task-routing-policy.json"))
        fixtures = load_json_within(root, root / "examples/task-routing.json")
        results = load_json_within(root, root / "examples/task-routing-results.json")
        capabilities = load_json_within(root, root / "examples/capability-evidence.json")
        if not isinstance(fixtures, list) or len(fixtures) < 8:
            raise ValueError("task routing fixtures are incomplete")
        for number, fixture in enumerate(fixtures, 1):
            if fixture.get("kind") != "synthetic-task-routing-fixture" or route_task(fixture["request"], policy) != fixture["expected"]:
                findings.append(f"task routing fixture {number} decision mismatch")
        if not isinstance(results, list) or len(results) < 5:
            raise ValueError("post-result fixtures are incomplete")
        for number, fixture in enumerate(results, 1):
            if fixture.get("kind") != "synthetic-task-result-fixture" or resolve_task_result(fixture["request"], policy) != fixture["expected"]:
                findings.append(f"task result fixture {number} decision mismatch")
        if not isinstance(capabilities, list) or len(capabilities) < 2:
            raise ValueError("capability examples incomplete")
        for capability in capabilities:
            # Exercise the exact evidence validator through a complete route request.
            route = capability["route"]
            request = fixtures[0]["request"].copy()
            request["local_gpu_enabled"] = route == "local"
            request["free_model_enabled"] = route == "free"
            request["capability_evidence"] = dict(request["capability_evidence"], **{route: capability["evidence"]})
            route_task(request, policy)
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        findings.append("missing or invalid forced task routing policy/fixtures")
    return findings


def validate_validation_record(root):
    """Validate closed metadata declarations; never infer that commands or tests ran."""
    root = Path(root).resolve()
    findings = []
    allowed = {
        "kind", "status", "validated_at_utc", "scope", "validated_content_commit", "clean_checkout",
        "repository_command", "harness_identities", "auth_provider_routes", "market_records", "market_sources",
        "synthetic_accounting_examples", "syntax_checks", "native_authenticated_trials", "savings_benchmark",
        "remote_ci_executed", "windows_macos_executed", "independent_review", "notes", "omniroute_inventory",
        "readme_assets", "remote_ci_status", "remote_ci_error", "remote_ci_checked_at_utc",
        "historical_native_help_checks", "additional_platform_surface_records", "omniroute_oauth_category_ids",
        "whole_repository_revalidation", "hypothetical_api_scenario", "forced_task_routing", "declared_test_modules",
    }
    object_keys = {
        "syntax_checks": {"json_fences", "toml_fences", "shell_fences_bash_n", "shell_snippets_executed", "yaml_fences"},
        "independent_review": {"source_lanes", "closure"},
        "omniroute_inventory": {"pin", "registered_engines", "normal_config_choices", "supporting_groups", "runtime_trial"},
        "readme_assets": {"badge_style", "badge_count", "badge_height", "banner_pixels", "banner_status", "visual_review"},
        "whole_repository_revalidation": {"base_commit", "base_files_accounted", "exact_replacements", "replacement_files", "scope", "unverified_boundaries"},
        "hypothetical_api_scenario": {"data", "combinations_checked", "local_gpu_upper_cases_checked", "arithmetic", "evidence_boundary"},
        "forced_task_routing": {"policy", "fixtures", "post_result_fixtures", "routes", "trigger", "failure_behavior", "evidence_boundary", "policy_version", "capability_examples", "schemas"},
    }
    integer_fields = {"harness_identities", "auth_provider_routes", "market_records", "market_sources",
                      "synthetic_accounting_examples", "additional_platform_surface_records", "omniroute_oauth_category_ids"}
    boolean_fields = {"clean_checkout", "native_authenticated_trials", "savings_benchmark", "remote_ci_executed", "windows_macos_executed"}
    string_fields = {"validated_at_utc", "scope", "validated_content_commit", "repository_command",
                     "remote_ci_status", "remote_ci_error", "remote_ci_checked_at_utc"}
    try:
        record = load_json_within(root, root / "validation/record.json")
        policy = load_json_within(root, root / "catalog/task-routing-policy.json")
        harnesses = load_json_within(root, root / "catalog/harnesses.json")
        if not isinstance(record, dict) or not set(record).issubset(allowed):
            findings.append("validation record fields are not closed-world")
            return findings
        if record.get("kind") != "repository-validation-record" or record.get("status") != "metadata-only":
            findings.append("validation record kind/status mismatch")
        for field in integer_fields:
            if field in record and (type(record[field]) is not int or record[field] < 0):
                findings.append("validation record field type mismatch")
        for field in boolean_fields:
            if field in record and type(record[field]) is not bool:
                findings.append("validation record field type mismatch")
        for field in string_fields:
            if field in record and (not isinstance(record[field], str) or not record[field]):
                findings.append("validation record field type mismatch")
        if "notes" in record and (not isinstance(record["notes"], list) or not all(isinstance(x, str) and x for x in record["notes"])):
            findings.append("validation record notes type mismatch")
        for field in ("native_authenticated_trials", "remote_ci_executed", "windows_macos_executed"):
            if record.get(field) is True:
                findings.append("validation record cannot claim execution")
        for field, keys in object_keys.items():
            if field in record and (not isinstance(record[field], dict) or not set(record[field]).issubset(keys)):
                findings.append("validation record nested fields/type mismatch")
        nested_integer_fields = {
            "syntax_checks": {"json_fences", "toml_fences", "shell_fences_bash_n"},
            "omniroute_inventory": {"registered_engines", "normal_config_choices", "supporting_groups"},
            "readme_assets": {"badge_count", "badge_height"},
            "whole_repository_revalidation": {"base_files_accounted", "exact_replacements", "replacement_files"},
            "hypothetical_api_scenario": {"combinations_checked", "local_gpu_upper_cases_checked"},
            "forced_task_routing": {"policy_version"},
        }
        nested_boolean_fields = {"syntax_checks": {"shell_snippets_executed"}, "omniroute_inventory": {"runtime_trial"}}
        for section, fields in nested_integer_fields.items():
            value = record.get(section)
            if isinstance(value, dict) and any(type(value[x]) is not int or value[x] < 0 for x in fields & set(value)):
                findings.append("validation record nested field type mismatch")
        for section, fields in nested_boolean_fields.items():
            value = record.get(section)
            if isinstance(value, dict) and any(type(value[x]) is not bool for x in fields & set(value)):
                findings.append("validation record nested field type mismatch")
        nested_array_fields = {"readme_assets": {"banner_pixels"}, "forced_task_routing": {"routes", "schemas"}}
        for section, keys in object_keys.items():
            value = record.get(section)
            if not isinstance(value, dict):
                continue
            non_strings = nested_integer_fields.get(section, set()) | nested_boolean_fields.get(section, set()) | nested_array_fields.get(section, set())
            if any(not isinstance(value[x], str) or not value[x] for x in (keys - non_strings) & set(value)):
                findings.append("validation record nested field type mismatch")
        if isinstance(record.get("syntax_checks"), dict) and record["syntax_checks"].get("shell_snippets_executed") is True:
            findings.append("validation record cannot claim execution")
        for section, fields in nested_array_fields.items():
            value = record.get(section)
            if isinstance(value, dict):
                for field in fields & set(value):
                    items = value[field]
                    expected = int if field == "banner_pixels" else str
                    if not isinstance(items, list) or not all(type(x) is expected and (expected is int or bool(x)) for x in items):
                        findings.append("validation record nested array type mismatch")
        trials = record.get("historical_native_help_checks")
        trial_keys = {"client", "available", "version", "version_exit", "help_exit", "scope"}
        if trials is not None and (not isinstance(trials, list) or any(
            not isinstance(x, dict) or set(x) != trial_keys or type(x["available"]) is not bool
            or type(x["version_exit"]) is not int or type(x["help_exit"]) is not int
            or any(not isinstance(x[k], str) or not x[k] for k in ("client", "version", "scope"))
            for x in trials
        )):
            findings.append("validation record historical check type mismatch")
        forced = record.get("forced_task_routing")
        if not isinstance(forced, dict) or type(forced.get("policy_version")) is not int:
            findings.append("validation record routing metadata is invalid")
        elif forced["policy_version"] != policy.get("version"):
            findings.append("validation record policy version is stale")
        if type(record.get("harness_identities")) is not int or record["harness_identities"] != len(harnesses):
            findings.append("validation record harness count is stale")
        modules = record.get("declared_test_modules")
        if not isinstance(modules, list) or not modules or len(modules) != len(set(modules)) or not all(
            isinstance(path, str) and path.startswith("tests/") and (root / path).is_file()
            for path in modules
        ):
            findings.append("validation record declared test suite is invalid")
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        findings.append("missing or invalid validation metadata")
    return findings


def route_local_gpu(request, policy):
    """Apply the published local-route gates; this never loads or selects a model."""
    required = {
        "task_class", "parameters_billions", "quantization_bits", "context_tokens",
        "available_memory_gib", "estimated_runtime_memory_gib", "tools_required", "tools_verified",
    }
    if not isinstance(request, dict) or set(request) != required:
        raise ValueError("local route request fields do not match schema")
    if request["task_class"] not in {"general-purpose", "specialist"}:
        raise ValueError("unknown task class")
    for key in ("parameters_billions", "quantization_bits", "context_tokens", "available_memory_gib", "estimated_runtime_memory_gib"):
        value = request[key]
        if isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"invalid {key}")
    if not all(isinstance(request[key], bool) for key in ("tools_required", "tools_verified")):
        raise ValueError("tool flags must be booleans")

    params = request["parameters_billions"]
    bits = request["quantization_bits"]
    if request["task_class"] == "general-purpose" and params <= policy["general_purpose"]["maximum_tiny_parameters_billions"]:
        return {"decision": "reject", "reason": "tiny-general-purpose"}
    if params >= 27 and bits < 2:
        return {"decision": "reject", "reason": "q1-27b"}
    if request["task_class"] == "general-purpose" and bits < policy["general_purpose"]["minimum_quantization_bits"]:
        return {"decision": "reject", "reason": "sub-four-bit-general-purpose"}
    if request["tools_required"] and not request["tools_verified"]:
        return {"decision": "reject", "reason": "unverified-tools"}
    if request["estimated_runtime_memory_gib"] * (1 + policy["general_purpose"]["headroom_fraction"]) > request["available_memory_gib"]:
        return {"decision": "reject", "reason": "memory-no-headroom"}

    candidates = []
    for tier in policy["tiers"]:
        bounds = tier["parameters_billions"]
        if bounds["min"] <= params <= bounds["max"] and bits >= tier["minimum_quantization_bits"]:
            if request["task_class"] == "general-purpose" and not tier["general_purpose"]:
                continue
            if request["available_memory_gib"] < tier["minimum_dedicated_vram_gib"]:
                continue
            if request["context_tokens"] < tier.get("minimum_context_tokens", 0):
                continue
            candidates.append(tier["id"])
    if not candidates:
        return {"decision": "reject", "reason": "no-eligible-tier"}
    return {"decision": "admit-for-capability-trial", "tier": candidates[0], "task_eligible": False}


def validate_local_gpu_routing(root):
    """Validate the native runtime-neutral policy and its synthetic decisions."""
    from datetime import date, datetime, timezone
    root = Path(root).resolve()
    findings = []
    try:
        policy = load_json_within(root, root / "catalog/local-gpu-routing.json")
        fixtures = load_json_within(root, root / "examples/local-gpu-routing.json")
        if not isinstance(policy, dict) or policy.get("kind") != "local-gpu-routing-policy" or policy.get("runtime_neutral") is not True:
            raise ValueError("invalid policy identity")
        general = policy["general_purpose"]
        if general["minimum_parameters_billions"] < 7 or general["maximum_tiny_parameters_billions"] != 2:
            findings.append("local GPU policy must reject tiny models and retain the 7B general-purpose floor")
        if general["minimum_quantization_bits"] < 4 or general["minimum_dedicated_vram_gib"] < 8 or general["minimum_system_or_unified_memory_gib"] < 16:
            findings.append("local GPU minimum-good hardware/quantization floor was weakened")
        if general["headroom_fraction"] < 0.15:
            findings.append("local GPU memory headroom must be at least 15 percent")
        hard_ids = {row["id"] for row in policy["hard_rejections"]}
        if not {"tiny-general-purpose", "q1-27b", "sub-four-bit-general-purpose", "memory-no-headroom", "unverified-tools"}.issubset(hard_ids):
            findings.append("local GPU hard-rejection inventory is incomplete")
        tiers = {row["id"]: row for row in policy["tiers"]}
        for required_tier in ("specialist-only", "minimum-good", "strong-local", "large-local"):
            if required_tier not in tiers:
                findings.append(f"local GPU tier missing: {required_tier}")
        if tiers.get("specialist-only", {}).get("general_purpose") is not False:
            findings.append("specialist-only tier cannot be general purpose")
        if tiers.get("large-local", {}).get("minimum_quantization_bits", 0) < 4:
            findings.append("large-local tier must reject Q1 and require Q4-or-better")
        if not isinstance(policy.get("sources"), list) or len(policy["sources"]) < 4 or not all(_http_url(x) for x in policy["sources"]):
            findings.append("local GPU policy requires current HTTP sources")
        checked = date.fromisoformat(policy.get("checked_on", ""))
        if checked > datetime.now(timezone.utc).date():
            findings.append("local GPU policy check date is in the future")
        if not isinstance(fixtures, list) or len(fixtures) < 5:
            raise ValueError("local GPU fixtures are incomplete")
        seen = set()
        for number, fixture in enumerate(fixtures, 1):
            if fixture.get("kind") != "synthetic-local-route-fixture":
                findings.append(f"local GPU fixture {number} is not labeled synthetic")
                continue
            name = fixture.get("name")
            if not isinstance(name, str) or not name or name in seen:
                findings.append(f"local GPU fixture {number} has an invalid or duplicate name")
            seen.add(name)
            if route_local_gpu(fixture["request"], policy) != fixture["expected"]:
                findings.append(f"local GPU fixture {number} decision mismatch")
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        findings.append("missing or invalid local GPU routing policy/fixtures")
    return findings


def normalize_usage(provider, usage):
    """Illustrate two declared usage schemas; never infer a bill or subscription quota."""
    if provider not in {"openai-responses", "anthropic-messages"}:
        raise ValueError("unsupported usage schema")
    if not isinstance(usage, dict):
        raise ValueError("usage must be an object")

    def number(mapping, key):
        value = mapping.get(key)
        if type(value) is not int or value < 0:
            raise ValueError(f"missing or invalid {key}")
        return value

    input_total = number(usage, "input_tokens")
    output_total = number(usage, "output_tokens")
    cached, reasoning = None, None
    if provider == "anthropic-messages":
        cached = number(usage, "cache_read_input_tokens")
        input_total += cached + number(usage, "cache_creation_input_tokens")
    else:
        for detail, key, maximum in (
            ("input_tokens_details", "cached_tokens", input_total),
            ("output_tokens_details", "reasoning_tokens", output_total),
        ):
            if detail in usage:
                if not isinstance(usage[detail], dict):
                    raise ValueError(f"invalid {detail}")
                value = number(usage[detail], key)
                if value > maximum:
                    raise ValueError(f"{key} exceeds its containing total")
                if key == "cached_tokens":
                    cached = value
                else:
                    reasoning = value
    return {
        "input_total": input_total,
        "output_total": output_total,
        "total": input_total + output_total,
        "cached_input": cached,
        "reasoning_output": reasoning,
    }


def validate_market(root):
    import json
    from datetime import date, datetime, timezone
    root = Path(root).resolve()
    findings = []

    def load(name):
        path = root / "catalog" / name
        try:
            if path.is_symlink() or not path.resolve().is_relative_to(root):
                raise ValueError("unsafe catalog path")
            rows = load_json_within(root, path)
            if not isinstance(rows, list) or not rows or not all(isinstance(x, dict) for x in rows):
                raise ValueError("nonempty object array required")
            return rows
        except (OSError, ValueError):
            findings.append(f"{name}: invalid or empty market catalog")
            return []

    sources = load("sources-market.json")
    items = load("market.json")
    source_urls, source_ids = set(), set()
    for source in sources:
        for key in ("id", "url", "title", "checked_on", "evidence_type", "caveat"):
            if not isinstance(source.get(key), str) or not source[key].strip():
                findings.append(f"market source: missing {key}")
        identity, url = source.get("id"), source.get("url")
        if isinstance(identity, str):
            if identity in source_ids:
                findings.append("market source: duplicate id")
            source_ids.add(identity)
        if _http_url(url):
            if url in source_urls:
                findings.append("market source: duplicate URL")
            source_urls.add(url)
        else:
            findings.append("market source: invalid URL")
    known = {x[k] for x in items for k in ("id", "name") if isinstance(x.get(k), str)}
    seen = set()
    for item_number, item in enumerate(items, 1):
        identity = item.get("id")
        label = f"market item row {item_number}"
        for key in ("id", "name", "category", "url", "rationale", "license_status", "evidence_scope", "checked_on"):
            if not isinstance(item.get(key), str) or not item[key].strip():
                findings.append(f"{label}: missing {key}")
        if isinstance(identity, str):
            if identity in seen:
                findings.append(f"{label}: duplicate id")
            seen.add(identity)
        if item.get("disposition") not in ("core-method", "optional", "experimental", "excluded"):
            findings.append(f"{label}: invalid disposition")
        if not _http_url(item.get("url")):
            findings.append(f"{label}: invalid URL")
        refs = item.get("sources")
        if not isinstance(refs, list) or not refs or any(not _http_url(x) or x not in source_urls for x in refs):
            findings.append(f"{label}: missing or unknown source reference")
        overlaps = item.get("overlapping_with")
        if not isinstance(overlaps, list) or any(not isinstance(x, str) or x not in known for x in overlaps):
            findings.append(f"{label}: invalid overlap reference")
    for row in sources + items:
        try:
            if date.fromisoformat(row.get("checked_on", "")) > datetime.now(timezone.utc).date():
                findings.append("market: check date is in the future")
        except (TypeError, ValueError):
            findings.append("market: invalid check date")
    return findings


OMNI_PIN = "b345c7f6cd4e1590d1177540813302375a75e332"
OMNI_ENGINE_IDS = {
    "lite", "caveman", "aggressive", "ultra", "rtk", "codex-responses", "session-dedup",
    "headroom", "ccr", "llmlingua", "ionizer", "relevance", "llm", "read-lifecycle", "omniglyph",
}
OMNI_NORMAL_IDS = OMNI_ENGINE_IDS - {"ionizer", "llm", "read-lifecycle"}
OMNI_SUPPORTING_IDS = {
    'mcp-description',
    'mcp-accessibility',
    'mcp-tool-cardinality',
    'output-styles',
    'reactive-context-fit',
    'adaptive-budget',
    'hard-budget',
    'provider-context-edit',
    'cache-aware-protection',
    'prefix-freeze',
    'live-zone',
    'compression-result-memo',
    'quantum-lock',
    'fidelity-gate',
    'risk-gate',
    'inflation-bailout-breaker',
    'response-cache',
    'native-prompt-cache',
    'reasoning-replay-cache',
    'request-idempotency',
    'worker-offloading',
    'output-token-cap',
}



def validate_addon_inventory(root):
    root = Path(root).resolve()
    findings = []
    try:
        data = load_json_within(root, root / "catalog/omniroute-features.json")
    except (OSError, UnicodeError, ValueError):
        return ["missing or invalid OmniRoute source inventory"]
    if not isinstance(data, dict) or data.get("kind") != "source-inspected-feature-inventory":
        return ["invalid OmniRoute source inventory kind"]
    if data.get("pinned_commit") != OMNI_PIN or data.get("runtime_tested") is not False:
        findings.append("OmniRoute pin/evidence boundary differs from the reviewed inventory")
    engines = data.get("engines")
    if not isinstance(engines, list) or not all(isinstance(x, dict) and isinstance(x.get("id"), str) for x in engines):
        return findings + ["invalid OmniRoute engine entries"]
    ids = [x["id"] for x in engines]
    if len(ids) != len(set(ids)) or set(ids) != OMNI_ENGINE_IDS:
        findings.append("OmniRoute engine registry coverage mismatch")
    declared = data.get("registered_engine_ids")
    normal = data.get("public_configurable_engine_ids")
    if not isinstance(declared, list) or not all(isinstance(x, str) for x in declared) or sorted(declared) != sorted(OMNI_ENGINE_IDS):
        findings.append("OmniRoute declared engine set mismatch")
    if not isinstance(normal, list) or not all(isinstance(x, str) for x in normal) or sorted(normal) != sorted(OMNI_NORMAL_IDS):
        findings.append("OmniRoute normal-config engine set mismatch")
    for engine in engines:
        expected = engine["id"] in OMNI_NORMAL_IDS
        if engine.get("in_public_catalog") is not expected or engine.get("writable_stacked_schema") is not expected:
            findings.append("OmniRoute engine config availability mismatch")
        sources = engine.get("sources")
        if not isinstance(sources, list) or not sources or not all(_http_url(x) and OMNI_PIN in x for x in sources):
            findings.append("OmniRoute engine needs pinned source URLs")
        if not isinstance(engine.get("risks_and_limits"), str) or not engine["risks_and_limits"].strip():
            findings.append("OmniRoute engine needs explicit limitations")
    groups = data.get("supporting_mechanisms")
    if not isinstance(groups, list) or len(groups) != 22 or not all(isinstance(x, dict) and isinstance(x.get("id"), str) for x in groups):
        findings.append("OmniRoute supporting-group coverage mismatch")
    else:
        if len({x["id"] for x in groups}) != len(groups) or {x["id"] for x in groups} != OMNI_SUPPORTING_IDS:
            findings.append("OmniRoute supporting-group identity mismatch")
        for group in groups:
            source = group.get("source_url")
            if not _http_url(source) or OMNI_PIN not in source:
                findings.append("OmniRoute supporting group needs pinned source")
            if any(not isinstance(group.get(key), str) or not group[key].strip() for key in ("scope", "caveat")):
                findings.append("OmniRoute supporting group needs scope and limitations")
    counts = data.get("counts")
    if not isinstance(counts, dict) or counts != {"registered_engines": 15, "normal_config_choices": 12, "supporting_groups": 22}:
        findings.append("OmniRoute declared inventory counts mismatch")
    return findings


def validate_assets(root):
    import xml.etree.ElementTree as ET
    import os
    root = Path(root).resolve()
    assets = root / "assets"
    if not assets.exists():
        return []
    if assets.is_symlink() or not assets.resolve().is_relative_to(root):
        return ["unsafe assets directory"]
    findings = []
    for directory, dirs, names in os.walk(assets, followlinks=False):
        for name in list(dirs):
            if (Path(directory) / name).is_symlink():
                findings.append("symlinked asset directory")
                dirs.remove(name)
        for name in names:
            path = Path(directory) / name
            if path.suffix.lower() != ".svg":
                continue
            label = path.relative_to(root)
            try:
                if path.stat().st_size > 2_000_000:
                    raise ValueError("oversized SVG")
                text = read_text_within(root, path)
                if "<!DOCTYPE" in text.upper() or "<!ENTITY" in text.upper():
                    findings.append(f"{label}: SVG declaration is not allowed")
                    continue
                element = ET.fromstring(text)
                if element.tag.split("}")[-1] != "svg":
                    raise ValueError("not SVG")
            except (OSError, UnicodeError, ValueError, ET.ParseError):
                findings.append(f"{label}: invalid or unsafe SVG")
                continue
            for node in element.iter():
                tag = node.tag.split("}")[-1].lower()
                if tag in {"script", "foreignobject", "iframe", "style", "image", "animate", "set"}:
                    findings.append(f"{label}: active/external SVG content is not allowed")
                for key, value in node.attrib.items():
                    key = key.split("}")[-1].lower()
                    if key.startswith("on") or (key in {"href", "src"} and not value.startswith("#")):
                        findings.append(f"{label}: active/external SVG attribute is not allowed")
                    if "url(" in value.lower() and not re.fullmatch(r"url\(\s*#[A-Za-z0-9_-]+\s*\)", value):
                        findings.append(f"{label}: external SVG resource is not allowed")
    return findings


PLATFORM_IDS = {'microsoft-copilot-chat', 'chatgpt-desktop-codex', 'claude-apps-cowork', 'librechat', 'dify', 'copilot-studio', 'zed', 'pydanticai', 'flowise-legacy', 'bolt', 'github-copilot-sdk', 'langflow', 'devin-cloud', 'codex-cloud', 'roo-code-legacy', 'n8n', 'openai-agents-sdk', 'microsoft-agent-framework', 'google-adk', 'mastra', 'openhands', 'agno', 'gemini-notebook', 'chatgpt-web', 'vercel-ai-sdk', 'open-webui', 'claude-agent-sdk', 'lovable', 'langgraph', 'replit-agent', 'crewai', 'kiro', 'gemini-apps', 'amazon-q-developer'}
PLATFORM_TIERS = {"documented configurable interface", "limited native/workflow-only support", "legacy or migration-only", "legacy documented configurable interface", "unsupported interface", "unverified"}


def validate_platform_coverage(root):
    from datetime import date, datetime, timezone
    root = Path(root).resolve()
    try:
        data = load_json_within(root, root / "catalog/coverage.json")
    except (OSError, ValueError):
        return ["missing or invalid platform coverage"]
    if not isinstance(data, list) or not all(isinstance(x, dict) and isinstance(x.get("id"), str) for x in data):
        return ["invalid platform records"]
    findings = []
    ids = [x["id"] for x in data]
    if len(ids) != len(set(ids)) or set(ids) != PLATFORM_IDS:
        findings.append("platform identity coverage mismatch")
    for row in data:
        label = row["id"]
        for key in ("name", "category", "evidence_level"):
            if not isinstance(row.get(key), str) or not row[key].strip(): findings.append(label + ": missing " + key)
        for key in ("current_status", "conservative", "aggressive", "delegation", "omniroute_interface", "upstream_auth", "billing"):
            if not isinstance(row.get(key), dict) or not row[key]: findings.append(label + ": missing " + key)
        interface = row.get("omniroute_interface")
        if not isinstance(interface, dict) or interface.get("tier") not in PLATFORM_TIERS:
            findings.append(label + ": invalid interface evidence tier")
        refs = row.get("sources")
        if not isinstance(refs, list) or not refs or not all(_http_url(x) for x in refs): findings.append(label + ": missing primary sources")
        limits = row.get("limitations")
        if not isinstance(limits, list) or not limits or not all(isinstance(x, str) and x.strip() for x in limits): findings.append(label + ": missing limits")
        try:
            if date.fromisoformat(row.get("checked_on", "")) > datetime.now(timezone.utc).date(): findings.append(label + ": future check date")
        except (TypeError, ValueError): findings.append(label + ": invalid check date")
    return findings


OMNI_AUTH_IDS = {'devin-cli', 'codex', 'codebuddy-cn', 'zed', 'grok-cli', 'openference', 'zed-hosted', 'agy', 'gitlab-duo', 'qoder', 'github', 'cline', 'trae', 'amazon-q', 'antigravity', 'claude', 'kimi-coding', 'cursor', 'xai-oauth', 'devin-desktop', 'ghe-copilot', 'clinepass', 'kilocode', 'kiro'}

def validate_auth_matrix(root):
    root = Path(root).resolve()
    try:
        data = load_json_within(root, root / "catalog/omniroute-auth.json")
    except (OSError, ValueError): return ["missing or invalid authentication matrix"]
    if not isinstance(data, dict) or data.get("kind") != "source-inspected-authentication-matrix": return ["invalid authentication matrix kind"]
    findings = []
    if data.get("runtime_tested") is not False or data.get("pin") != OMNI_PIN: findings.append("auth matrix evidence/pin mismatch")
    rows = data.get("rows")
    if not isinstance(rows, list) or not all(isinstance(x, dict) for x in rows): return findings + ["invalid auth matrix rows"]
    ids = []
    for row in rows:
        names = row.get("provider_ids")
        if not isinstance(names, list) or not names or not all(isinstance(x, str) for x in names): findings.append("invalid auth provider IDs")
        else: ids.extend(names)
        for key in ("technical_support", "interface_runtime", "policy_status", "account_test_boundary"):
            if not isinstance(row.get(key), str) or not row[key].strip(): findings.append("auth matrix missing " + key)
        refs = row.get("source_urls")
        if not isinstance(refs, list) or not refs or not all(_http_url(x) for x in refs): findings.append("auth matrix missing source")
        if row.get("runtime_tested") is not False: findings.append("auth row runtime boundary changed")
    if len(ids) != len(set(ids)) or set(ids) != OMNI_AUTH_IDS: findings.append("auth provider coverage mismatch")
    return findings


def validate_api_cost_scenario(root):
    from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
    root = Path(root).resolve()
    try:
        data = load_json_within(root, root / "examples/api-cost-scenario.json")
        if data.get("kind") != "hypothetical-api-cost-scenario" or data.get("not_a_benchmark") is not True or data.get("not_a_forecast") is not True:
            return ["API scenario must remain explicitly hypothetical, not a benchmark or forecast"]
        def fraction(value):
            x = Decimal(str(value))
            if not x.is_finite() or x < 0 or x > 1: raise ValueError("invalid fraction")
            return x
        baseline = Decimal(str(data["baseline_variable_api_cost"]))
        if not baseline.is_finite() or baseline <= 0: raise ValueError("invalid baseline")
        config = data["delegation"]
        share = fraction(config["eligible_remaining_spend"])
        worker = 1 - share + share * fraction(config["relative_worker_unit_cost"]) + fraction(config["additional_overhead"])
        expected = {(m, o, d) for m in ("Conservative", "Aggressive") for o in (False, True) for d in (False, True)}
        seen = set()
        findings = []
        for row in data["rows"]:
            mode, omni, delegation = row["mode"], row["compression"], row["cheaper_delegation"]
            if type(omni) is not bool or type(delegation) is not bool: raise ValueError("invalid switch")
            identity = (mode, omni, delegation)
            if identity not in expected or identity in seen: findings.append("API scenario configuration set mismatch")
            seen.add(identity)
            cost = baseline * (1 - fraction(data["base_reduction"][mode]))
            if omni: cost *= 1 - fraction(data["omniroute_net_increment"][mode])
            if delegation: cost *= worker
            rounded_cost = cost.quantize(Decimal(".01"), rounding=ROUND_HALF_UP)
            rounded_percent = int(((1 - cost / baseline) * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
            if Decimal(str(row["cost"])) != rounded_cost or row["rounded_reduction_percent"] != rounded_percent:
                findings.append("API scenario arithmetic mismatch")
        if seen != expected: findings.append("API scenario must cover all eight combinations")
        local = data["local_gpu_upper_case"]
        if local.get("mode") != "Aggressive" or local.get("compression") is not True:
            findings.append("local GPU upper case must use the declared Aggressive plus OmniRoute route")
        local_share = fraction(local["eligible_remaining_spend"])
        local_multiplier = 1 - local_share + local_share * fraction(local["relative_local_unit_cost"]) + fraction(local["additional_overhead"])
        local_cost = baseline * (1 - fraction(data["base_reduction"]["Aggressive"])) * (1 - fraction(data["omniroute_net_increment"]["Aggressive"])) * local_multiplier
        local_rounded_cost = local_cost.quantize(Decimal(".01"), rounding=ROUND_HALF_UP)
        local_rounded_percent = int(((1 - local_cost / baseline) * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
        if Decimal(str(local["cost"])) != local_rounded_cost or local["rounded_reduction_percent"] != local_rounded_percent or local_rounded_percent != 75:
            findings.append("local GPU upper-case arithmetic mismatch")
        if not isinstance(local.get("scope"), str) or "not an average" not in local["scope"]:
            findings.append("local GPU upper case must retain its evidence boundary")
        if not isinstance(data.get("assumptions"), str) or not data["assumptions"].strip(): findings.append("API scenario assumptions missing")
        return findings
    except (OSError, ValueError, TypeError, KeyError, AttributeError, InvalidOperation):
        return ["missing or invalid API scenario data"]
