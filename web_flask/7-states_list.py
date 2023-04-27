#!/usr/bin/python3
"""
Starting my first Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
import sys
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all('State').values()
    states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
