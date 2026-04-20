from extensions import db
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String


class Profile(db.Model):
    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True)

    # personal info
    birthday = db.Column(db.Date, nullable=True)
    gender = db.Column(db.String(20), nullable=True)

    # profile content
    bio = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(250), nullable=True)

    # metadata
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
