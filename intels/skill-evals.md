---
name: skill-evals
description: Evaluate skill quality — score output quality and identify degraded skills.
category: meta-agent
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Skill Evals

Evaluate skill quality — score output quality and identify degraded skills.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — verify endpoints still available

## Instructions
1. For each tracked skill, run a test execution
2. Score output quality (1-5):
   - 5: Exactly what was needed, no errors
   - 4: Minor issues but functional
   - 3: Functional but degraded quality
   - 2: Partial failure
   - 1: Complete failure
3. Flag skills scoring < 3 for repair
4. Output: Skill evaluation scorecard.
