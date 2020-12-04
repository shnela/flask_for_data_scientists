# Flask-SQLAlchemy
[README_PREVIOUS.md](./README_PREVIOUS.md)

## New requirements
[Flask-SQLAlchemy][] is `Flask` wrapper for [SQLAlchemy][]


## Create user model
* According to [A Minimal Application] requirements
* Use `id` and `username` fields only
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
```

### Database configuration
* [Available databases][]
* We'll use sqlite for now
* we store database in project catalog `f"sqlite:///{os.path.join(CURRENT_DIR, '..', 'test.db')}"`

## flask shell
In Cygwin or Ubuntu
```
# install all missing requirements if neccessary
pip install -r requirements.txt

# Maybe 3rd party system packages may be required
$ sudo apt-get install python3-dev

# run flask shell
FLASK_APP='main.py' SECRET_KEY='123' flask shell
```

## Creation of model
To create models in database
```
db.create_all()
```
must be called.

### In flask shell:
```python
# import user model
from web_app import User

# try to query elements
User.query.all()

# wrong, look at database in DBeaver
# then initialize models
from web_app import db
db.create_all()

# look at database in DBeaver
User.query.all()

# new user
u = User(username='Joe')
db.session.add(u)
db.session.commit()

# query all users
User.query.all()

# get first user
User.query.first()

# filter
User.query.filter_by(username='Joe')
User.query.filter_by(username='Mark')

# when queryset is empty first returns None
User.query.filter_by(username='Mark').first()

# delete
User.query.filter_by(username='Joe').delete()
```

## Faker - generate random users

Generate randomized users with [Faker][].

* create `create_user` with const name in `gen_fake_models.py`.
* Use `fake.unique.first_name()` to generate new `Users`.


[Flask-SQLAlchemy]: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
[SQLAlchemy]: https://www.sqlalchemy.org/
[A Minimal Application]: https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application
[Available databases]: https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format
[Faker]: https://pypi.org/project/Faker/
