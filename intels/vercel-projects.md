---
name: vercel-projects
description: Monitor Vercel deployments and Next.js ecosystem health.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Vercel Projects

Monitor Vercel deployments and Next.js ecosystem health.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic=Vercel+Next.js+deployment&category=tech` — deployment news
- `GET https://api.solvrbot.com/api/v1/github/trending?topic=nextjs&since=weekly` — Next.js activity

## Instructions
1. Check Vercel/Next.js news for incidents: `GET https://api.solvrbot.com/api/v1/news?topic=Vercel+outage+incident`
2. Fetch trending Next.js repos for ecosystem pulse
3. Monitor checks:
   - Service status: any reported incidents in last 24h?
   - Next.js updates: any breaking changes in trending repos?
4. Output: Vercel ecosystem health report.
