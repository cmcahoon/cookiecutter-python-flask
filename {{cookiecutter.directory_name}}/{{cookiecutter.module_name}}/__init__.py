from flask import Flask
from flask_migrate import Migrate


def create_app():
    # Create the application
    app = Flask(__name__, instance_relative_config=True)

    # Load settings
    app.config.from_object('{{cookiecutter.module_name}}.config.Config')

    # Initialize database context
    from .db import db
    db.init_app(app)

    # Initialize input validation
    from .marshmallow import ma
    ma.init_app(app)

    # Intialize database migration system
    migrate = Migrate(app, db)

    # Register blueprints
    from . import health, user
    app.register_blueprint(health.bp)
    app.register_blueprint(user.bp)

    return app
