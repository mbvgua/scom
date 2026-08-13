"""
configure essential variables and configurations tobe used within the app
"""

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


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

    # emails
    mail_server: str = "smtp.gmail.com"
    mail_port: int = 587
    mail_username: str
    mail_password: SecretStr
    mail_from: str
    mail_use_tls: bool
    official_home_mail: str


# instantiate the settings object
settings = Settings()
