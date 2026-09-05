# RugShield Reviewer Checklist

This checklist gives a reviewer a short, reproducible path through the published RugShield evidence.

## 1. Verify the repository release

Requires Python 3.10 or newer. No third-party packages are needed.

```bash
python -m unittest discover -s tests -v
python scripts/verify_release.py
```

The verifier checks that:

- the root and `contracts/` contract sources are byte-identical;
- the source SHA-256 matches the active Studionet deployment record;
- the documented offer terms and evidence bundle hashes recompute exactly;
- the expected contract methods and critical safety guards remain present;
- deployment, Full Consensus, website, and submission records use one consistent address and transaction;
- the website contains its required evidence sections and valid repository targets;
- no obvious private key or GitHub token pattern is committed.

GitHub Actions runs the same checks on every push and pull request.

## 2. Inspect the active contract

- Contract: `0x3df30229C9Fa2c5aAE7517adAFcCce1083DBE8c2`
- Explorer: https://explorer-studio.genlayer.com/address/0x3df30229C9Fa2c5aAE7517adAFcCce1083DBE8c2
- Deployment transaction: https://explorer-studio.genlayer.com/tx/0x4dfda33703ca703cf9f77620900f5735d194dbafb5a383c22cbe2283c648669b
- Deployed source SHA-256: `860260f2a1bc748563169969c7c4c03388fa8b41cc287d46c8f9b1b13526bc24`

## 3. Inspect the Full Consensus claim

- Claim transaction: https://explorer-studio.genlayer.com/tx/0x8a036068705c9c71c861e5ae6ad8710287aa7bdbe0e323cde7dca05b31b01db9
- Policy: `rugshield-policy-002`
- Claim round: `1`
- Result: `INCONCLUSIVE`
- Evidence state: two `HASH_MISMATCH` results, zero accepted citations
- Economic result: 1 GEN remained reserved and 0 GEN was paid

The exact committed inputs, retrieved hashes, result, and rationale are recorded in [`DEMO_EVIDENCE.md`](DEMO_EVIDENCE.md).

## 4. Scope boundary

The active deployment proves the safety fallback for changed evidence. It does not claim a completed live `COVERED` payout or `NOT_COVERED` denial. The dashboard identifies a connected MetaMask account but contract writes are executed in GenLayer Studio.
