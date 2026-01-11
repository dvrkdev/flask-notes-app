from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

from app.models import User


class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired(message="Username is required."),
            Length(min=5, max=64),
        ],
        description="Enter the username you used during registration.",
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Password is required."),
            Length(min=6),
        ],
        description="Enter the password you used during registration.",
    )

    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[
            DataRequired(message="Name is required."),
            Length(max=64),
        ],
        description="Write your first and last name.",
    )

    username = StringField(
        "Username",
        validators=[
            DataRequired(message="Username is required."),
            Length(min=5, max=64),
        ],
        description="Choose a unique username (5–64 characters).",
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Password is required."),
            Length(min=6),
        ],
        description="Create a strong password (minimum 6 characters).",
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(message="Please confirm your password."),
            EqualTo("password", message="Passwords do not match."),
        ],
        description="Re-enter your password to confirm it.",
    )

    submit = SubmitField("Create Account")

    def validate_username(self, username):
        if User.query.filter_by(username=username.data.strip()).first():
            raise ValidationError("That username is already taken.")


class NoteForm(FlaskForm):
    title = StringField(
        "Title",
        validators=[
            Length(max=128, message="Title cannot exceed 128 characters."),
        ],
        description="Optional note title.",
    )

    content = TextAreaField(
        "Content",
        validators=[
            DataRequired(message="Note content cannot be empty."),
        ],
        description="Write your note here.",
    )

    submit = SubmitField("Create Note")
