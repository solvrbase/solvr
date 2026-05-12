---
name: workflow-security-audit
description: Security audit for GitHub Actions and CI/CD workflows.
category: dev-code
tier: standard
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Workflow Security Audit

Security audit for GitHub Actions and CI/CD workflows.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic=GitHub+Actions+security+vulnerability` — workflow CVEs
- `POST https://api.solvrbot.com/api/v1/security/scan` — scan any contracts in workflows

## Instructions
1. Fetch GitHub Actions security news
2. Audit workflow files for:
   - Unpinned action versions (security risk)
   - Excessive permissions (write-all)
   - Secret exposure in logs
   - Supply chain risks (third-party actions)
3. For any contracts deployed via CI, run security scan
4. Output: Workflow security report with risk ratings.
