"""security_guard.py — Pre-transfer security check.

The Grok Defense Pattern.

On May 4, 2026, Grok was drained of $174K via a prompt injection attack.
The attacker gifted a Bankr Club Membership NFT to Grok's wallet, unlocking
full transfer capability. Then sent a crafted prompt. Grok executed it.

This pattern shows how a Solvr security check before any transfer would have
flagged the suspicious recipient wallet and blocked the transaction.

The rule is simple:
  Never execute a financial action without checking it first.
"""

import os
import re
from solvr_intel import SolvrIntel, SolvrIntelError

_ADDRESS_RE = re.compile(r"^0x[0-9a-fA-F]{40}$")

SOLVR_API_KEY = os.environ["SOLVR_API_KEY"]

# Wallets flagged as high-risk (extend with your own blocklist)
BLOCKED_WALLETS = {
    "0xe8e476bdd78b0aa6669509ec8d3e1c542d5a686b",  # Grok attacker wallet
}

# Maximum acceptable risk score before blocking (0 = no risk, 100 = max risk)
MAX_RISK_SCORE = 35


def check_before_transfer(token_address: str, recipient_wallet: str, amount_usd: float) -> dict:
    """Run a full pre-transfer security check.

    Returns:
        {
            "allowed": bool,
            "reason": str,
            "risk_score": int | None,
            "verdict": str | None,
            "flags": list,
        }
    """
    result = {
        "allowed": False,
        "reason": "",
        "risk_score": None,
        "verdict": None,
        "flags": [],
    }

    # 1. Validate address formats before any network call
    if not _ADDRESS_RE.match(token_address):
        result["reason"] = f"Invalid token address format: {token_address!r}"
        return result
    if not _ADDRESS_RE.match(recipient_wallet):
        result["reason"] = f"Invalid recipient address format: {recipient_wallet!r}"
        return result

    # 2. Blocklist check — instant reject
    if recipient_wallet.lower() in BLOCKED_WALLETS:
        result["reason"] = f"Recipient wallet is blocklisted: {recipient_wallet}"
        return result

    # 2. Token security scan via Solvr
    with SolvrIntel(SOLVR_API_KEY) as intel:
        try:
            scan = intel.security_scan(token_address)
        except SolvrIntelError as e:
            # Fail closed — if we can't verify, we don't execute
            result["reason"] = f"Security scan unavailable (HTTP {e.status}) — transfer blocked"
            return result

        risk_score = scan.get("risk_score", 100)
        verdict    = scan.get("verdict", "unknown")
        flags      = scan.get("flags", [])

        result["risk_score"] = risk_score
        result["verdict"]    = verdict
        result["flags"]      = flags

        if verdict == "danger" or risk_score > MAX_RISK_SCORE:
            result["reason"] = (
                f"Token failed security check — verdict: {verdict}, "
                f"risk score: {risk_score}/100, flags: {flags}"
            )
            return result

        # 3. Bundle/insider check for large transfers (>$1K)
        if amount_usd > 1000:
            try:
                bundle = intel.bundles(token_address)
                bundle_pct = bundle.get("data", {}).get("bundle_pct", 0)
                if bundle_pct > 30:
                    result["reason"] = (
                        f"High insider bundle concentration: {bundle_pct:.1f}% "
                        f"of supply held by coordinated early buyers"
                    )
                    return result
            except SolvrIntelError:
                pass  # bundle check is advisory — don't block on failure

    result["allowed"] = True
    result["reason"]  = f"Security check passed — risk score {risk_score}/100 ({verdict})"
    return result


def safe_transfer(token_address: str, recipient_wallet: str, amount: float, amount_usd: float):
    """Wrapper that enforces security check before any transfer execution.

    Replace the `execute_transfer()` call with your actual transfer logic.
    """
    print(f"\nTransfer requested:")
    print(f"  Token:     {token_address}")
    print(f"  Recipient: {recipient_wallet}")
    print(f"  Amount:    {amount} tokens (~${amount_usd:,.2f})")

    check = check_before_transfer(token_address, recipient_wallet, amount_usd)

    print(f"\nSecurity check: {'✓ ALLOWED' if check['allowed'] else '✗ BLOCKED'}")
    print(f"  Reason:  {check['reason']}")
    if check["risk_score"] is not None:
        print(f"  Risk:    {check['risk_score']}/100 ({check['verdict']})")
    if check["flags"]:
        print(f"  Flags:   {', '.join(check['flags'])}")

    if not check["allowed"]:
        raise PermissionError(f"Transfer blocked: {check['reason']}")

    # execute_transfer(token_address, recipient_wallet, amount)
    print("\n→ Transfer executed.")
    return True


# ── Demo ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Simulate the Grok attack scenario
    GROK_ATTACKER   = "0xe8e476bdd78b0aa6669509ec8d3e1c542d5a686b"
    DRB_TOKEN       = "0x3ec2156c5d4d915e88571c25aef8df0bc58e95b2"
    AMOUNT_TOKENS   = 3_000_000_000
    AMOUNT_USD      = 174_000

    print("=== Simulating the Grok attack scenario ===")
    print(f"Attacker wallet: {GROK_ATTACKER}")

    try:
        safe_transfer(DRB_TOKEN, GROK_ATTACKER, AMOUNT_TOKENS, AMOUNT_USD)
    except PermissionError as e:
        print(f"\n✓ Attack prevented: {e}")

    print("\n=== Normal transfer — safe token, legitimate recipient ===")
    SOLVR_TOKEN   = "0x"  # replace with actual $SOLVR contract
    MY_WALLET     = "0xYOUR_RECIPIENT_WALLET"

    try:
        safe_transfer(SOLVR_TOKEN, MY_WALLET, 1_000_000, 3.0)
    except PermissionError as e:
        print(f"Blocked: {e}")
