"""Ref table Address-Product"""
from src.app import db

roles_users_table = db.Table(
    "roles_users",
    db.Column("users_id", db.Integer(), db.ForeignKey("users.id")),
    db.Column("roles_id", db.Integer(), db.ForeignKey("roles.id")),
)
