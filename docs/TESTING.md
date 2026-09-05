# RugShield Testing

## Automated repository checks

The repository now includes dependency-free integrity regression tests and a fail-fast release verifier:

```bash
python -m unittest discover -s tests -v
python scripts/verify_release.py
```

GitHub Actions runs both commands on every push and pull request. The checks compile/parse the contract source, verify the byte-identical mirror and deployed SHA-256 fingerprint, recompute the demo terms and evidence-bundle commitments, validate cross-document addresses and transaction references, inspect critical safety markers, and validate the exported website structure and repository links.

These checks verify the published release and evidence package. They do not replace the linked Studionet Full Consensus execution.

## Active hardened deployment

`0x3df30229C9Fa2c5aAE7517adAFcCce1083DBE8c2`

## Completed on-chain tests

### Deployment
Hardened contract deployed successfully on GenLayer Studionet.

### Funding
`fund_pool()` funded the contract with 2 GEN.

### Offer creation
Created `rugshield-demo-002` with a canonical terms hash, 1 GEN coverage, and 1 GEN premium.

### Policy purchase
Purchased `rugshield-policy-002` for the exact 1 GEN premium. The contract reserved 1 GEN of liability.

### Evidence integrity / Full Consensus
Submitted a claim with two URLs and intentionally incorrect committed hashes. Both sources were retrieved but classified `HASH_MISMATCH`. The source standard failed and the final consensus verdict was `INCONCLUSIVE`.

### State preservation
After the claim:

- policy claim round = 1
- policy status = `INCONCLUSIVE`
- reserved liability = 1 GEN
- total payouts = 0 GEN
- free pool = 2 GEN

### Audit trail
`get_claim_revision("rugshield-policy-002", 1)` returned the committed bundle hash, retrieval manifest, fetched hashes, verdict, source counts, evidence quality, citations, and rationale.

## Earlier failure that motivated hardening

An earlier deployment attempted to retrieve an Etherscan page that returned a Cloudflare 403 challenge. The hardened contract changed the retrieval path so web failures become `UNAVAILABLE` evidence rather than crashing the claim. It also copies storage-backed values before entering nondeterministic execution and enforces fetched SHA-256 hashes against claimant commitments.

## Not claimed as completed on the active deployment

The final hardened deployment has **not** been used to execute a real `COVERED` payout or a `NOT_COVERED` denial. Those code paths exist in the contract, but this repository does not present them as completed active-deployment tests.
