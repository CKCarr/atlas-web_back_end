#!/usr/bin/env python3
""" 6. Basic Flask app
In this task, you will set up a basic Flask app.

Create a Flask app that has a single GET route ("/") and use flask.
jsonify to return a JSON payload of the form:
"""
from flask import Flask, jsonify, request, abort, \
        current_app, make_response, redirect, url_for
from auth import Auth


AUTH = Auth()

app = Flask(__name__)
# attach AUTH instance to app
app.auth = AUTH


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome():
    """ home page """
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


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ logout function
    find user with requested session_id
    if session_id is None, return 403
    if user is None, return 403
    if session_id is valid, destroy session
    return redirect to GET /
    """
    session_id = request.cookies.get('session_id', None)
    user = AUTH.get_user_from_session_id(session_id)

    if not session_id or not user:
        abort(403)

    AUTH.destroy_session(user.id)
    response = redirect(url_for('welcome'))
    response.set_cookie('session_id', '', expires=0)  # Remove the cookie
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
