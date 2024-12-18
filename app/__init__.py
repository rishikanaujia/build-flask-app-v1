import logging
from flask import Flask
from .config import AppConfig
from .custom_json_provider import CustomJSONProvider
from .routes import register_routes
from .cli import register_cli_commands


def create_app():
    """Flask application factory."""
    app = Flask(__name__)
    app.json = CustomJSONProvider(app)

    # Load and validate configuration
    try:
        app_config = AppConfig.from_env()
        app.config.update(app_config.dict())
        setup_logging(app.config["LOGGING_LEVEL"])
    except Exception as e:
        logging.error("Failed to initialize app: %s", e)
        raise

    # Register routes and CLI commands
    register_routes(app)
    register_cli_commands(app)

    return app


def setup_logging(level: str):
    """Setup logging configuration."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logging.info("Logging is set up with level: %s", level)
