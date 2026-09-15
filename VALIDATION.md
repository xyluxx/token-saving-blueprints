# What is validated

This page describes evidence boundaries. It is not a badge claiming that every provider account or savings percentage was tested.

## Repository checks

The repeatable commands are:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

They check supported internal Markdown navigation, required harness coverage, globally unambiguous aliases and canonical identity/guide associations, route enums/dates/source URLs, market/source catalogue references, guide sections, strict bounded JSON parsing, Python syntax, common private-path/credential patterns, the pinned OmniRoute inventory, provider-auth and platform coverage records, SVG safety, synthetic usage accounting, the runtime-neutral local GPU policy, forced task-routing contracts and derivable validation-record metadata. Unsafe input paths are rejected before opening them.

The forced-routing checks prove that valid policy precedence controls output, immutable safety gates cannot be removed, and local/free qualification composes fresh fingerprint-bound evidence for the exact task class, model identity, context, tools, output, data and verifier method. Post-result tests require exact agreement between route-decision verifier authorization and actual verifier identity/type/independence; they also cover correlation, explicit fallback authorization, the one-fallback bound and terminal late-result rejection. Policy JSON is canonical configurable routing data, while code plus schemas enforce the immutable v2 contract. Local GPU checks are coarse admission only and return `task_eligible: false`. They do not prove unrestricted natural-language classification, dispatch, verifier execution or runtime installation in every harness.

Operational Draft 2020-12 interoperability schemas live in [`schemas/`](schemas/). Shipped examples are validated by explicit dependency-free manual validators. Full standards validation—including every JSON Schema keyword and format—is intentionally delegated to external tooling; this repository does not invent a partial schema engine.

The checks are dependency-free on Python 3.10 or later. Windows can use `py -3`; actual operating systems exercised for a release are listed in [the validation record](validation/record.json). A portable script is not proof every native client was tested on every OS.

## Source-backed recipes

Guides use current official documentation and relevant implementation/schema evidence. Each states its check date, authentication/provider boundaries and remaining limitations. A command described in official docs is documented support, not proof it succeeded with a user's account.

The market scan records its selection scope, including exclusions. Published benchmarks retain their own models, task sets, denominators, quality caveats and overhead. None is relabeled as a benchmark of this repository.

## Native checks and what they do not prove

Where available, installed CLI version/help was inspected without changing authentication or configuration. This proves only the local command surface was present. It does not establish model entitlement, billing, tool execution, cancellation, plugin behavior or a complete native task.

Authenticated setup trials and complete-work savings comparisons must be performed on the chosen route with owner approval. The [one-change trial](docs/measurement.md) is designed for that. No automatic installer or credential broker is included.

## Release review

Before delivery, run the same checks from a clean checkout, inspect the full public surface for private data, and review practical operator paths and load-bearing claims. Record actual results and unresolved issues, not a self-assigned numerical score.

Any CI workflow file, if supplied, is only a definition until an actual run is observed. The release record distinguishes local results from remote CI.

## Reporting validation

Say what passed: documentation/fixture checks, source inspection or a particular native trial. Do not shorten those into “everything tested,” “no quality loss” or “works with any account.”


## Scenario arithmetic versus performance

The [README planning scenario](README.md#api-cost-planning-scenario) is calculated from explicit chosen assumptions in [scenario data](examples/api-cost-scenario.json). Checks cover all eight cloud mode/add-on combinations, the separate 75% local GPU upper case, decimal costs, whole-percentage rounding and nonbenchmark/nonforecast labels. Passing that check proves arithmetic consistency, not that the assumed savings occur. The banner retains its planning-scenario heading, and the README retains the full assumptions and nonbenchmark explanation.
