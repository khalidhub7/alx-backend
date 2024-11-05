#!/usr/bin/env python3
""" basic Flask app with Babel setup """
from flask import (Flask, request,
                   render_template)
from flask_babel import Babel
app = Flask(__name__)


class Config:
    """ config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"


app.config.from_object(Config)
babel = Babel(app=app)


@babel.localeselector
def get_locale():
    """ determine the best match
    with our supported languages """
    return request.accept_languages.best_match(
        app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home():
    """ single route """
    return render_template('2-index.html')
