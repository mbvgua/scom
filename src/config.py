"""
configure essential variables and configurations to be used within the app
"""

from functools import lru_cache
from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

# ensure paths are absolute
BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    """
    setup the project environment variables.this is a modern replacement for
    "python_dotenv" and it works really well. inheriting from "BaseSettings"
    allows for type hinting throughout the project.

    NOTE:
    - SecretStr: encrypt the variable, such that even if printed or leaked it
      only displays 10 asterisks as the value, regardless ofthe value. to get
      the actual value, you have to explicitly call it with
      ".get_secret_value()"
    """

    # load environment variables directly .env file
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",  # ignore extra vars not defined here
    )

    environment: str

    # --- filesystems
    static_dir: Path = BASE_DIR / "static"
    templates_dir: Path = BASE_DIR / "templates"

    # --- emails
    mail_server: str
    mail_port: int
    mail_username: str
    mail_password: SecretStr = SecretStr("")
    mail_from: str
    mail_use_tls: bool
    official_home_mail: str

    @property
    def is_production(self) -> bool:
        return self.environment.lower() == "production"


@lru_cache()
def get_settings() -> Settings:
    """
    this function is cleaner than just instantiating it directly, since that
    also worked but it also brought about an error from my LSP.
    """
    return Settings()
