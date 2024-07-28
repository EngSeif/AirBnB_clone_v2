#!/usr/bin/python3
""" Simple Flask App"""
from flask import Flask, render_template
from models.state import State
from models import storage
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def Close_session(exception):
    """
    Close Session
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def HoemPage():
    """
    Display WebPage
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    Amenities = storage.all(Amenity).values()
    Amenities = sorted(Amenities, key=lambda a: a.name)
    return render_template('10-hbnb_filters.html', states=states, Amenities= Amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
