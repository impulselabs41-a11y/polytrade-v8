import asyncio
from loguru import logger
from app.services.polymarket import get_active_markets
from app.services.binance import get_binance_price
from app.agents.market_analyst import MarketAnalystAgent
from app.agents.risk_manager import RiskManagerAgent
from app.simulation.miroshark_adapter import run_miroshark_simulation
from app.execution.paper_executor import paper_executor
from app.core.db import SessionLocal

async def full_pipeline():
    db = SessionLocal()
    try:
        markets = await get_active_markets(limit=5)
        binance_price = await get_binance_price()
        
        for market in markets:
            signals = {"binance_btc": binance_price["price"]}
            
            # Layer 1 + 2 + 3
            analyst = MarketAnalystAgent()
            raw_decision = await analyst.run(market, signals)
            
            # Layer 2 - Risk
            risk_manager = RiskManagerAgent()
            safe_decision = await risk_manager.run(raw_decision)
            
            # Layer 5 - Simulation
            sim_result = await run_miroshark_simulation(market)
            
            if safe_decision["direction"] != "HOLD" and sim_result["win_probability"] > 0.65:
                # Layer 6 - Execute (paper)
                await paper_executor.execute(safe_decision, db)
                logger.success(f"✅ Opportunity taken: {market['question']}")
            else:
                logger.info(f"⏭️ Skipped: {market['question']}")
    finally:
        db.close()

async def start_scanner():
    """Background worker - runs every 45 seconds"""
    logger.info("🔄 Scanner worker started")
    while True:
        try:
            await full_pipeline()
        except Exception as e:
            logger.error(f"Scanner error: {e}")
        await asyncio.sleep(45)  # scan every 45 seconds
