from flask import Flask

from blog import commands
from blog.extensions import db, login_manager, migrate, csrf, admin
from blog.models import User


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.config')

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)
    admin.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    from blog.views.users import user
    from blog.views.articles import article
    from blog.views.main import main
    from blog.views.auth import auth
    from blog.views.authors import author
    from blog.views import admin

    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(author)
    admin.register_views()


def register_commands(app: Flask):
    app.cli.add_command(commands.drop_db)
    app.cli.add_command(commands.create_users)
    app.cli.add_command(commands.create_articles)
