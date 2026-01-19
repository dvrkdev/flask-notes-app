from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_babel import _  # Import the translation function
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from app.extensions import db
from app.forms import LoginForm, RegisterForm
from app.models import User

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()

    if form.validate_on_submit():
        user = db.session.execute(
            db.select(User).where(User.username == form.username.data)
        ).scalar_one_or_none()

        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            # Use f-string with gettext for dynamic names
            flash(_("Welcome back, %(name)s 👋", name=user.name), "success")

            next_page = request.args.get("next")
            return redirect(next_page or url_for("main.index"))

        flash(_("Invalid username or password."), "danger")

    return render_template("auth/login.html", form=form)


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = RegisterForm()

    if form.validate_on_submit():
        try:
            user = User(
                name=form.name.data,
                username=form.username.data,
                email=form.email.data,
                password_hash=generate_password_hash(form.password.data),
                profile_pic_url=form.profile_pic_url.data,
            )
            db.session.add(user)
            db.session.commit()

            flash(_("Account created successfully 🎉"), "success")
            return redirect(url_for("auth.login"))

        except Exception:
            db.session.rollback()
            flash(_("Something went wrong."), "danger")

    return render_template("auth/register.html", form=form)


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash(_("You are now logged out."), "info")
    return redirect(url_for("auth.login"))
