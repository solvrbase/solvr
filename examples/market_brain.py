"""market_brain.py — Full trading intelligence loop.

An agent that queries Solvr for world news, macro data, and TA
before making any trading decision. Demonstrates the complete
intelligence stack: news → macro → TA → decision.

This is the kind of agent that used Solvr's intel to correctly
call the BTC and ETH bias in the /tradetoday example.
"""

import os
from solvr_intel import SolvrIntel

SOLVR_API_KEY = os.environ["SOLVR_API_KEY"]


def get_market_context(asset: str = "BTC") -> dict:
    """Pull full market context for a trading decision."""
    with SolvrIntel(SOLVR_API_KEY) as intel:

        # 1. World news — any macro event that could move markets
        news = intel.news(topic=f"{asset} crypto market", category="business", limit=3)

        # 2. US macro — Fed rate, VIX, yield curve
        fed_rate    = intel.worlddata("fed rate")
        vix         = intel.worlddata("vix")
        yield_curve = intel.worlddata("yield curve")

        # 3. Technical analysis
        ta = intel.ta_analysis(asset, interval="4h")

    return {
        "asset":       asset,
        "news":        news.get("articles", []),
        "fed_rate":    fed_rate.get("formatted"),
        "vix":         vix.get("formatted"),
        "yield_curve": yield_curve.get("formatted"),
        "rsi":         ta.get("rsi"),
        "macd_hist":   ta.get("macd", {}).get("hist"),
        "bb_upper":    ta.get("bollinger", {}).get("upper"),
        "bb_lower":    ta.get("bollinger", {}).get("lower"),
        "bb_mid":      ta.get("bollinger", {}).get("mid"),
        "adx":         ta.get("adx"),
        "raw_ta":      ta,
    }


def decide(ctx: dict) -> str:
    """Simple rules-based signal from market context.

    Replace with your own model or pass to an LLM for interpretation.
    """
    rsi       = ctx.get("rsi") or 50
    macd_hist = ctx.get("macd_hist") or 0
    adx       = ctx.get("adx") or 0

    signals = []

    if rsi < 35:
        signals.append("RSI oversold → bullish")
    elif rsi > 68:
        signals.append("RSI overbought → bearish")
    else:
        signals.append(f"RSI neutral ({rsi:.1f})")

    if macd_hist > 0:
        signals.append("MACD bullish crossover")
    elif macd_hist < 0:
        signals.append("MACD bearish crossover")

    if adx > 25:
        signals.append(f"Strong trend (ADX {adx:.1f})")

    bias = "LONG" if macd_hist > 0 and rsi < 65 else "SHORT" if macd_hist < 0 and rsi > 55 else "WAIT"
    return f"Bias: {bias} | Signals: {' · '.join(signals)}"


if __name__ == "__main__":
    for asset in ["BTC", "ETH"]:
        print(f"\n{'='*50}")
        print(f"Market intelligence: {asset}")
        print('='*50)

        ctx = get_market_context(asset)

        print(f"Fed rate:    {ctx['fed_rate']}")
        print(f"VIX:         {ctx['vix']}")
        print(f"Yield curve: {ctx['yield_curve']}")
        print(f"RSI (4H):    {ctx['rsi']:.1f}")
        print(f"MACD hist:   {ctx['macd_hist']:.2f}")
        print(f"ADX:         {ctx['adx']:.1f}")

        if ctx["news"]:
            print(f"\nTop headline: {ctx['news'][0]['title']}")

        print(f"\n{decide(ctx)}")
