from flask import Flask
from app.models import db
from app.views import entry, user
from flask_migrate import Migrate


def create_app(config_file):
    app = Flask(__name__)
    app.config.from_object(config_file)

    db.init_app(app)

    migrate = Migrate()
    migrate.init_app(app, db)

    app.register_blueprint(entry.app)
    app.register_blueprint(user.app)

    return app
