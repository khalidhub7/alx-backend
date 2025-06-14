#!/usr/bin/env python3
""" basic babel app """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ app config for Babel settings """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Retrieves the locale for a web page"""
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False,
           methods=['GET'])
def home():
    """ render the home page template """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
