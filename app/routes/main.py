from flask import Blueprint, render_template

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/")
def home():
    return render_template("main/home.html")


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
