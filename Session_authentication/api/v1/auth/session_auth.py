#!/usr/bin/env python3
""" Session authentication module

    This module contains the SessionAuth class

    Attributes:
        SessionAuth: The SessionAuth class which inherits from Auth
"""
from .auth import Auth
import uuid

class SessionAuth(Auth):
    """ SessionAuth class

    Args:
        Auth (class) : Inherits from Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a Session ID for a user_id

        Args:
            user_id (str, optional): User ID. Defaults to None.

        Returns:
            str: Session ID
        """
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        # Generate a session ID
        session_id = str(uuid.uuid4())
        # Link the user_id to the session_id
        self.user_id_by_session_id[session_id] = user_id

        # Return the session ID
        return session_id
