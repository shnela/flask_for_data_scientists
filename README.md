# Flask-Moment

[README_PREV.md](./README_PREV.md)

[Flask-Moment docs](https://github.com/miguelgrinberg/flask-moment/)

[Moment.js docs](https://momentjs.com/)


## Fix
```
default=datetime.utcnow
```
is better than
```
default=lambda: datetime.now(tz=timezone.utc))
```