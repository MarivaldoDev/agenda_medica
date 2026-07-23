from datetime import date, time

from flask.testing import FlaskClient

from app.extensions import db
from app.models import Schedule


def test_login_success(client: FlaskClient, user) -> None:
    response = client.post(
        "/auth/login",
        data={
            "username": "admin",
            "password": "123456",
        },
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/")


def test_login_with_email_success(client: FlaskClient, user) -> None:
    response = client.post(
        "/auth/login",
        data={
            "username": "admin@example.com",
            "password": "123456",
        },
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/")


def test_login_invalid_password(client: FlaskClient, user) -> None:
    response = client.post(
        "/auth/login",
        data={
            "username": "admin",
            "password": "senha_errada",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert "Usuário ou senha inválidos" in response.text


def test_login_required_success(client: FlaskClient) -> None:
    response = client.get("/", follow_redirects=False)

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/auth/login?next=%2F")

    redirect = client.get(response.headers["Location"], follow_redirects=True)
    assert "Você precisa fazer login para acessar esta página." in redirect.text


def test_login_required_authenticated(client: FlaskClient, user) -> None:
    client.post(
        "/auth/login",
        data={
            "username": "admin",
            "password": "123456",
        },
        follow_redirects=True,
    )

    response = client.get("/", follow_redirects=False)

    print(response.data[1])

    assert response.status_code == 200
    assert "admin" in response.text


def test_api_returns_formatted_date_and_time(client):
    schedule = Schedule(
        patient="Maria Silva",
        cpf="123.456.789-00",
        doctor="Dr. João",
        specialty="Cardiologia",
        date=date(2026, 7, 20),
        time=time(8, 30),
        insurance="Unimed",
        status="Agendado",
    )

    db.session.add(schedule)
    db.session.commit()

    response = client.get("/api/schedules")
    data = response.get_json()[0]

    assert data["date"] == "2026-07-20"
    assert data["time"] == "08:30"
