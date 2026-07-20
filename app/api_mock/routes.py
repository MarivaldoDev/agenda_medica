from flask import Blueprint, jsonify

from app.api_mock.fake_data import SCHEDULES


bp = Blueprint(
    "api_mock",
    __name__,
    url_prefix="/api",
)


@bp.route("/schedules")
def schedules():
    return jsonify(SCHEDULES)