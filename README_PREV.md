# Flask-SQLAlchemy
[README_PREVIOUS.md](./README_PREVIOUS.md)

## New views
* `users`
* `user_details`
* `add_user`

## Link to `user_details`

 Link to `user_details` from `users.html` using
 ```html
<a href="{{ url_for('user_details', user_id=user.id) }}">{{ user.id }}</a>
```

## Display some info in `user_details.html`
Right now it's only static html `<h1>User info here</h1>`.  
Display `user.id` and `user.username`.

## Assignments
### Create new User view
* Update `UserForm` with `username = StringField...` and `submit` fields.
* and use it in `user_add` view
* you'll have to create new html template analogical to `upload.html`

### Paginate Users
[Flask - paginate][]

Add `PER_PAGE` paramter to app config.  
Replace `users` view content with:
```python
    page = int(request.values.get('page', 1))
    users_paginator = User.query.paginate(
        page=page, per_page=current_app.config['PER_PAGE']
    )
    return render_template('users_paginated.html', users_paginator=users_paginator)
```
In `users_paginated.html` iterate over `users_paginator.items` instead of `users`.

[Flask - paginate]: https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.BaseQuery.paginate
