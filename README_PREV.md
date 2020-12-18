# Cleanup
[README_PREV.md](./README_PREV.md)

## Separate config file

[Load config from object][]

* Save config values in `Config` object in `__init__.py`

```python
class Config:
    SECRET_KEY = ...

...
app.config.from_object(Config)
```

* Move config object to new `config.py` file

## Move models out of `__init__.py`

* Move `User` class to newly created `models.py`
* Import `db` in models
* Fix imports of `User` class - `gen_fake_models`

## Views and forms to separate files

* Move forms to `forms.py` and views to `views.py`
* Import missing `app` and `LoginForm` in `views.py`
* import `views` in __init__.py - decorators have to register methods

[Load config from object]: https://flask.palletsprojects.com/en/1.1.x/api/#flask.Config.from_object
