from flask import jsonify
import numpy as np
import pandas as pd

import app


def register_routes(app):
    """Register application routes."""
    @app.route("/")
    def home():
        return jsonify({"message": "Welcome to the app", "env": app.config["ENV"]})

    @app.route("/data")
    def get_data():
        response_data = {
            "array": np.array([1, 2, 3]),
            "number": np.float64(42.42),
            "timestamp": pd.Timestamp("2023-12-18 10:00:00"),
            "dataframe": pd.DataFrame({"A": [1, 2], "B": [3, 4]}),
        }
        return jsonify(response_data)

    @app.route("/reload-config", methods=["POST"])
    def reload_config():
        try:
            app_config = app.AppConfig.from_env()
            app.config.update(app_config.dict())
            app.setup_logging(app.config["LOGGING_LEVEL"])
            return jsonify({"message": "Configuration reloaded successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/health")
    def health():
        return jsonify({"status": "healthy"}), 200
