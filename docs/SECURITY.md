# RugShield Security Notes

RugShield is a Studionet prototype, not production insurance. The design intentionally emphasizes a few explicit trust and safety boundaries.

## Evidence integrity

Claimants commit URLs and SHA-256 hashes before adjudication. Validators independently retrieve sources and compare fetched content with the commitment.

- `VERIFIED` content may be used.
- `HASH_MISMATCH` content is rejected.
- `UNAVAILABLE` content is rejected.

This prevents a claim from silently relying on web content that changed after commitment.

## Source diversity

Evidence bundles require 2–5 URLs and at least two distinct hosts.

The locked source policy for the demo requires at least one authoritative source or two independent credible sources.

## Prompt-injection boundary

Retrieved source content is wrapped as untrusted evidence and the adjudication prompt explicitly instructs the model to treat it as data rather than instructions.

## Economic safety

Coverage is reserved when a policy is purchased. Owner withdrawals are limited to the free pool so reserved coverage cannot be withdrawn as surplus.

An `INCONCLUSIVE` verdict does not release the reserved liability or trigger a payout.

## Consensus stability

Validator agreement is bound to the economically meaningful verdict rather than exact free-form rationale wording. This reduces liveness failures caused by semantically equivalent but textually different model outputs.

## Known prototype limitations

- Website wallet connection is identification-only and does not submit RugShield transactions.
- No production security audit has been performed.
- No real-world insurance licensing/compliance claim is made.
- The active hardened deployment has not completed a live `COVERED` or `NOT_COVERED` final-settlement test.
