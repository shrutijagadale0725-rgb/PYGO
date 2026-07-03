# PYGO

A free, interactive Python learning path. Real Python runs in the student's
browser via Pyodide (WebAssembly) — no server-side code execution, no cost
per student, scales to as many learners as you want for free.

## What's actually here

- **Flask** — serves pages, handles accounts, stores progress
- **Pyodide** (loaded from a CDN in the browser) — runs the student's Python
  code client-side. This already works with zero backend involvement.
- **SQLite** (via Flask-SQLAlchemy) — stores users + completed lessons
- **Flask-Login** — simple email/password auth

## Project structure

```
pygo/
├── run.py                  # entry point
├── config.py
├── requirements.txt
└── app/
    ├── __init__.py          # app factory
    ├── models.py            # User, Progress
    ├── lessons.py           # ALL lesson content lives here
    ├── auth.py               # signup/login/logout routes
    ├── main.py                # home, lesson page, progress API
    ├── templates/
    │   ├── base.html
    │   ├── index.html        # hero + full path
    │   ├── lesson.html        # single lesson (editor or stub)
    │   ├── login.html
    │   └── signup.html
    └── static/
        ├── css/style.css
        └── js/lesson.js       # Pyodide editor logic, shared by every lesson
```

## Run it locally

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

Visit http://127.0.0.1:5000 — the database (`app/instance/pygo.db`) is
created automatically on first run.

## Adding a new lesson

Only `app/lessons.py` needs to change. Find the stub entry for the lesson
(e.g. `"data-types"`) and fill in the same fields `"variables"` has:

```python
{
    "slug": "data-types",
    "title": "Data Types",
    "subtitle": "What's Inside the Box",
    "topic": "Basics",
    "order": 2,
    "xp": 50,
    "story_html": "<p>...</p>",
    "challenge_html": "...",
    "starter_code": "...",
    "check_pattern": r"...",        # regex run against the student's stdout
    "placeholder_value": "...",     # value that means "hasn't been changed yet"
    "success_message": "...",
}
```

The page, editor, XP, and progress saving all work automatically — no new
routes or templates needed.

## How the checker works

This is intentionally simple and trust-based (it's a free learning tool, not
an exam): each lesson has a `check_pattern` regex. After the student runs
their code, the JS matches that regex against the captured stdout. If it
matches and isn't still the placeholder value, the lesson is marked complete
and XP is awarded via `/api/complete`. Good enough for "did you actually try
this," not meant to be cheat-proof.

## Deploying for free

Any of these have a free tier that runs Flask comfortably:

- **Render** — easiest, auto-deploys from GitHub, free Postgres available
  when you outgrow SQLite
- **Railway** — similar, generous free usage
- **PythonAnywhere** — simplest for a first deploy, slightly more manual

For any of them: push this folder to GitHub, connect the repo, set the start
command to `gunicorn run:app` (add `gunicorn` to requirements.txt for
production), and set a real `SECRET_KEY` environment variable.

## What's NOT built yet

- Lessons 2–20 are stubs ("coming soon") — only Variables is fully written,
  as the proof of concept
- No password reset flow
- No admin UI for adding lessons (you edit `lessons.py` directly for now)
- No server-side Python execution — fine for ~everything through OOP, but
  topics like real file I/O or networking would need a sandboxed execution
  service later
