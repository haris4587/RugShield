# RugShield Architecture

## Components

RugShield currently has two layers:

1. **GenLayer Intelligent Contract (`rugshield.py`)** — authoritative policy, pool, evidence, consensus, and settlement logic.
2. **Dashboard (`site/index.html` / live Genspark artifact)** — presents the deployment and evidence and provides optional MetaMask wallet identification.

The dashboard does not submit RugShield contract transactions directly; Studionet contract writes are currently executed through GenLayer Studio.

## State model

### ProtectionOffer
Stores the token, chain, premium, coverage amount, sale deadline, coverage duration, claim grace period, trigger rules, source policy, terms hash, and active flag.

### ProtectionPolicy
Stores holder, timestamps, coverage amount, premium, lifecycle status, claim round, and latest adjudication metadata.

### Pool accounting

`reserved_liability` tracks coverage amounts that must remain available for unsettled policies.

`free_pool = contract balance - reserved_liability`

Owner surplus withdrawals are restricted to the free pool.

## Lifecycle

### 1. Fund
Owner or another sender calls `fund_pool()` with GEN.

### 2. Create offer
Owner calls `create_offer(...)`. The contract recomputes canonical JSON terms and checks the supplied SHA-256 `terms_hash`.

### 3. Buy protection
A user calls `buy_protection(...)` with the exact premium. The contract reserves the coverage amount.

### 4. Submit evidence
The policy holder submits 2–5 evidence URLs and SHA-256 commitments plus a canonical bundle hash.

### 5. Retrieve and classify
Inside nondeterministic execution, validators retrieve each source in text mode and classify it as `VERIFIED`, `HASH_MISMATCH`, or `UNAVAILABLE`.

### 6. Adjudicate
Only verified sources can count toward the locked source policy. The model returns `COVERED`, `NOT_COVERED`, or `INCONCLUSIVE` plus audit metadata.

### 7. Consensus
Validators independently rerun adjudication. Consensus is bound to the economically meaningful verdict so harmless free-form wording differences do not create unnecessary disagreement.

### 8. Settle
- `COVERED`: release reserve and transfer coverage to the holder.
- `NOT_COVERED`: release reserve without payout.
- `INCONCLUSIVE`: keep the reserve and allow another claim round before the deadline.
- Expired unresolved policies can be finalized with `expire_policy()` after the claim deadline.
