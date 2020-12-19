# Connecting to MSSQL

[README_PREV.md](./README_PREV.md)

## Test MSSQL connection

### Connect using dBeaver to MSSQL
Credentials will be sent on zoom.

## How to connect to other database in Flask?

###[Flask - Connection URI Format][] review.
So we're going to replace
```
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(current_dir, '..', 'test.db')}"
```
with something, right?

### Flask-SQLAlchemy is only SQLAlchemy wrapper
[Microsoft SQL Server options in SQLAlchemy][]

We'll use [PyODBC][]

Connection string will look like:
```
mssql+pyodbc://<username>:<password>@<dsnname>?driver=SQL+Server+Client+Name
```
`pyodbc` is installed with `pip` and is already added to `requirements.txt`.

### PyODBC requires ODBC Driver
Download one for windows [ODBC Driver 17 for SQL Server®][]

## Update application run configuration
Add new environment variable: `SQLALCHEMY_DATABASE_URI`.

Update both:
* run configuration
* gen_fake_models configuration

Value of `SQLALCHEMY_DATABASE_URI` is sent by zoom

## Test new database
1. Run `auxiliary_code/gen_fake_models.py`
1. Run application

[Flask - Connection URI Format]: https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format
[Microsoft SQL Server options in SQLAlchemy]: https://docs.sqlalchemy.org/en/14/dialects/mssql.html
[PyODBC]: https://docs.sqlalchemy.org/en/14/dialects/mssql.html
[ODBC Driver 17 for SQL Server®]: https://www.microsoft.com/en-us/download/details.aspx?id=56567
