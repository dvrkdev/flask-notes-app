from datetime import datetime as dt

from flask_login import UserMixin

from app import db


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    profile_pic_url = db.Column(db.String(255))
    username = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"{self.id}: {self.username}"


class Note(db.Model):
    __tanlename__ = "notes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=dt.utcnow)

    def __repr__(self):
        return f"{self.id}: {self.content[:50]}..."
