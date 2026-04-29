from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str
    redis_url: str = "redis://redis:6379/0"
    enable_real_trading: bool = False

    deepseek_api_key: str
    openrouter_api_key: str = ""
    llm_model: str = "deepseek-chat"

    polymarket_private_key: str | None = None
    polymarket_wallet_address: str | None = None

    max_position_usd: int = 5000
    max_daily_loss_usd: int = 1000
    max_open_positions: int = 5
    cooldown_seconds: int = 3600

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()
