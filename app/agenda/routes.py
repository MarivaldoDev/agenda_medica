from flask import Blueprint, render_template

bp = Blueprint("agenda", __name__)


@bp.route("/")
def index():
    return "<h1>Agenda Médica</h1>"

