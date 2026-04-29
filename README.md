# polytrade-v8

**6-Layer Polymarket Paper Trading Bot** (exactly as in the PDF)

Paper trading = default. Real money only if `ENABLE_REAL_TRADING=true`

## How to run locally
1. Copy `.env.example` → `.env` and fill your keys
2. `docker compose up -d`
3. Open http://localhost:3000 (frontend)
4. Backend API: http://localhost:8000/docs

Railway deployment ready with `railway.json`
