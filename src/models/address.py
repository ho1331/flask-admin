"""Address model"""

from sqlalchemy.orm import validates
from src.app import db
from src.models.base import BaseModel


class Address(db.Model, BaseModel):
    """
    class Address
    """

    __tablename__ = "addresses"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    country = db.Column(db.String(30), unique=False, nullable=False)
    city = db.Column(db.String(30), unique=False, nullable=False)
    street = db.Column(db.String(30), unique=False, nullable=False)
    build = db.Column(db.Integer, unique=False, nullable=False)

    @validates("build")
    def validate_weight(self, key, field):
        """
        Check build number input
        """
        if 0 < field:
            return field
        else:
            raise AssertionError("field 'build should be > 0")
