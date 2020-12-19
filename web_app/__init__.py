import os

from flask import Flask
from flask_basicauth import BasicAuth
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from .config import Config

CURRENT_DIR = os.path.dirname(__file__)

app = Flask(__name__)
app.config.from_object(Config)

Bootstrap(app)
Moment(app)
toolbar = DebugToolbarExtension(app)
db = SQLAlchemy(app)
basic_auth = BasicAuth(app)

# blueprints registration
from .main import bp as main_bp
app.register_blueprint(main_bp)
