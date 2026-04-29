from abc import ABC, abstractmethod
from app.services.llm import TradeDecision

class BaseAgent(ABC):
    @abstractmethod
    async def run(self, market_data: dict, signals: dict) -> dict:
        pass
