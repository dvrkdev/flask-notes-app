from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.forms import LoginForm, RegisterForm
from app.models import User

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            flash("Welcome back!", "success")  # TODO: change this flash message
            return redirect(url_for("main.index"))
        else:
            flash(
                "Incorrect username or password", "danger"
            )  # TODO: change this flash message
    return render_template("login.html", form=form)


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(
            name=form.name.data, username=form.username.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash(
            "Registration successful! You can now log in.", "success"
        )  # TODO: update this flash message
        return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logout!", "info")  # TODO: update this flash message
    return redirect(url_for("auth.login"))
