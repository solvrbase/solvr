---
name: intel-leaderboard
description: Intel performance leaderboard — ranked by value delivered.
category: meta-agent
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Intel Leaderboard

Intel performance leaderboard — ranked by value delivered.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — usage context

## Instructions
1. Load intel execution history from memory
2. Score each intel:
   - Execution frequency (how often it ran)
   - Success rate (% successful runs)
   - Output quality (from evals)
   - Value generated (alerts fired, insights delivered)
3. Rank intels from highest to lowest value
4. Identify bottom 3 intels for review/retirement
5. Output: Intel leaderboard with scores and recommendations.
