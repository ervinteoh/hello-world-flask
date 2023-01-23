import os
from abc import ABC, abstractmethod

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
WORKING_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))


class BaseConfig(ABC):

    # pylint: disable=too-few-public-methods, invalid-name

    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
    STATIC_FOLDER = "static"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_FOLDER = "templates"

    @property
    @abstractmethod
    def DATABASE_URI(self):
        pass

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        database_url = os.environ.get("DATABASE_URL")
        return database_url or f"sqlite:///{self.DATABASE_URI}"


class DebugConfig(BaseConfig):

    DATABASE_URI = os.path.join(WORKING_DIR, "development.sqlite")


class TestingConfig(BaseConfig):

    DATABASE_URI = ":memory:"
    TESTING = True


class ReleaseConfig(BaseConfig):

    DATABASE_URI = os.path.join(WORKING_DIR, "production.sqlite")


def get_config():
    if os.environ.get("FLASK_TESTING"):
        return TestingConfig()
    if os.environ.get("FLASK_DEBUG"):
        return DebugConfig()
    return ReleaseConfig()
