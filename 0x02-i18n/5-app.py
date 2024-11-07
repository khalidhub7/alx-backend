#!/usr/bin/env python3
""" basic Flask app with Babel setup """
from flask import Flask, request, g, render_template
from flask_babel import Babel

app = Flask(__name__)

class Config:
    """ config class """
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
    """ determine the best match with our supported languages """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def home():
    """ single route """
    return render_template('5-index.html')

def get_user(user_id):
    """ user dictionary """
    return users.get(user_id)

@app.before_request
def before_request():
    """ run before all requests """
    login_as = request.args.get('login_as')
    g.user = get_user(int(login_as)) if login_as else None

if __name__ == '__main__':
    app.run(debug=True)
