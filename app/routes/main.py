from flask import (Blueprint, flash, jsonify, redirect, render_template,
                   request, url_for)
from flask_login import current_user, login_required

from app import db
from app.forms import NoteForm
from app.models import Note

bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET", "POST"])
@login_required
def index():
    form = NoteForm()

    notes = (
        db.session.execute(
            db.select(Note)
            .where(Note.user_id == current_user.id)
            .order_by(Note.created_at.desc())
        )
        .scalars()
        .all()
    )

    if form.validate_on_submit():
        note = Note(
            content=form.content.data,
            user_id=current_user.id,
        )
        db.session.add(note)
        db.session.commit()

        flash("Your note has been created ✨", "success")
        return redirect(url_for("main.index"))

    return render_template(
        "index.html",
        form=form,
        notes=notes,
    )


@bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_note(id):
    note = Note.query.get_or_404(id)
    form = NoteForm(obj=note)
    
    if form.validate_on_submit():
        note.content = form.content.data
        db.session.commit()
        flash('Note updated', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('edit_note.html', form=form, note=note)


@bp.route("/delete-note", methods=["POST"])
@login_required
def delete_note():
    data = request.get_json(silent=True)

    if not data or "noteId" not in data:
        return jsonify({"error": "Invalid request"}), 400

    note = db.session.get(Note, data["noteId"])

    if not note:
        return jsonify({"error": "Note not found"}), 404

    if note.user_id != current_user.id:
        return jsonify({"error": "Unauthorized"}), 403

    db.session.delete(note)
    db.session.commit()

    return jsonify({"success": True})


# 404 Not Found
@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template("errors/404.html"), 404


# 500 Internal Server Error
@bp.app_errorhandler(500)
def internal_error(error):
    return render_template("errors/500.html"), 500
