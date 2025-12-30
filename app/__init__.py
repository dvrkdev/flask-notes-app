from flask import Flask

def create_app():
    app = Flask(__name__)

    # register blueprints
    from app.routes import auth, main
    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)
    
    return app