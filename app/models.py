from flask_login import UserMixin
from sqlalchemy.sql import func

from app.extensions import db


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(72), nullable=False)
    username = db.Column(db.String(64), nullable=False, unique=True, index=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    profile_pic_url = db.Column(db.String(255))

    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    notes = db.relationship(
        "Note",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="select",
    )

    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"


class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    is_public = db.Column(db.Boolean, default=False, nullable=False)

    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    user = db.relationship("User", back_populates="notes")

    def __repr__(self):
        preview = self.content[:30].replace("\n", " ")
        return f"<Note id={self.id} content='{preview}...'>"
