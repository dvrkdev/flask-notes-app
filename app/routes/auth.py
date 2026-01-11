from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.forms import LoginForm, RegistrationForm
from app.models import User

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            flash(f"Welcome back, {user.username}!", "success")
            return redirect(url_for("main.home"))
        else:
            flash("Invalid username or password.", "danger")
    return render_template("auth/login.html", form=form)


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(
            name=form.name.data, username=form.username.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        flash("Your account has been successfully created!", "success")
        return redirect(url_for("main.home"))
    return render_template("auth/register.html", form=form)


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You are logged out.", "danger")
    return redirect(url_for("main.home"))
