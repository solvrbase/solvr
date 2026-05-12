---
name: pr-review
description: AI-assisted pull request review framework using context from tech news and security.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Pr Review

AI-assisted pull request review framework using context from tech news and security.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={library}+vulnerability+CVE` — known CVEs
- `POST https://api.solvrbot.com/api/v1/security/scan` — contract security if applicable

## Instructions
1. For PRs touching dependencies, check CVEs: `GET https://api.solvrbot.com/api/v1/news?topic=LIBRARY+vulnerability`
2. For PRs touching smart contracts, run security scan
3. Review checklist:
   - [ ] No known vulnerable dependencies
   - [ ] No hardcoded secrets or addresses
   - [ ] Gas efficiency (for contracts)
   - [ ] Test coverage
4. Output: PR review summary with pass/fail checklist.
