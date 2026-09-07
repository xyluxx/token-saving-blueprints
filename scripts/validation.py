"""Dependency-free checks for this documentation repository, not an AI runtime."""
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


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


def read_text_within(root, path):
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
    return path.read_text(encoding="utf-8")


def load_json_within(root, path):
    import json
    return json.loads(read_text_within(root, path))


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
    identity_map = {}
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
                    json.loads(text)
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
                        json.loads(block)
                    except ValueError:
                        findings.append(f"{label}: invalid JSON code fence {number}")
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
