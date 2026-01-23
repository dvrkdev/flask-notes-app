from flask_babel import lazy_gettext as _l
# from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import (BooleanField, EmailField, PasswordField, StringField,
                     SubmitField, TextAreaField, URLField)
from wtforms.validators import (URL, DataRequired, Email, Length, Optional,
                                ValidationError)

from app.extensions import db
from app.models import User


class RegisterForm(FlaskForm):
    name = StringField(
        _l("Full Name"),
        validators=[
            DataRequired(message=_l("Please enter your name.")),
            Length(min=3, max=72),
        ],
        render_kw={"placeholder": _l("John Doe")},
    )

    username = StringField(
        _l("Username"),
        validators=[
            DataRequired(message=_l("Please choose a username.")),
            Length(min=5, max=64),
        ],
        render_kw={"placeholder": _l("john_doe")},
    )

    email = EmailField(
        _l("Email Address"),
        validators=[
            DataRequired(message=_l("Email is required.")),
            Email(message=_l("Please enter a valid email address.")),
        ],
        render_kw={"placeholder": _l("john.doe@example.com")},
    )

    password = PasswordField(
        _l("Password"),
        validators=[
            DataRequired(message=_l("Please set a password.")),
            Length(min=6, max=128),
        ],
        render_kw={"placeholder": "••••••••"},
    )

    profile_pic_url = URLField(
        _l("Profile Picture URL"),
        validators=[
            Optional(),
            URL(message=_l("Enter a valid image URL.")),
        ],
        render_kw={"placeholder": "https://example.com/image.png"},
    )

    submit = SubmitField(_l("Create Account"))

    def validate_username(self, username):
        user = db.session.scalar(db.select(User).where(User.username == username.data))
        if user:
            raise ValidationError(_l("This username is already taken."))

    def validate_email(self, email):
        user = db.session.scalar(db.select(User).where(User.email == email.data))
        if user:
            raise ValidationError(_l("This email is already registered."))


class LoginForm(FlaskForm):
    username = StringField(
        _l("Username"),
        validators=[DataRequired(message=_l("Username is required."))],
        render_kw={"placeholder": _l("john_doe")},
    )

    password = PasswordField(
        _l("Password"),
        validators=[DataRequired(message=_l("Password is required."))],
        render_kw={"placeholder": "••••••••"},
    )

    remember_me = BooleanField(_l("Keep me logged in"))  # Standard UX addition

    submit = SubmitField(_l("Login"))


class NoteForm(FlaskForm):
    content = TextAreaField(
        _l("Content"),
        validators=[
            DataRequired(message=_l("Your note cannot be empty.")),
            Length(max=280, message=_l("Please keep your note under 280 characters.")),
        ],
        render_kw={
            "placeholder": _l("What's happening?"),
            "rows": 3,
            "maxlength": 280,  # Browser-level enforcement
        },
    )

    submit = SubmitField(_l("Post"))
