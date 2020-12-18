import os

from flask import render_template, session, url_for, send_from_directory, request, current_app
from werkzeug.utils import redirect, secure_filename

from . import app, db
from .forms import UserForm, LoginForm
from .models import User


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


@app.route('/user/<int:user_id>')
def user_details(user_id):
    user = User.query.get(user_id)
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
