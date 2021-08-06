"""Ref table Address-Product"""
from src.app import db

ProductAdress = db.Table(
    "ProductAdress",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("product_id", db.Integer, db.ForeignKey("products.id")),
    db.Column("address_id", db.Integer, db.ForeignKey("addresses.id")),
)
