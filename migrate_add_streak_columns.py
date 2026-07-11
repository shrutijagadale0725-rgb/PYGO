"""
One-time migration: adds the two new streak-tracking columns
(current_streak, last_active_date) to the existing `user` table.

This does NOT touch any existing rows, accounts, or progress - it only
adds two new columns with safe defaults. Safe to run more than once;
it checks whether each column already exists before adding it.

Run this ONCE, from the project root, in the same environment/database
the app actually uses:

    python migrate_add_streak_columns.py
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
        if "current_streak" not in existing_columns:
            conn.execute(text("ALTER TABLE user ADD COLUMN current_streak INTEGER DEFAULT 0 NOT NULL"))
            print("Added current_streak column.")
        else:
            print("current_streak already exists, skipping.")

        if "last_active_date" not in existing_columns:
            conn.execute(text("ALTER TABLE user ADD COLUMN last_active_date DATE"))
            print("Added last_active_date column.")
        else:
            print("last_active_date already exists, skipping.")

        conn.commit()

print("Migration complete. Existing accounts and progress are untouched.")