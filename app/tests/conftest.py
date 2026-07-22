import pytest

from app import create_app
from app.config import TestConfig
from app.extensions import db
from app.models.user import User


@pytest.fixture
def app():
    app = create_app(TestConfig)

    assert app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///:memory:"

    with app.app_context():
        db.create_all()

        yield app

        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def user(app):
    user = User(
        username="admin",
        email="admin@example.com",
    )
    user.set_password("123456")

    db.session.add(user)
    db.session.commit()

    return user
