#!/usr/bin/env python3
""" basic_auth module
    Class BasicAuth
        created to manage the API authentication.
        Inherits from Auth class.
"""
from .auth import Auth


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
