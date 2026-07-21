from flask import Blueprint, jsonify

from app.models import Schedule


bp = Blueprint(
    "api_mock",
    __name__,
    url_prefix="/api",
)


@bp.route("/schedules")
def schedules():
    schedules = Schedule.query.all()
    return jsonify([schedule.to_dict() for schedule in schedules])