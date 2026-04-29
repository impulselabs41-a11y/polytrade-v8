from fastapi import APIRouter
from app.api.v1.endpoints import scanner, decisions, portfolio

api_router = APIRouter()
api_router.include_router(scanner.router, prefix="/scanner", tags=["scanner"])
api_router.include_router(decisions.router, prefix="/decisions", tags=["decisions"])
api_router.include_router(portfolio.router, prefix="/portfolio", tags=["portfolio"])
