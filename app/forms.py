from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError

from app import db
from app.models import User


class RegisterForm(FlaskForm):
    name = StringField(
        "Full name",
        validators=[DataRequired(), Length(min=3, max=72)],
        render_kw={"placeholder": "John Doe"},
    )

    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=5, max=64)],
        render_kw={"placeholder": "john_doe"},
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=6, max=128)],
        render_kw={"placeholder": "••••••••"},
    )

    submit = SubmitField("Create account")

    def validate_username(self, username):
        """
        WTForms automatically calls:
        validate_<fieldname>
        """
        user = db.session.execute(
            db.select(User).where(User.username == username.data)
        ).scalar_one_or_none()

        if user:
            raise ValidationError("This username is already taken.")


class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=5, max=64)],
        render_kw={"placeholder": "john_doe"},
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=6, max=128)],
        render_kw={"placeholder": "••••••••"},
    )

    submit = SubmitField("Login")


class NoteForm(FlaskForm):
    content = TextAreaField(
        "Note",
        validators=[DataRequired(), Length(min=1, max=500)],
        render_kw={
            "placeholder": "Write your note here...",
            "rows": 5,
        },
    )
    is_public = BooleanField("Make this note public")

    submit = SubmitField("Create note")
