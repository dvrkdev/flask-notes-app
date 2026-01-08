from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

from app.models import User


class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired(message="Username is required."),
            Length(
                min=5,
                max=64,
                message="Username must be between 5 and 64 characters long!",
            ),
        ],
        description="Enter the username you used during registration.",
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Password is required."),
            Length(
                min=6,
                message="The password must be at least 6 characters long.",
            ),
        ],
        description="Enter the password you used during registration.",
    )

    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[
            DataRequired(message="Name is required."),
            Length(
                min=1,
                max=64,
                message="The name must be between 1 and 64 characters long!",
            ),
        ],
        description="Write it correctly, first name, then last name.",
    )

    username = StringField(
        "Username",
        validators=[
            DataRequired(message="Username is required."),
            Length(
                min=5,
                max=64,
                message="Username must be between 5 and 64 characters long!",
            ),
        ],
        description="Choose a unique username (5–64 characters).",
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Password is required."),
            Length(
                min=6,
                message="The password must be at least 6 characters long.",
            ),
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
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is taken. Please choose another.")
