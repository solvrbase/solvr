---
name: skill-leaderboard
description: Skills performance leaderboard — ranked by value delivered.
category: meta-agent
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Skill Leaderboard

Skills performance leaderboard — ranked by value delivered.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — usage context

## Instructions
1. Load skill execution history from memory
2. Score each skill:
   - Execution frequency (how often it ran)
   - Success rate (% successful runs)
   - Output quality (from evals)
   - Value generated (alerts fired, insights delivered)
3. Rank skills from highest to lowest value
4. Identify bottom 3 skills for review/retirement
5. Output: Skill leaderboard with scores and recommendations.
