from flask import Blueprint, render_template
from flask_login import login_required

from app.agenda.services import ScheduleService

bp = Blueprint("agenda", __name__)


@bp.route("/")
@login_required
def index():
    result = ScheduleService.list_schedules()
    return render_template("agenda/index.html", **result)
