# Coding efficiency policy

Apply only to coding tasks, as a scoped addition to the project's existing instructions. Do not replace existing rules, safety policy or test requirements. Loading extra policy itself adds context, so keep it relevant.

1. Understand the requested behavior and affected implementation before selecting a shortcut.
2. Look for an existing function or pattern before creating another one. Prefer the standard library or a native platform feature when it satisfies the complete requirement.
3. Avoid speculative abstractions, wrappers, dependencies and scaffolding. Prefer a small maintainable change, not the fewest characters at any cost.
4. Fix the shared root cause rather than duplicating symptom guards. Read actual callers, dynamic paths and tests where needed.
5. Use a precise native patch when appropriate and verify the resulting diff against the current source version.
6. Preserve every requested feature, security boundary, accessibility requirement and mandatory check. Never ship a smaller substitute and ask afterward whether the full request was wanted.
7. Do not impose a one-test ceiling. Run the project's required unit, integration, security and acceptance checks, and describe only what actually ran.
8. Keep failures, uncertainty and missing evidence visible. Stop speculative loops; continue only toward a named unmet criterion with a useful next check.

This original scope-preserving adaptation draws on [Ponytail](https://github.com/DietrichGebert/ponytail). Upstream attribution and MIT notice are retained in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md). Upstream full/ultra behavior is not imported wholesale, and its benchmark percentages are not results for this adaptation.
