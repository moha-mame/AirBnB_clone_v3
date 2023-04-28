#!/usr/bin/python3
"""
"""
from flask import Flask
from api.v1.views import app_views
from models import storage
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")

@app.teardown_appcontext
def teardown_context(exception):
    """Calls storage.close() at the end of the request"""
    storage.close()

if __name__ == "__main__":
    if getenv("HBNB_API_HOST"):
        host = getenv("HBNB_API_HOST")
    else:
        host = '0.0.0.0'
    if getenv("HBNB_API_PORT"):
        port = getenv("HBNB_API_PORT")
    else:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
