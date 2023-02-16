from flask_login import UserMixin
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash

from blog.extensions import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    is_staff = db.Column(db.Boolean, default=False)

    def __init__(self, email, first_name, last_name, password, is_staff):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.is_staff = is_staff

    def check_password_hash(self, password: str) -> bool:
        return check_password_hash(self.password, password)

# class Article(db.Model):
#     __tablename__ = 'articles'
#
#     title = db.Column(db.String(255))
#     text = db.Column(db.String)
#     author = relationship('User')
