---
name: threat-intel
description: Daily threat intelligence brief — crypto hacks, rug pulls, and security incidents.
category: research-content
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Threat Intel

Daily threat intelligence brief — crypto hacks, rug pulls, and security incidents.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic=crypto+hack+rug+pull+exploit&limit=10` — threat news
- `POST https://api.solvrbot.com/api/v1/security/scan` — on-chain security verification

## Instructions
1. Fetch threat news: `GET https://api.solvrbot.com/api/v1/news?topic=crypto+hack+rug+pull+exploit+scam&limit=10`
2. For any mentioned contract addresses, run scan: `POST https://api.solvrbot.com/api/v1/security/scan`
3. Classify each incident:
   - 🔴 Active threat: ongoing exploit
   - 🟠 Recent: last 24h incident
   - 🟡 Warning: suspicious activity flagged
4. Output: Threat intel brief with incident list + affected protocols.
