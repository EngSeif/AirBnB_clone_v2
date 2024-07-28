from flask import Flask, render_template_string
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Closes the SQLAlchemy session after each request."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a HTML page with a list of all State objects."""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda s: s.name)
    return render_template_string('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
