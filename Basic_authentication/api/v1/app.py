#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize auth to None
auth = None

# Get AUTH_TYPE from environment
AUTH_TYPE = os.getenv('AUTH_TYPE')

# Conditionally create a BasicAuth instance based on AUTH_TYPE
if AUTH_TYPE == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif AUTH_TYPE:
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized_error(error) -> str:
    """ Not authorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error(error) -> str:
    """ forbidden handler """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request_func() -> None:
    """ Before request handler function
            before_request_func = None
            A dictionary with lists of functions that will be called
            at the beginning of each request.
            The key of the dictionary is the name of the blueprint
            this function is active for,
            or None for all requests.
            To register a function, use the before_request() decorator.
    """
    if auth is None:
        return

    # paths to exclude from authentication
    excluded_paths = ['/api/v1/status/',
                      '/api/v1/unauthorized/',
                      '/api/v1/forbidden/']
    # check if request path is excluded
    if not auth.require_auth(request.path, excluded_paths):
        return

    # check if request is not authenticated
    if auth.authorization_header(request) is None:
        abort(401)

    # check if request is not authenticated
    if auth.current_user(request) is None:
        abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
