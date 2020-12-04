# Flask-WTF

[README_PREV.md](./README_PREV.md)

## New requirements
* [Flask-WTF][]
* Already placed in `requirements.txt`
  * pyCharm will  install automatically
  * for Cygwin/Ubuntu `$ pip install -r requirements.txt`

### Flask-WTF is based on WTF-Forms
[WTF-Forms][]

### `__init__.py` is updated
* [WTF-Forms - Basic fields][]
* [WTF-Forms - Built-in validators][]

## Prerequisite 
SECRET_KEY required (https://pinetools.com/random-string-generator)
Add it in pyCharm config run.

## Assignment
Add new field in form - `age` and save value in `session`.
This field should be positive integer, so IntegerField and NumberRange should be used.
If `age` isn't present in session - display 0.
Test form with missing data, negative values and strings instead of int.
After sending ('user1', 43), we should be redirected to `index` which will display "Hello fasada (32)!"


## Integration Flask-WTF with Flask-Bootstrap
We're using [Flask-WTF - Creating Forms][] for generating `LoginForm` in `main.py`.  
We're struggling with displaying it in `login.html`.

Let's integrate `Flask-WTF` with [Flask-Bootstrap integration][]

### Why?
#### More beautiful
[Bootstrap forms][] - looks nice

#### Simpler to use in html
```html
<form method="POST">
  {{ wtf.quick_form(form) }}
</form>
```

But first [wtf macro][] is required.
```html
{% import "bootstrap/wtf.html" as wtf %}
```
Add it to `base.html`

## Assignments
* Display name of logged in user in top right corner, or 'Unknown'
* Implement logout view which will remove `name` and `age` keys from session
Then link new view to "Log out" button in right top corner.
This should be simple GET function (no form required)
(use `del`)

[Flask-WTF]: https://flask-wtf.readthedocs.io/en/stable/
[WTF-Forms]: https://wtforms.readthedocs.io/en/2.3.x/
[WTF-Forms - Basic fields]: https://wtforms.readthedocs.io/en/2.3.x/fields/#basic-fields
[WTF-Forms - Built-in validators]: https://wtforms.readthedocs.io/en/2.3.x/validators/#built-in-validators
[Flask-WTF - Creating Forms]: https://flask-wtf.readthedocs.io/en/stable/quickstart.html#creating-forms
[Flask-Bootstrap integration]: https://pythonhosted.org/Flask-Bootstrap/basic-usage.html
[Bootstrap forms]: https://getbootstrap.com/docs/3.3/css/#forms
[wtf macro]: https://pythonhosted.org/Flask-Bootstrap/macros.html#macros
