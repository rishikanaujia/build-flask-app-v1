from flask import Flask

from app.config import AppConfig
from app.custom_json_provider import CustomJsonProvider


def create_app():
    """Flask application factory."""
    app = Flask(__name__)
    app.json=CustomJsonProvider
    app_config = AppConfig.from_env()
    app.config.update(app_config.dict())
    # Register routes and CLI commands

    return app

