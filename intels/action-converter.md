---
name: action-converter
description: Convert goals and news into concrete, prioritized action items.
category: productivity
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Action Converter

Convert goals and news into concrete, prioritized action items.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={goal_context}&limit=5` — current opportunities
- `GET https://api.solvrbot.com/api/v1/worlddata?query={relevant_metric}` — data context

## Instructions
1. Fetch relevant news to identify timely action opportunities
2. Given a goal, convert to SMART actions:
   - Specific: what exactly to do
   - Measurable: how to know it's done
   - Achievable: is it feasible this week?
   - Relevant: does it advance the goal?
   - Time-bound: by when?
3. Prioritize using Eisenhower matrix (urgent/important)
4. Output: Prioritized action list with deadlines.
