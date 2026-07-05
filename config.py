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