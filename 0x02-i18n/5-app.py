#!/usr/bin/env python3
""" basic Flask app with Babel setup """
from flask import (Flask, request, g,
                   render_template)
from parameterized import parameterized
from flask_babel import Babel
app = Flask(__name__)


class Config:
    """ config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"


users = {1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
         2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
         3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
         4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"}, }

app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ determine the best match
    with our supported languages """
    argss = request.args
    if 'locale' in argss:
        if argss['locale'] in app.config['LANGUAGES']:
            return argss['locale']
    return request.accept_languages.best_match(
        app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home():
    """ single route """
    return render_template('5-index.html')


def get_user(user_id):
    """ user dictionary """
    if user_id in users:
        return users[user_id]
    return None


@app.before_request
def before_request():
    """ run before all requests """
    login_as = request.args.get('login_as')
    if login_as is None:
        g.user = None
    else:
        g.user = get_user(int(login_as))


if __name__ == '__main__':
    app.run(debug=True)
