from flask import redirect, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import (
    RoleMixin,
    Security,
    SQLAlchemyUserDatastore,
    UserMixin,
    current_user,
)
from src.app import app, db

roles_users_table = db.Table(
    "roles_users",
    db.Column("users_id", db.Integer(), db.ForeignKey("users.id")),
    db.Column("roles_id", db.Integer(), db.ForeignKey("roles.id")),
)


class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(80))
    active = db.Column(db.Boolean())
    roles = db.relationship(
        "Roles", secondary=roles_users_table, backref=db.backref("user", lazy="dynamic")
    )

    def __str__(self):
        return self.email


class Roles(db.Model, RoleMixin):
    __tablename__ = "roles"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name


user_datastore = SQLAlchemyUserDatastore(db, Users, Roles)
security = Security(app, user_datastore)


# Instantiate Flask-Admin
admin = Admin(
    app, name="Admin Panel", base_template="my_master.html", template_mode="bootstrap3"
)


# Create a ModelView to add to our administrative interface
class UserModelView(ModelView):
    def is_accessible(self):
        return current_user.is_active and current_user.is_authenticated

    def _handle_view(self, name):
        if not self.is_accessible():
            return redirect(url_for("security.login"))

    column_list = ("email", "password", "roles", "active")


class RoleModelView(ModelView):
    column_list = ("name", "description")
