from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from werkzeug.exceptions import NotFound

from blog.extensions import db
from blog.models import User, Article

user = Blueprint('user', __name__, url_prefix='/user', static_folder='../static')


@user.route('/')
def user_list():
    users = User.query.all()

    return render_template(
        'users/user_list.html',
        users=users,
    )


@user.route('/<int:pk>')
@login_required
def profile(pk: int):
    selected_user = User.query.filter_by(id=pk).one_or_none()
    user_articles = Article.query.filter_by(author=pk)

    if not selected_user:
        raise NotFound(f"User #{pk} doesn't exist")
    return render_template(
        'users/profile.html',
        user=selected_user,
        articles=user_articles
    )


@user.route('/delete_user/<int:pk>')
@login_required
def delete_user(pk: int):
    User.query.filter_by(id=pk).delete()
    db.session.commit()
    return redirect(url_for('user.user_list'))
