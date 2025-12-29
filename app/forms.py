from flask_wtf import FlaskForm
from wtforms import (BooleanField, PasswordField, StringField, SubmitField,
                     TextAreaField, URLField)
from wtforms.validators import (URL, DataRequired, Length, Optional, Regexp,
                                ValidationError)
from flask_babel import lazy_gettext as _l  # Use lazy_gettext for forms

from app import db
from app.models import User


class RegisterForm(FlaskForm):
    name = StringField(
        _l("Full name"),
        validators=[
            DataRequired(message=_l("This field is required.")), 
            Length(min=3, max=72)
        ],
        render_kw={"placeholder": _l("John Doe")},
    )

    username = StringField(
        _l("Username"),
        validators=[
            DataRequired(message=_l("This field is required.")), 
            Length(min=5, max=64)
        ],
        render_kw={"placeholder": _l("john_doe")},
    )

    password = PasswordField(
        _l("Password"),
        validators=[
            DataRequired(message=_l("This field is required.")), 
            Length(min=6, max=128)
        ],
        render_kw={"placeholder": "••••••••"},
    )

    profile_pic_url = URLField(
        _l("Profile picture URL (Optional)"),
        validators=[
            Optional(),
            URL(message=_l("Invalid URL.")),
        ],
        render_kw={"placeholder": "https://example.com/image.png"},
    )

    submit = SubmitField(_l("Create account"))

    def validate_username(self, username):
        user = db.session.execute(
            db.select(User).where(User.username == username.data)
        ).scalar_one_or_none()

        if user:
            raise ValidationError(_l("This username is already taken."))


class LoginForm(FlaskForm):
    username = StringField(
        _l("Username"),
        validators=[DataRequired(message=_l("This field is required."))],
        render_kw={"placeholder": _l("john_doe")},
    )

    password = PasswordField(
        _l("Password"),
        validators=[DataRequired(message=_l("This field is required."))],
        render_kw={"placeholder": "••••••••"},
    )

    submit = SubmitField(_l("Login"))


class NoteForm(FlaskForm):
    content = TextAreaField(
        _l("Note"),
        validators=[DataRequired(message=_l("This field is required.")), Length(min=1, max=500)],
        render_kw={
            "placeholder": _l("Write your note here..."),
            "rows": 5,
        },
    )
    is_public = BooleanField(_l("Make this note public"))

    submit = SubmitField(_l("Create note"))