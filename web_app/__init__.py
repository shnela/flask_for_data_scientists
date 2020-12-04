import os

from flask import Flask, render_template, session, url_for, send_from_directory
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from werkzeug.utils import redirect, secure_filename
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired, ValidationError

CURRENT_DIR = os.path.dirname(__file__)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = os.path.abspath(os.path.join(CURRENT_DIR, 'uploaded_data'))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(CURRENT_DIR, '..', 'test.db')}"

Bootstrap(app)
toolbar = DebugToolbarExtension(app)


class LoginForm(FlaskForm):
    input_data = FileField('Test data', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_input_data(self, field):
        data = field.data
        if not data or not data.filename.endswith('.csv'):
            raise ValidationError('Only csv files allowed')


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


@app.route('/download/')
def download():
    filename = session['filename']
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename, as_attachment=True)


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    # show diff between GET and POST
    form = LoginForm()
    if form.validate_on_submit():
        file = form.input_data.data
        filename = secure_filename(file.filename)
        session['filename'] = filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index'))
    return render_template('upload.html', form=form)


@app.route('/session_kv_storage/<key>/<int:val>/')
def session_kv_storage(key, val):
    from flask import session, redirect, url_for
    session[key] = val
    return redirect(url_for('.index'))
