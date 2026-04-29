from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.router import api_router
from app.db.session import engine, Base
import asyncio
from app.workers.scanner import start_scanner
from loguru import logger

app = FastAPI(title="polytrade-v8", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)
    logger.info("🚀 polytrade-v8 started - Paper trading mode: {}".format(not settings.enable_real_trading))
    asyncio.create_task(start_scanner())

@app.get("/health")
async def health():
    return {"status": "healthy", "real_trading_enabled": settings.enable_real_trading}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
