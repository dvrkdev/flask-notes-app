from urllib.parse import urlparse

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_babel import _
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
        # Clean lookup for user
        user = db.session.scalar(
            db.select(User).where(User.username == form.username.data)
        )

        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(
                user,
                remember=getattr(form, "remember_me", False) and form.remember_me.data,
            )
            flash(_("Welcome back, %(name)s 👋", name=user.name), "success")

            # Validate the 'next' redirect to prevent Open Redirect attacks
            next_page = request.args.get("next")
            if not next_page or urlparse(next_page).netloc != "":
                next_page = url_for("main.index")
            return redirect(next_page)

        flash(_("Invalid username or password."), "danger")

    return render_template("auth/login.html", form=form)


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = RegisterForm()
    if form.validate_on_submit():
        # Check for existing user to provide helpful feedback
        existing_user = db.session.scalar(
            db.select(User).where(
                (User.username == form.username.data) | (User.email == form.email.data)
            )
        )
        if existing_user:
            flash(_("Username or email already registered."), "warning")
            return render_template("auth/register.html", form=form)

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

            # --- LOG IN USER AUTOMATICALLY ---
            login_user(user)
            flash(
                _("Registration successful! Welcome, %(name)s! 🚀", name=user.name),
                "success",
            )
            return redirect(url_for("main.index"))

        except Exception:
            db.session.rollback()
            flash(_("A database error occurred. Please try again."), "danger")

    return render_template("auth/register.html", form=form)


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash(_("You have been logged out."), "info")
    return redirect(url_for("auth.login"))
