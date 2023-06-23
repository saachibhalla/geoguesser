from os import environ, path
from distutils.util import strtobool

app_dir = path.abspath(path.dirname(__file__))

class Config:
    FLASK_ENV = environ.get('FLASK_ENV')
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODICATIONS = False

class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(app_dir, 'data', environ.get('DEV_DB_NAME'))

class Testing(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = environ.get('TEST_DB_URI')

class Production(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = environ.get('PROD_DB_URI')