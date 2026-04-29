from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.db.models import PaperTrade

router = APIRouter()

@router.get("/")
async def get_portfolio(db: Session = Depends(get_db)):
    trades = db.query(PaperTrade).all()
    total_pnl = sum(t.pnl for t in trades if t.pnl)
    return {
        "open_positions": len([t for t in trades if t.status == "open"]),
        "total_pnl": total_pnl,
        "trades": [t.__dict__ for t in trades]
    }
