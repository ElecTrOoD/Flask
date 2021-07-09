from flask import url_for
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from werkzeug.utils import redirect


def register_views():
    from blog import models
    from blog.extensions import admin, db

    admin.add_view(UserAdminView(models.User, db.session, category='Models', endpoint='user_admin'))
    admin.add_view(AuthorAdminView(models.Author, db.session, category='Models', endpoint='author_admin'))
    admin.add_view(ArticleAdminView(models.Article, db.session, category='Models', endpoint='article_admin'))
    admin.add_view(TagAdminView(models.Tag, db.session, category='Models', endpoint='tag_admin'))


class CustomAdminView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_staff

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))


class CustomAdminIndexView(AdminIndexView):

    @expose()
    def index(self):
        if not (current_user.is_authenticated and current_user.is_staff):
            return redirect(url_for('auth.login'))
        return super().index()


class UserAdminView(CustomAdminView):
    column_exclude_list = ('password',)
    column_details_exclude_list = ('password',)
    column_export_exclude_list = ('password',)
    column_searchable_list = ('username', 'first_name', 'last_name', 'email')
    form_columns = ('username', 'first_name', 'last_name', 'email', 'is_staff')
    column_editable_list = ('username', 'first_name', 'last_name', 'email', 'is_staff')


class AuthorAdminView(CustomAdminView):
    column_searchable_list = ('user.username',)
    create_modal = True
    edit_modal = True


class ArticleAdminView(CustomAdminView):
    can_export = True
    export_types = ('csv', 'xlsx')
    column_filters = ('author_id',)


class TagAdminView(CustomAdminView):
    column_searchable_list = ('name',)
    create_modal = True
    edit_modal = True
