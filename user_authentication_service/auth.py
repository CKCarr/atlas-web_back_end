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
        """
        Validates the user login credentials.

        :param email: The user's email
        :param password: The user's password
        :return: True if the credentials are valid, False otherwise
        """
        import bcrypt

        # Try to find the user by email
        user = self._db.find_user_by(email=email)

        if user is None:
            return False

        if user:
            # Ensure the hashed_password is in bytes format if it's not
            hashed_password = user.hashed_password
            if isinstance(hashed_password, str):
                hashed_password = hashed_password.encode()
            

            # Check if the provided password matches the stored hashed password
            if bcrypt.checkpw(password.encode(), hashed_password):
                return True

        return False

    # private method
    def _generate_uuid(self) -> str:
        """ Generate a UUID """
        from uuid import uuid4

        new_uuid = uuid4()
        return str(new_uuid)
