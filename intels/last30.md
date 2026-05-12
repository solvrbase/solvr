---
name: last30
description: 30-day digest of major developments in any topic.
category: research-content
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Last30

30-day digest of major developments in any topic.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={topic}&limit=10` — news digest

## Instructions
1. Fetch max news on topic: `GET https://api.solvrbot.com/api/v1/news?topic=TOPIC&limit=10`
2. Group by theme/sub-topic
3. Identify the 5 biggest developments of the period
4. Note any trend changes or reversals
5. Output: 30-day review with timeline of key events and net impact assessment.
