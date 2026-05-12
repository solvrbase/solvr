---
name: deal-flow
description: Startup and VC deal flow monitor — funding rounds, new launches, M&A.
category: productivity
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Deal Flow

Startup and VC deal flow monitor — funding rounds, new launches, M&A.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic=startup+funding+venture+series&limit=10` — deals
- `GET https://api.solvrbot.com/api/v1/news?topic=acquisition+merger+M%26A&limit=5` — M&A
- `GET https://api.solvrbot.com/api/v1/worlddata?query=venture+capital` — VC market context

## Instructions
1. Fetch funding news: `GET https://api.solvrbot.com/api/v1/news?topic=startup+funding+raised+million&limit=10`
2. Fetch M&A news: `GET https://api.solvrbot.com/api/v1/news?topic=acquisition+merger&limit=5`
3. Parse deal details: company, amount, stage, investors
4. Filter by sector if specified
5. Output: Deal flow digest with deal size and sector tags.
