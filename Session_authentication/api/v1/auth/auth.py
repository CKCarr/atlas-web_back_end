#!/usr/bin/env python3
""" auth module
    Class Auth
        created to manage the API authentication.

        public instance methods:
            require_auth
            authorization_header
            current_user
"""
import os
from flask import request
from typing import List, TypeVar


class Auth():
    """ Auth CLass
    template to manage the API authentication.
    """

    def __init__(self):
        """
        __init__ constructor method for Auth class to create an instance
        """
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth public method
        determines if the path requires authentication

        Args:
            path (str): will be used later,
            excluded_paths (List[str]): will be used later,

        Returns:
            bool:
                False - path is not required to be authenticated
                True - path is required to be authenticated
        """
        # check if path is none and excluded_paths are None or empty
        if path is None:
            return True
        # check if path contains excluded_paths
        if not excluded_paths:
            return True
        # Ensure the path is slash tolerant
        # remove trailing slash from path
        path = path.strip('/')

        # check the path in excluded_paths
        for ex_paths in excluded_paths:
            # remove trailing slash from paths
            ex_paths = ex_paths.strip('/')
            # check if path is in excluded_paths
            if path == ex_paths or path.startswith(ex_paths + '/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization header public method

            Args:
            request (object): flask request object

            Returns:
                None - request is none
                request header value - return request header value
        """
        # check if request is None
        if request is None:
            return None
        # check if request does not contain Authorization header
        if 'Authorization' not in request.headers:
            return None
        # if Authorization header exists, return the header value
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user public method
            Args:
                request (object): flask request object
            Returns:
        """
        return None

    def session_cookie(self, request=None):
        """ session_cookie public method
        Args:
            request (object): flask request object
        Returns:
            None - request is None or cookie named SESSION_NAME
        """
        if request is None:
            return None

        # use the environment variable SESSION_NAME
        # to define the name of the cookie
        session_name = os.getenv('SESSION_NAME')
        if not session_name:
            return None

        # return the value of the cookie request named session_name
        return request.cookies.get(session_name)
