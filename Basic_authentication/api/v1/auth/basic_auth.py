#!/usr/bin/env python3
""" basic_auth module
    Class BasicAuth
        created to manage the API authentication.
        Inherits from Auth class.
"""
from .auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth CLass
    template to manage the API authentication.
    """

    def __init__(self):
        """
        __init__ constructor method for BasicAuth class to create an instance
        """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ extract_base64_authorization_header method
        Args:
            authorization_header: string containing the header
        Returns:
            the Base64 part of the Authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """ decode_base64_authorization_header method
        Args:
            base64_authorization_header: string containing the header
        Returns:
            the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(
                base64_authorization_header, str):
            return None
        try:
            # convert base64_authorization_header to bytes
            # using utf-8 encoding
            base64_bytes = base64_authorization_header.encode('utf-8')
            # decode base64_bytes using base64 standard encoding
            # and convert to string
            decoded_bytes = base64.b64decode(base64_bytes)
            # convert decoded_bytes to string using utf-8 encoding
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> (str, str):
        """ extract_user_credentials method
        Args:
            decoded_base64_authorization_header: string containing the header
        Returns:
            the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(
                decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        # split decoded_base64_authorization_header by ':'
        # and return tuple of email and password
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str
            ) -> TypeVar('User'):
        """ user_object_from_credentials method
        Args:
            user_email: string containing the user email
            user_pwd: string containing the user password
        Returns:
            the User instance based on his email and password.
        """
        if user_email is None or not isinstance(user_email, str) or \
           user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
            if not users:
                return None

            user = users[0]

            if user.is_valid_password(user_pwd):
                return user
            else:
                return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user method
                Overloads Auth's current_user method
                to retrieve the User instance for a request.
        Args:
            request: request object
        Returns:
            the User instance based on his email and password.
        """
        # get authorization header from request
        auth_header = self.authorization_header(request)
        # get base64 part of authorization header
        base64_auth_header = self.extract_base64_authorization_header(
            auth_header)
        # get decoded value of base64 part of authorization header
        decoded_base64_auth_header = self.decode_base64_authorization_header(
            base64_auth_header)
        # get user credentials from decoded value of base64 part
        # of authorization header
        user_credentials = self.extract_user_credentials(
            decoded_base64_auth_header)
        # get user email and password from user credentials
        user_email, user_pwd = user_credentials
        # get user instance based on user email and password
        user = self.user_object_from_credentials(user_email, user_pwd)
        # return user instance
        return user
