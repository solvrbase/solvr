---
name: reg-monitor
description: Regulatory compliance monitor — track new rules affecting your domain.
category: productivity
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Reg Monitor

Regulatory compliance monitor — track new rules affecting your domain.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic=regulation+compliance+law+{domain}&limit=10` — regulatory news
- `GET https://api.solvrbot.com/api/v1/worlddata?query={country}+regulation` — policy context

## Instructions
1. Fetch regulatory news for target domains: crypto, AI, finance, privacy, etc.
2. Classify by impact:
   - 🔴 Immediate: effective now, action required
   - 🟡 Upcoming: proposed rule, prepare now
   - 🟢 Watch: early stage, monitor
3. For each regulation: jurisdiction, effective date, required action
4. Output: Compliance calendar with action items.
