from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from flask_babel import _  # Import translation function

from app import db
from app.forms import NoteForm
from app.models import Note

bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET", "POST"])
@login_required
def index():
    form = NoteForm()

    if form.validate_on_submit():
        note = Note(
            content=form.content.data,
            is_public=form.is_public.data,
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

    total_notes = len(notes)
    public_notes = len([note for note in notes if note.is_public])
    private_notes = total_notes - public_notes

    return render_template(
        "index.html",
        form=form,
        notes=notes,
        total_notes=total_notes,
        public_notes=public_notes,
        private_notes=private_notes,
    )


# =========================
# View single note
# =========================
@bp.route("/note/<int:id>")
@login_required
def view_note(id):
    note = Note.query.get_or_404(id)

    # Private note → only owner
    if not note.is_public and note.user_id != current_user.id:
        flash(_("This note is private 🔒"), "danger")
        return redirect(url_for("main.index"))

    return render_template("view_note.html", note=note)


# =========================
# Edit note
# =========================
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
        note.is_public = form.is_public.data
        db.session.commit()

        flash(_("Note updated ✨"), "success")
        return redirect(url_for("main.index"))

    return render_template("edit_note.html", form=form, note=note)


# =========================
# Delete note
# =========================
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


# =========================
# Public notes
# =========================
@bp.route("/public")
def public_notes():
    notes = (
        db.session.execute(
            db.select(Note)
            .where(Note.is_public.is_(True))
            .order_by(Note.created_at.desc())
        )
        .scalars()
        .all()
    )

    return render_template("public_notes.html", notes=notes)