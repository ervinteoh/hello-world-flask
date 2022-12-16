import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
WORKING_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))


class AppConfig:

    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
    STATIC_FOLDER = "static"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_FOLDER = "templates"
    DATABASE_URI = os.path.join(WORKING_DIR, "database.sqlite")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", f"sqlite:///{DATABASE_URI}")
