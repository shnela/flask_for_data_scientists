# Modular Applications with Blueprints
[README_PREV.md](./README_PREV.md)

> Flask uses a concept of blueprints for making application components and supporting common patterns within an
>application or across applications. Blueprints can greatly simplify how large applications work and provide a central
>means for Flask extensions to register operations on applications.
>A Blueprint object works similarly to a Flask application object, but it is not actually an application.
>Rather it is a blueprint of how to construct or extend an application.


[Blueprints - flask docs][]

But, what actually is [blueprint (wiki)][]?

## Important changes
* Bluepring is defined in `web_app/main/__init__.py`
* Blueprint is now registered in `web_app/__init__.py` with `app.register_blueprint` function.
* In `web_app/main/views.py` we no longer use `app`, instead we're using defined `bp`.
* `app` is still available, but as `flask.current_app` module.
* Urls has changed. They required blueprint name in `url_for`. [Building URLs - Flask][]

[blueprint (wiki)]: https://en.wikipedia.org/wiki/Blueprint
[Blueprints - flask docs]: https://flask.palletsprojects.com/en/1.1.x/blueprints/
[Building URLs - Flask]: https://flask.palletsprojects.com/en/1.1.x/blueprints/#building-urls
