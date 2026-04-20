from extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from flask_login import UserMixin
from flask_gravatar import Gravatar

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
        if self.profile and self.profile.image_url:
            return self.profile.image_url

        # fallback to gravatar
        return gravatar(self.email)
