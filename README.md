# 🌍 Travello — Django Travel Website (basic)

This repository contains a travel-themed Django web application that uses the Travello HTML templates for the frontend and PostgreSQL for the production database. The project is organized under the `basic/` folder in this workspace.

Briefly, the app provides:
- Admin-managed destinations and places (images, price, description, offers)
- Django authentication (register / login / logout)
- Dynamic homepage and destination pages rendered from the DB
- Static assets served via Django `{% static %}` and collected with `collectstatic`

---

**Table of contents**
- Features
- Tech stack
- Project structure (relevant paths)
- Local development setup (Windows / PowerShell)
- Environment variables (.env)
- Database setup (PostgreSQL)
- Running migrations & server
- Collecting static files
- Creating admin user
- Pushing to GitHub
- Troubleshooting

---

## 🚀 Features

- Admin panel for managing destinations and content
- Dynamic templates (Travello) connected to Django models
- User registration and login using Django Auth
- Uses PostgreSQL in production (psycopg2-binary)

## 🛠️ Tech Stack

- Python 3.11+ / 3.12+ (tested with 3.13 on this machine)
- Django 5.2.8
- PostgreSQL (production)
- psycopg2-binary
- python-dotenv (load `.env` variables)

## 📁 Project structure (key files)

- `basic/` — Django project directory (settings, urls, wsgi/asgi)
  - `basic/settings.py` — project settings (reads from `.env`)
  - `basic/urls.py` — root URLConf
- `templates/` — project templates (index.html, contact.html, about.html, etc.)
- `static/` — source static assets used by templates
- `accounts/` — app that holds register/login views and templates
- `travello/` — main app that manages travel/destination models
- `calc/`, other apps — additional app code
- `requirements.txt` — Python dependencies
- `.gitignore` — ignores envs, assets, db and secrets

> Note: paths above are relative to `C:\Users\tanuj\OneDrive\Desktop\projects\basic` in your workspace.

---

## Local development setup (PowerShell)

1. Open PowerShell and activate your virtual environment (example path used in this workspace):

```powershell
& 'C:\Users\tanuj\OneDrive\Desktop\projects\Envs\test\Scripts\Activate.ps1'
```

2. Install dependencies from `requirements.txt`:

```powershell
cd C:\Users\tanuj\OneDrive\Desktop\projects\basic
python -m pip install -r requirements.txt
```

3. Create a `.env` file in the project root (`basic/.env`) with the following values (example):

```
SECRET_KEY=replace_this_with_a_secure_value
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

4. Ensure `.env` is not tracked by git (it should be in `.gitignore`).

## PostgreSQL setup

- Make sure PostgreSQL is installed and running on `DB_HOST:DB_PORT` and that the database and user exist (or create them):

```powershell
# Example commands (run in psql or pgAdmin as appropriate)
CREATE DATABASE your_db_name;
CREATE USER your_db_user WITH PASSWORD 'your_db_password';
GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;
```

## Run migrations & start server

```powershell
cd C:\Users\tanuj\OneDrive\Desktop\projects\basic
python manage.py migrate
python manage.py runserver
```

If migrations fail with a connection error, check that `DB_PASSWORD` is set and Postgres is running.

## Collect static files (for production)

```powershell
python manage.py collectstatic --noinput
```

This copies files from `static/` into the `STATIC_ROOT` (`assets/` in this project). Do not commit collected `assets/` to the repo — it is ignored.

## Create admin user

```powershell
python manage.py createsuperuser
```

Then visit `http://127.0.0.1:8000/admin/` and log in to manage destinations and content.

## Pushing the `basic/` folder to GitHub (recommended workflow)

1. Initialize repository (if not already):

```powershell
cd C:\Users\tanuj\OneDrive\Desktop\projects\basic
git init
git add .gitignore
git commit -m "Add .gitignore"
```

2. Make focused commits (templates, app changes, settings):

```powershell
git add templates/ accounts/ travello/ basic/settings.py requirements.txt
git commit -m "Project: templates, apps and dotenv-based settings"
```

3. Create a remote repo on GitHub (do NOT initialize with README/License), then:

```powershell
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

Security: double-check `.env` and `basic/settings.py` do not contain plaintext secrets before pushing.

---

## Troubleshooting

- psycopg2 OperationalError: "no password supplied" — make sure `DB_PASSWORD` is set in `.env` or system environment variables.
- Template static files missing / CSS not loading — ensure templates include `{% load static %}` and asset paths use `{% static '...' %}`; run `collectstatic` when appropriate.
- Virtualenv / pip launcher errors — activate the correct venv, or use `python -m pip install ...` to avoid stale pip wrappers.

## Additional notes

- If you want me to create a GitHub repository and push the code, provide the remote URL or allow me to use `gh` (GitHub CLI) and I'll push for you.
- If you'd like a `.env` file created here with placeholders, I can add it (I will not add real secrets).

---

If you'd like, I can now:
- create the `.env` file with placeholders,
- run `python -m pip install -r requirements.txt` in your venv,
- run `python manage.py migrate` and `python manage.py runserver` to verify the app starts,
- or initialize and commit the repo locally and prepare the push commands.

Tell me which of these you'd like me to perform next.
