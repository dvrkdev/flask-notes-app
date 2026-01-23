# Flask Notes App

Flask Notes App is a minimal, secure, and responsive web-based note-taking application designed with simplicity in mind, providing a clean interface for capturing thoughts while following modern [Flask](https://flask.palletsprojects.com/) and [SQLAlchemy](https://www.sqlalchemy.org/) patterns. A live demo of the Flask Notes App is available at [Flask Notes App Live Demo](https://flasknotesapp.pythonanywhere.com/).

> [!note] **Note:**
> The GitHub repository currently does not contain any code in the main directory. The code is available in the [v1.5.0 release](https://github.com/dvrkdev/flask-notes-app/releases/tag/v1.5.0).

The app features secure authentication with user registration and login managed via Flask-Login, full CRUD functionality for creating, reading, updating, and deleting notes, and rich text editing through CKEditor. It has a modern, responsive UI built with Bootstrap 5.3, including a Dark Mode toggle, multi-language support with Flask-Babel, and robust security measures such as CSRF protection, password hashing with Werkzeug, and Open Redirect prevention.

The project structure includes organized directories for models, forms, routes, extensions, static files, and templates, with migrations handled by Flask-Migrate and configurations in `config.py`. To set it up, clone the repository, create and activate a virtual environment, install dependencies from `requirements/dev.txt`, configure environment variables in a `.env` file, initialize the database with `flask db upgrade`, and run the app using `flask run`. The project uses Flask and SQLAlchemy, with icons credited to [Freepik via Flaticon](https://www.flaticon.com/free-icons/notes), and is distributed under the MIT License.
