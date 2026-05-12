---
name: dependency-audit
description: Audit project dependencies for known vulnerabilities and outdated packages.
category: dev-code
tier: standard
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Dependency Audit

Audit project dependencies for known vulnerabilities and outdated packages.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={package}+CVE+vulnerability` — dependency CVEs
- `GET https://api.solvrbot.com/api/v1/github/trending?topic={ecosystem}&since=weekly` — ecosystem updates

## Instructions
1. For each dependency, check CVE news: `GET https://api.solvrbot.com/api/v1/news?topic=PACKAGE+vulnerability+CVE`
2. Check if newer versions are available via trending repos
3. Risk matrix:
   - Active CVE: CRITICAL — update immediately
   - Deprecated: HIGH — find alternative
   - Outdated major: MEDIUM — plan upgrade
   - Outdated minor: LOW — update when convenient
4. Output: Dependency audit report with upgrade roadmap.
