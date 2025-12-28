import os

from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

__version__ = "1.0.0"

def create_app():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
        static_url_path="/",
    )

    # ----------------------------
    # Configuration
    # ----------------------------
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///website.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-fallback-key")

    # ----------------------------
    # Extensions
    # ----------------------------
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # ----------------------------
    # Flask-Login
    # ----------------------------
    login_manager.login_view = "auth.login"
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_message_category = "warning"

    # ----------------------------
    # Blueprints
    # ----------------------------
    from app.routes import auth, main

    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)

    # ----------------------------
    # User loader
    # ----------------------------
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
