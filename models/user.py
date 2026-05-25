from extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from flask_login import UserMixin
from flask_gravatar import Gravatar
from flask import url_for

gravatar = Gravatar()


class UserTable(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))
    # This will act like a List of BlogPost objects attached to each User.
    # The "author" refers to the author property in the BlogPost class.
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("CommentPost", back_populates="comment_author")
    profile = relationship("Profile", backref="user", uselist=False)

    @property
    def avatar(self):
        url = self.profile.image_url if self.profile else None

        # fallback
        if not url:
            return gravatar(self.email)

        # external URL
        if url.startswith(("http://", "https://")):
            return url

        # local static file
        return url_for("static", filename=url)