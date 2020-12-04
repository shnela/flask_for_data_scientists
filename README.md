# Flash messages

[Flask flashing instructions](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/)

* Flash for logged in user
* comment out some login fields
* Display messages in base.html
* flash messages goes from login -> index and accumulates
* Make prettier with [Dismissible alerts](https://getbootstrap.com/docs/3.4/components/#alerts-dismissible)
* Log out notification


## Additional assignment - Flashing With Categories
https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/#flashing-with-categories

Make logout alert yellow with (class="alert alert-warning")

Use parameter `category` in function [flash](https://flask.palletsprojects.com/en/1.1.x/api/#flask.flash)
and `with_categories` in function `get_flashed_messages`
