import os

from dotenv import load_dotenv
from flask import Flask, request, session
from flask_babel import Babel, _
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
babel = Babel()
ckeditor = CKEditor()


def get_locale():
    return session.get("lang") or request.accept_languages.best_match(["en", "uz"])


__version__ = "1.4.0"


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
    app.config["CKEDITOR_SERVE_LOCAL"] = True
    app.config["CKEDITOR_PKG_TYPE"] = "basic"
    app.config["CKEDITOR_ENABLE_CODESNIPPET"] = True
    app.config["CKEDITOR_HEIGHT"] = 400
    # app.config["CKEDITOR_UI_COLOR"] = "#9AB8F3"
    # app.config["CKEDITOR_SKIN"] = "moono-dark"

    # ----------------------------
    # Extensions
    # ----------------------------
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    ckeditor.init_app(app)
    babel.init_app(app)

    # ----------------------------
    # Flask-Login
    # ----------------------------
    login_manager.login_view = "auth.login"
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
