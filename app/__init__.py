from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

bootstrap5 = Bootstrap5()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')

    # initialize extensions
    bootstrap5.init_app(app)
    db.init_app(app)

    # register blueprints
    from app.routes import auth, main
    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)

    return app