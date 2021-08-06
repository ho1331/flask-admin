"""Admin views classes"""
from flask import redirect, url_for
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user


class UserView(ModelView):
    """
    User view
    """

    def is_accessible(self):
        return current_user.is_active and current_user.is_authenticated

    def _handle_view(self, name):
        if not self.is_accessible():
            return redirect(url_for("security.login"))

    column_list = ("email", "password", "roles", "active")
    column_filters = ["email", "roles.name"]


class RoleView(ModelView):
    """
    Role view
    """

    column_list = ("name", "description")
    column_filters = ["name"]


class ProductView(ModelView):
    """
    Product view
    """

    column_list = ("name", "color", "weight", "price")
    column_filters = ["address", "name", "color", "weight", "price"]


class AddressView(ModelView):
    """
    Address view
    """

    column_list = ("country", "city", "street", "build")
    column_filters = ("country", "city", "street", "build")
