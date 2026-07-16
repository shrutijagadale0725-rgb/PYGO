# PYGO 🐍

A free, interactive Python learning path for absolute beginners. Real Python
runs directly in the browser via Pyodide (WebAssembly) — no server-side code
execution, no cost per student, scales to as many learners as you want for
free.

**Live:** https://pygo.pythonanywhere.com

Built solo as a first step for anyone who's never written a line of code and
doesn't want to sit through a 10+ hour video to write their first one. It's
not a "become a Python expert" course — it's Basics → Logic → Collections →
Functions → Structure → OOP, ending in a real mini project, with zero
paywall anywhere in the path.

## What's actually here

- **33 complete, hand-written lessons** — every one has real story content,
  a coding challenge, starter code, and an automated checker
- **Flask** — serves pages, handles accounts, stores progress
- **Pyodide** (loaded from a CDN in the browser) — runs the student's
  Python code client-side, no backend execution involved
- **SQLite** (via Flask-SQLAlchemy) — stores users, progress, streaks
- **Flask-Login** — email/password auth
- **Flask-WTF** — CSRF protection on every form and API call
- **Flask-Mail** — real password reset emails via Gmail SMTP

### Features
- 🎮 Full 33-lesson path: Basics, Logic, Collections, Functions, Structure, OOP, Project
- 🔥 Daily streak tracking (grows on any solve, not just new lessons)
- ⭐ XP, levels, and a live-updating progress dashboard
- 🏆 A real finish-line celebration once all 33 lessons are complete
- 🖼️ Pick-your-own pixel-art avatar (fox, panda, penguin, cat, shiba)
- 🔑 Full password reset flow via email
- ⚙️ Settings: change display name, change password, delete account
- 🎉 Confetti + sound on every lesson completion
- 💯 100% free, no ads, no paywall — ever

## Project structure

```
pygo/
├── run.py                        # entry point (loads .env, starts app)
├── config.py                     # SECRET_KEY, mail config, DB path
├── requirements.txt
├── migrate_add_streak_columns.py # one-time DB migrations (safe to re-run)
├── migrate_add_avatar_column.py
└── app/
    ├── __init__.py                # app factory (db, login, csrf, mail)
    ├── models.py                  # User, Progress
    ├── lessons.py                 # ALL 33 lessons live here
    ├── auth.py                    # signup/login/logout/reset/settings routes
    ├── main.py                    # home, lesson page, progress API
    ├── templates/
    │   ├── base.html              # topbar, settings sidebar, streak pill
    │   ├── index.html             # hero, "what is Python", full path, finish modal
    │   ├── lesson.html             # single lesson (editor or stub)
    │   ├── login.html / signup.html
    │   └── forgot_password.html / reset_password.html
    └── static/
        ├── css/style.css
        ├── img/avatars/            # 5 pixel-art avatar PNGs
        └── js/
            ├── lesson.js           # Pyodide editor logic, shared by every lesson
            ├── pixel-bubble.js     # NPC-style nudge/info bubble system
            ├── settings-panel.js
            └── variables-demo.js   # guest homepage live preview
```

## Run it locally

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

Visit http://127.0.0.1:5000 — the database (`instance/pygo.db`) is created
automatically on first run.

### Environment variables (`.env`)

```
SECRET_KEY=some-random-string
MAIL_USERNAME=your-gmail-address@gmail.com
MAIL_PASSWORD=your-gmail-app-password   # NOT your real Gmail password
```

Password reset emails won't send without the two `MAIL_*` variables set —
everything else works fine without them.

## Adding a new lesson

Only `app/lessons.py` needs to change. Add a dict to `LESSONS` with:

```python
{
    "slug": "your-lesson-slug",
    "title": "Lesson Title",
    "subtitle": "A short subtitle",
    "topic": "Basics",              # groups lessons on the homepage
    "order": 34,                    # position in the path
    "xp": 50,
    "story_html": "<p>...</p>",
    "challenge_html": "...",
    "starter_code": "...",
    "check_pattern": r"...",        # regex run against the student's stdout
    "placeholder_value": "...",     # the value that means "hasn't been changed yet"
    "success_message": "...",
}
```

The page, editor, XP, streak tracking, and progress saving all work
automatically — no new routes or templates needed.

**Important:** `placeholder_value` must exactly match what the *unmodified*
starter code actually prints, or the lesson will auto-complete with zero
changes. See "How the checker works" below.

## How the checker works

Intentionally simple and trust-based (it's a free learning tool, not an
exam): each lesson has a `check_pattern` regex with exactly one capturing
group. After the student runs their code, `lesson.js` matches that regex
against the captured stdout. If it matches, isn't still the placeholder
value, and the code doesn't still contain any `forbid_in_code` text (used
for the rare lesson where output alone can't prove the fix, e.g. list
comprehensions), the lesson is marked complete and XP + streak are recorded
via `/api/complete`.

Every one of the 33 `check_pattern`/`placeholder_value` pairs has been
verified two ways: the *unfixed* starter code is correctly blocked, and a
*correctly fixed* solution correctly passes.

## Deploying

Currently live on **PythonAnywhere** (free tier). To redeploy after changes:

```bash
git pull origin main
workon pygo-venv                   # or: source /path/to/venv/bin/activate
pip install -r requirements.txt
python migrate_add_streak_columns.py   # safe to re-run, skips if already applied
python migrate_add_avatar_column.py    # same
```
Then reload the web app from the PythonAnywhere Web tab. Migrations must run
*before* reloading — reloading first will crash on the missing columns.

Free-tier PythonAnywhere allows outbound SMTP specifically to Gmail (a
standing firewall exception), which is what makes password reset emails work
without a paid plan.

## What's next (ideas, not commitments)

- A privacy policy / terms page
- A lightweight smoke-test script (signup → complete a lesson → reset
  password) to catch regressions before they reach the live site
- Favicon
  service later
