from flask import Flask

from app.config import Config
from app.extensions import db, migrate, login_manager
from app.commands.seed import seed_command
from app.agenda.routes import bp as agenda_bp
from app.auth.routes import bp as auth_bp

from app.api_mock.routes import bp as api_mock_bp


def register_extensions(app: Flask) -> None:
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.login_message = "Você precisa fazer login para acessar esta página."
    login_manager.login_message_category = "warning"


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(auth_bp)
    app.register_blueprint(agenda_bp)
    app.register_blueprint(api_mock_bp)


def register_commands(app: Flask) -> None:
    app.cli.add_command(seed_command)


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    from app.auth import login_principal  # registra o user_loader

    return app