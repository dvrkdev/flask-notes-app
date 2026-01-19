import os

from flask import Flask, request

from app import extensions as ex
from config import DevelopmentConfig

__version__ = "1.4.0"


def create_app(config_class=DevelopmentConfig):
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
        static_url_path="/",
    )
    app.config.from_object(config_class)

    # 1. Initialize Extensions
    init_extensions(app)

    # 2. Register Blueprints
    from app.routes import auth, main

    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)

    # 3. Configure Login Behavior
    ex.login_manager.login_view = "auth.login"
    ex.login_manager.login_message_category = "warning"

    # 4. User Loader (Modern Syntax)
    from app.models import User

    @ex.login_manager.user_loader
    def load_user(user_id):
        # Using db.session.get is the modern way in SQLAlchemy 2.0+
        return ex.db.session.get(User, int(user_id))

    # 5. Language Selection (Essential for Flask-Babel)
    @ex.babel.localeselector
    def get_locale():
        # Check for user-specific locale, then session, then header
        return request.accept_languages.best_match(
            app.config.get("LANGUAGES", ["en", "uz", "ru"])
        )

    return app


def init_extensions(app):
    """Helper to initialize all extensions."""
    ex.db.init_app(app)
    ex.migrate.init_app(app, ex.db)
    ex.login_manager.init_app(app)
    ex.ckeditor.init_app(app)
    ex.csrf.init_app(app)
    ex.babel.init_app(app)
