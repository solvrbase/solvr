---
name: issue-triage
description: Triage and prioritize open issues using news context and security data.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Issue Triage

Triage and prioritize open issues using news context and security data.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={issue_topic}+{project}&category=tech` — context
- `POST https://api.solvrbot.com/api/v1/security/scan` — security impact assessment

## Instructions
1. For each open issue, fetch related news for context
2. Classify severity:
   - P0: security vulnerability, data loss
   - P1: functionality broken for most users
   - P2: degraded UX
   - P3: minor/cosmetic
3. For security issues, run scan if contract address involved
4. Output: Prioritized issue list with severity and context.
