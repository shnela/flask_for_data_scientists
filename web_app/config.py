import os

CURRENT_DIR = os.path.dirname(__file__)


class Config:
    PER_PAGE = 10
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOAD_FOLDER = os.path.abspath(os.path.join(CURRENT_DIR, 'uploaded_data'))
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(CURRENT_DIR, '..', 'test.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
