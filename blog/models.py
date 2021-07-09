from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship

from blog.app import db

article_tag_association_table = Table(
    'article_tag_association',
    db.metadata,
    db.Column('article_id', db.Integer, db.ForeignKey('articles.id'), nullable=False),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), nullable=False)
)


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

    def __repr__(self):
        return self.username


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='author')
    articles = relationship('Article', back_populates='author')

    def __repr__(self):
        return self.user.username


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, ForeignKey('authors.id'), nullable=False)
    title = db.Column(db.String(255))
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship('Author', back_populates='articles')
    tags = relationship('Tag', secondary=article_tag_association_table, back_populates='articles')

    def __init__(self, title, text, author):
        self.title = title
        self.text = text
        self.author = author

    def __repr__(self):
        return self.title


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    articles = relationship('Article', secondary=article_tag_association_table, back_populates='tags')

    def __repr__(self):
        return self.name
