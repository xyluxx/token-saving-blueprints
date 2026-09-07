# Documents, research and structured data

This playbook is for business reports, contracts, CRM exports, recruiting records, financial reconciliation and source-backed research. The method changes with the coverage requirement.

## Complete calculation is not complete semantic review

If the task is “sum every eligible invoice,” code can process every record and return reconciled totals and exceptions. The model need not read every cell to calculate.

If the task is “review every contract obligation,” every relevant passage still needs semantic review. A top-k excerpt or statistical sample is not a completed review.

## Conservative sequence

1. Identify the exact source, owner, date/version and authority. Keep current corrections ahead of old summaries.
2. Fetch all required pages/attachments into the user's authorized workspace. Record counts, cursors, missing pages and errors.
3. Parse data with the native supported tools. Preserve record IDs, role assignments, units, decimals, dates/time zones, zero/null/missing and multiplicity.
4. Perform deterministic joins, filters and calculations over the complete eligible set.
5. Retrieve exact passages for interpretation with headings, qualifiers, neighboring context and source locations.
6. Produce the actual requested artifact through code where possible. Do not make the model reproduce a large table cell by cell.
7. Verify counts, totals, source coverage, citations and the final artifact. State incompleteness rather than hiding failed pages.

## Aggressive additions

For exploratory or synthesis work, use question-aware passage selection and source-linked notes. Keep an index of omitted sections and unresolved questions so restoration is possible. When the question changes, reconsider whether the selected context remains sufficient.

Representative samples are allowed only when the task explicitly permits them. Never use anomaly retention as proof that all ordinary-but-important records survived.

## Research workflow

Search broadly enough to resolve the question, then read the primary source that supports each important claim. A snippet, abstract or README headline may omit the decisive table or limitation. Separate official documentation, implementation inspection, author benchmarks, independent evidence and your own tests.

Reuse a current source index, not a cached conclusion about a different question. Preserve contradictions and date/version boundaries. A shorter report can be useful; a report missing the requested analysis cannot be called efficient.

## Financial and operational safeguards

Use decimal-safe computation and source-linked reconciliation. Preserve reversals, duplicate events, missing values and entity relationships. Refresh live state before an approved external action and verify the exact target afterward. Previous draft approval or a cached “sent” answer is not new permission.

## Record

Use [task contract](../../templates/task-contract.md), [working set](../../templates/working-set.md) and [trial record](../../templates/trial-record.md). Compare complete work, not just the size of the excerpt returned to the model.
