from typing import Dict

import requests as requests
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from blog.extensions import db
from blog.forms.article import CreateArticleForm
from blog.models import Article, Author, Tag

article = Blueprint('article', __name__, static_folder='../static', url_prefix='/article')


@article.route('/', methods=['GET'])
def article_list():
    articles = Article.query.all()

    return render_template(
        'articles/list.html',
        articles_list=articles,
    )


@article.route('/list_rpc', methods=['GET'])
def article_list_rpc():
    articles: Dict = requests.get('http://127.0.0.1:5000/api/articles/event_get_list/').json()['data']
    return render_template(
        'articles/list.html',
        articles_list=articles,
    )


@article.route('/tag/<int:tag_id>', methods=['GET'])
def article_list_by_tag(tag_id: int):
    selected_tag = Tag.query.filter_by(id=tag_id).options(joinedload(Tag.articles)).one_or_none()
    articles = selected_tag.articles

    return render_template(
        'articles/list.html',
        articles_list=articles,
    )


@article.route('/<int:article_id>')
@login_required
def article_detail(article_id: int):
    selected_article = Article.query.filter_by(id=article_id).options(joinedload(Article.tags)).one_or_none()
    if not selected_article:
        raise NotFound(f'Article with id {article_id} not found.')

    return render_template(
        'articles/details.html',
        article=selected_article)


@article.route('/write', methods=['GET'])
@login_required
def create_article_form():
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]
    return render_template('articles/create.html', form=form)


@article.route('/write', methods=['POST'])
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]

    if form.validate_on_submit():
        if current_user.author:
            author = current_user.author
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)

        _article = Article(title=form.title.data.strip(), text=form.text.data, author=author)

        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                _article.tags.append(tag)

        db.session.add(_article)

        db.session.commit()
        return redirect(url_for('article.article_detail', article_id=_article.id))

    return render_template('articles/create.html', form=form)


@article.route('/delete/<int:pk>')
@login_required
def delete(pk: int):
    selected_article = Article.query.filter_by(id=pk).one_or_none()
    selected_article.tags.clear()
    if Article.query.filter_by(author_id=selected_article.author.id).count() == 1:
        Author.query.filter_by(id=selected_article.author_id).delete()
    Article.query.filter_by(id=pk).delete()
    db.session.commit()

    return redirect('/article')
