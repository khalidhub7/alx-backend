#!/usr/bin/env python3
""" basic flask app """
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ app config for Babel settings """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False,
           methods=['GET'])
def home():
    """ home """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
