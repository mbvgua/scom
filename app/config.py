from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # load environment variables directly .env file
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"          # ignore extra vars not defined here
    )

    mail_server: str = "smtp.gmail.com"
    mail_port: int = 587
    mail_username:str
    mail_password:SecretStr
    mail_from:str
    mail_use_tls:bool
    official_home_mail: str

# instantiate the settings object
settings = Settings()
