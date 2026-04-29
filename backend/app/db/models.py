from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, JSON, ForeignKey
from sqlalchemy.sql import func
from app.core.db import Base

class Market(Base):
    __tablename__ = "markets"
    id = Column(String, primary_key=True, index=True)
    question = Column(String, nullable=False)
    yes_price = Column(Float)
    volume = Column(Float, default=0)
    liquidity = Column(Float, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class AgentDecision(Base):
    __tablename__ = "agent_decisions"
    id = Column(Integer, primary_key=True, index=True)
    market_id = Column(String, ForeignKey("markets.id"))
    direction = Column(String)  # BUY / SELL / HOLD
    size_usd = Column(Float)
    confidence = Column(Float)
    expected_value = Column(Float)
    risk_score = Column(Float)
    explanation = Column(String)
    edge = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class PaperTrade(Base):
    __tablename__ = "paper_trades"
    id = Column(Integer, primary_key=True, index=True)
    market_id = Column(String)
    direction = Column(String)
    size_usd = Column(Float)
    entry_price = Column(Float)
    status = Column(String, default="open")  # open / closed
    pnl = Column(Float, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

# Add more tables later if needed
