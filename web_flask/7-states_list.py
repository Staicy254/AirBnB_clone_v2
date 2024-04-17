#!/usr/bin/python3
"""Flask web application displaying -- list of states with sorting."""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """
    The states_list page, retrieving and sorting states from storage.
    """
    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda x: x.name)  # Sort by state name
    context = {'states': all_states}
    return render_template('7-states_list.html', **context)


@app.teardown_appcontext
def teardown(exc):
    """
    The Flask app/request context end event listener, closing the storage.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

