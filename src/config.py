import os

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Landing 0gl04q"
    BASE_DIR: str = os.path.join(os.path.dirname(__file__), "..")
    STATIC_DIR: str = os.path.join(BASE_DIR, "static")
    TEMPLATES_DIR: str = os.path.join(BASE_DIR, "templates")

    TG_BOT_TOKEN: str = ""
    TG_CHAT_ID: str = ""

    model_config = SettingsConfigDict(env_file=BASE_DIR + "/.env")

settings = Settings()