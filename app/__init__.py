import os
from dotenv import load_dotenv
from flask import Flask, request, session
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_babel import Babel, _

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
babel = Babel()

def get_locale():
    # Priority: 1. Session 2. Browser header
    return session.get("lang") or request.accept_languages.best_match(
        ["en", "uz"]
    )

__version__ = "1.2.1"


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
    app.config["BABEL_DEFAULT_LOCALE"] = "uz"
    app.config["BABEL_SUPPORTED_LOCALES"] = ["en", "uz"]

    # ----------------------------
    # Extensions
    # ----------------------------
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    
    # Correctly initialize Babel with the locale selector
    # babel.init_app(app, locale_selector=get_locale)
    babel.init_app(app)

    # ----------------------------
    # Flask-Login
    # ----------------------------
    login_manager.login_view = "auth.login"
    # Wrap the login message in _() so it can be extracted
    login_manager.login_message = _("You must be logged in to access this page.")
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