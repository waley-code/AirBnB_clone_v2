#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page: (inside the tag BODY)"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display a HTML page with City: <city.id>: <B><city.name></B>"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """close db session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
