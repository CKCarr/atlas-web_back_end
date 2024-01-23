#!/usr/bin/env python3
"""
    4. Hash password

In this task you will define a _hash_password method
that takes in a password string arguments and returns bytes.

The returned bytes is a salted hash of the input password,
hashed with bcrypt.hashpw.
"""
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Hash a password for storing.

    :param password: The password to hash.
    :return: A salted hash of the input password.
    """
    import bcrypt
    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Instance of Auth class
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers user """
        try:
            users = self._db.find_user_by(email=email)

            if users:
                raise ValueError('User {} already exists'.format(email))

        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """ Checks if login is valid """
        try:
            users = self._db.find_user_by(email=email)

            if users:
                return True

        except NoResultFound:
            return False
