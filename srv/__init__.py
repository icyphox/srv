from flask import Flask


def init_app():
    app = Flask(__name__, static_url_path="", static_folder="uploads")
    app.config.from_object("config.Config")

    with app.app_context():
        from . import main

    return app
