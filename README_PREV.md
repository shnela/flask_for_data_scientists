# Routing
[README_PREV.md](./README_PREV.md)

## New app layout
[Simple Packages](https://flask.palletsprojects.com/en/1.1.x/patterns/packages/#simple-packages).

Let's keep web files in `web_app` catalog. Don't mix it with READMEs, instructions and other playground scripts...


## New view (index)
[Flask docs - Routing](https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing)

### Add other one (with arguments)
```python
@app.route('/user/<username>/')
def profile(username):
    return f"{username}'s profile"
```

### Remember about trailing slashes
```python
@app.route('/user/<name>')  # problematic
@app.route('/user/<name>/')
```

## Set `FLASK_ENV=development`
[Flask docs - Debug Mode](https://flask.palletsprojects.com/en/1.1.x/quickstart/#debug-mode)
1. it activates the debugger
1. it activates the automatic reloader
1. it enables the debug mode on the Flask application.

### Cygwin
```bash
# run application
$ FLASK_APP='main.py' FLASK_ENV=development flask run
```

### pyCharm
Add `FLASK_ENV=development` in `Run configuration` -> `Environment variables`

## Assignments

### 1. Url converters
[Flask docs - Variable rules](https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules)

#### Define functions:
* hello_number(number: int):
* hello_uuid(uuid):
* hello_both(text, number):

#### Visit:
* http://127.0.0.1:5000/user/name/
* http://127.0.0.1:5000/user/42/
* http://127.0.0.1:5000/user/123e4567-e89b-12d3-a456-426614174000/
* http://127.0.0.1:5000/user/he/man/42/  # make it work


### 2. `hello_from_kwargs` available in two urls
Make `hello_from_kwargs` view available under `/other_link/<name>/`

### 3. Use `add_url_rule` instead of `app.route` decorator.
Use [`add_url_rule`](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.add_url_rule) instead of `app.route`
decorator.
