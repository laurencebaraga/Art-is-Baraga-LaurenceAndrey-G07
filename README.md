# Art-is

Art-is is a web app where student artists can share their artworks and get critiques from other students.

## Tech Stack

- Python 3
- Django (full stack, using Django templates)
- SQLite for development (will be switched to PostgreSQL/Supabase later)
- Pillow (for profile photo uploads)
- python-dotenv (for the `.env` file)

## Setup (Windows PowerShell)

### 1. Clone the repo

```
git clone <your-repo-url>
cd <repo-folder>
```

### 2. Create and turn on the virtual environment

Create it (first time only):

```
python -m venv .venv
```

Turn it on:

```
.venv\Scripts\activate
```

You should see `(.venv)` at the start of the terminal line.

If PowerShell says scripts are disabled, run this once and try again:

```
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

To turn it off, type `deactivate`.

### 3. Install the packages

```
pip install -r requirements.txt
```

### 4. Create the `.env` file

Create a file named `.env` in the project root (the same folder as `manage.py`) with this inside:

```
SECRET_KEY=put-your-own-secret-key-here
DEBUG=True
```

To make a secret key:

```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Set up the database

```
python manage.py migrate
```

### 6. Create the admin account

```
python manage.py createsuperuser
```

Use the test account below. If Django warns that the password is too similar to the username, type `y` to continue, since this is only for local testing.

### 7. Run the server

```
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser. To stop the server, press `Ctrl + C`.

## Test Account (local development only)

| Field | Value |
|---|---|
| Username | `superadmin` |
| Password | `superadmin123` |

This account only exists in the local database, so create it with the `createsuperuser` step above. Change this password before using a real database or deploying the project.

To test the Artist role, register a new account on the Register page.

## Main URLs

| URL | Page |
|---|---|
| `/accounts/register/` | Register |
| `/accounts/login/` | Login |
| `/accounts/profile/` | View profile |
| `/accounts/profile/edit/` | Edit profile |
| `/` | Redirects to the dashboard for your role |
| `/artist/` | Artist dashboard |
| `/admin-panel/` | Admin dashboard |
| `/admin/` | Django admin site |

## Project Structure

```
artis/
├── manage.py
├── requirements.txt
├── .env                  (not pushed)
├── .gitignore
├── artis/                (project settings and main urls)
├── accounts/             (custom user, forms, register, login, profile)
├── dashboard/            (role-based dashboards)
└── templates/
    ├── base.html
    ├── accounts/
    └── dashboard/
```

## Commit Style

This project uses conventional commits, for example:

- `feat(accounts): add register form`
- `fix(accounts): correct email validation`
- `chore: update requirements`

## Notes

- `.env`, `.venv/`, `db.sqlite3`, and `media/` are in `.gitignore` and should never be pushed.

## Author

Lastname, Firstname - Section