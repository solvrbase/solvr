---
name: auto-merge
description: Evaluate PRs for safe auto-merge based on security and dependency checks.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Auto Merge

Evaluate PRs for safe auto-merge based on security and dependency checks.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={dependency}+CVE+vulnerability` — dependency security

## Instructions
1. Check each changed dependency for CVEs
2. Safe merge criteria:
   - No new CVEs introduced
   - Tests pass (check CI status)
   - No hardcoded secrets
   - Minor version bump or patch only
3. Flag for human review:
   - Breaking changes (major version)
   - New dependencies added
   - Security-sensitive files changed
4. Output: SAFE_TO_MERGE or NEEDS_REVIEW with reasoning.
