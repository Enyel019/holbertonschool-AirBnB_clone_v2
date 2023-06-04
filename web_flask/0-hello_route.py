#!/usr/bin/python3
"""Write a script that starts a Flask web application."""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """The function "hello" is defined but its implementation is missing."""
    return "Hello HBNB"


if __name__ == '__main__':
    app.rum(host="0.0.0.0", port="5000")
