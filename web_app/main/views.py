import os
from datetime import datetime, timezone

from flask import render_template, session, url_for, send_from_directory, request, current_app
from werkzeug.utils import redirect, secure_filename

from . import bp
from .forms import UserForm, LoginForm, PostForm
from .. import db, basic_auth
from ..models import User, Post


@bp.route('/')
@basic_auth.required
def index():
    user_info = {
        'name': session.get('name', 'Unknown'),
        'age': session.get('age', 0),
    }
    return render_template('index.html', user_info=user_info)


@bp.route('/user/')
def users():
    page = int(request.values.get('page', 1))
    users_paginator = User.query.paginate(
        page=page, per_page=current_app.config['PER_PAGE']
    )
    return render_template('users_paginated.html', users_paginator=users_paginator)


@bp.route('/user/add/', methods=['GET', 'POST'])
def user_add():
    form = UserForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('.users'))
    return render_template('user_create.html', form=form)


@bp.route('/user/<int:user_id>/')
def user_details(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user_details.html', user=user)


@bp.route('/post/<int:post_id>/')
def post_details(post_id):
    post = Post.query.get_or_404(post_id)
    now_with_tz = datetime.now(tz=timezone.utc)
    now_without_tz = datetime.now(tz=timezone.utc)
    return render_template('post_details.html', post=post,
                           now_with_tz=now_with_tz, now_without_tz=now_without_tz)


@bp.route('/post/add/', methods=['GET', 'POST'])
def post_add():
    form = PostForm()
    # form.author.choices = [(1, 'User1'), (2, 'User2')]
    form.author.choices = [(u.id, u.username) for u in User.query.all()]
    if form.validate_on_submit():
        new_post = Post(
            content=form.content.data,
            user_id=form.author.data,
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('.user_details', user_id=new_post.user_id))
    return render_template('post_create.html', form=form)


@bp.route('/download/')
def download():
    filename = session['filename']
    return send_from_directory(current_app.config['UPLOAD_FOLDER'],
                               filename, as_attachment=True)


@bp.route('/upload/', methods=['GET', 'POST'])
def upload():
    form = LoginForm()
    if form.validate_on_submit():
        file = form.input_data.data
        filename = secure_filename(file.filename)
        session['filename'] = filename
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('.index'))
    return render_template('upload.html', form=form)
