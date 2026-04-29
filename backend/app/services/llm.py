from openai import AsyncOpenAI
from pydantic import BaseModel
from app.core.config import settings
from loguru import logger

class TradeDecision(BaseModel):
    market_id: str
    direction: str          # "BUY" or "SELL"
    size_usd: float
    confidence: float       # 0.0 - 1.0
    expected_value: float
    risk_score: float
    explanation: str
    edge: str

client = AsyncOpenAI(
    api_key=settings.deepseek_api_key,
    base_url="https://api.deepseek.com/v1"
)

async def get_brain_decision(market_data: dict, signals: dict) -> TradeDecision:
    prompt = f"""You are the Brain Layer of a $1M Polymarket bot.
Market: {market_data}
Signals: {signals}

Return ONLY valid JSON matching the TradeDecision schema.
Focus on probability gap, edge, and risk."""

    try:
        response = await client.chat.completions.create(
            model=settings.llm_model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.3
        )
        return TradeDecision.model_validate_json(response.choices[0].message.content)
    except Exception as e:
        logger.error(f"LLM error: {e}")
        # Fallback safe decision
        return TradeDecision(
            market_id=market_data.get("id", "unknown"),
            direction="HOLD",
            size_usd=0,
            confidence=0.0,
            expected_value=0,
            risk_score=10,
            explanation="LLM call failed - safe fallback",
            edge="no_edge"
        )
