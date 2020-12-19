# REST API - user authentication

[README_PREVIOUS.md](./README_PREVIOUS.md)

[Flask-BasicAuth](https://flask-basicauth.readthedocs.io/en/latest/)

## Add new env variables to configuration
* BASIC_AUTH_USERNAME=user
* BASIC_AUTH_PASSWORD=pass

**Remember that those data should be keep secret on production**

### In config
```
BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME')
BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD')
BASIC_AUTH_FORCE = True
```

### You may want to protect only part of views:
Disable `BASIC_AUTH_FORCE = True` in `Config`

And decorate protected endpoints with `@basic_auth.required`.

Endpoints which save to database are updated in `ml_runner/api/sms.py`
