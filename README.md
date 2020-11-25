# Flask

[What is flask according to duck?](https://duckduckgo.com/?q=flask&t=ffab&atb=v192-1&ia=web)

## April Fool's joke
> Flask was created by Armin Ronacher of Pocoo, an international group of Python enthusiasts formed in 2004.
According to Ronacher, the idea was originally an April Fool's joke that was popular enough to make into a serious
application.
>
> When Ronacher and Georg Brandl created a bulletin board system written in Python,
>the Pocoo projects Werkzeug and Jinja were developed.
>
> Flask has become popular among Python enthusiasts.
> As of October 2020, it has second most stars on GitHub among Python web-development frameworks,
only slightly behind Django, and was voted the most popular web framework in the Python Developers Survey 2018.

_Wiki_

## [Pallets Project](https://palletsprojects.com/)
> The Pallets Projects are a collection of Python web development libraries that were independently developed by
Armin Ronacher and later used as the basis of the Flask microframeworkToday the Pallets Projects are a community-driven
organization with the goal to maintain and improve those libraries.

## Who's [Armin Ronacher](https://en.wikipedia.org/wiki/Armin_Ronacher)??

## [Django](https://duckduckgo.com/?t=ffab&q=django+web+framework&atb=v192-1&ia=web) THE alternative
[Django team](https://www.djangoproject.com/foundation/teams/)

## Flask is minimal, Django is huge
* But both are popular: [Flask](https://stackshare.io/flask) vs [Django](https://stackshare.io/django)
* Flask is easier to gasp

## Let's run it
* In cygwin
* In Ubuntu  
* And pyCharm

### Test different ports
[How](https://flask.palletsprojects.com/en/1.1.x/cli/#setting-command-options)

#### In source file (pyCharm run)
Like `app.run(port=5001)`

#### In Cygwin / Ubuntu
* `FLASK_APP='main.py' flask run --port 5002`
* `FLASK_APP='main.py' FLASK_RUN_PORT=5002 flask run`

### But What does `if __name__ == “__main__”`: do?
[Stack answer](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)
