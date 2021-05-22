from random import choice, randint

from lorem_text import lorem

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
