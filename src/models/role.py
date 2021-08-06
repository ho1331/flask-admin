"""Role model"""
from flask_security import RoleMixin
from src.app import db
from src.models.base import BaseModel


class Roles(db.Model, RoleMixin, BaseModel):
    __tablename__ = "roles"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name
