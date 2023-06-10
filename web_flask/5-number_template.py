#!/usr/bin/python3
"""Write a script that starts a Flask web application."""

from flask import Flask
from flask import render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """First route message."""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    """Second route message."""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Third route message."""
    return f"C {text.replace('_', ' ')}"


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """Third route message."""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>')
def python_is_int(n):
    """Fourth route message."""
    return f'{n} is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    """Fifth route message."""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
