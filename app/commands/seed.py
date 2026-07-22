from datetime import date, time, timedelta
from random import choice

import click
from flask.cli import with_appcontext

from app.extensions import db
from app.models import Schedule, User

from .infos import DOCTORS, INSURANCES, PATIENTS, STATUS


def create_test_user() -> None:
    """Criar um usuário de teste."""
    if User.query.filter_by(email="admin@teste.com").first():
        click.echo("O usuário de teste já existe..")
        return

    user = User(username="admin", email="admin@teste.com")
    user.set_password("123456")

    db.session.add(user)
    db.session.commit()

    click.echo("Usuário de teste criado com sucesso.")


def create_schedules() -> None:
    if Schedule.query.first():
        return

    schedules = generate_schedules()
    db.session.add_all(schedules)
    db.session.commit()


def generate_schedules() -> list[Schedule]:
    schedules = []

    base_date = date.today()

    for index in range(20):
        patient = choice(PATIENTS)
        doctor, specialty = choice(DOCTORS)
        insurance = choice(INSURANCES)
        status = choice(STATUS)

        schedule = Schedule(
            patient=patient,
            cpf=f"{100+index:03}.{200+index:03}.{300+index:03}-{index:02}",
            doctor=doctor,
            specialty=specialty,
            date=base_date + timedelta(days=index % 5),
            time=time(8 + index % 8, (index % 2) * 30),
            insurance=insurance,
            status=status,
        )

        schedules.append(schedule)

    return schedules


@click.command("seed")
@with_appcontext
def seed_command() -> None:
    db.create_all()

    create_test_user()
    create_schedules()

    click.echo("Banco de dados populado com sucesso.")
