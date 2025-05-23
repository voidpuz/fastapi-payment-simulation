from starlette_admin.contrib.sqla import Admin, ModelView

from app.admin.views import UserView
from app.database import engine
from app.models import Merchant, Payment, Transaction, Card, User
from app.admin.auth import JSONAuthProvider


admin = Admin(
    engine,
    title="Fast Admin",
    auth_provider=JSONAuthProvider(login_path="/login", logout_path="/logout"),
)


admin.add_view(UserView(User, icon="fa fa-user"))
admin.add_view(ModelView(Payment, engine))
admin.add_view(ModelView(Merchant, engine))
admin.add_view(ModelView(Transaction, engine))
admin.add_view(ModelView(Card, engine))
