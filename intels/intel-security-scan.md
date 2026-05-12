---
name: intel-security-scan
description: Security audit for agent intels — check for prompt injection and unsafe patterns.
category: dev-code
tier: standard
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Intel Security Scan

Security audit for agent intels — check for prompt injection and unsafe patterns.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic=prompt+injection+AI+agent+security` — latest attack patterns
- `POST https://api.solvrbot.com/api/v1/security/scan` — verify any contract addresses in intels

## Instructions
1. Fetch latest AI security threats: `GET https://api.solvrbot.com/api/v1/news?topic=prompt+injection+AI+agent`
2. Scan intel content for:
   - Hardcoded private keys or API keys
   - Unsafe eval/exec patterns
   - Prompt injection vulnerabilities
   - Unvalidated external inputs
3. For any contract addresses in intels, run security scan
4. Output: Security audit report with severity ratings.
