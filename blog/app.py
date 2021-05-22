<< << << < Updated
upstream
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return 'This is a GET request'
    else:
        return 'This is a POST request'

== == == =
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()


def create_app() -> Flask:
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'mvg)aj&47rgeyh#jhtmg0s7#l-6t*u$m170prpok1(1l(5wyyg'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from blog.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    from blog.article.views import article
    from blog.auth.views import auth
    from blog.main.views import main
    from blog.user.views import user

    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(main)
    app.register_blueprint(auth)

>> >> >> > Stashed
changes
