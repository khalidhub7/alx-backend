#!/usr/bin/env python3
""" Basic Flask app with Babel setup """
from flask import Flask, request, g, render_template
from flask_babel import Babel
from pytz import timezone, exceptions

app = Flask(__name__)


class Config:
    """ Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Determine the best match with our supported languages """
    args = request.args
    h_locale = request.headers.get('locale')
    if 'locale' in args:
        if args['locale'] in app.config['LANGUAGES']:
            return args['locale']
    if 'login_as' in args:
        id = int(args.get('login_as'))
        user = users.get(id)
        if user:
            if user['locale'] in app.config['LANGUAGES']:
                return user['locale']
    if h_locale in app.config['LANGUAGES']:
        return h_locale
    return request.accept_languages.best_match(
        app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home():
    """ Single route """
    return render_template('7-index.html')


def get_user(user_id):
    """ User dictionary """
    if user_id in users:
        return users[user_id]
    return None


@app.before_request
def before_request():
    """ Run before all requests """
    login_as = request.args.get('login_as')
    if login_as is None:
        g.user = None
    else:
        g.user = get_user(int(login_as))


@babel.timezoneselector
def get_timezone():
    """
Determine the appropriate time zone """
    args = request.args
    timez = args.get('timezone')
    if timez:
        try:
            pytz.timezone(timez)
            return timez
        except pytz.UnknownTimeZoneError:
            pass
    if 'login_as' in args:
        user_id = int(args.get('login_as'))
        user = users.get(user_id)
        if user:
            user_timez = user['timezone']
            if user_timez:
                try:
                    pytz.timezone(user_timez)
                    return user_timez
                except pytz.UnknownTimeZoneError:
                    pass
    return 'UTC'


if __name__ == '__main__':
    app.run(debug=True)
