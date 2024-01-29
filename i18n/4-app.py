#!/usr/bin/env python3
""" Basic Flask app
for i18n exercise
flask app to render index.html
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Config Class for Babel
    Determine available languages with our Flask application.
    set default locale and time zone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
# set config for flask app
app.config.from_object(Config)
# initialize babel
babel = Babel(app)


# @babel.localeselector
def get_locale():
    """get_locale function
    to determine the best match with our supported languages."""
    # Check if request has locale parameter and if it's supported
    requested_locale = request.args.get('locale')
    if requested_locale in app.config['LANGUAGES']:
        return requested_locale
    # locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel.init_app(app, locale_selector=get_locale)

@app.route('/')
def index():
    """ index function
    to route / request to index.html
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
