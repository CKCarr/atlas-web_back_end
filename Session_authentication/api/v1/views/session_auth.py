#!/usr/bin/env python3
""" Session authentication view module

    This module handles all routes for the Session authentication.
    Methods:
        session_login: POST /api/v1/auth_session/login
        session_logout: DELETE /api/v1/auth_session/logout
"""
import os
from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models.user import User


@app_views.route('/auth_session/login/', methods=['POST'],
                 strict_slashes=False)
def session_login():
    """
    Login route for Session authentication
            POST /api/v1/auth_session/login

    Return:
        - User object JSON represented
    """
    email = request.form.get('email')
    if not email:
        return jsonify({'error': "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({'error': "password missing"}), 400

    user = User.search({'email': email})
    if not user:
        return jsonify({'error': "no user found for this email"}), 404

    # check if password is valid in first user found
    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({'error': "wrong password"}), 401

    # create a session ID for the user ID
    # import auth instance here to avoid circular import
    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    # set cookie with session ID
    session_name = os.getenv('SESSION_NAME')
    if not session_name:
        return jsonify({'error': "SESSION_NAME not set"}), 400

    # create response
    response = jsonify(user.to_json())
    response.set_cookie(session_name, session_id, httponly=True, secure=True)
    return response
