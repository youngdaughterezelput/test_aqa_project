from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    base_url: str = "https://opensource-demo.orangehrmlive.com"
    browser: str = "chromium"
    headless: bool = True
    timeout: int = 10000
    viewport_width: int = 1440
    viewport_height: int = 900

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
