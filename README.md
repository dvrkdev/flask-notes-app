# Flask Notes App

A simple **digital notebook** web application built with **Flask, Flask-Login, Flask-WTF, and SQLAlchemy**.
Users can register, log in, create, and delete notes securely. The app uses **Bootstrap 5** for a responsive UI.

**Live demo:** [flasknotesapp.pythonanywhere.com](https://flasknotesapp.pythonanywhere.com/)

**GitHub repository:** [https://github.com/dvrkdev/flask-notes-app](https://github.com/dvrkdev/flask-notes-app)

---

## Features

* ✅ User authentication (register, login, logout)
* ✅ Create, read, and delete notes
* ✅ AJAX-powered delete for smooth UX
* ✅ Responsive UI with Bootstrap 5
* ✅ CSRF protection with Flask-WTF
* ✅ Flash messages for actions

---

## Installation

```bash
git clone https://github.com/dvrkdev/flask-notes-app.git
cd flask-notes-app
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
export FLASK_APP=app
flask run
```

---

## Usage

1. Open your browser and go to `http://127.0.0.1:5000/`.
2. Register a new account.
3. Add, view, and delete your notes.

---

## Optional Improvements

* Edit notes
* Search & filter notes
* Pagination for many notes
* Markdown support
* Dark/Light theme toggle
