from flask import Flask, request, session

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

    ex.babel.init_app(app)
    ex.login_manager.init_app(app)
    ex.ckeditor.init_app(app)
    ex.csrf.init_app(app)
    ex.db.init_app(app)

    # login manager configurations
    ex.login_manager.login_view = "auth.login"
    ex.login_manager.login_message = "You must be logged in to access this page."
    ex.login_manager.login_message_category = "warning"

    # blueprints
    from app.routes import auth, main

    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)

    # user loader
    from app.models import User

    @ex.login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
