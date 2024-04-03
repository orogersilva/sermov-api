from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    logging_level: str = "INFO"
    testing: bool = False
    postgres_uri: str
    auth_secret_key: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()