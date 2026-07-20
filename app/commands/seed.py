import click
from flask.cli import with_appcontext

from app.extensions import db
from app.models import User


@click.command("seed")
@with_appcontext
def seed_command() -> None:
    """Criar um usuário de teste."""

    if User.query.filter_by(email="admin@teste.com").first():
        click.echo("O usuário de teste já existe..")
        return

    user = User(username="admin", email="admin@teste.com")
    user.set_password("123456")

    db.session.add(user)
    db.session.commit()

    click.echo("Usuário de teste criado com sucesso.")

