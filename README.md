# 📝 Flask Notes App

A simple and secure **digital notebook** web application built with **Flask**.
Users can register, log in, and manage personal notes in a clean, responsive interface powered by **Bootstrap 5**.

🌐 **Live demo:**
👉 [https://flasknotesapp.pythonanywhere.com/](https://flasknotesapp.pythonanywhere.com/)

📦 **GitHub repository:**
👉 [https://github.com/dvrkdev/flask-notes-app](https://github.com/dvrkdev/flask-notes-app)

---

## ✨ Features

* 🔐 User authentication (Register / Login / Logout)
* 🗒️ Create, view, edit, and delete personal notes
* 👤 Notes are user-specific and securely protected
* 🛡️ CSRF protection with Flask-WTF
* 💬 Flash messages for user feedback
* 📱 Fully responsive UI using Bootstrap 5

---

## 🛠️ Tech Stack

* **Backend:** Flask, Flask-Login, Flask-WTF
* **Database:** SQLAlchemy (SQLite)
* **Frontend:** HTML, Jinja2, Bootstrap 5
* **Auth & Security:** Flask-Login, CSRF protection

---

## 🚀 Installation & Setup

Clone the repository:

```bash
git clone https://github.com/dvrkdev/flask-notes-app.git
cd flask-notes-app
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
export FLASK_APP=app        # Linux / macOS
set FLASK_APP=app           # Windows (CMD)
flask run
```

Open your browser and visit:
👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📌 Usage

1. Register a new account.
2. Log in securely.
3. Create, edit, and delete your notes.
4. All notes are private and tied to your account.

---

## 🌱 Possible Improvements

* 🔍 Search & filter notes
* 📄 Pagination for large note lists
* 🧾 Markdown support
* 🌙 Dark / Light theme toggle
* 🕒 Edit history or timestamps

---

## 🎨 Credits

Icons used in the project: [Paper icons by Pixel perfect – Flaticon](https://www.flaticon.com/free-icons/paper)
