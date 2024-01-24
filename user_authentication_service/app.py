#!/usr/bin/env python3
""" 6. Basic Flask app
In this task, you will set up a basic Flask app.

Create a Flask app that has a single GET route ("/") and use flask.
jsonify to return a JSON payload of the form:
"""
from flask import Flask, jsonify, request, abort, \
        current_app, make_response
from auth import Auth


AUTH = Auth()

app = Flask(__name__)
# attach AUTH instance to app
app.auth = AUTH


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """ Hello world """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ Register user """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        new_user = AUTH.register_user(email, password)
        return jsonify({"email": new_user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ login function
    send response to post request
    401 if email/password not valid
    if email and password are valid
    return a cookie session id
    create a session for the user
    """
    # parse form data -request
    email = request.form.get('email')
    password = request.form.get('password')

    # validate email and password
    is_valid = AUTH.valid_login(email, password)

    # handle invalid credentials
    if not is_valid:
        abort(401)

    # create response -Session id cookie
    session_id = AUTH.create_session(email)

    # store id in session cookie
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie('session_id', session_id)

    # return response
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
