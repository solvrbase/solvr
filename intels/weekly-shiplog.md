---
name: weekly-shiplog
description: Weekly development shiplog — what shipped, what's in progress, what's next.
category: productivity
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Weekly Shiplog

Weekly development shiplog — what shipped, what's in progress, what's next.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/github/trending?since=weekly&limit=10` — ecosystem shipments
- `GET https://api.solvrbot.com/api/v1/news?topic=product+launch+shipped&category=tech&limit=5` — launch news

## Instructions
1. Fetch what shipped in the ecosystem this week
2. Log your own shipments (provided as input)
3. Format shiplog:
   ```
   ## SHIPPED
   - [feature/fix] — impact: [user-facing change]

   ## IN PROGRESS
   - [item] — ETA: [date]

   ## NEXT
   - [item] — priority: HIGH/MED/LOW
   ```
4. Cross-reference with ecosystem to identify competitive gaps.
