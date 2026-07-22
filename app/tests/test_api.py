from datetime import date, time

from app.extensions import db
from app.models import Schedule


def test_should_return_schedules(client):
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

    assert response.status_code == 200

    data = response.get_json()

    assert isinstance(data, list)
    assert len(data) == 1

    assert data[0]["patient"] == "Maria Silva"
    assert data[0]["insurance"] == "Unimed"
    assert data[0]["status"] == "Agendado"


def test_should_return_empty_schedule_list(client):
    response = client.get("/api/schedules")

    assert response.status_code == 200
    assert response.get_json() == []
