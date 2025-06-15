#!/usr/bin/env python3
""" basic babel app """
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """ app config for Babel settings """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """ user by url param """
    user_id = request.args.get('login_as', None)
    return users.get(int(user_id)) if user_id else None


@app.before_request
def before_request() -> None:
    """ set `g.user` before each request """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ select best matching language """
    fromuser = g.user.get('locale') if g.user else None
    fromurl = request.args.get('locale')
    bestmatchlang = request.accept_languages.best_match(
        Config.LANGUAGES)

    locale = fromurl or fromuser or bestmatchlang
    return locale \
        if locale and locale in Config.LANGUAGES \
        else Config.BABEL_DEFAULT_LOCALE


@app.route('/', strict_slashes=False,
           methods=['GET'])
def home():
    """ render the home page template """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
