# 📓 Flask Notes App

Flask Notes App is a minimal, secure, and responsive web-based note-taking application. It is designed with simplicity in mind, providing a clean interface for capturing thoughts while following modern Flask and SQLAlchemy patterns.

🚀 **Live Demo:** [https://flasknotesapp.pythonanywhere.com/](https://flasknotesapp.pythonanywhere.com/)

---

## ✨ Features

* **Secure Authentication:** User registration and login with session management via Flask-Login.
* **Full CRUD:** Create, Read, Update, and Delete notes with ease.
* **Rich Text Editing:** Integrated with CKEditor for formatted notes (bold, lists, etc.).
* **Modern UI:** Responsive design built with Bootstrap 5.3 and a built-in Dark Mode toggle.
* **Internationalization:** Multi-language support (English, Uzbek, Russian) powered by Flask-Babel.
* **Security First:** CSRF protection, password hashing with Werkzeug, and Open Redirect prevention.

---

## 📂 Project Structure

```text
flask-notes-app/
├── app/
│   ├── models.py          # Database schemas (User, Note)
│   ├── forms.py           # WTForms for Auth and Notes
│   ├── routes/            # Blueprints (auth.py, main.py)
│   ├── extensions.py      # Extension initializations (DB, Login, etc.)
│   ├── static/            # CSS, JS, and Images
│   └── templates/         # Jinja2 HTML templates
├── migrations/            # Flask-Migrate database history
├── config.py              # Environment configurations
├── main.py                # Application entry point
└── requirements/          # Dependency files (common.txt, dev.txt)

```

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone [https://github.com/dvrkdev/flask-notes-app.git](https://github.com/dvrkdev/flask-notes-app.git)
cd flask-notes-app

```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

```

### 3. Install dependencies

```bash
pip install -r requirements/dev.txt

```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
FLASK_APP=main.py
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db

```

### 5. Initialize the Database

```bash
flask db upgrade

```

### 6. Run the application

```bash
flask run

```

---

## 📜 License & Credits

* **Framework:** [Flask](https://flask.palletsprojects.com/)
* **Database:** [SQLAlchemy](https://www.sqlalchemy.org/)
* **Icons:** [Notes icons by Freepik - Flaticon](https://www.flaticon.com/free-icons/notes)

Distributed under the MIT License. See `LICENSE` for more information.
