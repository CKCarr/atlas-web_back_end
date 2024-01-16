#!/usr/bin/env python3
""" basic_auth module
    Class BasicAuth
        created to manage the API authentication.
        Inherits from Auth class.
"""
from .auth import Auth
import base64


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
