from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_babel import _
from flask_ckeditor.utils import cleanify
from flask_login import current_user, login_required

from app.extensions import db
from app.forms import NoteForm
from app.models import Note

bp = Blueprint("main", __name__)


@bp.route("/")
@login_required
def index():
    """View all notes for the current user."""
    query = (
        db.select(Note)
        .where(Note.user_id == current_user.id)
        .order_by(Note.created_at.desc())
    )
    notes = db.session.execute(query).scalars().all()

    return render_template("main/index.html", notes=notes)


@bp.route("/new", methods=["GET", "POST"])
@login_required
def add_note():
    """Create a new note."""
    form = NoteForm()
    if form.validate_on_submit():
        note = Note(content=cleanify(form.content.data), user_id=current_user.id)
        db.session.add(note)
        db.session.commit()
        flash(_("Your note has been created ✨"), "success")
        return redirect(url_for("main.index"))

    return render_template("main/add_note.html", form=form)


@bp.route("/note/<int:id>")
@login_required
def view_note(id):
    """View a single note."""
    note = db.get_or_404(Note, id)

    if note.user_id != current_user.id:
        flash(_("Access denied."), "danger")
        return redirect(url_for("main.index"))

    return render_template("main/view_note.html", note=note)


@bp.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_note(id):
    """Edit an existing note."""
    note = db.get_or_404(Note, id)

    if note.user_id != current_user.id:
        flash(_("You are not allowed to edit this note."), "danger")
        return redirect(url_for("main.index"))

    # Populate form with existing note data
    form = NoteForm(obj=note)

    if form.validate_on_submit():
        note.content = cleanify(form.content.data)
        db.session.commit()
        flash(_("Note updated ✨"), "success")
        return redirect(url_for("main.index"))

    return render_template("main/edit_note.html", form=form, note=note)


@bp.route("/delete/<int:id>", methods=["POST"])
@login_required
def delete_note(id):
    """Delete a note (Restricted to POST for security)."""
    note = db.get_or_404(Note, id)

    if note.user_id != current_user.id:
        flash(_("Action unauthorized."), "danger")
        return redirect(url_for("main.index"))

    db.session.delete(note)
    db.session.commit()
    flash(_("Note deleted"), "success")
    return redirect(url_for("main.index"))
