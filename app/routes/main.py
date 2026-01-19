from flask import Blueprint, flash, redirect, render_template, url_for
from flask_babel import _
from flask_ckeditor.utils import cleanify
from flask_login import current_user, login_required

from app.extensions import db
from app.forms import NoteForm
from app.models import Note

bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET", "POST"])
@login_required
def index():
    form = NoteForm()

    if form.validate_on_submit():
        note = Note(
            content=cleanify(form.content.data),
            user_id=current_user.id,
        )
        db.session.add(note)
        db.session.commit()
        flash(_("Your note has been created ✨"), "success")
        return redirect(url_for("main.index"))

    notes = (
        db.session.execute(
            db.select(Note)
            .where(Note.user_id == current_user.id)
            .order_by(Note.created_at.desc())
        )
        .scalars()
        .all()
    )

    return render_template(
        "main/index.html",
        form=form,
        notes=notes,
    )


@bp.route("/note/<int:id>")
@login_required
def view_note(id):
    note = Note.query.get_or_404(id)

    # Private note → only owner
    if note.user_id != current_user.id:
        flash(_("This note is private 🔒"), "danger")
        return redirect(url_for("main.index"))

    return render_template("main/view_note.html", note=note)


@bp.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_note(id):
    note = Note.query.get_or_404(id)

    if note.user_id != current_user.id:
        flash(_("You are not allowed to do this"), "danger")
        return redirect(url_for("main.index"))

    form = NoteForm(obj=note)

    if form.validate_on_submit():
        note.content = form.content.data
        db.session.commit()

        flash(_("Note updated ✨"), "success")
        return redirect(url_for("main.index"))

    return render_template("main/edit_note.html", form=form, note=note)


@bp.route("/delete/<int:id>", methods=["GET", "POST"])
@login_required
def delete_note(id):
    note = Note.query.get_or_404(id)

    if note.user_id != current_user.id:
        flash(_("You are not allowed to do this"), "danger")
        return redirect(url_for("main.index"))

    db.session.delete(note)
    db.session.commit()

    flash(_("Note deleted"), "success")
    return redirect(url_for("main.index"))
