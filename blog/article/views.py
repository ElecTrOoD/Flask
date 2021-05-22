from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from werkzeug.exceptions import NotFound

from blog.app import db
from blog.models import Article, User

article = Blueprint('article', __name__, static_folder='../static', url_prefix='/article')


@article.route('/')
def article_list():
    articles = Article.query.all()

    return render_template(
        'articles/articles_list.html',
        articles_list=articles,
    )


@article.route('/<int:pk>')
@login_required
def get_article(pk: int):
    _article = Article.query.filter_by(id=pk).one_or_none()

    if not _article:
        raise NotFound(f'Article with id {pk} not found.')

    user = User.query.filter_by(id=_article.author).one_or_none()
    return render_template(
        'articles/details.html',
        article=_article,
        username=user.username)


@article.route('/write', methods=['POST', 'GET'])
@login_required
def new_article():
    if request.method == 'GET':
        return render_template('articles/write_new.html')

    user = current_user.id
    title = request.form.get('title')
    text = request.form.get('text')

    db.session.add(
        Article(
            title=title,
            text=text,
            author=user))
    db.session.commit()
    return redirect('/article')


@article.route('/delete/<int:pk>')
@login_required
def delete(pk: int):
    Article.query.filter_by(id=pk).delete()
    db.session.commit()
    return redirect('/article')
