---
name: deploy-prototype
description: Deploy a code prototype using Solvr data and GitHub-hosted infrastructure.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Deploy Prototype

Deploy a code prototype using Solvr data and GitHub-hosted infrastructure.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/github/trending?topic={framework}&limit=5` — deployment options
- `GET https://api.solvrbot.com/api/v1/news?topic={framework}+deploy&category=tech` — deployment news

## Instructions
1. Fetch popular deployment tools for the tech stack
2. Check for deployment-related news (outages, updates): `GET https://api.solvrbot.com/api/v1/news?topic=FRAMEWORK+deploy`
3. Deployment checklist:
   - [ ] Environment variables secured
   - [ ] No hardcoded API keys
   - [ ] Health endpoint configured
   - [ ] Rate limits configured
4. Output: Deployment readiness report.
