from flask import Flask
from core.modules.theater import register_theater_route

def create_app(config_object):
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    _register_config(app, config_object)
    _register_extensions(app)
    _register_routes(app)
    _register_views(app)

    return app


def _register_config(app: Flask, config_object):
    app.config.from_object(config_object)


def _register_routes(app: Flask):
    from .extensions import api
    register_theater_route(api, app)


def _register_extensions(app: Flask):
    from .extensions import db, api, migrate
    from core.modules.theater.models import Theater, Section, Seat
    
    api.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

def _register_views(app: Flask):
    @app.route('/')
    def index():
        return ''
