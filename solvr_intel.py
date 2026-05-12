"""Solvr Intelligence API — Python client.

Covers all public data endpoints:
  - news            Real-time world headlines
  - worlddata       180+ country economic data + US macro (FRED)
  - security_scan   Token rug check (GoPlus + honeypot)
  - bundles         Insider/bundle detection
  - token_intel     Unified token report (price, MC, security, socials)
  - dex_search      Token search by name/symbol/address
  - dex_trending    Trending tokens
  - dex_token       Token details by contract address
  - dex_analytics   Multi-timeframe price/volume/liquidity
  - ta_quick        RSI + MACD + Bollinger Bands
  - ta_analysis     Full TA: Stochastic, ADX, ATR, multi-EMA

Install:
    pip install httpx

Usage:
    from solvr_intel import SolvrIntel

    intel = SolvrIntel("solvr_your_key_here")
    scan  = intel.security_scan("0x...")
    news  = intel.news("Federal Reserve")
    ta    = intel.ta_quick("BTC")
"""

import re
import httpx
from typing import Optional

BASE_URL = "https://api.solvrbot.com"

_ADDRESS_RE = re.compile(r"^0x[0-9a-fA-F]{40}$")


def _validate_address(address: str) -> str:
    if not _ADDRESS_RE.match(address):
        raise ValueError(f"Invalid contract address: {address!r}")
    return address.lower()


class SolvrIntelError(Exception):
    def __init__(self, status: int, message: str):
        super().__init__(f"HTTP {status}: {message}")
        self.status = status


class SolvrIntel:
    """Synchronous client for the Solvr Intelligence API."""

    def __init__(self, api_key: str, base_url: str = BASE_URL, timeout: float = 30.0):
        self._headers = {"Authorization": f"Bearer {api_key}"}
        self._client  = httpx.Client(base_url=base_url, headers=self._headers, timeout=timeout)

    def _get(self, path: str, **params) -> dict:
        resp = self._client.get(path, params={k: v for k, v in params.items() if v is not None})
        if not resp.is_success:
            raise SolvrIntelError(resp.status_code, resp.text)
        return resp.json()

    def _post(self, path: str, **body) -> dict:
        resp = self._client.post(path, json={k: v for k, v in body.items() if v is not None})
        if not resp.is_success:
            raise SolvrIntelError(resp.status_code, resp.text)
        return resp.json()

    # ── Free tier ─────────────────────────────────────────────────────────────

    def news(self, topic: Optional[str] = None, category: str = "general", limit: int = 5) -> dict:
        """Real-time headlines from BBC, Guardian, Al Jazeera, NPR, TechCrunch.

        Args:
            topic:    keyword filter (e.g. "Federal Reserve", "Base blockchain")
            category: general | world | tech | business | science | health | politics
            limit:    1–10 articles (default 5)
        """
        return self._get("/api/v1/news", topic=topic, category=category, limit=limit)

    def worlddata(self, query: str, country: Optional[str] = None) -> dict:
        """Economic and demographic data for 180+ countries + US macro via FRED.

        Args:
            query:   indicator name — "fed rate", "gdp", "inflation", "population",
                     "vix", "s&p 500", "yield curve", "co2", "life expectancy", etc.
            country: country name or ISO-2 code (e.g. "Philippines", "US", "CN").
                     Omit for global/US aggregate.
        """
        return self._get("/api/v1/worlddata", query=query, country=country)

    def dex_search(self, q: str) -> dict:
        """Search tokens by name, symbol, or contract address."""
        return self._get("/api/v1/dex/search", q=q)

    def dex_trending(self) -> dict:
        """Currently trending tokens across all chains."""
        return self._get("/api/v1/dex/trending")

    # ── Standard tier (500M+ $SOLVR) ──────────────────────────────────────────

    def token_intel(self, address: str) -> dict:
        """Unified token report — price, MC, FDV, liquidity, volume, security,
        holder count, social links, factory, pair URL. DB-first for speed.

        Args:
            address: contract address (0x + 40 hex chars)
        """
        return self._get(f"/api/v1/intel/{_validate_address(address)}")

    def security_scan(self, address: str, chain: str = "base") -> dict:
        """Multi-source token security scan.

        Returns risk_score (0–100), verdict (safe/caution/danger), and flags.
        Sources: GoPlus + Honeypot.is + liquidity analysis + deployer history.

        Args:
            address: contract address
            chain:   "base" (default) | "ethereum"
        """
        if chain not in ("base", "ethereum"):
            raise ValueError(f"Unsupported chain: {chain!r}")
        return self._post("/api/v1/security/scan", address=_validate_address(address), chain=chain)

    def bundles(self, address: str, max_early_buyers: int = 20) -> dict:
        """Detect coordinated insider buying patterns in the first buyers of a token.

        Args:
            address:          contract address
            max_early_buyers: wallets to analyze (default 20, max 50)
        """
        if not 1 <= max_early_buyers <= 50:
            raise ValueError("max_early_buyers must be between 1 and 50")
        return self._post("/api/v1/security/bundles", address=_validate_address(address), max_early_buyers=max_early_buyers)

    def dex_token(self, address: str) -> dict:
        """Token details by contract address — aggregates all pairs."""
        return self._get(f"/api/v1/dex/token/{_validate_address(address)}")

    def dex_analytics(self, q: str) -> dict:
        """Multi-timeframe price, volume, and liquidity analytics."""
        return self._get("/api/v1/dex/analytics", q=q)

    def ta_quick(self, symbol: str) -> dict:
        """Quick TA snapshot: RSI, MACD, Bollinger Bands.

        Args:
            symbol: ticker — "BTC", "ETH", "AAPL", etc.
        """
        return self._post("/api/v1/ta/quick", symbol=symbol)

    # ── Full tier (1B+ $SOLVR) ────────────────────────────────────────────────

    def ta_analysis(self, symbol: str, interval: str = "1day") -> dict:
        """Full technical analysis stack.

        Indicators: RSI, MACD, Bollinger Bands, Stochastic, ADX, ATR, EMA (multi-TF).

        Args:
            symbol:   ticker — "BTC", "ETH", "AAPL", etc.
            interval: "1day" | "4h" | "1h" | "1week"
        """
        return self._post("/api/v1/ta/analysis", symbol=symbol, interval=interval)

    # ── Utilities ─────────────────────────────────────────────────────────────

    def is_safe(self, address: str, max_risk: int = 30) -> bool:
        """Quick boolean safety check for a token address.

        Returns True if risk_score <= max_risk and not a honeypot.

        Args:
            address:  contract address
            max_risk: maximum acceptable risk score (default 30 = low risk)
        """
        try:
            scan = self.security_scan(address)
            return scan.get("risk_score", 100) <= max_risk
        except SolvrIntelError:
            return False

    def close(self):
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()


