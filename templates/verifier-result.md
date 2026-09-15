# Verifier and post-result record v2

- Schema version: 2
- Task ID / expected task ID:
- Decision ID / expected decision ID:
- Worker ID / expected worker ID:
- Worker route: local / free
- Evidence reference / expected evidence reference:
- Verifier result: pass / fail / unknown
- Verifier type: deterministic / human / independent-model
- Verifier identity:
- Verifier independence: independent / self-check / required
- Expected verifier identity (copied from route decision, not verifier-supplied):
- Expected verifier type (copied from route decision):
- Expected verifier independence (copied from route decision; `independent` in v2):
- Main fallback explicitly authorized: true / false
- Main fallback count:
- Execution state: worker-result-pending / accepted / stopped / cancelled / timed-out / main-fallback-failed

The reference reducer requires the actual verifier identity/type/independence tuple to exactly match the authoritative expected tuple from the route decision. It rejects correlation or verifier-authorization mismatches, non-independent verification, fallback beyond the policy bound, and every late result received in a terminal state. It returns an action; it does not execute one.
