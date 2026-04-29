import httpx

async def get_active_markets(limit: int = 20):
    """Fetch live Polymarket markets via public Gamma API"""
    async with httpx.AsyncClient() as client:
        r = await client.get("https://gamma-api.polymarket.com/markets")
        markets = r.json()[:limit]
        return [{"id": m["id"], "question": m["question"], "yes_price": m.get("yes_price", 0.5)} for m in markets]
