from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from app import db
from app.forms import NoteForm
from app.models import Note

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/", methods=["POST", "GET"])
@login_required
def home():
    notes = Note.query.order_by(Note.created_at.desc()).all()
    form = NoteForm()
    if form.validate_on_submit():
        note = Note(
            title=form.title.data, content=form.content.data, user_id=current_user.id
        )
        db.session.add(note)
        db.session.commit()
        flash("Note created successfully.", "success")
        return redirect(url_for("main.home"))
    return render_template("main/home.html", notes=notes, form=form)


@bp.route("/create")
def create_note():
    return render_template("main/create_note.html")


@bp.route("/read")
def read_note():
    return render_template("main/read_note.html")


@bp.route("/update")
def update_note():
    return render_template("main/update_note.html")


@bp.route("/delete")
def delete_note():
    return "delete note"
