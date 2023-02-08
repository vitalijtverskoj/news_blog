from flask_login import UserMixin
from sqlalchemy.orm import relationship

from blog.extensions import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    is_staff = db.Column(db.Boolean, default=False)

    def __init__(self, email, name, password, is_staff):
        self.email = email
        self.password = password
        self.name = name
        self.is_staff = is_staff


# class Article(db.Model):
#     __tablename__ = 'articles'
#
#     title = db.Column(db.String(255))
#     text = db.Column(db.String)
#     author = relationship('User')
