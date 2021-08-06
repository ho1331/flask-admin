"""User model"""
from flask_security import UserMixin
from src.app import db
from src.models.base import BaseModel
from src.models.user_role import roles_users_table


class Users(db.Model, UserMixin, BaseModel):
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
