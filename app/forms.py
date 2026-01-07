from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


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
            Length(min=6, message="The password must be at least 6 characters long."),
        ],
        description="Enter the password you used during registration.",
    )
    submit = SubmitField("Login")
