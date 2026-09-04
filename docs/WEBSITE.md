# RugShield Website

## Live dashboard

https://www.genspark.ai/artifact/rE6IIiOEbP3asatrnrvv2g

The dashboard presents the final Studionet deployment, active contract address, source hash, Full Consensus claim result, pool state, transaction evidence, and GitHub documentation links.

A repository snapshot of the dashboard source is stored in [`../site/index.html`](../site/index.html).

## MetaMask connection

The website includes a real MetaMask connection flow using `window.ethereum`.

It can:

- request account access via `eth_requestAccounts`
- show the connected address in shortened form
- react to `accountsChanged`
- provide a local disconnect state
- attempt `wallet_revokePermissions` where supported
- gracefully handle missing MetaMask

Wallet connection is for account identification only. RugShield Studionet transactions are currently executed through GenLayer Studio.

## Active deployment shown by the site

- Network: GenLayer Studionet
- Contract: `0x3df30229C9Fa2c5aAE7517adAFcCce1083DBE8c2`
- Source SHA-256: `860260f2a1bc748563169969c7c4c03388fa8b41cc287d46c8f9b1b13526bc24`
- Offer: `rugshield-demo-002`
- Policy: `rugshield-policy-002`
- Verdict: `INCONCLUSIVE`
- Evidence state: `HASH_MISMATCH`
- Reserved liability: 1 GEN
- Total payouts: 0 GEN
