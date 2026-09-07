# Continue: limited maintenance coverage, not a new recommendation

[Start here](../../START-HERE.md) · [Conservative](../modes/conservative.md) · [Aggressive](../modes/aggressive.md) · [Authentication and billing](../auth-and-billing.md) · [Measurement](../measurement.md)

Checked 2026-09-06 (UTC). Evidence: documented unless stated otherwise; no authenticated agent task or savings benchmark was run.

## Who this is for

Existing Continue users preserving or migrating a known working setup. **Continue's first-party homepage says it was acquired by Cursor, and the public repository says it is no longer actively maintained and is read-only.** The editor and standalone `cn` CLI therefore have **limited** classification here, even though their documentation remains reachable. This is not an endorsement of an obscure replacement fork.[28][29]

The pinned final-release README documents a final 2.0.0 release across VS Code, CLI and JetBrains, including removal of authentication and anonymous telemetry. It recommends the CLI over the JetBrains plugin.[93]

## Authentication and billing routes

* Existing editor BYOK/local/cloud configuration: Continue's published schema defines models/providers and roles in `config.yaml`. A known working direct provider or local endpoint may remain usable, but that must be verified against the pinned installed version and provider. Archived documentation alone does not establish maintained compatibility or ongoing security fixes.[21][28]
* Hosted account: old documentation describes Continue login, assistants/models and MCP configuration. The CLI docs also describe `CONTINUE_API_KEY`. These are historical route descriptions: the final-release README says authentication was removed. Do not follow the older login instructions in a final 2.0.0 client. They are not proof the hosted service or old subscription offer is available now. Do not start a new paid plan or rely on hosted assets for recovery.[20][29][93]
* Standalone CLI: `cn` has its own TUI, headless execution and context controls. Older quickstarts describe direct provider credentials and hosted login; the final 2.0.0 README says Continue authentication was removed. Provider inference credentials are still a separate requirement for keyed upstreams. Do not presume every editor `config.yaml` provider or setting works identically in the frozen CLI.[20]
* Subscription OAuth boundary: no new consumer ChatGPT/Claude subscription route is established here. A provider API key is separately billed, not funded by an unrelated chat subscription.

Record existing provider costs or local compute costs separately from any historical Continue subscription. Hosted billing and data-export deadlines were not established from the opened first-party text; no current cancellation/refund promise is made.

## Conservative recipe

This is a maintenance path for an already installed, working setup. It is not an installation or account-onboarding sequence.

1. Back up local configuration, project instructions, retained conversations and source files using the organization's approved method. Record extension/CLI version, selected provider/model/effort, account dependency and tools. Do not export credentials into a public repository.
2. Check that the selected provider/endpoint and existing account route are still supported by their owner before using sensitive source material. If this cannot be established, stop and migrate to an approved maintained harness rather than troubleshooting through a random fork.
3. Editor: open the existing Continue chat/config selector. Keep the model and roles unchanged. The published schema supports `rules` and explicitly configured `context`/`mcpServers`; use an existing local rule, or paste the task instruction below into the chat rather than rewriting global config. Do not migrate old JSON automatically just to perform this task.[18][21]
4. CLI: run `cn --version` and `cn --help` on the existing installation before relying on the frozen quickstart. If that installed help confirms `--readonly`, start `cn --readonly` in the project for investigation; attach only needed files with `@`. Do not use `--auto`, headless unattended execution or a new hosted login for this evaluation.[20]
5. Use this task instruction:

   > Keep the current provider, model, effort and permissions. Enumerate the complete candidate set; read exact relevant ranges and dependencies, maintaining coverage. Use existing deterministic tools for bulk operations and all-row calculations. Do not clear history or substitute a sample for full review. Any implementation must be minimal and followed by all required tests and honest failure reporting.

6. Approve implementation separately in the existing editor session, or leave CLI read-only mode deliberately after reviewing the plan and confirming the installed interaction controls. Review every task diff and run the complete project checks with existing tools. If controls or provider behavior differ from the docs, stop; this guide supplies no invented workaround.

## Aggressive recipe

No new automated history-compression integration or production expansion is recommended for an unmaintained harness.[28]

For an existing authorized maintenance task only:

1. Use the normal IDE terminal or existing local parser to retain full test/query output and create a view with revision, complete coverage/counts, all failures and original-source locations. This is operator-prepared context, not an extension interception layer.
2. Attach that view explicitly in the existing editor chat or `cn` TUI. Retain the full original material and read every page if every record must be reviewed. Do not enable experimental history mutation in a frozen client.
3. At a clean boundary, retain the current session and create a handoff for a new session or a separately approved maintained harness. Preserve requirements, identifiers, permissions, test evidence, pending work and completed external actions. Verify these against originals before continuing.
4. On lost requirements, stale source revisions, incomplete counts or test discrepancies, stop using the shortened view and reopen the full evidence. If originals depend on an unavailable hosted service, report the recovery blocker.

Control ceiling: legacy native attachments/tools plus explicit operator-supplied context. Open source does not mean a safe runtime hook already exists. Building a fork, proxy or compressor would be a different project, not this blueprint.

## Verify and roll back

Record actual installed controls, full test results, diff quality and the existing provider's usage when available. No token-usage API or quota refund is assumed. If the provider meter is absent, report only observable attachment/log size and task outcome, clearly labeled as observations rather than billing.

Restore the backed-up local rule/config and original attachments. Reopen the retained session/raw evidence or migrate only after approval. Undo task edits through reviewed diffs/backups while preserving unrelated work. Do not delete the last local copy of account-dependent data or disconnect an account as a rollback shortcut. External writes and provider charges are irreversible through local file restoration.

## Limits and evidence

**Limited:** discontinued active maintenance is established from first-party statements, while reachable docs provide only the historical feature contract.[28][29] Native execution, current hosted service availability, provider compatibility and exact sunset/export dates were not validated. Both editor and CLI deserve migration coverage because of their established ecosystem, not promotion as a new mainstream deployment choice.[18][20]

## Sources

[18] https://docs.continue.dev
[20] https://docs.continue.dev/cli/quickstart
[21] https://docs.continue.dev/reference
[28] https://github.com/continuedev/continue
[29] https://www.continue.dev
[93] https://raw.githubusercontent.com/continuedev/continue/68d2702077bc3d8aecf282ec450ee5372da81cdf/README.md
