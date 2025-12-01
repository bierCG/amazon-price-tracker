from pydantic_settings import BaseSettings, SettingsConfigDict

import os

env = os.getenv('ENV')

class Settings(BaseSettings):
    DATABASE_URL: str
    DRIVER_NAME: str
    USER_NAME: str
    PASSWORD: str
    HOST: str
    PORT: str
    DATABASE: str

    model_config = SettingsConfigDict(env_file=f'.env', env_file_encoding='utf-8')

settings = Settings()