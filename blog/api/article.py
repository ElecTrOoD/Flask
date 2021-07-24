from combojsonapi.event.resource import EventsResource
from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.api.permissions.article import ArticlePatchPermission
from blog.extensions import db
from blog.models import Article
from blog.schemas import ArticleSchema


class ArticleListEvent(EventsResource):

    def event_get_list(self, *args, **kwargs):
        data = []
        for article in Article.query.all():
            data.append({'id': article.id, 'title': article.title})
        return {'data': data}

    def event_get_count(self, *args, **kwargs):
        return {'count': Article.query.count()}



class ArticleDetailEvent(EventsResource):

    def event_get_count_by_author(self, **kwargs):
        return {'count': Article.query.filter(Article.author_id == kwargs['id']).count()}


class ArticleList(ResourceList):
    events = ArticleListEvent
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }


class ArticleDetail(ResourceDetail):
    events = ArticleDetailEvent
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
        'permission_patch': [ArticlePatchPermission],
    }
