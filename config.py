import os
from pathlib import Path

# Project root (the folder this file lives in)
BASE_DIR = Path(__file__).resolve().parent

# Single source of truth for where the instance folder (holds the sqlite
# db) lives, so config.py and app/__init__.py can never disagree on it.
INSTANCE_DIR = BASE_DIR / "instance"

# Use as_posix() so the path uses forward slashes even on Windows -
# sqlite/SQLAlchemy URIs expect that, backslashes can break the connection.
DB_PATH = (INSTANCE_DIR / "pygo.db").as_posix()


class Config:
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", f"sqlite:///{DB_PATH}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Shown as the "Feedback or found a bug?" link in the settings sidebar.
    # Point this at your repo's issues page, e.g.
    # "https://github.com/your-username/pygo/issues"
    GITHUB_URL = os.environ.get("GITHUB_URL", "https://github.com/shrutijagadale0725-rgb/PYGO")

    # Gmail SMTP for password reset emails. MAIL_PASSWORD must be a Gmail
    # "app password" (myaccount.google.com/apppasswords), never your real
    # Gmail account password. Both are set as environment variables on
    # PythonAnywhere, never committed to the repo.
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_USERNAME")