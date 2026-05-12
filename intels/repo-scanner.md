---
name: repo-scanner
description: Full repository security scan — dependencies, contracts, and secrets.
category: dev-code
tier: standard
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Repo Scanner

Full repository security scan — dependencies, contracts, and secrets.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={library}+CVE+vulnerability` — dependency CVEs
- `POST https://api.solvrbot.com/api/v1/security/scan` — contract security

## Instructions
1. Scan all dependencies for CVEs via news
2. For any smart contracts in the repo, run security scan
3. Secret detection patterns to check:
   - API keys (ALCHEMY_, ANTHROPIC_, etc.)
   - Private keys (0x + 64 hex)
   - Database connection strings
4. Output: Security scan report with severity ratings + remediation.
