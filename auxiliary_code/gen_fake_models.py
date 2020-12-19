from faker import Faker

from web_app import db
from web_app.models import User, Post

fake = Faker()


def create_users(users_number=10):
    for _ in range(users_number):
        u = User(username=fake.unique.first_name())
        db.session.add(u)
        db.session.commit()


def delete_all():
    User.query.delete()
    Post.query.delete()
    db.session.commit()


def create_posts(n=10):
    for _ in range(n):
        p = Post(content=fake.unique.text())
        db.session.add(p)
    db.session.commit()


if __name__ == '__main__':
    db.create_all()
    delete_all()
    create_users(100)
    create_posts(100)
