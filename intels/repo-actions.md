---
name: repo-actions
description: Automate repository actions using Solvr intelligence as triggers.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Repo Actions

Automate repository actions using Solvr intelligence as triggers.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={project}+security` — security triggers
- `GET https://api.solvrbot.com/api/v1/github/trending?topic={tech}` — ecosystem signals

## Instructions
1. Define trigger conditions (security alerts, trending activity, etc.)
2. Map triggers to actions:
   - New CVE for dependency → create issue
   - Project trending → update README/marketing
   - Security incident in ecosystem → audit affected code
3. Execute action when trigger fires
4. Log action to audit trail.
