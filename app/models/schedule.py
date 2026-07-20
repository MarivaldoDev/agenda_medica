from app.extensions import db


class Schedule(db.Model):
    __tablename__ = "schedules"

    id = db.Column(db.Integer, primary_key=True)

    patient = db.Column(
        db.String(100),
        nullable=False,
    )

    cpf = db.Column(
        db.String(14),
        nullable=False,
        index=True,
    )

    doctor = db.Column(
        db.String(100),
        nullable=False,
    )

    specialty = db.Column(
        db.String(100),
        nullable=False,
    )

    date = db.Column(
        db.Date,
        nullable=False,
    )

    time = db.Column(
        db.Time,
        nullable=False,
    )