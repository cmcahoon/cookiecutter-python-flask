from os import environ


class Config:
    # Flask configuration
    DEBUG = environ.get('DEBUG')
    FLASK_ENV = environ.get('FLASK_ENV')
    SECRET_KEY = environ.get('SECRET_KEY')

    # SQLAlchemy configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')

    # Application configuration
