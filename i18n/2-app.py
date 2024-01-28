#!/usr/bin/env python3
""" Create a basic Flask App
    with a single '/' route and an index.html template
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Configure available languages in our app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
# Use Config class as config for our app
app.config.from_object(Config)

# Instantiate Babel object in module-level variable babel
babel = Babel()
babel.init_app(app)


# @babel.localeselector
def get_locale():
    """ Return user preferred locale, if not available return best match """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# # decorator not working set locale directly
# babel.localeselector(get_locale)


@app.route('/')
def index():
    """ Return index.html template """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
