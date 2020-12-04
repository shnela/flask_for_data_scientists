from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    user_info = {
        'name': 'Mike',
        'age': 42,
    }
    return render_template('index.html', user_info=user_info)


@app.route('/user/<username>/<int:amount>/')
def profile(username, amount):
    return render_template('profile.html', username=username, amount=amount)
