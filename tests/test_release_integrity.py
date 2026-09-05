from __future__ import annotations

import ast
import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "rugshield.py"
MIRROR = ROOT / "rugshield.py"


class RugShieldReleaseTests(unittest.TestCase):
    def test_contract_sources_are_identical_and_parse(self) -> None:
        canonical = CONTRACT.read_bytes()
        self.assertEqual(canonical, MIRROR.read_bytes())
        ast.parse(canonical.decode("utf-8"))
        self.assertEqual(
            hashlib.sha256(canonical).hexdigest(),
            "860260f2a1bc748563169969c7c4c03388fa8b41cc287d46c8f9b1b13526bc24",
        )

    def test_demo_offer_terms_commitment(self) -> None:
        terms = {
            "chain_name": "Ethereum",
            "claim_grace_seconds": 86400,
            "coverage_amount": 10**18,
            "coverage_duration_seconds": 604800,
            "offer_id": "rugshield-demo-002",
            "premium": 10**18,
            "sale_duration_seconds": 86400,
            "source_policy": (
                "Require at least one authoritative source or two independent credible sources. "
                "Evidence must identify the exact token and chain and establish the event timing."
            ),
            "token_address": "0x1111111111111111111111111111111111111111",
            "token_name": "RugShield Demo Token",
            "trigger_rules": (
                "COVERED only if credible evidence shows liquidity removal, blocked selling, malicious "
                "transfer restrictions, or another explicit rug event affecting the exact token on the "
                "stated chain during the coverage window. Price decline alone is not covered."
            ),
        }
        encoded = json.dumps(terms, sort_keys=True, separators=(",", ":")).encode("utf-8")
        self.assertEqual(
            hashlib.sha256(encoded).hexdigest(),
            "1ce43a4d3fc8d1bf566c3037d6eb880dd6fccfedf3fc15667655425bbf778031",
        )

    def test_demo_evidence_bundle_commitment(self) -> None:
        bundle = {
            "hashes": ["0" * 64, "1" * 64],
            "urls": ["https://example.com/", "https://www.iana.org/help/example-domains"],
        }
        encoded = json.dumps(bundle, sort_keys=True, separators=(",", ":")).encode("utf-8")
        self.assertEqual(
            hashlib.sha256(encoded).hexdigest(),
            "b6e431a96411148e7b15a6a9cc3c1a322e109e9da42c7ab4f1511375337fcabf",
        )

    def test_full_release_verifier(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "verify_release.py")],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
