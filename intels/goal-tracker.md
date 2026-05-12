---
name: goal-tracker
description: Track goal progress using external signals and data milestones.
category: productivity
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Goal Tracker

Track goal progress using external signals and data milestones.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={goal_domain}&limit=5` — goal context
- `GET https://api.solvrbot.com/api/v1/worlddata?query={metric}` — progress metrics

## Instructions
1. Load goals from memory (stored on previous run)
2. For each goal, fetch relevant context: market conditions, benchmarks, news
3. Check goal milestones against current data
4. Alert on: milestone reached, goal at risk, new opportunity
5. Output: Goal progress report with status (ON_TRACK/AT_RISK/COMPLETED).
