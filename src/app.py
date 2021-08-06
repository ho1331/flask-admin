"""basic app params"""
from flask import Flask, url_for
from flask_admin import Admin
from flask_admin import helpers as admin_helpers
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from src.config import Config
from src.models.role import Roles
from src.models.user import Users


def create_app():
    """
    create app params
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    Migrate(app, db, directory="src/models/migrations")
    return app


app = create_app()
login_manager = LoginManager(app)

# create users datastore
user_datastore = SQLAlchemyUserDatastore(db, Users, Roles)
security = Security(app, user_datastore)


# Instantiate Flask-Admin
admin = Admin(
    app, name="Admin Panel", base_template="my_master.html", template_mode="bootstrap3"
)


@app.before_first_request
def create_user():
    db.drop_all()
    db.create_all()
    user_datastore.create_user(email="admin", password="admin")
    db.session.commit()


# Add the context processor
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        get_url=url_for,
        h=admin_helpers,
    )
