import os

from flask import Flask, render_template, session, url_for, send_from_directory, request, current_app
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from werkzeug.exceptions import abort
from werkzeug.utils import redirect, secure_filename
from wtforms import SubmitField, FileField, StringField
from wtforms.validators import DataRequired, ValidationError

CURRENT_DIR = os.path.dirname(__file__)

app = Flask(__name__)
app.config['PER_PAGE'] = 10
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = os.path.abspath(os.path.join(CURRENT_DIR, 'uploaded_data'))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(CURRENT_DIR, '..', 'test.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Bootstrap(app)
toolbar = DebugToolbarExtension(app)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)


class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Submit')


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


@app.route('/user/')
def users():
    page = int(request.values.get('page', 1))
    users_paginator = User.query.paginate(
        page=page, per_page=current_app.config['PER_PAGE']
    )
    return render_template('users_paginated.html', users_paginator=users_paginator)


@app.route('/user/add/', methods=['GET', 'POST'])
def user_add():
    form = UserForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users'))
    return render_template('user_create.html', form=form)


@app.route('/user/<int:user_id>/')
def user_details(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user_details.html', user=user)


@app.route('/download/')
def download():
    filename = session['filename']
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename, as_attachment=True)


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    form = LoginForm()
    if form.validate_on_submit():
        file = form.input_data.data
        filename = secure_filename(file.filename)
        session['filename'] = filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index'))
    return render_template('upload.html', form=form)


@app.route('/return_error/<int:response_code>/')
def return_response_with_code(response_code):
    return f'Return {response_code}', response_code


@app.route('/abort_error/<int:response_code>/')
def abort_response_with_code(response_code):
    abort(response_code)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500
