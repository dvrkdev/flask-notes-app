from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

# TODO: add description to every fields
# TODO: add validator to the even fields


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=72)])
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=5, max=64)]
    )
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Create Account")

    # TODO: create username validator here!


class LoginForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=5, max=64)]
    )
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Login")


class NoteForm(FlaskForm):
    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField("Create")
