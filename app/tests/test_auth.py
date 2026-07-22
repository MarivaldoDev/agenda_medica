from flask.testing import FlaskClient


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
