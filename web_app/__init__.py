from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    user_info = {
        'name': 'Mike',
        'age': 42,
    }
    return render_template('index.html', user_info=user_info)


@app.route('/user/<username>/<amount>/')
def profile(username, amount):
    return f"<h1>{username}'s profile ({amount})</h1>"
