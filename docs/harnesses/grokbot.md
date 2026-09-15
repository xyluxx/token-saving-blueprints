# Grokbot: identity and decision boundary

[Start here](../../START-HERE.md) · [Conservative](../modes/conservative.md) · [Aggressive](../modes/aggressive.md) · [Auth and billing](../auth-and-billing.md) · [Measurement](../measurement.md)

Checked 2026-09-06 UTC. Status: unresolved identity. Not approved for automatic installation, authentication or setup.

## Who this is for

Anyone handed the name “Grokbot” without an exact publisher, repository URL and version. This is a requested boundary entry, not a claim that a small repository is a mainstream harness or that all similarly named products are the same.

Verified candidates:

| Candidate | What its own source describes | Decision boundary |
| :--- | :--- | :--- |
| `pftq/GrokBot` | Windows mouse/keyboard desktop automation with Grok or ChatGPT API keys | A desktop-control script, not official Grok Build.[9] |
| `Franzferdinan51/GrokBot` | README now titled “Grok Build Desktop,” a community desktop/orchestration app using a maintained Grok Build fork | Not the official xAI CLI; its own provider bridge and autonomy settings need separate review.[10] |
| Official xAI “Grok Bot” | A hosted persistent cloud-computer teammate product | Distinct from both repositories and the terminal Grok Build CLI.[21] |
| Official `xai-org/grok-build` | Terminal coding agent installed as `grok` | Use the [Grok Build guide](grok-build.md) only if this is what the reader meant.[28] |

Repository identity snapshots: `pftq/GrokBot` at `0e7eb599f81dc1bc0e3be110824d528df27282c7`; `Franzferdinan51/GrokBot` at `ef97ca50d0fb122095b9ac6bc633753c6663407b`. These identify inspected project documentation, not signed-binary verification or an endorsement.

## Authentication and billing routes

No generic recipe is safe because the candidates have different trust and billing boundaries.

1. The pftq README asks for an xAI or OpenAI API key in a local `apikey.txt`, says it chooses the provider based on the key, and recommends administrator execution. That is not native subscription OAuth. Do not apply its installation instructions to another candidate, and do not run it elevated merely to follow this guide.[9]
2. The Franzferdinan51 README describes official Grok OAuth plus community-managed provider paths, including a Hermes-managed Codex OAuth localhost bridge, MiniMax and third-party APIs. Those are project claims, not independently exercised authentication or provider-term approval. A local bridge still intermediates credentials and protocol state; it is not approved automatically by this blueprint.[10]
3. Official Grok Bot describes an account-based hosted product, shared user-scoped VM and included/extra usage depending on plan. Its docs contain differing plan-eligibility lists and Cursor references. A successful xAI API-key setup does not establish Grok Bot entitlement, and the documentation inspected does not establish an interchangeable local BYOK installation recipe.[21][22]
4. Official Grok Build has native user login, API keys, enterprise auth and custom-provider configuration, all documented separately in its own guide.[27]

For any chosen candidate, the owner must confirm the exact account, intended billing product, endpoint, model, refresh ownership, data access and permission defaults. Native subscriptions are not generic API keys; separate API, cloud and gateway charges must be verified. No candidate receives another candidate's credentials. Until identity is resolved, auth precedence and safe defaults remain unresolved too.

## Conservative recipe

1. Obtain the exact publisher/repository or official product URL, platform, release/version and the intended use: terminal coding, desktop control or hosted cloud teammate.
2. Compare that identity with the source descriptions above. Reject unrelated search hits or lookalike package names. Confirm release provenance and license before any installation.
3. Review the chosen product's credential storage, permission defaults, shell/desktop/network capabilities, model selection and any autonomous schedules. Require an individually owned account and explicit approval before granting access.
4. Once resolved, start with a small read-only local fixture. Apply exact reads, deterministic bulk work, retained source data and complete tests through that product's actual tools. Instruction text is advisory unless a verified native control enforces it.
5. Record a separate route audit before marking any setup approved. The unresolved catalog entry must stay unresolved until a human makes the identity decision.

## Aggressive recipe

Not executable while identity is unresolved. Do not port a hook, compaction flag, API base URL or credential file from another Grok-named tool.

After identity is approved, investigate the chosen product's supported observation controls and checkpoint recovery. Retain original sources, exact state, approvals, failures and already-performed actions. A community README's “token-aware context” or memory claim is not proof of lossless compression or a safe rewrite seam.[10]

For official hosted Grok Bot, all Bots on an account share files, browser sessions and app logins on one computer. A separate Bot name is not a security boundary. Selective memory must not leak one user's or client's information to another workflow.[21]

## Verify and roll back

The real first verification is an identity decision recorded with the exact source and version. Then test native login, a read-only fixture, a denied harmless action, session resume, and a controlled approved write/readback in an isolated environment. Check account billing directly and retain actual logs without secrets.

Until then, rollback is simple: install nothing, import no tokens, change no defaults and grant no service access. For an existing chosen installation, back up its own config and revoke only credentials granted to that exact app if the trial fails. Do not delete a shared Grok/Claude/Codex auth directory to remove an unrelated desktop wrapper. Restore sources/checkpoints, not a replay of external writes.

## Limits and evidence

This is targeted identity research, not an exhaustive census of every Grok-named project. Search returned empty results even on a broad control; direct GitHub and official documentation retrieval succeeded. The candidates are verified as distinct documented projects/products, but no installer, signed release, account or end-to-end run was tested.

The official Grok Bot discovery does not resolve what an unspecified “Grokbot” request meant. Current hosted-product eligibility and community subscription bridges require their own checks. The catalog route is explicitly `unresolved`, with `control: unresolved` and no approval for automatic setup.

## Sources

[9] https://raw.githubusercontent.com/pftq/GrokBot/main/README.md — grokbot-pftq
[10] https://raw.githubusercontent.com/Franzferdinan51/GrokBot/main/README.md — grokbot-franz
[21] https://docs.x.ai/grok-bot/overview — grokbot-official
[22] https://docs.x.ai/grok-bot/faq — grokbot-faq
[27] https://raw.githubusercontent.com/xai-org/grok-build/72a61251fcffb464bcc687aeb5a998e5a98ec0c9/crates/codegen/xai-grok-pager/docs/user-guide/02-authentication.md — grok-auth-source
[28] https://raw.githubusercontent.com/xai-org/grok-build/72a61251fcffb464bcc687aeb5a998e5a98ec0c9/README.md — grok-cli-source
