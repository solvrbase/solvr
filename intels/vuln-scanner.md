---
name: vuln-scanner
description: Scan for vulnerabilities in code dependencies and smart contracts.
category: dev-code
tier: standard
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Vuln Scanner

Scan for vulnerabilities in code dependencies and smart contracts.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic=CVE+vulnerability+{dependency}` — CVE news
- `POST https://api.solvrbot.com/api/v1/security/scan` — contract security scan

## Instructions
1. For each dependency, search CVEs: `GET https://api.solvrbot.com/api/v1/news?topic=CVE+DEPENDENCY&limit=5`
2. For smart contracts, run full scan: `POST https://api.solvrbot.com/api/v1/security/scan`
3. Severity classification:
   - Critical: remote code execution, fund loss risk
   - High: privilege escalation, data exposure
   - Medium: limited impact
   - Low: informational
4. Output: Vulnerability report with remediation steps.
