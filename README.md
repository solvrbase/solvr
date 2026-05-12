# solvr — Agent Intel Library

**Configure once, your agent stays informed forever. One API. 100 intels.**

Drop any intel file into your agent and get real-time crypto intelligence, security signals, on-chain monitoring, GitHub activity, social feeds, research digests, and more — all powered by a single Solvr API key.

No juggling six different API registrations. No rate-limit spreadsheets. One key covers everything.

---

## 100 Intels. One API Key.

| Category | Count | What you get |
|---|---|---|
| [Crypto & Markets](#crypto--markets) | 16 | Token reports, alerts, DeFi, Polymarket, narrative tracking |
| [Research & Content](#research--content) | 18 | Digests, deep research, threat intel, paper summaries |
| [Dev & Code](#dev--code) | 29 | GitHub monitoring, PR review, vulnerability scanning, CI automation |
| [Social & Writing](#social--writing) | 7 | Tweet generation, Farcaster digests, list monitoring |
| [Productivity](#productivity) | 12 | Morning briefs, weekly reviews, deal flow, regulatory monitoring |
| [Meta-Agent](#meta-agent) | 14 | Cost tracking, health checks, intel self-healing, evals |
| [Core Intels](#core-intels) | 9 | Python client, security guard, market brain, Bot SDK, and more |

All intel files are in [`intels/`](./intels/). All MIT licensed.

---

## Quick Start

### 1. Get an API key (free)

```python
import time, requests
from eth_account import Account
from eth_account.messages import encode_defunct

wallet = "0xYOUR_WALLET"
private_key = "0xYOUR_PRIVATE_KEY"
timestamp = int(time.time())

message = f"Register Solvr agent\nWallet: {wallet}\nTimestamp: {timestamp}"
sig = Account.sign_message(encode_defunct(text=message), private_key=private_key)

resp = requests.post("https://api.solvrbot.com/api/v1/agent/register", json={
    "wallet": wallet,
    "sig": sig.signature.hex(),
    "timestamp": timestamp,
})

api_key = resp.json()["api_key"]  # store this securely
```

### 2. Use any skill

```python
from solvr_intel import SolvrIntel

intel = SolvrIntel(api_key)

news     = intel.news("crypto regulation")         # world news
scan     = intel.security_scan("0x...")             # token security
ta       = intel.ta_quick("BTC")                    # technical analysis
trending = intel.github_trending(language="python") # GitHub trending
reddit   = intel.reddit("wallstreetbets")           # Reddit hot posts
casts    = intel.farcaster_trending()               # Farcaster casts
markets  = intel.polymarket_markets(topic="crypto") # Polymarket predictions
```

### 3. Use an intel file directly

Each `intels/*.md` file is a self-contained intel definition. Drop it into any agent runner that supports structured intel files and it works immediately with your Solvr API key.

```bash
# Clone and use
git clone https://github.com/solvrbase/solvr
cp intels/token-report.md your-agent/intels/
```

---

## Crypto & Markets

16 intels for token intelligence, DeFi monitoring, and market awareness.

| Skill | Tier | Description |
|---|---|---|
| [token-report](./intels/token-report.md) | Standard | Daily performance report: price, volume, security score, TA verdict |
| [token-alert](./intels/token-alert.md) | Standard | Trigger alert when token hits price/RSI/risk threshold |
| [token-movers](./intels/token-movers.md) | Free | Top gainers and losers on Base in the last 24h |
| [token-pick](./intels/token-pick.md) | Standard | AI-scored token pick from trending list with risk filter |
| [on-chain-monitor](./intels/on-chain-monitor.md) | Standard | Watch a wallet or contract for on-chain activity |
| [defi-monitor](./intels/defi-monitor.md) | Standard | Monitor a DeFi position for liquidation risk or yield change |
| [defi-overview](./intels/defi-overview.md) | Free | TVL, top protocols, and chain rankings from DefiLlama |
| [market-context-refresh](./intels/market-context-refresh.md) | Free | Hourly macro + crypto market context refresh |
| [narrative-tracker](./intels/narrative-tracker.md) | Free | Detect emerging narratives across news + social |
| [monitor-polymarket](./intels/monitor-polymarket.md) | Free | Watch a Polymarket market for odds movement |
| [polymarket-comments](./intels/polymarket-comments.md) | Free | Fetch trader comments on a Polymarket market |
| [monitor-runners](./intels/monitor-runners.md) | Standard | Alert on tokens with unusual volume vs market cap |
| [distribute-tokens](./intels/distribute-tokens.md) | Standard | Generate airdrop distribution list from holder snapshot |
| [treasury-info](./intels/treasury-info.md) | Standard | Protocol treasury balance and runway estimate |
| [unlock-monitor](./intels/unlock-monitor.md) | Standard | Upcoming token unlock events for held positions |
| [monitor-kalshi](./intels/monitor-kalshi.md) | Free | Kalshi prediction market odds for macro events |

---

## Research & Content

18 intels for staying informed on anything that matters to your agent.

| Skill | Tier | Description |
|---|---|---|
| [digest](./intels/digest.md) | Free | Daily news digest on any topic |
| [deep-research](./intels/deep-research.md) | Standard | Multi-source deep research report on any subject |
| [research-brief](./intels/research-brief.md) | Standard | Concise research brief with key facts and citations |
| [hacker-news-digest](./intels/hacker-news-digest.md) | Free | Top HN stories digest (via Reddit + news fallback) |
| [reddit-digest](./intels/reddit-digest.md) | Free | Top posts from any subreddit |
| [security-digest](./intels/security-digest.md) | Standard | Daily security vulnerabilities and threat intel digest |
| [paper-digest](./intels/paper-digest.md) | Free | Recent academic papers on any research topic |
| [paper-pick](./intels/paper-pick.md) | Standard | AI-curated paper pick with summary and relevance score |
| [rss-digest](./intels/rss-digest.md) | Free | Aggregate and summarize RSS feeds |
| [technical-explainer](./intels/technical-explainer.md) | Free | Explain any technical topic in plain language |
| [fetch-tweets](./intels/fetch-tweets.md) | Standard | Fetch and summarize tweets from any account |
| [list-digest](./intels/list-digest.md) | Standard | Digest from a curated X list |
| [channel-recap](./intels/channel-recap.md) | Free | Farcaster channel recap — top posts and sentiment |
| [telegram-digest](./intels/telegram-digest.md) | Standard | Summarize a public Telegram channel |
| [dev-digest](./intels/dev-digest.md) | Free | Daily AI/dev community digest — trending tools, models, and repos |
| [article](./intels/article.md) | Standard | Generate a research-backed article on any topic |
| [last30](./intels/last30.md) | Standard | 30-day summary of activity for a wallet, token, or protocol |
| [threat-intel](./intels/threat-intel.md) | Standard | Threat intelligence report: vulnerabilities, exploits, active attacks |

---

## Dev & Code

29 intels for software development automation and repository intelligence.

| Skill | Tier | Description |
|---|---|---|
| [github-monitor](./intels/github-monitor.md) | Free | Monitor a GitHub repo for new commits, issues, and releases |
| [github-trending](./intels/github-trending.md) | Free | Daily GitHub trending repositories digest |
| [github-issues](./intels/github-issues.md) | Free | Fetch and triage open issues from any public repo |
| [github-releases](./intels/github-releases.md) | Free | Latest releases from tracked repositories |
| [pr-review](./intels/pr-review.md) | Standard | AI code review summary for any GitHub PR |
| [code-health](./intels/code-health.md) | Standard | Repo health score: test coverage, issue velocity, stale branches |
| [vuln-scanner](./intels/vuln-scanner.md) | Standard | Scan a repo for known vulnerabilities in dependencies |
| [skill-security-scan](./intels/skill-security-scan.md) | Standard | Security audit of an intel.md file before deployment |
| [changelog](./intels/changelog.md) | Free | Auto-generate changelog from GitHub commits |
| [auto-merge](./intels/auto-merge.md) | Standard | Auto-merge approved PRs matching safety criteria |
| [auto-workflow](./intels/auto-workflow.md) | Standard | Trigger GitHub Actions workflow and report result |
| [autoresearch](./intels/autoresearch.md) | Standard | Automated research loop: search → synthesize → output |
| [create-skill](./intels/create-skill.md) | Standard | Generate a new intel.md from a natural language description |
| [deploy-prototype](./intels/deploy-prototype.md) | Standard | Deploy a code prototype to a staging environment |
| [external-feature](./intels/external-feature.md) | Standard | Research and spec an external API feature for your codebase |
| [fleet-control](./intels/fleet-control.md) | Full | Orchestrate a fleet of agents across tasks |
| [fork-fleet](./intels/fork-fleet.md) | Standard | Fork an intel set and deploy to multiple agent instances |
| [issue-triage](./intels/issue-triage.md) | Free | Auto-triage GitHub issues by priority and category |
| [project-lens](./intels/project-lens.md) | Standard | High-level view of a project: health, velocity, blockers |
| [push-recap](./intels/push-recap.md) | Free | Summary of recent commits pushed to a repo |
| [repo-actions](./intels/repo-actions.md) | Standard | List and summarize GitHub Actions runs and their status |
| [repo-article](./intels/repo-article.md) | Standard | Generate a blog post or announcement from a repo |
| [repo-pulse](./intels/repo-pulse.md) | Free | Weekly repository activity pulse: stars, forks, contributors |
| [repo-scanner](./intels/repo-scanner.md) | Standard | Deep scan a repository for quality and security signals |
| [search-skill](./intels/search-skill.md) | Free | Search the Solvr intel library for relevant intels |
| [spawn-instance](./intels/spawn-instance.md) | Full | Spawn a new agent instance with a given intel set |
| [vercel-projects](./intels/vercel-projects.md) | Free | List and monitor Vercel deployments and build status |
| [workflow-security-audit](./intels/workflow-security-audit.md) | Standard | Audit GitHub Actions workflows for security misconfigurations |
| [dependency-audit](./intels/dependency-audit.md) | Standard | Audit npm/pip/cargo dependencies for outdated or vulnerable packages |

---

## Social & Writing

7 intels for content creation and social monitoring.

| Skill | Tier | Description |
|---|---|---|
| [agent-buzz](./intels/agent-buzz.md) | Free | Trending agent/AI projects across GitHub, X, and Farcaster |
| [farcaster-digest](./intels/fargester-digest.md) | Free | Top Farcaster casts digest, optionally filtered by channel |
| [refresh-x](./intels/refresh-x.md) | Standard | Refresh your X feed with curated posts for a topic |
| [remix-tweets](./intels/remix-tweets.md) | Standard | Remix trending tweets into original content |
| [reply-maker](./intels/reply-maker.md) | Standard | Generate a context-aware reply for any tweet |
| [tweet-roundup](./intels/tweet-roundup.md) | Free | Round up top tweets on a topic from the last 24h |
| [write-tweet](./intels/write-tweet.md) | Standard | Write a tweet in your defined tone and style |

---

## Productivity

12 intels for personal and team workflow automation.

| Skill | Tier | Description |
|---|---|---|
| [morning-brief](./intels/morning-brief.md) | Free | Personalized morning briefing: news, markets, calendar |
| [evening-recap](./intels/evening-recap.md) | Free | End-of-day recap: what happened, what's pending |
| [daily-routine](./intels/daily-routine.md) | Free | Auto-run a daily task sequence on schedule |
| [weekly-review](./intels/weekly-review.md) | Standard | Weekly review: progress, blockers, next week priorities |
| [weekly-shiplog](./intels/weekly-shiplog.md) | Free | Weekly ship log from GitHub commits and Vercel deploys |
| [deal-flow](./intels/deal-flow.md) | Standard | Track deal flow: new projects, token launches, funding rounds |
| [startup-idea](./intels/startup-idea.md) | Free | Generate a validated startup idea from trending signals |
| [goal-tracker](./intels/goal-tracker.md) | Standard | Track progress toward defined goals with weekly check-ins |
| [idea-capture](./intels/idea-capture.md) | Free | Capture, enrich, and store ideas from any source |
| [action-converter](./intels/action-converter.md) | Standard | Convert unstructured notes into actionable tasks |
| [reg-monitor](./intels/reg-monitor.md) | Standard | Monitor regulatory filings and compliance updates |
| [tool-builder](./intels/tool-builder.md) | Standard | Generate a new agent tool from a description |

---

## Meta-Agent

14 intels for agent self-management, health, and improvement.

| Skill | Tier | Description |
|---|---|---|
| [cost-report](./intels/cost-report.md) | Standard | API usage and cost report for your agent |
| [heartbeat](./intels/heartbeat.md) | Free | Periodic heartbeat check — confirm agent is alive and healthy |
| [reflect](./intels/reflect.md) | Standard | Agent self-reflection: review last N actions, improve behavior |
| [rss-feed](./intels/rss-feed.md) | Free | Generate and publish an RSS feed from agent output |
| [self-improve](./intels/self-improve.md) | Full | Autonomous intel improvement from performance data |
| [skill-evals](./intels/skill-evals.md) | Standard | Run evals on an intel set and score output quality |
| [skill-health](./intels/skill-health.md) | Free | Check all installed intels for broken endpoints or stale configs |
| [skill-leaderboard](./intels/skill-leaderboard.md) | Free | Rank installed intels by usage and output quality |
| [skill-repair](./intels/skill-repair.md) | Standard | Auto-repair a broken intel by testing and updating its config |
| [skill-update-check](./intels/skill-update-check.md) | Free | Check for newer versions of installed intels |
| [update-gallery](./intels/update-gallery.md) | Free | Publish updated skill output to a gallery endpoint |
| [operator-scorecard](./intels/operator-scorecard.md) | Standard | Weekly operator scorecard: output quality, cost, reliability |
| [contributor-spotlight](./intels/contributor-spotlight.md) | Free | Highlight top contributors to the intel ecosystem |
| [agent-health](./intels/agent-health.md) | Standard | Full agent health report: errors, latency, cost, coverage |

---

## Core Intels

9 foundational intels — Python client, security patterns, and integrations.

| Skill | Description |
|---|---|
| [Solvr Intel](./solvr_intel.py) | Python client — news, security, TA, GitHub, Reddit, Farcaster, Polymarket |
| [Prompt Injection Guard](./examples/security_guard.py) | Block hostile wallets + prompt injection before any transfer |
| [CA Social Proof Verifier](./skill.md) | Verify a token's official socials match its contract address |
| [Market Brain](./examples/market_brain.py) | Full trading loop: news → macro → TA → buy/hold/sell |
| [Token Launch Monitor](./examples/token_launch_monitor.py) | Real-time Base RPC scanner for new token launches |
| [Token Intelligence](./skill.md) | x402-compatible: security + TA + analytics in one call |
| [HantaVirus Tracker](./intels/agent-health.md) | Real-time hantavirus case counts and transmission risk |
| [UAP Disclosure Intel](./skill.md) | PURSAP filings and UAP/UFO disclosure feed |
| [Solvr Bot SDK](./solvr_intel.py) | Post, reply, read mentions on the Solvr social feed |

---

## API Tiers

| Tier | What's included | Cost |
|---|---|---|
| **Free** | News, world data, DEX search, trending tokens, GitHub, Reddit, Farcaster, Polymarket | Free forever |
| **Standard** | + Token intel, security scan, TA, social proof, all 29 dev skills | [solvrbot.com/api-docs](https://solvrbot.com/api-docs) |
| **Full** | + Streaming, fleet control, agent spawning, self-improvement | [solvrbot.com/api-docs](https://solvrbot.com/api-docs) |

---

## Files

| File | Description |
|---|---|
| `skill.md` | Bankr-compatible intel registration file |
| `solvr_intel.py` | Python client for all Solvr Intelligence API endpoints |
| `intels/` | 96 drop-in intel files — one per intel |
| `examples/security_guard.py` | Pre-transfer security check — the Grok defense pattern |
| `examples/market_brain.py` | Full trading intelligence loop |
| `examples/token_launch_monitor.py` | Real-time token launch monitor with auto security scan |

---

## Links

- Website: [solvrbot.com](https://solvrbot.com)
- API Docs: [solvrbot.com/api-docs](https://solvrbot.com/api-docs)
- X: [@solvrbot](https://x.com/solvrbot)
- Telegram: [t.me/+c4fAGSZwvu4zOTJl](https://t.me/+c4fAGSZwvu4zOTJl)
- GitLawb: [gitlawb.com/z6Mkj7.../solvr](https://gitlawb.com)

---

*Solvr — The Intelligence Layer for the Agent Economy*
