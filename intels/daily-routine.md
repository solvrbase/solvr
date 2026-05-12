---
name: daily-routine
description: Build and optimize daily routines using intelligence signals.
category: productivity
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Daily Routine

Build and optimize daily routines using intelligence signals.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?category=health&limit=5` — health/science insights
- `GET https://api.solvrbot.com/api/v1/worlddata?query=productivity+research` — research context

## Instructions
1. Fetch latest productivity/health research: `GET https://api.solvrbot.com/api/v1/news?topic=productivity+sleep+focus`
2. Fetch supporting science: `GET https://api.solvrbot.com/api/v1/news?category=science&topic=cognitive+performance`
3. Recommend daily routine optimizations based on latest research
4. Structure as time-blocked schedule with evidence-based rationale.
