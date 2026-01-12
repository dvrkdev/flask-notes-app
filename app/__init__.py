from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

bootstrap5 = Bootstrap5()
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
ckeditor = CKEditor()


def create_app():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
        static_url_path="/",
    )
    app.secret_key = "dev-fallback-key-1-22-333-4444-55555"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///note.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["CKEDITOR_PKG_TYPE"] = "basic"
    app.config["CKEDITOR_HEIGHT"] = 300
    app.config["CKEDITOR_LANGUAGE"] = "en"
    app.config["CKEDITOR_DISABLE_CDN"] = False
    app.config["CKEDITOR_CONFIG"] = {
        "default": {
            "versionCheck": False,
        },
        "fontSize_sizes": "12/12px;14/14px;16/16px;18/18px;20/20px;24/24px;32/32px;",
        "toolbar": [["Bold", "Italic", "Underline"], ["FontSize"]],
    }

    # initialize extensions
    bootstrap5.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    ckeditor.init_app(app)

    # login manager setup
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to view this page."
    login_manager.login_message_category = "info"

    # user loader
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    # register blueprints
    from app.routes import auth, main

    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)

    return app
