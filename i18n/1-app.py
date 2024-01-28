#!/usr/bin/env python3
""" Create a basic Flask App

    with a single '/' route and an index.html template
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ Configure available languages in our app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# instantiate Flask app object
app = Flask(__name__)
# use Config class as config for our app
app.config.from_object(Config)
# instantiate Babel object in module level variable babel
babel = Babel(app)


@app.route('/')
def index():
    """ Return index.html template """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
