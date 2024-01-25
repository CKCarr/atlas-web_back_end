#!/usr/bin/env python3
""" 6. Basic Flask app
In this task, you will set up a basic Flask app.

Create a Flask app that has a single GET route ("/") and use flask.
jsonify to return a JSON payload of the form:
"""
from flask import Flask, jsonify, request, abort
from flask import current_app, make_response, redirect, url_for
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


@app.route('/sessions', methods=['POST'])
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


@app.route('/sessions', methods=['DELETE'])
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

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    
    return redirect('/')


@app.route('/profile', methods=['GET'])
def profile():
    """ profile function
    if session_id is None, return 403
    if user is None, return 403
    if session_id is valid, return jsonify of user
    """
    session_id = request.cookies.get('session_id')

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """ reset password function
    if email not registered, return 403
    if email is valid, generate token
    return jsonify of reset_token
    """
    email = request.form.get('email')

    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """ update password function
    if email not registered, return 403
    if email is valid, generate token
    return jsonify of reset_token
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
