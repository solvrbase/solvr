---
name: token-report
description: Daily performance report for any Base token — price, volume, security score, TA verdict.
category: crypto-markets
tier: standard
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Token Report

Daily performance report for any Base token — price, volume, security score, TA verdict.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/intel/{address}` — unified token intel
- `POST https://api.solvrbot.com/api/v1/ta/analysis` — full technical analysis

## Instructions
1. Fetch token intel: `GET https://api.solvrbot.com/api/v1/intel/{address}`
2. Fetch TA: `POST https://api.solvrbot.com/api/v1/ta/analysis` with `{"symbol": "TOKEN_SYMBOL"}`
3. Combine and format report:

```
📊 $SYMBOL DAILY REPORT
Price:    ${price_usd} ({change_24h:+.1f}% 24h)
MCap:     ${market_cap:,.0f}
Volume:   ${volume_24h:,.0f}
Risk:     {risk_score}/100 — {verdict}
RSI:      {rsi} | MACD: {macd_signal}
Verdict:  BREAKOUT / BREAKDOWN / ACCUMULATION / QUIET
```

4. Alert if risk_score > 50 or price change > ±20% in 24h.
