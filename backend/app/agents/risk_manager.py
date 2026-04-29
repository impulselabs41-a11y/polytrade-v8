from app.agents.base import BaseAgent
from app.core.config import settings

class RiskManagerAgent(BaseAgent):
    async def run(self, decision: dict) -> dict:
        # Strict safety checks (Layer 2)
        if decision["size_usd"] > settings.max_position_usd:
            decision["direction"] = "HOLD"
            decision["size_usd"] = 0
            decision["explanation"] += " | RISK: Position size exceeded"
        
        if decision["risk_score"] > 7:
            decision["direction"] = "HOLD"
            decision["size_usd"] = 0
            decision["explanation"] += " | RISK: High risk score rejected"
        
        return decision
