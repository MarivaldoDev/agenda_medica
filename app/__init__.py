from flask import Flask

from app.config import Config
from app.extensions import db, migrate, login_manager
from app.commands.seed import seed_command
from app.agenda.routes import bp as agenda_bp
from app.auth.routes import bp as auth_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(agenda_bp)

    from app.auth import login_principal

    app.cli.add_command(seed_command)

    return app