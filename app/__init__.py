import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import INSTANCE_DIR

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message = "Log in to save your progress."
login_manager.login_message_category = "info"


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Must match the folder config.py builds the sqlite path from, or the
    # database file's directory won't exist when SQLAlchemy tries to open it.
    INSTANCE_DIR.mkdir(parents=True, exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    from app.auth import auth_bp
    from app.main import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    @app.context_processor
    def inject_globals():
        return {"github_url": app.config.get("GITHUB_URL", "https://github.com")}
    with app.app_context():
        db.create_all()

    return app
