from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    name = db.Column(db.String(64))
    profile_pic_url = db.Column(db.String(255))
    username = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'{self.id}: {self.username}'