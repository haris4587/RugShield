# RugShield Full Consensus Demo Evidence

This document records the safety-path Full Consensus test against the active hardened Studionet deployment.

## Contract and policy

- **Contract:** `0x3df30229C9Fa2c5aAE7517adAFcCce1083DBE8c2`
- **Policy:** `rugshield-policy-002`
- **Claim transaction:** https://explorer-studio.genlayer.com/tx/0x8a036068705c9c71c861e5ae6ad8710287aa7bdbe0e323cde7dca05b31b01db9

## Claim statement

```text
The holder alleges that RugShield Demo Token suffered a rug event during the active coverage window. The submitted evidence must be verified against the committed hashes and evaluated under the locked source policy.
```

## Committed evidence bundle

```json
{
  "urls": [
    "https://example.com/",
    "https://www.iana.org/help/example-domains"
  ],
  "hashes": [
    "0000000000000000000000000000000000000000000000000000000000000000",
    "1111111111111111111111111111111111111111111111111111111111111111"
  ],
  "bundle_hash": "b6e431a96411148e7b15a6a9cc3c1a322e109e9da42c7ab4f1511375337fcabf"
}
```

The committed hashes were intentionally incorrect. The purpose was to verify that changed/uncommitted live content cannot silently become payout evidence.

## Retrieval manifest

```json
[
  {
    "url": "https://example.com/",
    "status": "HASH_MISMATCH",
    "committed_sha256": "0000000000000000000000000000000000000000000000000000000000000000",
    "fetched_sha256": "13f5e50297bde87abbf51cd1cd43678109b1a72a52c1cefa3b56844464e4f25c"
  },
  {
    "url": "https://www.iana.org/help/example-domains",
    "status": "HASH_MISMATCH",
    "committed_sha256": "1111111111111111111111111111111111111111111111111111111111111111",
    "fetched_sha256": "6df12620d6e1c1029a1534fc0b2e0eba7107db6daba73f6ae8e52f32386c340a"
  }
]
```

## Consensus result

```json
{
  "authoritative_source_count": 0,
  "citations": [],
  "claim_round": 1,
  "confidence_band": "LOW",
  "event_type": "unverified",
  "evidence_quality": 0,
  "independent_source_count": 0,
  "matched_rule": "none",
  "source_standard_met": false,
  "verdict": "INCONCLUSIVE"
}
```

Rationale:

> All submitted sources are unusable because both committed URLs are marked HASH_MISMATCH, so none may count toward the locked source policy or be cited. With no VERIFIED usable evidence, the exact token, chain, event type, and event timing within the coverage window cannot be established. Under the policy, this requires an INCONCLUSIVE result.

## What this proves

1. Evidence is bound to claimant-provided SHA-256 commitments.
2. Validators independently retrieve the committed URLs.
3. Live content that differs from the commitment is marked `HASH_MISMATCH`.
4. Mismatched sources cannot count toward the source standard or accepted citations.
5. Weak/unverifiable evidence falls back to `INCONCLUSIVE` rather than an unsafe payout or denial.
6. The claim revision preserves the bundle hash, fetched hashes, retrieval states, verdict, and rationale.
7. The 1 GEN protection liability remained reserved and total payouts remained 0 GEN.
