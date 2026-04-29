from fastapi import APIRouter, Depends
from app.services.llm import get_brain_decision
from app.execution.paper_executor import paper_executor
from app.core.config import settings

router = APIRouter()

@router.post("/run")
async def run_full_scan():
    # Placeholder - real scanner runs in background worker
    return {
        "status": "scan_started",
        "message": "6-layer pipeline running (paper mode)",
        "real_trading": settings.enable_real_trading
    }
