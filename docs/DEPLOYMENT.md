# RugShield Studionet Deployment

## Active deployment

- **Network:** GenLayer Studionet
- **Contract address:** `0x3df30229C9Fa2c5aAE7517adAFcCce1083DBE8c2`
- **Deployment transaction:** `0x4dfda33703ca703cf9f77620900f5735d194dbafb5a383c22cbe2283c648669b`
- **Mode:** Normal / Full Consensus
- **Simulation Mode:** Off
- **Constructor arguments:** none

## Successful demo transactions

| Step | Transaction |
|---|---|
| Deploy fixed RugShield contract | `0x4dfda33703ca703cf9f77620900f5735d194dbafb5a383c22cbe2283c648669b` |
| Fund pool with 2 GEN | `0x4f59a706428b1b61bf5f59d4876ecd6295b660f507066b5eba3294d59b6b8553` |
| Create demo offer | `0xc9bd3b41ed45a422e53fe43f9be47565c1e306549fa99ae7ed70f4d5fcd247b5` |
| Buy protection | `0x5fda179fffb658323eb67527edaf0d7b47b009467f3e0c79255d9dd8ef4a1483` |
| Full Consensus claim | `0x8a036068705c9c71c861e5ae6ad8710287aa7bdbe0e323cde7dca05b31b01db9` |

## Demo offer

- **Offer ID:** `rugshield-demo-002`
- **Token:** `RugShield Demo Token`
- **Token address:** `0x1111111111111111111111111111111111111111`
- **Chain:** `Ethereum`
- **Coverage amount:** `1000000000000000000` base units = 1 GEN
- **Premium:** `1000000000000000000` base units = 1 GEN
- **Sale duration:** `86400` seconds
- **Coverage duration:** `604800` seconds
- **Claim grace period:** `86400` seconds
- **Terms hash:** `1ce43a4d3fc8d1bf566c3037d6eb880dd6fccfedf3fc15667655425bbf778031`

Trigger rules:

> COVERED only if credible evidence shows liquidity removal, blocked selling, malicious transfer restrictions, or another explicit rug event affecting the exact token on the stated chain during the coverage window. Price decline alone is not covered.

Source policy:

> Require at least one authoritative source or two independent credible sources. Evidence must identify the exact token and chain and establish the event timing.

## Demo policy

- **Policy ID:** `rugshield-policy-002`
- **Coverage:** 1 GEN
- **Premium paid:** 1 GEN
- **Final demo status:** `INCONCLUSIVE`
- **Claim round:** `1`
- **Final verdict:** `INCONCLUSIVE`

## Final pool state

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

This demonstrates that an inconclusive claim does not incorrectly release the reserved protection liability or pay the claimant.
