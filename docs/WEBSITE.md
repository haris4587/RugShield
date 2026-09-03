# RugShield Website

## Current demo site

https://www.genspark.ai/artifact/rE6IIiOEbP3asatrnrvv2g

The Genspark-built RugShield dashboard presents the active Studionet deployment, completed Full Consensus demo, transaction evidence, contract source links, final pool state, and claim result.

## Wallet connection

The website includes a real MetaMask connection flow through the browser-injected `window.ethereum` provider. It can:

- request wallet access with `eth_requestAccounts`
- display the connected address in shortened form
- react to `accountsChanged`
- show a local disconnect state and attempt `wallet_revokePermissions` when supported
- fail gracefully if MetaMask is unavailable

Wallet connection is currently used for account identification only. RugShield Studionet transactions are still executed through GenLayer Studio; the website does not claim to submit contract transactions directly.

## Active deployment shown on the site

- **Network:** GenLayer Studionet
- **Contract:** `0x3df30229C9Fa2c5aAE7517adAFcCce1083DBE8c2`
- **Deployed source SHA-256:** `860260f2a1bc748563169969c7c4c03388fa8b41cc287d46c8f9b1b13526bc24`
- **Demo offer:** `rugshield-demo-002`
- **Demo policy:** `rugshield-policy-002`
- **Claim verdict:** `INCONCLUSIVE`
- **Evidence state:** `HASH_MISMATCH`
- **Reserved liability after claim:** `1 GEN`
- **Total payouts:** `0 GEN`

## Submission note

The site is a demo/dashboard layer. The authoritative technical evidence is the public GitHub repository, active Studionet contract, and explorer-linked Full Consensus transactions documented in `DEPLOYMENT.md` and `DEMO_EVIDENCE.md`.
