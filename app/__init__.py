from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

bootstrap5 = Bootstrap5()
db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.secret_key = "dev-fallback-key-1-22-333-4444-55555"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///note.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # initialize extensions
    bootstrap5.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

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
