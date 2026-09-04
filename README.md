# RugShield

**Consensus-backed rug-pull protection powered by GenLayer Intelligent Contracts.**

RugShield is a GenLayer Studionet prototype that lets an owner fund a protection pool, publish fixed-term coverage offers, let users purchase policies with GEN, and submit SHA-256 committed evidence for multi-validator claim adjudication.

> Prototype / demonstration only. RugShield is not production insurance or a financial product.

## Live project

- **Website:** https://www.genspark.ai/artifact/rE6IIiOEbP3asatrnrvv2g
- **GitHub:** https://github.com/haris4587/RugShield
- **Network:** GenLayer Studionet
- **Active contract:** `0x3df30229C9Fa2c5aAE7517adAFcCce1083DBE8c2`
- **Contract explorer:** https://explorer-studio.genlayer.com/address/0x3df30229C9Fa2c5aAE7517adAFcCce1083DBE8c2
- **Contract source SHA-256:** `860260f2a1bc748563169969c7c4c03388fa8b41cc287d46c8f9b1b13526bc24`

## Why RugShield

RugShield focuses on the evidence trust boundary. A live webpage is not automatically accepted as evidence. A claimant commits URLs and SHA-256 digests before adjudication. During consensus, validators independently retrieve each source and classify it as:

- `VERIFIED` — fetched content matches the committed hash
- `HASH_MISMATCH` — fetched content differs from the commitment
- `UNAVAILABLE` — the source cannot be retrieved

Only `VERIFIED` sources may count toward the source policy or appear in accepted citations.

## Claim outcomes

The Intelligent Contract supports three consensus outcomes:

- `COVERED` — a covered rug event is established under the locked policy terms and source policy
- `NOT_COVERED` — verified evidence establishes that the claim does not satisfy the policy
- `INCONCLUSIVE` — evidence is insufficient, conflicting, unavailable, changed, or fails the locked source standard

A payout can occur only after a `COVERED` verdict.

## Core contract capabilities

- GEN-funded protection pool
- reserved-liability accounting
- canonical SHA-256 offer terms
- exact-premium policy purchases
- fixed coverage and claim windows
- evidence URL + hash commitments
- minimum two-host source diversity
- GenLayer nondeterministic web retrieval
- AI-assisted multi-validator adjudication
- `VERIFIED` / `HASH_MISMATCH` / `UNAVAILABLE` retrieval manifest
- append-only claim revisions
- safe `INCONCLUSIVE` fallback when source standards fail
- owner surplus withdrawal limited to the free pool

## Public methods

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

## Verified Studionet demo

The current deployment completed this flow using Normal / Full Consensus with Simulation Mode disabled:

1. Funded the pool with **2 GEN**.
2. Created offer `rugshield-demo-002` with **1 GEN coverage** and **1 GEN premium**.
3. Purchased policy `rugshield-policy-002`.
4. Submitted a claim with two intentionally incorrect committed SHA-256 values.
5. Validators independently fetched both pages and marked both sources `HASH_MISMATCH`.
6. No usable verified evidence remained, so consensus returned `INCONCLUSIVE`.
7. The **1 GEN liability remained reserved** and **0 GEN was paid out**.

### Final pool state

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

## Successful transactions

| Step | Explorer |
| --- | --- |
| Deploy hardened contract | https://explorer-studio.genlayer.com/tx/0x4dfda33703ca703cf9f77620900f5735d194dbafb5a383c22cbe2283c648669b |
| Fund pool (2 GEN) | https://explorer-studio.genlayer.com/tx/0x4f59a706428b1b61bf5f59d4876ecd6295b660f507066b5eba3294d59b6b8553 |
| Create demo offer | https://explorer-studio.genlayer.com/tx/0xc9bd3b41ed45a422e53fe43f9be47565c1e306549fa99ae7ed70f4d5fcd247b5 |
| Buy protection | https://explorer-studio.genlayer.com/tx/0x5fda179fffb658323eb67527edaf0d7b47b009467f3e0c79255d9dd8ef4a1483 |
| Full Consensus claim | https://explorer-studio.genlayer.com/tx/0x8a036068705c9c71c861e5ae6ad8710287aa7bdbe0e323cde7dca05b31b01db9 |

## Website

The current Genspark dashboard shows the active contract, final pool state, explorer-linked transaction evidence, claim result, and GitHub documentation. It includes a real MetaMask connection flow through `window.ethereum` for **wallet identification only**. RugShield contract transactions are currently executed through GenLayer Studio.

Website source snapshot is included in [`site/index.html`](site/index.html).

## Repository structure

```text
RugShield/
├── README.md
├── PROJECT.md
├── rugshield.py                 # compatibility mirror
├── contracts/
│   ├── README.md
│   └── rugshield.py             # canonical contract source
├── site/
│   ├── README.md
│   └── index.html               # exported website snapshot
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DEPLOYMENT.md
│   ├── DEMO_EVIDENCE.md
│   ├── SECURITY.md
│   ├── TESTING.md
│   ├── WEBSITE.md
│   └── SUBMISSION.md
├── .gitignore
└── LICENSE
```

The deployed contract is mirrored at the repository root so existing website links remain valid. The organized project path is [`contracts/rugshield.py`](contracts/rugshield.py); both copies should remain byte-identical.

## Documentation

- [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md) — active deployment and transactions
- [`docs/DEMO_EVIDENCE.md`](docs/DEMO_EVIDENCE.md) — exact Full Consensus safety-path claim
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — contract design and lifecycle
- [`docs/TESTING.md`](docs/TESTING.md) — completed test flow and scope
- [`docs/SECURITY.md`](docs/SECURITY.md) — evidence and fund-safety boundaries
- [`docs/WEBSITE.md`](docs/WEBSITE.md) — dashboard and wallet behavior
- [`docs/SUBMISSION.md`](docs/SUBMISSION.md) — copy/paste submission evidence links

## Current testing scope

The active hardened deployment has been verified for deployment, funding, offer creation, policy purchase, evidence hash mismatch handling, `INCONCLUSIVE` consensus, claim revision recording, and reserved-liability preservation. A `COVERED` payout and `NOT_COVERED` denial were not executed on this final deployment and are therefore not claimed as completed tests.

