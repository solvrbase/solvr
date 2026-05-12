---
name: intel-evals
description: Evaluate intel quality — score output quality and identify degraded intels.
category: meta-agent
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Intel Evals

Evaluate intel quality — score output quality and identify degraded intels.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — verify endpoints still available

## Instructions
1. For each tracked intel, run a test execution
2. Score output quality (1-5):
   - 5: Exactly what was needed, no errors
   - 4: Minor issues but functional
   - 3: Functional but degraded quality
   - 2: Partial failure
   - 1: Complete failure
3. Flag intels scoring < 3 for repair
4. Output: Intel evaluation scorecard.