# ── Async client ──────────────────────────────────────────────────────────────

class AsyncSolvrIntel:
    """Async version of SolvrIntel for asyncio-based agents."""

    def __init__(self, api_key: str, base_url: str = BASE_URL, timeout: float = 30.0):
        self._headers = {"Authorization": f"Bearer {api_key}"}
        self._client  = httpx.AsyncClient(base_url=base_url, headers=self._headers, timeout=timeout)

    async def _get(self, path: str, **params) -> dict:
        resp = await self._client.get(path, params={k: v for k, v in params.items() if v is not None})
        if not resp.is_success:
            raise SolvrIntelError(resp.status_code, resp.text)
        return resp.json()

    async def _post(self, path: str, **body) -> dict:
        resp = await self._client.post(path, json={k: v for k, v in body.items() if v is not None})
        if not resp.is_success:
            raise SolvrIntelError(resp.status_code, resp.text)
        return resp.json()

    async def news(self, topic=None, category="general", limit=5):
        return await self._get("/api/v1/news", topic=topic, category=category, limit=limit)

    async def worlddata(self, query, country=None):
        return await self._get("/api/v1/worlddata", query=query, country=country)

    async def token_intel(self, address):
        return await self._get(f"/api/v1/intel/{_validate_address(address)}")

    async def security_scan(self, address, chain="base"):
        if chain not in ("base", "ethereum"):
            raise ValueError(f"Unsupported chain: {chain!r}")
        return await self._post("/api/v1/security/scan", address=_validate_address(address), chain=chain)

    async def bundles(self, address, max_early_buyers=20):
        if not 1 <= max_early_buyers <= 50:
            raise ValueError("max_early_buyers must be between 1 and 50")
        return await self._post("/api/v1/security/bundles", address=_validate_address(address), max_early_buyers=max_early_buyers)

    async def ta_quick(self, symbol):
        return await self._post("/api/v1/ta/quick", symbol=symbol)

    async def ta_analysis(self, symbol, interval="1day"):
        return await self._post("/api/v1/ta/analysis", symbol=symbol, interval=interval)

    async def is_safe(self, address: str, max_risk: int = 30) -> bool:
        try:
            scan = await self.security_scan(address)
            return scan.get("risk_score", 100) <= max_risk
        except SolvrIntelError:
            return False

    async def close(self):
        await self._client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *_):
        await self.close()
