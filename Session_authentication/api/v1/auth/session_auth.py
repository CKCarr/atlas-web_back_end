#!/usr/bin/env python3
""" Session authentication module

    This module contains the SessionAuth class

    Attributes:
        SessionAuth: The SessionAuth class which inherits from Auth
"""
import uuid
from .auth import Auth
from models.user import User


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
        if not isinstance(user_id, str):
            return None
        # Generate a session ID
        session_id = str(uuid.uuid4())
        # Link the user_id to the session_id
        self.user_id_by_session_id[session_id] = user_id

        # Return the session ID
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns a User ID based on a Session ID

        Args:
            session_id (str, optional): Session ID. Defaults to None.

        Returns:
            str: User ID or None
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        # Return the user_id associated with the session_id
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Returns a User instance based on a cookie value

        Args:
            request (_type_, optional): flask request. Defaults to None.
        """
        # Get the Session ID from a cookie
        session_id = self.session_cookie(request)
        # check is session_ id is None
        if not session_id:
            return None
        # Get the User ID from the Session ID
        user_id = self.user_id_for_session_id(session_id)
        # check if user_id is None
        if not user_id:
            return None
        # Return the User ID
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ Deletes the user session / logout

        Args:
            request (_type_, optional): flask request
                Defaults to None.
        """
        if not request:
            return False

        # Get the Session ID from a cookie
        session_id = self.session_cookie(request)
        if not session_id:
            return False

        # Get the User ID from the Session ID
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False

        # Delete the sessionid from the dictionary
        if session_id in self.user_id_by_session_id:
            del self.user_id_by_session_id[session_id]
            return True
        return False
