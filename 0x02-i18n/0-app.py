#!/usr/bin/env python3
""" basic flask app """

from flask import Flask
app = Flask(__name__)


@app.route(
    '/', strict_slashes=False, methods=['GET']
)
def home():
    """ home """
    return "<h1>Welcome to Holberton</h1>"


if __name__ == '__main__':
    app.run(
        host='localhost', port=5000
    )
