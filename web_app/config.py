import os

CURRENT_DIR = os.path.dirname(__file__)


class Config:
    PER_PAGE = 10
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOAD_FOLDER = os.path.abspath(os.path.join(CURRENT_DIR, 'uploaded_data'))

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-BasicAuth
    BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME')
    BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD')
    BASIC_AUTH_FORCE = True
