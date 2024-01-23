#!/usr/bin/env python3
"""
    4. Hash password

In this task you will define a _hash_password method
that takes in a password string arguments and returns bytes.

The returned bytes is a salted hash of the input password,
hashed with bcrypt.hashpw.
"""
from db import DB


def _hash_password(password: str) -> bytes:
    """ Returns salted hash of input password """
    import bcrypt
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Instance of Auth class
        """
        self._db = DB()

    def valid_login(self, email: str, password: str) -> bool:
        """ Checks if login is valid """
        import bcrypt
        users = self._db.find_user_by(email=email)
        if users:
            if bcrypt.checkpw(password.encode(), users[0]['hashed_password']):
                return True
        return False
