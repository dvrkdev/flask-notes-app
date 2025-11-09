from flask_login import UserMixin
from sqlalchemy.sql import func

from app import db


class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    def __repr__(self):
        return f"{self.id}. {self.content[:30]} ..."


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(72), nullable=False)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    notes = db.relationship("Note", backref="author", lazy=True)

    def __repr__(self):
        return f"{self.username} {self.name}"
