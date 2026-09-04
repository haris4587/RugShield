# RugShield Submission Reference

## Title

**RugShield: Consensus-Backed Rug Pull Protection**

## Primary description

RugShield is a GenLayer Intelligent Contract prototype for token rug-pull protection. Users buy fixed-term coverage from a GEN-funded protection pool and submit SHA-256 committed evidence when they believe a covered rug event occurred. GenLayer validators independently retrieve the evidence, verify it against the committed hashes, apply locked trigger rules and source standards, and reach consensus on COVERED, NOT_COVERED, or INCONCLUSIVE. In the Studionet demo, both submitted sources produced HASH_MISMATCH results, so they were rejected as usable evidence. Consensus returned INCONCLUSIVE, no payout occurred, and the 1 GEN protection liability remained reserved.

## Required URLs

- **Website:** https://www.genspark.ai/artifact/rE6IIiOEbP3asatrnrvv2g
- **GitHub repository:** https://github.com/haris4587/RugShield
- **Contract source:** https://github.com/haris4587/RugShield/blob/main/rugshield.py
- **GenLayer explorer contract:** https://explorer-studio.genlayer.com/address/0x3df30229C9Fa2c5aAE7517adAFcCce1083DBE8c2
- **Deployment evidence:** https://github.com/haris4587/RugShield/blob/main/docs/DEPLOYMENT.md
- **Demo evidence:** https://github.com/haris4587/RugShield/blob/main/docs/DEMO_EVIDENCE.md

## Strongest transaction evidence

Full Consensus claim:

https://explorer-studio.genlayer.com/tx/0x8a036068705c9c71c861e5ae6ad8710287aa7bdbe0e323cde7dca05b31b01db9

## Evidence summary

Deployed and tested the hardened RugShield Intelligent Contract on GenLayer Studionet using Normal / Full Consensus. The protection pool was funded with 2 GEN, a 1 GEN policy was purchased, and a claim was submitted using SHA-256 committed evidence. Validators independently retrieved both sources and detected HASH_MISMATCH for each, so neither could satisfy the locked source policy. Consensus returned INCONCLUSIVE, no incorrect payout occurred, and the 1 GEN liability remained reserved. The claim revision preserves the bundle hash, fetched hashes, retrieval states, verdict, and rationale for later audit.
