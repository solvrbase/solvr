---
name: code-health
description: Codebase health check — surface dependency risks and quality signals.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Code Health

Codebase health check — surface dependency risks and quality signals.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic=security+vulnerability+npm+pip` — dependency CVEs
- `GET https://api.solvrbot.com/api/v1/github/trending?topic=security` — security tools trending

## Instructions
1. Check for CVE news on key dependencies: `GET https://api.solvrbot.com/api/v1/news?topic=DEPENDENCY+vulnerability`
2. Fetch trending security tools for potential improvements
3. Health dimensions:
   - Dependency security (no known CVEs)
   - Code activity (recent commits)
   - Documentation (README quality)
4. Output: Health score with action items.
