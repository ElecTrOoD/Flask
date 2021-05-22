<< << << < Updated
upstream
from blog.app import app

if __name__ == '__main__':
    app.run(
        host='localhost',
        use_debugger=True
    )
== == == =
from werkzeug.security import generate_password_hash

from blog.app import create_app, db

app = create_app()


@app.cli.command('init-db')
def init_db():
    db.create_all()


@app.cli.command('create-users')
def create_users():
    from blog.models import User
    from random_data import get_random_user, users_count

    db.session.add(
        User(username='admin',
             email=f'admin@admin.com',
             password=generate_password_hash(f'admin'),
             is_staff=True))
    db.session.commit()

    for i in range(1, users_count + 1):
        data_1 = get_random_user()
        db.session.add(
            User(username=data_1,
                 email=f'test{i}@test.test',
                 password=generate_password_hash(f'test{i}')))
        db.session.commit()


@app.cli.command('create-articles')
def create_articles():
    from blog.models import Article
    from random_data import get_random_article, article_count

    for i in range(1, article_count + 1):
        data_1, data_2, data_3 = get_random_article()
        db.session.add(
            Article(title=data_1,
                    text=data_2,
                    author=data_3
                    ))
        db.session.commit()


@app.cli.command('drop-db')
def recreate_db():
    db.drop_all()

>> >> >> > Stashed
changes
