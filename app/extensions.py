# app/extensions.py

from flask_babel import Babel
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

babel = Babel()
login_manager = LoginManager()
csrf = CSRFProtect()
ckeditor = CKEditor()
db = SQLAlchemy()
migrate = Migrate()
