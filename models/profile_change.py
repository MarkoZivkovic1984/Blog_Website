from extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text
from datetime import datetime


class ProfileChangeLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # THIS is required

    user_id = db.Column(db.Integer, nullable=False)
    field = db.Column(db.String(50))
    old_value = db.Column(db.Text)
    new_value = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.now)