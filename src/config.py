"""app conf"""
from os import getenv


class Config:
    """
    class Config
    """

    # WEB
    DEBUG = True
    TESTING = True

    # SQLAlchemy
    DB_HOST = getenv("DB_HOST")
    DB_USER = getenv("DB_USER")
    DB_PASSWORD = getenv("DB_PASSWORD")
    SECRET_KEY = getenv("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432"
    )
    # Configure a specific Bootswatch theme
    FLASK_ADMIN_SWATCH = "sandstone"

    SECURITY_PASSWORD_SALT = "none"
    # Configure application to route to the Flask-Admin index view upon login
    SECURITY_POST_LOGIN_VIEW = "/admin/"
    # Configure application to route to the Flask-Admin index view upon logout
    SECURITY_POST_LOGOUT_VIEW = "/admin/"
    # Configure application to route to the Flask-Admin index view upon registering
    SECURITY_POST_REGISTER_VIEW = "/admin/"
    SECURITY_REGISTERABLE = True
    # Configure application to not send an email upon registration
    SECURITY_SEND_REGISTER_EMAIL = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
