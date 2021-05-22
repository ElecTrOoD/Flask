from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from werkzeug.exceptions import NotFound

from blog.app import db

user = Blueprint('user', __name__, static_folder='../static', url_prefix='/user')


@user.route('/')
def user_list():
    from blog.models import User

    users = User.query.all()

    return render_template(
        'users/user_list.html',
        users=users,
    )


@user.route('/<int:pk>')
@login_required
def profile(pk: int):
    from blog.models import User
    from blog.models import Article

    _user = User.query.filter_by(id=pk).one_or_none()
    _articles = Article.query.filter_by(author=pk)

    if not _user:
        raise NotFound(f"User #{pk} doesn't exist")
    return render_template(
        'users/profile.html',
        user=_user,
        articles=_articles
    )


@user.route('/delete_user/<int:pk>')
@login_required
def delete_user(pk: int):
    from blog.models import User

    _user = User.query.filter_by(id=pk).delete()
    db.session.commit()
    return redirect(url_for('user.user_list'))
