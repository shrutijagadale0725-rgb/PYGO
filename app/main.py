from flask import Blueprint, render_template, abort, jsonify, request, flash, redirect, url_for
from flask_login import current_user, login_required
from app import db
from app.models import Progress
from app.lessons import LESSONS, get_lesson, is_playable, next_slug, continue_slug, is_unlocked

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    completed = current_user.completed_slugs if current_user.is_authenticated else set()
    hero_lesson = get_lesson(continue_slug(completed))
    unlocked = {l["slug"]: is_unlocked(l, completed) for l in LESSONS}
    dash_percent = round(len(completed) / len(LESSONS) * 100) if LESSONS else 0
    return render_template(
        "index.html",
        lessons=LESSONS,
        completed=completed,
        hero_lesson=hero_lesson,
        unlocked=unlocked,
        dash_percent=dash_percent,
    )


@main_bp.route("/lesson/<slug>")
def lesson(slug):
    lesson_data = get_lesson(slug)
    if lesson_data is None:
        abort(404)

    completed_slugs = current_user.completed_slugs if current_user.is_authenticated else set()

    if is_playable(lesson_data) and not is_unlocked(lesson_data, completed_slugs):
        flash("Finish the earlier lessons in the path first!", "info")
        return redirect(url_for("main.index"))

    completed = slug in completed_slugs
    nxt = next_slug(slug)

    return render_template(
        "lesson.html",
        lesson=lesson_data,
        playable=is_playable(lesson_data),
        completed=completed,
        next_slug=nxt,
    )


@main_bp.route("/api/complete", methods=["POST"])
@login_required
def complete_lesson():
    data = request.get_json(silent=True) or {}
    slug = data.get("slug")
    lesson_data = get_lesson(slug)

    if lesson_data is None or not is_playable(lesson_data):
        return jsonify({"ok": False, "error": "Unknown or non-playable lesson."}), 400

    existing = Progress.query.filter_by(user_id=current_user.id, lesson_slug=slug).first()
    if existing is None:
        progress = Progress(
        user_id=current_user.id,
        lesson_slug=slug,
        xp_earned=lesson_data["xp"],
    )
    db.session.add(progress)

# Record activity for the streak on ANY successful solve today — new
# lesson or a revisit of one already completed. This is what lets the
# streak keep growing after someone's finished the whole curriculum.
    current_user.record_activity()
    db.session.commit()

    return jsonify({
        "ok": True,
        "total_xp": current_user.total_xp,
        "level": current_user.level,
        "streak": current_user.current_streak,
        "next_slug": next_slug(slug),
    })
from flask import Blueprint, render_template, abort, jsonify, request, flash, redirect, url_for
from flask_login import current_user, login_required
from app import db
from app.models import Progress
from app.lessons import LESSONS, get_lesson, is_playable, next_slug, continue_slug, is_unlocked

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    completed = current_user.completed_slugs if current_user.is_authenticated else set()
    hero_lesson = get_lesson(continue_slug(completed))
    unlocked = {l["slug"]: is_unlocked(l, completed) for l in LESSONS}
    dash_percent = round(len(completed) / len(LESSONS) * 100) if LESSONS else 0
    return render_template(
        "index.html",
        lessons=LESSONS,
        completed=completed,
        hero_lesson=hero_lesson,
        unlocked=unlocked,
        dash_percent=dash_percent,
    )


@main_bp.route("/lesson/<slug>")
def lesson(slug):
    lesson_data = get_lesson(slug)
    if lesson_data is None:
        abort(404)

    completed_slugs = current_user.completed_slugs if current_user.is_authenticated else set()

    if is_playable(lesson_data) and not is_unlocked(lesson_data, completed_slugs):
        flash("Finish the earlier lessons in the path first!", "info")
        return redirect(url_for("main.index"))

    completed = slug in completed_slugs
    nxt = next_slug(slug)

    return render_template(
        "lesson.html",
        lesson=lesson_data,
        playable=is_playable(lesson_data),
        completed=completed,
        next_slug=nxt,
    )


@main_bp.route("/api/complete", methods=["POST"])
@login_required
def complete_lesson():
    data = request.get_json(silent=True) or {}
    slug = data.get("slug")
    lesson_data = get_lesson(slug)

    if lesson_data is None or not is_playable(lesson_data):
        return jsonify({"ok": False, "error": "Unknown or non-playable lesson."}), 400

    existing = Progress.query.filter_by(user_id=current_user.id, lesson_slug=slug).first()
    if existing is None:
        progress = Progress(
            user_id=current_user.id,
            lesson_slug=slug,
            xp_earned=lesson_data["xp"],
        )
        db.session.add(progress)
        current_user.record_activity()
        db.session.commit()

    return jsonify({
        "ok": True,
        "total_xp": current_user.total_xp,
        "level": current_user.level,
        "streak": current_user.current_streak,
        "next_slug": next_slug(slug),
    })