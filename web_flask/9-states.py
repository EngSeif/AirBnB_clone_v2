#!/usr/bin/python3
""" Simple Flask App"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def Close_session(exception):
    storage.close()


@app.route('/states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    if id is None:
        return render_template('9-states.html', state=None)
    state = storage.all(State).get(f'State.{id}')
    if state is None:
        return render_template('9-states.html', state=None)
    return render_template('9-states.html', state=state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
