import httpx
from app.core.config import settings

async def get_binance_price(symbol: str = "BTCUSDT") -> dict:
    """Simple price feed for signals"""
    async with httpx.AsyncClient() as client:
        r = await client.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
        data = r.json()
        return {"symbol": symbol, "price": float(data["price"])}
