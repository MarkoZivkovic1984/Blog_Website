from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_gravatar import Gravatar
from sqlalchemy.orm import DeclarativeBase


# Base class for models
class Base(DeclarativeBase):
    pass


# Extensions (no app yet)
db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()
gravatar = Gravatar(size=100, rating='g', default='retro')

