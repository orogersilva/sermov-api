from fastapi import FastAPI
import logging
import sys
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    logging_level: str = "INFO"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()

logging.basicConfig(
    stream=sys.stdout,
    level=settings.logging_level,
    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",  # noqa: E501
    datefmt="%d/%b/%Y %H:%M:%S",
)

logger = logging.getLogger("sermov-api-logger")

sermov_api_description = """
This is the Sermov API.
"""

app = FastAPI(
    title="Sermov API",
    description=sermov_api_description,
    version="0.1.0",
)

@app.get("/")
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}