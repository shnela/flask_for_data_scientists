import os

from flask import Flask, render_template, session, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired, regexp as regexp_validator

CURRENT_DIR = os.path.dirname(__file__)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = os.path.abspath(os.path.join(CURRENT_DIR, 'uploaded_data'))  # folder must exist
Bootstrap(app)


class LoginForm(FlaskForm):
    input_data = FileField('Test data', validators=[DataRequired(),
                                                    regexp_validator(u'^.*.csv', message='Only csf files allowed')])
    submit = SubmitField('Submit')


@app.route('/')
def index():
    user_info = {
        'name': session.get('name', 'Unknown'),
        'age': session.get('age', 0),
    }
    return render_template('index.html', user_info=user_info)


@app.route('/user/<username>/<int:amount>/')
def profile(username, amount):
    return render_template('profile.html', username=username, amount=amount)


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    # show diff between GET and POST
    form = LoginForm()
    if form.validate_on_submit():
        # request.files is empty...
        return redirect(url_for('index'))
    return render_template('upload.html', form=form)
