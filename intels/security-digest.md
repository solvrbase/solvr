---
name: security-digest
description: Daily security & threat intelligence digest — hacks, exploits, CVEs.
category: research-content
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Security Digest

Daily security & threat intelligence digest — hacks, exploits, CVEs.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic=cybersecurity+hack+exploit&limit=10` — security news
- `GET https://api.solvrbot.com/api/v1/news?topic=CVE+vulnerability&category=tech&limit=5` — CVE news

## Instructions
1. Fetch security news: `GET https://api.solvrbot.com/api/v1/news?topic=cybersecurity+hack+exploit&limit=10`
2. Fetch CVE news: `GET https://api.solvrbot.com/api/v1/news?topic=CVE+vulnerability&limit=5`
3. Categorize:
   - 🔴 Critical: active exploits, zero-days
   - 🟡 High: patches available, data breaches
   - 🟢 Info: security research, best practices
4. Output prioritized security digest.
