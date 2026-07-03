from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        display_name = request.form.get("display_name", "").strip() or "Coder"
        password = request.form.get("password", "")

        if not email or not password:
            flash("Email and password are required.", "error")
            return render_template("signup.html")

        if User.query.filter_by(email=email).first():
            flash("An account with that email already exists.", "error")
            return render_template("signup.html")

        user = User(email=email, display_name=display_name)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash(f"Welcome to PYGO, {user.display_name}! Let's start coding.", "success")
        return redirect(url_for("main.index"))

    return render_template("signup.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        user = User.query.filter_by(email=email).first()

        if user is None or not user.check_password(password):
            flash("Incorrect email or password.", "error")
            return render_template("login.html")

        login_user(user)
        flash(f"Welcome back, {user.display_name}! Let's start coding.", "success")
        next_url = request.args.get("next")
        return redirect(next_url or url_for("main.index"))

    return render_template("login.html")


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@auth_bp.route("/update-profile", methods=["POST"])
@login_required
def update_profile():
    display_name = request.form.get("display_name", "").strip()

    if not display_name:
        flash("Display name can't be empty.", "error")
        return redirect(request.referrer or url_for("main.index"))

    current_user.display_name = display_name
    db.session.commit()
    flash("Display name updated.", "success")
    return redirect(request.referrer or url_for("main.index"))


@auth_bp.route("/change-password", methods=["POST"])
@login_required
def change_password():
    current_password = request.form.get("current_password", "")
    new_password = request.form.get("new_password", "")
    confirm_password = request.form.get("confirm_password", "")

    if not current_user.check_password(current_password):
        flash("Current password is incorrect.", "error")
        return redirect(request.referrer or url_for("main.index"))

    if len(new_password) < 6:
        flash("New password must be at least 6 characters.", "error")
        return redirect(request.referrer or url_for("main.index"))

    if new_password != confirm_password:
        flash("New passwords don't match.", "error")
        return redirect(request.referrer or url_for("main.index"))

    current_user.set_password(new_password)
    db.session.commit()
    flash("Password updated.", "success")
    return redirect(request.referrer or url_for("main.index"))


@auth_bp.route("/delete-account", methods=["POST"])
@login_required
def delete_account():
    # Fetch a fresh, real model instance before logging out - the
    # current_user proxy becomes unusable once the session is cleared.
    user = db.session.get(User, current_user.id)

    logout_user()

    if user is not None:
        db.session.delete(user)  # cascades to delete all their Progress rows too
        db.session.commit()

    flash("Your account and all your progress have been permanently deleted.", "info")
    return redirect(url_for("main.index"))