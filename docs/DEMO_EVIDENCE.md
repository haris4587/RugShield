# RugShield Demo Evidence

This document records the Full Consensus claim test performed against the active RugShield Studionet deployment.

## Contract and policy

- **Contract:** `0x3df30229C9Fa2c5aAE7517adAFcCce1083DBE8c2`
- **Policy:** `rugshield-policy-002`
- **Claim transaction:** `0x8a036068705c9c71c861e5ae6ad8710287aa7bdbe0e323cde7dca05b31b01db9`

## Claim statement

```text
The holder alleges that RugShield Demo Token suffered a rug event during the active coverage window. The submitted evidence must be verified against the committed hashes and evaluated under the locked source policy.
```

## Committed evidence bundle

URLs:

```json
[
  "https://example.com/",
  "https://www.iana.org/help/example-domains"
]
```

Committed hashes:

```json
[
  "0000000000000000000000000000000000000000000000000000000000000000",
  "1111111111111111111111111111111111111111111111111111111111111111"
]
```

Bundle hash:

```text
b6e431a96411148e7b15a6a9cc3c1a322e109e9da42c7ab4f1511375337fcabf
```

The hashes were intentionally incorrect for this safety test. The purpose was to prove that live web content that does not match the claimant's committed digest is rejected as usable evidence instead of being silently trusted.

## Retrieval manifest

```json
[
  {
    "committed_sha256": "0000000000000000000000000000000000000000000000000000000000000000",
    "fetched_sha256": "13f5e50297bde87abbf51cd1cd43678109b1a72a52c1cefa3b56844464e4f25c",
    "status": "HASH_MISMATCH",
    "url": "https://example.com/"
  },
  {
    "committed_sha256": "1111111111111111111111111111111111111111111111111111111111111111",
    "fetched_sha256": "6df12620d6e1c1029a1534fc0b2e0eba7107db6daba73f6ae8e52f32386c340a",
    "status": "HASH_MISMATCH",
    "url": "https://www.iana.org/help/example-domains"
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

Rationale returned by the claim adjudication:

> All submitted sources are unusable because both committed URLs are marked HASH_MISMATCH, so none may count toward the locked source policy or be cited. With no VERIFIED usable evidence, the exact token, chain, event type, and event timing within the coverage window cannot be established. Under the policy, this requires an INCONCLUSIVE result.

## Resulting policy state

After the claim:

```json
{
  "claim_round": 1,
  "coverage_amount": 1000000000000000000,
  "last_bundle_hash": "b6e431a96411148e7b15a6a9cc3c1a322e109e9da42c7ab4f1511375337fcabf",
  "last_citations": [],
  "last_confidence_band": "LOW",
  "last_event_type": "unverified",
  "last_matched_rule": "none",
  "last_verdict": "INCONCLUSIVE",
  "offer_id": "rugshield-demo-002",
  "premium_paid": 1000000000000000000,
  "status": "INCONCLUSIVE"
}
```

## What this test proves

1. RugShield binds submitted evidence to claimant-provided SHA-256 commitments.
2. Validators independently retrieve the committed URLs during adjudication.
3. Changed or intentionally mismatched evidence is marked `HASH_MISMATCH`.
4. Mismatched sources cannot count toward the source standard or be cited.
5. A weak/unverifiable claim resolves to `INCONCLUSIVE` rather than triggering an incorrect payout or denial.
6. The claim revision preserves the evidence bundle hash, fetched hashes, retrieval states, verdict, and rationale for later audit.
7. The 1 GEN protection liability remains reserved after the inconclusive result.

## Earlier retrieval failure and hardening

An earlier test deployment attempted to render an Etherscan page that returned a Cloudflare/403 challenge to validators. The contract was subsequently hardened so failed web retrieval becomes an `UNAVAILABLE` evidence state rather than crashing the entire claim, and storage-backed values are copied before entering nondeterministic execution. The active deployment documented above is the hardened version.
