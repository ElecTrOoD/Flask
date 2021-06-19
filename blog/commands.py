import click
from werkzeug.security import generate_password_hash
from blog.extensions import db


@click.command('create-users')
def create_users():
    from blog.models import User
    from blog.extensions import get_random_user, users_count
    from wsgi import app

    with app.app_context():
        for i in range(1, users_count + 1):
            data_1 = get_random_user()
            db.session.add(
                User(username=data_1,
                     email=f'test{i}@test.test',
                     password=generate_password_hash(f'test{i}')))
            db.session.commit()


@click.command('create-articles')
def create_articles():
    from blog.models import Article
    from wsgi import app
    from blog.extensions import article_count, get_random_article

    with app.app_context():
        for i in range(1, article_count + 1):
            data_1, data_2, data_3 = get_random_article()
            db.session.add(
                Article(title=data_1,
                        text=data_2,
                        author=data_3
                        ))
            db.session.commit()


@click.command('drop-db')
def drop_db():
    from wsgi import app

    db.drop_all(app=app)
