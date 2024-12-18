import os
import configparser
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

        # Reading the config file from the app's configs directory
        config.read(os.path.join(os.path.dirname(__file__), "configs/app_config.ini"))

        # Fallback to environment variables
        env = os.environ.get("FLASK_ENV", config.get("DEFAULT", "env", fallback="dev"))

        return AppConfig(
            ENV=os.getenv("ENV", config.get(env, "env", fallback=env)),
            DEBUG=os.getenv("DEBUG", config.getboolean(env, "debug", fallback=False)),
            HOST=os.getenv("HOST", config.get(env, "host", fallback="127.0.0.1")),
            PORT=int(os.getenv("PORT", config.get(env, "port", fallback=5000))),
            LOGGING_LEVEL=os.getenv(
                "LOGGING_LEVEL", config.get(env, "logging_level", fallback="INFO")
            ),
        )
