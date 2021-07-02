from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from blog.app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    is_staff = db.Column(db.Boolean, nullable=False, default=False)

    author = relationship('Author', uselist=False, back_populates='user')

    def __init__(self, username, first_name, last_name, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='author')
    article = relationship('Article', back_populates='author')


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, ForeignKey('authors.id'), nullable=False)
    title = db.Column(db.String(255))
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship('Author', back_populates='article')

    def __init__(self, title, text, author):
        self.title = title
        self.text = text
        self.author = author
