# RugShield

RugShield is a GenLayer Intelligent Contract prototype for consensus-backed token protection. It lets an owner fund a protection pool, publish fixed-term protection offers, let users buy policies with GEN, and submit hashed evidence bundles for AI-assisted multi-validator claim adjudication.

## What RugShield demonstrates

- GEN-funded protection pool with reserved-liability accounting
- Protection offers bound to canonical SHA-256 terms
- Exact-premium policy purchases
- Claim windows and policy expiry
- Evidence bundles committed by URL + SHA-256 hash
- Minimum source diversity across at least two hosts
- GenLayer nondeterministic web retrieval and AI adjudication
- Safe handling of unavailable or changed evidence
- `COVERED`, `NOT_COVERED`, and `INCONCLUSIVE` claim outcomes
- Auditable claim revisions with retrieval manifests
- Payout only after a `COVERED` verdict
- Consensus bound to the economically meaningful verdict rather than free-form wording

## Studionet deployment

**Active contract:** `0x3df30229C9Fa2c5aAE7517adAFcCce1083DBE8c2`

**Deployment transaction:** [`0x4dfda337...648669b`](https://explorer-studio.genlayer.com/tx/0x4dfda33703ca703cf9f77620900f5735d194dbafb5a383c22cbe2283c648669b)

**Deployed source SHA-256:** `860260f2a1bc748563169969c7c4c03388fa8b41cc287d46c8f9b1b13526bc24`

The active contract was deployed in GenLayer Studio on Studionet with Simulation Mode disabled and Normal / Full Consensus.

## Verified demo flow

The active Studionet deployment has completed the following flow:

1. Funded the protection pool with **2 GEN**.
2. Created `rugshield-demo-002`, a **1 GEN coverage / 1 GEN premium** demo offer.
3. Purchased `rugshield-policy-002`.
4. Submitted a Full Consensus claim using two committed evidence URLs with intentionally mismatching SHA-256 hashes.
5. Validators fetched both sources, detected both `HASH_MISMATCH` states, rejected them as usable evidence, and returned **`INCONCLUSIVE`**.
6. The policy remained `INCONCLUSIVE` with the **1 GEN liability still reserved** and **0 GEN paid out**.

Final pool state after the demo:

```json
{
  "balance": 3000000000000000000,
  "free_pool": 2000000000000000000,
  "reserved_liability": 1000000000000000000,
  "total_funding": 2000000000000000000,
  "total_payouts": 0,
  "total_premiums": 1000000000000000000
}
```

See [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md), [`docs/DEMO_EVIDENCE.md`](docs/DEMO_EVIDENCE.md), and [`docs/WEBSITE.md`](docs/WEBSITE.md) for the exact transactions, claim evidence, and current demo-site details.

## Contract

The deployed source is [`rugshield.py`](rugshield.py).

Important public methods:

- `fund_pool()`
- `create_offer(...)`
- `set_offer_active(...)`
- `buy_protection(...)`
- `submit_claim(...)`
- `expire_policy(...)`
- `withdraw_surplus(...)`
- `get_pool_status()`
- `get_offer(...)`
- `get_policy(...)`
- `get_claim_revision(...)`

## Evidence trust boundary

RugShield does not treat a live webpage as automatically valid evidence. The claimant commits URLs and content SHA-256 hashes before adjudication. During consensus, validators retrieve each URL and classify it as:

- `VERIFIED` — live content hash matches the committed hash
- `HASH_MISMATCH` — live content changed or does not match the claimant commitment
- `UNAVAILABLE` — validators cannot retrieve the source

Only `VERIFIED` evidence is allowed to count toward the locked source policy or appear in accepted citations. If the source standard cannot be satisfied, the contract requires an `INCONCLUSIVE` verdict instead of paying or denying on weak evidence.

## Demo dashboard

**Current RugShield website:** https://www.genspark.ai/artifact/rE6IIiOEbP3asatrnrvv2g

The current Genspark dashboard presents the final Studionet deployment, transaction evidence, Full Consensus claim result, and final pool state. It also includes a real MetaMask connection flow for wallet identification through `window.ethereum`.

Wallet connection is for account identification only. Current RugShield Studionet contract transactions are executed through GenLayer Studio; the website does not claim to submit on-chain RugShield transactions directly.

## Network

Built for GenLayer **Studionet** testing and multi-validator consensus.

Studionet Explorer: https://explorer-studio.genlayer.com/

## Status

Prototype / demonstration project. The current deployment is intended for GenLayer project evaluation and testnet experimentation, not production insurance or financial use.
