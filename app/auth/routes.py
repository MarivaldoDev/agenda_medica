from app.models import User
from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user

from app.auth.forms import LoginForm


bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(
            form.username.data,
            form.password.data,
        )

        if user:
            login_user(user)
            return redirect(url_for("agenda.index"))

        flash("Usuário ou senha inválidos.", "danger")

    return render_template("auth/login.html", form=form)


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))