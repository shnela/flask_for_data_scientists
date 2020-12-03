# Jinja2 templates
[README_PREV.md](./README_PREV.md)

* [Flask docs - Rendering Templates][]
* [Jinja2 docs - Rendering Templates][]


## Variables
* [Jinja2 docs - Variables][]

### Filters
* [Jinja2 docs - Filters][]
* [Jinja2 docs - List of Builtin Filters][]
```
{{ "stRanGE sTRing"|lower }}
```

## Template Inheritance
* [Jinja2 docs - Template Inheritance][]
* Make `index.html` based on `base.html`

## Control Structures
* [Jinja2 docs - List of Control Structures][]

### Interesting structures
* For loop
* If statement
* Assignments 

## Assignments
### Use `render_template` in `profile` endpoint
Instead of simply returning string - render jinja template (you'll have to create new `.html` file).  
Display corresponding message.

### Use `for` loop in `profile` template.
Update new template of `profile` endpoint, which will display `name` value `anount` times using html list.
* [Statements doc - for][]
* [HTML unordered list doc][]

Tips!:
* Python loop iterating n times: `for _ in range(n):`
* `amount` passed from kwargs is of type str (must be converted to int `int(amount)`)
* Inside of control structures you don't have to use `{{ }}` brackets in order to access variables.

### Use `if` statement in `profile` template.
If `name` pased to `hello_from_kwargs` equals `Admin` - display name only once.  
All other names should work as before.

Additionally wrap every second name in list with `<strong>This text is important!</strong>`

* [Statements doc - if](https://jinja2docs.readthedocs.io/en/stable/templates.html#if)
* [HTML strong tag doc](https://www.w3schools.com/tags/tag_strong.asp)

Tips!:
* use `loop.index` and check modulo 2 to detect even / odd elements

### Use `filters`
* Make sure that we won't use for loop for any "admin" variation (ADMIN, Admin, aDmin, aDMIn).
* Truncate name to 10 characters


[Flask docs - Rendering Templates]: https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
[Jinja2 docs - Rendering Templates]: https://jinja2docs.readthedocs.io/en/stable/templates.html
[Jinja2 docs - Variables]: https://jinja2docs.readthedocs.io/en/stable/templates.html#variables
[Jinja2 docs - Filters]: https://jinja2docs.readthedocs.io/en/stable/templates.html#filters
[Jinja2 docs - Template Inheritance]: https://jinja2docs.readthedocs.io/en/stable/templates.html#template-inheritance
[Jinja2 docs - List of Builtin Filters]: https://jinja2docs.readthedocs.io/en/stable/templates.html#builtin-filters
[Jinja2 docs - List of Control Structures]: https://jinja2docs.readthedocs.io/en/stable/templates.html#list-of-control-structures
[Statements doc - for]: https://jinja2docs.readthedocs.io/en/stable/templates.html#for
[Statements doc - if]: https://jinja2docs.readthedocs.io/en/stable/templates.html#if
[HTML unordered list doc]: https://www.w3schools.com/HTML/html_lists.asp
[HTML strong tag doc]: https://www.w3schools.com/tags/tag_strong.asp
