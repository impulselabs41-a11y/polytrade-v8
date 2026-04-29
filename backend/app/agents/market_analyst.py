from app.agents.base import BaseAgent
from app.services.llm import get_brain_decision

class MarketAnalystAgent(BaseAgent):
    async def run(self, market_data: dict, signals: dict) -> dict:
        # Layer 3 + Layer 1 combined simple call
        decision = await get_brain_decision(market_data, signals)
        return decision.model_dump()
