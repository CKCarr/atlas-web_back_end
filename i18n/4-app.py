#!/usr/bin/env python3
""" Create a basic Flask App
    with a single '/' route and an index.html template
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, refresh
from flask_babel import _


class Config:
    """ Configure available languages in our app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
# Use Config class as config for our app
app.config.from_object(Config)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

# Instantiate Babel object in module-level variable babel
babel = Babel(app)


def get_locale():
    """ Return user preferred locale, if not available return best match """
    url_locale = request.args.get('locale')
    if url_locale in app.config['LANGUAGES']:
        print(f"URL Locale: {url_locale}")  # Debug print
        return url_locale
    best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
    print(f"Best Match Locale: {best_match}")  # Debug print
    return best_match


@app.before_request
def before_request():
    """ Set global variable g.locale to current request locale """
    g.locale = get_locale()
    print(f"Current Locale: {g.locale}")  # Debug print
    refresh()


# def get_locale():
#     return 'fr'  # Force French for testing



@app.route('/')
def index():
    """ Return index.html template """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
    babel.init_app(app, locale_selector=get_locale)
