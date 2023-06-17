#!/usr/bin/python3
"""Write a script that starts a Flask web application."""
from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """Render a template that displays a list of states."""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def cities_states():
    """Render a template that displays cities grouped by states."""
    states = storage.all(State).values()
    return render_template('7-dump.html', states=states)


@app.route('/states/<string:id>')
def cit_b_st(id):
    """The function "cit_b_st" takes an input parameter the function."""
    lis = storage.all('State')
    if "State." + id in lis:
        state = lis["State." + id]
    else:
        state = None
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Close the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
