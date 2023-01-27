from flask_login import UserMixin
from sqlalchemy.orm import relationship

from blog.extensions import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, email, password):
        self.email = email
        self.password = password


# class Article(db.Model):
#     __tablename__ = 'articles'
#
#     title = db.Column(db.String(255))
#     text = db.Column(db.String)
#     author = relationship('User')
