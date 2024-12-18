from flask import jsonify


def register_routes(app):
    """Register application routes."""
    @app.route("/")
    def home():
        return jsonify({"message": "Welcome to the app", "env": app.config["ENV"]})