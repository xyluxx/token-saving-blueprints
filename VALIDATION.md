# What is validated

This page describes evidence boundaries. It is not a badge claiming that every provider account or savings percentage was tested.

## Repository checks

The repeatable commands are:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

They check supported internal Markdown navigation, required harness coverage and canonical identity/display-name associations, route enums/dates/source URLs, market/source catalogue references, guide sections, JSON examples, Python syntax, common private-path/credential patterns, the pinned OmniRoute inventory, provider-auth and platform coverage records, SVG safety and synthetic usage accounting. Unsafe input paths are rejected before opening them. Unit tests include deliberately broken inputs, not only happy paths. These checks are not a complete CommonMark parser, secret detector or semantic source verifier.

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
