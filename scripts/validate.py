#!/usr/bin/env python3
"""Validate blueprint documents and fixtures. Never install or alter a harness."""
import argparse
import json
from pathlib import Path
import sys

from validation import load_json_within, normalize_usage, validate_content, validate_links, validate_market, validate_routes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    findings = validate_links(root) + validate_routes(root) + validate_content(root) + validate_market(root)
    examples_checked = 0
    try:
        examples = load_json_within(root, root / "examples/usage-normalization.json")
        if not isinstance(examples, list) or not examples:
            raise ValueError("examples must be a nonempty array")
        for row in examples:
            if row.get("kind") != "synthetic-fixture":
                raise ValueError("accounting example must be labeled synthetic")
            normalized = normalize_usage(row["provider"], row["usage"])
            if normalized["total"] != row["expected_total"]:
                raise ValueError("accounting example total does not match")
            examples_checked += 1
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        findings.append(f"accounting examples: {type(exc).__name__}; inspect the declared schema")
    print(json.dumps({
        "status": "fail" if findings else "pass",
        "scope": "repository documents, schemas, privacy patterns and synthetic accounting only; not native account or savings validation",
        "accounting_examples_checked": examples_checked,
        "findings": findings,
    }, indent=2))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
