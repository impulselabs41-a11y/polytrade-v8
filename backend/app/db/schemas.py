from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TradeDecision(BaseModel):
    market_id: str
    direction: str
    size_usd: float
    confidence: float
    expected_value: float
    risk_score: float
    explanation: str
    edge: str

class MarketSchema(BaseModel):
    id: str
    question: str
    yes_price: Optional[float] = None
