from starlette_admin.contrib.sqla import ModelView

from app.models import User


class UserView(ModelView):
    fields = ["id", "email", "first_name", "last_name", "is_active", "is_staff", "is_superuser", "joined_at"]
    exclude_fields_from_list = ["joined_at"]
    exclude_fields_from_create = ["joined_at"]
    exclude_fields_from_edit = ["joined_at"]
    export_fields = ["id", "email", "first_name", "last_name", "is_active", "joined_at"]
    export_types = ["csv", "excel", "pdf", "print"]

