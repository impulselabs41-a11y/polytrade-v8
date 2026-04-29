from app.core.config import settings
from loguru import logger
from app.db.models import PaperTrade
from sqlalchemy.orm import Session

class PaperExecutor:
    async def execute(self, decision: dict, db: Session):
        if settings.enable_real_trading:
            logger.warning("🔴 REAL TRADING ATTEMPT BLOCKED - Paper mode only!")
            return {"status": "blocked", "reason": "real_trading_disabled"}
        
        # Paper trade only
        trade = PaperTrade(
            market_id=decision["market_id"],
            direction=decision["direction"],
            size_usd=decision["size_usd"],
            entry_price=0.5,  # placeholder
            status="open"
        )
        db.add(trade)
        db.commit()
        
        logger.info(f"📄 PAPER TRADE EXECUTED → {decision['direction']} ${decision['size_usd']} on {decision['market_id']}")
        return {"status": "paper_executed", "trade_id": trade.id, "decision": decision}

paper_executor = PaperExecutor()
