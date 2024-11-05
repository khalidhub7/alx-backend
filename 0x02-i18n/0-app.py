#!/usr/bin/env python3
""" basic flask app """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    """ single route """
    return render_template('0-index.html')
