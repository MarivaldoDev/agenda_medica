from app.extensions import db


class Schedule(db.Model):
    __tablename__ = "schedules"

    id = db.Column(db.Integer, primary_key=True)
    patient = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), nullable=False, index=True)
    doctor = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    insurance = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def to_dict(self) -> dict[str, str | int]:
        """Converte o agendamento para um dicionário JSON."""

        return {
            "id": self.id,
            "patient": self.patient,
            "cpf": self.cpf,
            "doctor": self.doctor,
            "specialty": self.specialty,
            "date": self.date.isoformat(),
            "time": self.time.strftime("%H:%M"),
            "insurance": self.insurance,
            "status": self.status,
        }
