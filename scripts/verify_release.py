#!/usr/bin/env python3
"""Fail-fast integrity checks for the published RugShield release."""

from __future__ import annotations

import ast
import hashlib
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "rugshield.py"
CONTRACT_MIRROR = ROOT / "rugshield.py"
SITE = ROOT / "site" / "index.html"

EXPECTED_SOURCE_SHA256 = "860260f2a1bc748563169969c7c4c03388fa8b41cc287d46c8f9b1b13526bc24"
CONTRACT_ADDRESS = "0x3df30229C9Fa2c5aAE7517adAFcCce1083DBE8c2"
CLAIM_TX = "0x8a036068705c9c71c861e5ae6ad8710287aa7bdbe0e323cde7dca05b31b01db9"
TERMS_HASH = "1ce43a4d3fc8d1bf566c3037d6eb880dd6fccfedf3fc15667655425bbf778031"
BUNDLE_HASH = "b6e431a96411148e7b15a6a9cc3c1a322e109e9da42c7ab4f1511375337fcabf"

REQUIRED_PUBLIC_METHODS = {
    "fund_pool",
    "create_offer",
    "set_offer_active",
    "buy_protection",
    "submit_claim",
    "expire_policy",
    "withdraw_surplus",
    "get_pool_status",
    "get_offer",
    "get_policy",
    "get_claim_revision",
}

REQUIRED_DOCS = (
    ROOT / "README.md",
    ROOT / "PROJECT.md",
    ROOT / "docs" / "DEPLOYMENT.md",
    ROOT / "docs" / "DEMO_EVIDENCE.md",
    ROOT / "docs" / "SUBMISSION.md",
)


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.links: list[str] = []

    def handle_starttag(self, _tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.append(values["id"] or "")
        if values.get("href"):
            self.links.append(values["href"] or "")


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def check(name: str, condition: bool, detail: str = "") -> None:
    if not condition:
        suffix = f": {detail}" if detail else ""
        raise AssertionError(f"{name}{suffix}")
    print(f"[ok] {name}")


def verify_contract() -> None:
    canonical = CONTRACT.read_bytes()
    mirror = CONTRACT_MIRROR.read_bytes()
    source_text = canonical.decode("utf-8")
    source_hash = hashlib.sha256(canonical).hexdigest()

    check("contract mirror is byte-identical", canonical == mirror)
    check(
        "contract fingerprint matches deployed release",
        source_hash == EXPECTED_SOURCE_SHA256,
        source_hash,
    )

    tree = ast.parse(source_text, filename=str(CONTRACT))
    contract_class = next(
        (node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == "RugShield"),
        None,
    )
    check("RugShield contract class exists", contract_class is not None)
    method_names = {
        node.name for node in contract_class.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    check(
        "expected public contract surface is present",
        REQUIRED_PUBLIC_METHODS <= method_names,
        ", ".join(sorted(REQUIRED_PUBLIC_METHODS - method_names)),
    )

    safety_markers = (
        'assert gl.message.sender_address == policy.holder, "only policy holder"',
        'assert amount <= self._free_pool(), "amount exceeds free pool"',
        'assert len(set(hosts)) >= 2, "sources must span at least two hosts"',
        '"status": "VERIFIED" if hash_matches else "HASH_MISMATCH"',
        "self.claim_revisions[revision_key] = json.dumps(",
    )
    for marker in safety_markers:
        check(f"contract safety marker: {marker[:46]}", marker in source_text)


def verify_demo_commitments() -> None:
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
    check("documented offer terms hash recomputes", canonical_sha256(terms) == TERMS_HASH)

    bundle = {
        "hashes": ["0" * 64, "1" * 64],
        "urls": ["https://example.com/", "https://www.iana.org/help/example-domains"],
    }
    check("documented evidence bundle hash recomputes", canonical_sha256(bundle) == BUNDLE_HASH)


def verify_documentation() -> None:
    for path in REQUIRED_DOCS:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        check(f"{rel} names the active contract", CONTRACT_ADDRESS in text)
        check(f"{rel} links the Full Consensus claim", CLAIM_TX in text)

    deployment = (ROOT / "docs" / "DEPLOYMENT.md").read_text(encoding="utf-8")
    evidence = (ROOT / "docs" / "DEMO_EVIDENCE.md").read_text(encoding="utf-8")
    check("deployment document contains the offer terms hash", TERMS_HASH in deployment)
    check("evidence document contains the bundle hash", BUNDLE_HASH in evidence)
    check("evidence document records INCONCLUSIVE", '"verdict": "INCONCLUSIVE"' in evidence)


def verify_site() -> None:
    html = SITE.read_text(encoding="utf-8")
    parser = SiteParser()
    parser.feed(html)

    duplicates = sorted({value for value in parser.ids if parser.ids.count(value) > 1})
    check("website element IDs are unique", not duplicates, ", ".join(duplicates))
    for section in ("top", "how", "deployment", "claim", "pool", "txs", "evidence"):
        check(f"website section #{section} exists", section in parser.ids)
    check("website shows the active contract", CONTRACT_ADDRESS in html)
    check("website links the Full Consensus claim", any(CLAIM_TX in link for link in parser.links))
    check("website includes a MetaMask account request", "eth_requestAccounts" in html)
    check(
        "website discloses identification-only wallet scope",
        "account identification" in html and "executed through GenLayer Studio" in html,
    )

    for link in parser.links:
        if "github.com/haris4587/RugShield/blob/main/" not in link:
            continue
        relative = link.split("/blob/main/", 1)[1].split("#", 1)[0]
        check(f"website GitHub target exists: {relative}", (ROOT / relative).is_file())


def verify_no_obvious_secrets() -> None:
    patterns = {
        "GitHub token": re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"),
        "private key PEM": re.compile(r"-----BEGIN (?:RSA |EC )?PRIVATE KEY-----"),
    }
    candidates = [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts and "__pycache__" not in path.parts
    ]
    for label, pattern in patterns.items():
        hits = []
        for path in candidates:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if pattern.search(text):
                hits.append(str(path.relative_to(ROOT)))
        check(f"no obvious {label} committed", not hits, ", ".join(hits))


def main() -> int:
    try:
        verify_contract()
        verify_demo_commitments()
        verify_documentation()
        verify_site()
        verify_no_obvious_secrets()
    except (AssertionError, OSError, SyntaxError, ValueError) as exc:
        print(f"[failed] {exc}", file=sys.stderr)
        return 1
    print("\nRugShield release verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
