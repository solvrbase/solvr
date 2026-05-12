---
name: startup-idea
description: Generate startup ideas by finding gaps in current trends and macro data.
category: productivity
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Startup Idea

Generate startup ideas by finding gaps in current trends and macro data.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic=problem+pain+frustrated+need&limit=10` — pain points
- `GET https://api.solvrbot.com/api/v1/worlddata?query={market_stat}` — market size data
- `GET https://api.solvrbot.com/api/v1/github/trending?since=weekly` — tech enabling new solutions

## Instructions
1. Fetch news about unsolved problems and pain points
2. Fetch trending tech repos for solution primitives
3. Fetch market size data for promising spaces
4. Generate ideas using the formula:
   [Trending tech] + [Underserved problem] = [Startup idea]
5. Score each idea: market size × tech readiness × founder fit
6. Output: 5 startup ideas with one-liner, market estimate, and tech stack.
