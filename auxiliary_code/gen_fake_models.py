from web_app import db, User
from faker import Faker

fake = Faker()


def create_users(users_number=10):
    pass


def delete_all():
    User.query.delete()
    db.session.commit()


if __name__ == '__main__':
    db.create_all()
    delete_all()
    print(User.query.count())
    create_users(100)
    print(User.query.count())
