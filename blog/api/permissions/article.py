from combojsonapi.permission import PermissionMixin, PermissionUser, PermissionForPatch
from flask_combo_jsonapi.exceptions import AccessDenied
from flask_login import current_user

from blog.models import Article


class ArticlePatchPermission(PermissionMixin):
    PATCH_AVAILABLE_FIELDS = (
        'title',
        'text',
    )

    def patch_permission(self, *args, user_permission: PermissionUser = None, **kwargs) -> PermissionForPatch:
        self.permission_for_patch.allow_columns = (self.PATCH_AVAILABLE_FIELDS, 10)
        return self.permission_for_patch

    def patch_data(self, *args, data=None, obj=None, user_permission: PermissionUser = None, **kwargs) -> dict:
        if not current_user.is_staff or current_user.id == obj.author_id:
            raise AccessDenied('No access')

        permission_for_patch = user_permission.permission_for_patch_permission(model=Article)
        return {
            k: v
            for k, v in data.items()
            if k in permission_for_patch.columns
        }
