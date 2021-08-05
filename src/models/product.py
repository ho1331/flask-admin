"""Product model"""

from sqlalchemy.orm import validates
from src.app import db
from src.models.adress_product import ProductAdress
from src.models.base import BaseModel


class Product(db.Model, BaseModel):
    """
    class Product
    """

    __tablename__ = "products"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    color = db.Column(db.String(30), unique=False, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    address = db.relationship(
        "Address", secondary=ProductAdress, backref="product_address"
    )

    @validates("weight")
    def validate_weight(self, key, field):
        """
        Check weight input
        """
        if 0 < field:
            return field
        else:
            raise AssertionError("field 'weight should be > 0")

    @validates("price")
    def validate_price(self, key, field):
        """
        Check price input
        """
        if 0 <= field:
            return field
        else:
            raise AssertionError("field 'price should be >= 0")
