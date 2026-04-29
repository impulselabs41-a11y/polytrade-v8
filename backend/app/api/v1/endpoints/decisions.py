from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.db.models import AgentDecision
from typing import List

router = APIRouter()

@router.get("/")
async def get_decisions(db: Session = Depends(get_db)) -> List[dict]:
    decisions = db.query(AgentDecision).order_by(AgentDecision.created_at.desc()).limit(20).all()
    return [d.__dict__ for d in decisions]
