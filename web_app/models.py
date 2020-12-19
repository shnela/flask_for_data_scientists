from datetime import datetime, timezone

from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(), nullable=False)
    creation_date = db.Column(db.DateTime(timezone=True), nullable=False,
                              default=lambda: datetime.now(tz=timezone.utc))
