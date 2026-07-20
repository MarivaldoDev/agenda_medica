from flask import Flask

from app.config import Config
from app.extensions import db, migrate, login_manager
from app.routes import bp
from app.commands.seed import seed_command


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    app.register_blueprint(bp)

    from app.auth import login

    app.cli.add_command(seed_command)

    return app