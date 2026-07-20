from flask import Blueprint, render_template
from app.agenda.services import ScheduleService
from flask_login import login_required

bp = Blueprint("agenda", __name__)


@bp.route("/")
# @login_required
def index():
    schedules = ScheduleService.list_schedules()
    return render_template("agenda/index.html", schedules=schedules)
