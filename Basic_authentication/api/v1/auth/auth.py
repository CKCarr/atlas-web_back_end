#!/usr/bin/env python3
""" auth module
    Class Auth
        created to manage the API authentication.

        public instance methods:
            require_auth
            authorization_header
            current_user
"""
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

        Args:
            path (str): will be used later,
            excluded_paths (List[str]): will be used later,

        Returns:
            bool:
                False - path is not required to be authenticated
                True - path is required to be authenticated
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ authorization header public method

            Args:
            request (object): flask request object

            Returns:
                None - request is none
                request header value - return request header value
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user public method
            Args:
                request (object): flask request object
            Returns:
                None - request is none
                None - request doesn't contain user credentials
                None - failed to retrieve user instance for request.user_id
                user instance - current user
        """
        return None
