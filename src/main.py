from flask import render_template

from src.app import admin, app, db
from src.models.address import Address
from src.models.product import Product
from src.models.role import Roles
from src.models.user import Users
from src.views.models_views import AddressView, ProductView, RoleView, UserView

# Add administrative views to Flask-Admin
admin.add_view(UserView(Users, db.session))
admin.add_view(RoleView(Roles, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(AddressView(Address, db.session))


# Define the index route
@app.route("/")
def index():
    return render_template("index.html")
