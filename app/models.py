from datetime import datetime, timezone, timedelta
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    display_name = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    current_streak = db.Column(db.Integer, default=0, nullable=False)
    last_active_date = db.Column(db.Date, nullable=True)
    avatar = db.Column(db.String(20), default="fox", nullable=False)

    progress = db.relationship("Progress", backref="user", lazy=True, cascade="all, delete-orphan")

    def set_password(self, raw_password):
        self.password_hash = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        return check_password_hash(self.password_hash, raw_password)

    def record_activity(self):
        today = datetime.now(timezone.utc).date()
        if self.last_active_date == today:
            return
        if self.last_active_date == today - timedelta(days=1):
            self.current_streak += 1
        else:
            self.current_streak = 1
        self.last_active_date = today

    @property
    def total_xp(self):
        return sum(p.xp_earned for p in self.progress)

    @property
    def level(self):
        # One level per completed lesson, floored at 1 so a brand-new
        # user still sees "LV 1" instead of "LV 0" before finishing anything.
        return max(1, len(self.progress))

    @property
    def completed_slugs(self):
        return {p.lesson_slug for p in self.progress}


class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    lesson_slug = db.Column(db.String(120), nullable=False)
    xp_earned = db.Column(db.Integer, default=0)
    completed_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    __table_args__ = (db.UniqueConstraint("user_id", "lesson_slug", name="uq_user_lesson"),)
