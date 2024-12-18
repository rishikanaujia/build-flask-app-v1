from flask.cli import with_appcontext
from gevent.pywsgi import WSGIServer
import logging

def register_cli_commands(app):
    """Register CLI commands."""
    @app.cli.command("runserver")
    @with_appcontext
    def runserver():
        """Run the application with WSGIServer."""
        host = app.config["HOST"]
        port = app.config["PORT"]
        if app.config["ENV"] == "dev":
            app.run(host=host, port=port, debug=app.config["DEBUG"])
        else:
            http_server = WSGIServer((host, port), app)
            logging.info(f"Listening at: {host}:{port}")
            http_server.serve_forever()
