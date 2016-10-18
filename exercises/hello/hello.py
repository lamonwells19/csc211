#!/usr/bin/env python3

from flask import flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World!"
