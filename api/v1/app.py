#!/usr/bin/python3
"""Flask web application"""

from flask import Flask, abort, jsonify
from api.v1.views import app_views
from models import storage
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_context(exception):
    """Calls storage.close() at the end of the request"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handler for 404 errors"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    if getenv("HBNB_API_HOST"):
        host = getenv("HBNB_API_HOST")
    else:
        host = '0.0.0.0'
    if getenv("HBNB_API_PORT"):
        port = getenv("HBNB_API_PORT")
    else:
        port = '5000'
    app.run(host=host, port=port, threaded=True, debug=True)
