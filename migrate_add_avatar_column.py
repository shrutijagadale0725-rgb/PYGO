"""
One-time migration: adds the new `avatar` column to the existing `user`
table, defaulting every existing user to "fox".

This does NOT touch any existing rows, accounts, or progress - it only
adds one new column with a safe default. Safe to run more than once;
it checks whether the column already exists before adding it.

Run this ONCE, from the project root, in the same environment/database
the app actually uses:

    python migrate_add_avatar_column.py

Run it in BOTH places:
  1. Locally, if you have a local database with real data you want to keep.
  2. On PythonAnywhere (in a Bash console, inside your project folder,
     with your venv activated) - this is the important one, since that's
     where your real live users are.
"""
from dotenv import load_dotenv
load_dotenv()

from sqlalchemy import text, inspect
from app import create_app, db

app = create_app()

with app.app_context():
    inspector = inspect(db.engine)
    existing_columns = {col["name"] for col in inspector.get_columns("user")}

    with db.engine.connect() as conn:
        if "avatar" not in existing_columns:
            conn.execute(text("ALTER TABLE user ADD COLUMN avatar VARCHAR(20) DEFAULT 'fox' NOT NULL"))
            print("Added avatar column (defaulted to 'fox' for all existing users).")
        else:
            print("avatar column already exists, skipping.")

        conn.commit()

print("Migration complete. Existing accounts and progress are untouched.")
