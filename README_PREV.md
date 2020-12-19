# `User` has written the `Post` - one to many

[README_PREV.md](./README_PREV.md)

## First let's look at moved templates
Now templates are inside blueprint.


## Look at our `User` and `Post` models in dBeaver
```
test.db -> Tables -> ER Diagram
```

And compare with [this](https://fmhelp.filemaker.com/help/18/fmp/en/index.html#page/FMP_Help/one-to-many-relationships.html)
explanation.

## One to many in `Flask-SQLAlchemy`

[One to many - Flask](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#one-to-many-relationships)

```python
class User:
    ...
    posts = db.relationship('Post', backref='user', lazy=True)

class Post:
    ...
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
```

We edited only `post` **database table** - we've added `user_id` column.  

### Test new model in flask shell
[how to run flask shell](INSTRUCTIONS_TO_COPY.md)

```
>>> from ml_runner.models import Post
>>> Post.query.first()
# doesn't work :(
>>> from ml_runner import db
>>> db.create_all()
>>> Post.query.first()
# did it help?
```

But we have to **delete** Post tables and recreate it again.
[Flask-sqlalchemy](https://flask-migrate.readthedocs.io/en/latest/) would help.

1. **Close flask shell - ctrl-D**
1. **Delete db file**

Then run in shell
```
>>> from ml_runner import db
>>> from ml_runner.models import Post
>>> db.create_all()
>>> Post.query.first()
# nice!
```

Generate some users and posts in `gen_fake_models.py`

```
>>> from ml_runner.models import User, Post
>>> u = User.query.first()
>>> p1 = Post.query.first()
>>> p2 = Post.query.offset(1).first()
>>> p1.user_id = u.id
>>> p2.user_id = u.id
>>> from ml_runner import db
>>> db.session.add(p1, p2)
>>> db.session.commit()

# pause for dBeaver

>>> u.posts
[<Post 1>, <Post 2>]
>>> p1.user
<User 'Debra'>
```

## Let's display Posts
Right now we can use `posts` variable as part of `User` model.

It's used in `web_app/main/templates/user_details.html`.

## Assignment
Before you start, update `auxiliary_code/gen_fake_models.py` with:
```python
create_users(20, posts_per_user=10)
```
and run.

### Make `web_app/main/views.py:post_details` works.
It requires:
* accessing `Post` from database
* new custom template
* base it on `user_details` endpoint
* Display:
  * `id`
  * Author - `user`
  * `content`
  * Link back `` go back link

### Implement `post_add` endpoint
* You'll require new `PostForm` with fields:
  * `content`: use [StringField wtf field][] with [TextArea wtf widget][]
  * `user_id`: use `author = SelectField('Author', choices=[(1, 'User1'), (2, 'User2')]...)`
* Saving `Post` to database
* Base it on `user_add`.

### Add nice breadcrumbs on top of page
* [Breadcrumbs from bootstrap](https://getbootstrap.com/docs/3.3/components/#breadcrumbs)
* Add it in html on top of every page:
  * `users`
  * `user_details`
  * `post_details`
* https://readingraphics.com/book-summary-dont-make-me-think/ -> Web Navigation


[StringField wtf field]: https://wtforms.readthedocs.io/en/2.3.x/fields/#wtforms.fields.StringField
[TextArea wtf widget]: https://wtforms.readthedocs.io/en/2.3.x/widgets/#wtforms.widgets.TextArea
