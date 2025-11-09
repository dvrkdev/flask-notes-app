import os

import dotenv
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

dotenv.load_dotenv()

login_manager = LoginManager()
db = SQLAlchemy()


def create_app():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
        static_url_path="/",
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///website.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY", "dev-fallback-key"
    )  # TODO: use python-dotenv to create local environment variables

    login_manager.init_app(app)
    db.init_app(app)

    from app.routes import auth, main

    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)

    from app.models import User

    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to view this page."  # TODO: change this flash message to the better version
    login_manager.login_message_category = "danger"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
