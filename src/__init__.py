from flask import Flask

from src import extensions, models, settings
from src.views import public


def create_app() -> Flask:
    app = Flask(__name__)
    config = settings.get_config()
    app.config.from_object(config)
    app.url_map.strict_slashes = False

    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app: Flask):
    extensions.db.init_app(app)
    extensions.migrate.init_app(app, extensions.db)


def register_blueprints(app: Flask):
    app.register_blueprint(public.blueprint)


def register_shellcontext(app: Flask):
    shell_context = {
        "db": extensions.db,
        "User": models.User,
    }

    app.shell_context_processor(lambda: shell_context)
