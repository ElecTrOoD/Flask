import re
from random import choice, randint
from string import digits, punctuation

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from lorem_text import lorem

login_manager = LoginManager()
db = SQLAlchemy()

NAMES = ['Mike', 'Alice', 'John', 'Kevin', 'Andrew', 'Douglas', 'Gordon', 'Brad', 'Ethan', 'Jacob']
SURNAMES = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Wright', 'Baker']
WORDS = 400

users_count = 5
article_count = users_count * 4


def get_random_user():
    name = f'{choice(NAMES)} {choice(SURNAMES)}'
    return name


def get_random_article():
    title = lorem.words(randint(3, 8))
    text = lorem.words(WORDS)
    author = randint(2, users_count + 1)
    return title, text, author


def validate_data(name, email, password):
    if (not len(set(digits + punctuation + '@').intersection(name)) > 0 and len(name) < 255) and \
            re.findall(r'"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)"?', email) and \
            6 < len(password) <= 24:
        return True
    else:
        return False
