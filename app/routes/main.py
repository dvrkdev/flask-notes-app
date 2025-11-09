import json

from flask import (Blueprint, flash, jsonify, redirect, render_template,
                request, url_for)
from flask_login import current_user, login_required

from app import db
from app.forms import NoteForm
from app.models import Note

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/", methods=["GET", "POST"])
@login_required
def index():
    form = NoteForm()
    notes = (
        Note.query.filter_by(user_id=current_user.id)
        .order_by(Note.created_at.desc())
        .all()
    )
    if form.validate_on_submit():
        note = Note(content=form.content.data, user_id=current_user.id)
        db.session.add(note)
        db.session.commit()
        flash("Note created successfully!", "success")
        return redirect(url_for("main.index"))

    return render_template("index.html", form=form, notes=notes)


@bp.route("/delete-note", methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    note_id = note["noteId"]
    note = Note.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
