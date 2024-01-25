#!/usr/bin/env python3
"""
Auth class to interact with the authentication database.

"""
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid


def _hash_password(password: str) -> bytes:
    """
    Hash a password for storing.

    :param password: The password to hash.
    :return: A salted hash of the input password.
    """
    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def _generate_uuid() -> str:
    """ Generate a UUID

    :return: A string representation of a new UUID
    """

    new_uuid = uuid.uuid4()
    return str(new_uuid)


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

        try:
            # Attempt to find the user by email
            user = self._db.find_user_by(email=email)

            if user is None:
                return False

            # Ensure the hashed_password is in bytes format if it's not
            hashed_password = user.hashed_password
            if isinstance(hashed_password, str):
                hashed_password = hashed_password.encode()

            # Check if the provided password matches the stored hashed password
            return bcrypt.checkpw(password.encode(), hashed_password)

        except NoResultFound:
            # No user found with the given email
            return False

    def create_session(self, email: str) -> str:
        """ Create Session ID
        for the user with the specified email.
        :param email: User's email
        :return: Session ID as a string
        """
        try:
            # find corresponding user to email
            user = self._db.find_user_by(email=email)
            if user is None:
                return None
            # generate a new UUID
            session_id = _generate_uuid()
            # store new uuid in database as user's session_id
            self._db.update_user(user.id, session_id=session_id)
            # return the session ID
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """ Get user from session ID

        Args:
            session_id (str): session ID

        Returns:
            str: user's email or None
        """
        if session_id is None:
            return None

        try:
            # find corresponding user to email
            user = self._db.find_user_by(session_id=session_id)
            return user.email

        except NoResultFound:
            # No user found with the given email
            return None

    def destroy_session(self, user_id: int) -> None:
        """ Destroy session

        Args:
            user_id (int): user's id

        Returns:
            None
        """
        if user_id is None:
            return None

        try:
            # find corresponding user to email
            self._db.update_user(user_id, session_id=None)
            return None

        except NoResultFound:
            # No user found with the given email
            return None

    def get_reset_password_token(self, email: str) -> str:
        """ Get reset password token

        Args:
            email (str): user's email

        Returns:
            str: reset token or None
        """
        if email is None:
            return None

        try:
            # find corresponding user to email
            user = self._db.find_user_by(email=email)
            # generate a new UUID
            reset_token = _generate_uuid()
            # store new uuid in database as user's session_id
            self._db.update_user(user.id, reset_token=reset_token)
            # return the session ID
            return reset_token

        except NoResultFound:
            # No user found with the given email
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ Update password

        Args:
            reset_token (str): reset token
            password (str): password

        Returns:
            None
        """
        if reset_token is None or password is None:
            return None

        try:
            # find corresponding user to email
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hashed_password,
                                 reset_token=None)
            return None

        except NoResultFound:
            # No user found with the given email
            return None
