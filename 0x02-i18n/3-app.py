#!/usr/bin/env python3
""" Basic flask app """
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """ App config for Babel settings """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Select best matching language """
    bestMatchLang = request.accept_languages.best_match(
        Config.LANGUAGES)
    return bestMatchLang


@app.route('/', strict_slashes=False,
           methods=['GET'])
def home():
    """ Render the home page template """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
