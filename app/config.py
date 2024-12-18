import configparser
import os
from pydantic import BaseModel


class AppConfig(BaseModel):
    ENV: str
    DEBUG: bool
    HOST: str
    PORT: int
    LOGGING_LEVEL: str

    @staticmethod
    def from_env():
        """Load configuration from environment or .ini file."""
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), "configs/app_config.ini"))
        env = os.environ.get("FLASK_ENV", "dev")
        return AppConfig(
            ENV=os.getenv("ENV", config.get(env, "env", fallback="dev")),
            DEBUG=os.getenv("DEBUG", config.getboolean(env, "debug", fallback="false")),
            HOST=os.getenv("HOST", config.get(env, "host", fallback="127.0.0.1")),
            PORT=os.getenv("PORT", config.getint(env, "port", fallback=5000)),
            LOGGING_LEVEL=os.getenv(
                "LOGGING_LEVEL", config.get(env, "logging_level", fallback="INFO")
            ),
        )
