from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from werkzeug.exceptions import NotFound

from blog.extensions import db
from blog.forms.article import ArticleWriteForm
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
    selected_article = Article.query.filter_by(id=pk).one_or_none()
    if not selected_article:
        raise NotFound(f'Article with id {pk} not found.')

    author = User.query.filter_by(id=selected_article.author).one_or_none()
    if not author:
        raise NotFound(f'User with id {selected_article.author} not found.')

    return render_template(
        'articles/details.html',
        article=selected_article,
        username=author.username)


@article.route('/write', methods=['GET'])
@login_required
def new_article():
    form = ArticleWriteForm()
    return render_template('articles/write_new.html', form=form)


@article.route('/write', methods=['POST'])
@login_required
def new_article_post():
    form = ArticleWriteForm(request.form)
    db.session.add(
        Article(
            title=form.title.data,
            text=form.text.data,
            author=current_user.id
        ))
    db.session.commit()

    return redirect('/article')


@article.route('/delete/<int:pk>')
@login_required
def delete(pk: int):
    Article.query.filter_by(id=pk).delete()
    db.session.commit()

    return redirect('/article')
