"""token_launch_monitor.py — Watch new token launches with auto security scan.

Polls Solvr's trending endpoint, auto-scans new tokens, and only
surfaces ones that pass a configurable risk threshold.
"""

import os
import time
from solvr_intel import SolvrIntel, SolvrIntelError

SOLVR_API_KEY  = os.environ["SOLVR_API_KEY"]
POLL_INTERVAL  = 60        # seconds between trending checks
MAX_RISK_SCORE = 30        # only surface tokens scoring <= this
SEEN_TOKENS: set = set()   # track already-seen tokens


def scan_new_launches():
    with SolvrIntel(SOLVR_API_KEY) as intel:
        trending = intel.dex_trending()
        tokens   = trending.get("tokens", [])

        for token in tokens:
            address = token.get("address") or token.get("pairAddress")
            if not address or address in SEEN_TOKENS:
                continue

            SEEN_TOKENS.add(address)

            try:
                scan = intel.security_scan(address)
            except SolvrIntelError:
                continue

            risk    = scan.get("risk_score", 100)
            verdict = scan.get("verdict", "unknown")
            flags   = scan.get("flags", [])

            symbol = token.get("baseToken", {}).get("symbol", "?")
            price  = token.get("priceUsd", "?")
            volume = token.get("volume", {}).get("h24", 0)

            if risk <= MAX_RISK_SCORE:
                print(f"\n✓ NEW SAFE LAUNCH: ${symbol}")
                print(f"  Address:    {address}")
                print(f"  Price:      ${price}")
                print(f"  Vol 24h:    ${volume:,.0f}")
                print(f"  Risk score: {risk}/100 ({verdict})")
            else:
                print(f"✗ Skipped ${symbol} — risk {risk}/100 ({verdict}) {flags}")


if __name__ == "__main__":
    print(f"Monitoring token launches (risk threshold: {MAX_RISK_SCORE}/100)...")
    while True:
        scan_new_launches()
        time.sleep(POLL_INTERVAL)
