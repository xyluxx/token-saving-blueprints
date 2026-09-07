# Measure the work, not just the prompt

A quick local trial can guide an operator without pretending to be a universal benchmark. Use the same task, model, effort, legitimate auth, source state and required checks. Compare only the proposed change.

## Four evidence levels

1. **Documented:** a current official guide describes the route or setting.
2. **Source-inspected:** the relevant implementation/schema was read at a recorded revision.
3. **Local-fixture-verified:** a local example or repository check was exercised. This is not an authenticated native workflow.
4. **Native task-tested:** the actual version/account route completed a permitted task and its recovery/rollback checks.

A published study or author benchmark is a separate external result, not a fifth level certifying your installation. See [evidence](evidence.md).

## The practical one-change trial

1. Select a representative task with known acceptance criteria.
2. Record the native setup and any existing optimizations. Do not disable legitimate baseline features to manufacture a larger saving.
3. Complete the baseline task and retain actual usage/outcome evidence.
4. Restore an equivalent starting state. Apply one approved reversible change.
5. Complete the same task, including every required check.
6. Record retries, restoration, failed attempts and human repair.
7. Keep, revise or revert the change based on the complete result.

For nondeterministic tasks, repeat and vary task types before generalizing. A single clean example is a useful smoke test, not proof of average quality or savings. Pair source snapshots, preserve all failures and avoid unrelated plugin/memory differences between arms.

## Count the right fields

Use provider-reported usage when available and label estimates explicitly.

- OpenAI-style input totals may already include cached input. Cached input is a breakdown, not extra tokens to add.
- Reasoning may already be included in output. Do not add it again.
- Anthropic-style ordinary input and cache-read/cache-creation inputs may be separate fields. Normalize them according to the actual API/version.
- Internal/server tool loops can report cumulative processing that is not current context occupancy.
- Missing telemetry is unknown, not zero.

Store per-model counts and the counting method. Different tokenizers and non-model compute need separate notes. The [synthetic usage examples](../examples/README.md) illustrate accounting only; they are not measured savings.

## Compare complete workloads

Use the ratio of aggregate baseline and candidate totals for a declared workload, and report per-task distributions separately. Include helper calls, retries, restores, failed optimized attempts and any fallback to the baseline. Do not average tiny-task percentages as if they represented the business workload.

Use [usage ledger](../templates/usage-ledger.csv) and [trial record](../templates/trial-record.md). An agent can populate these from supported receipts, but must not invent fields the provider does not expose.

## Keep money separate

For APIs, compare actual or clearly estimated charges under the correct rates/cache classes and include added service costs. For subscriptions, record observed allowance effects and completed work; the monthly fee may be unchanged.

Do not apply an API price to RTK's estimated token counter and call it a subscription saving. Do not add a compressor's percentage to an avoided-call estimate if they cover the same baseline work.

## Acceptance before a public claim

Check all required features, tests, records, identifiers, source qualifiers, permissions and current corrections. Use executable checks for deterministic work and blinded human/rubric review for semantic work. “No statistically significant difference” is not proof of equivalence.

A wider claim needs an explicit workload mix, repeated paired runs, source/version records, uncertainty, failures, subgroup/tail behavior and enough samples for the intended conclusion. Critical finance/security/transactional requirements are not traded away through an average score.

Suitable wording:

> On the named tasks and versions in this record, the selected change reduced measured total tokens by the reported amount, with the listed acceptance results, retries and limitations.

Unsuitable wording:

> This saves 75% on every subscription with identical quality.

## Separate setup cost from recurring value

A reusable recipe or index has an initial development/indexing cost and ongoing validation/maintenance costs. Compare them with the repeated work actually avoided. A no-change monitor can avoid inference entirely while still consuming CPU, storage and network resources.

## Stop the experiment honestly

Revert when it changes model/auth unexpectedly, loses required information, adds repeated recovery or does not improve the actual task. Keep useful negative results; they prevent the same bad optimization being retried by every operator.
