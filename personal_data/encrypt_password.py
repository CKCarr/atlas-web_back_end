#!/usr/bin/env python3
"""
encrypt_password Module

This module provides functionality for encrypting passwords.

It includes the hash_password function,
which can be used to securely hash passwords for storage.

import bcrypt
    The bcrypt package is used for hashing passwords.

Functions:
    hash_password(password: str) -> bytes

    Returns a salted, hashed password, which is a byte string.

    The method is using the bcrypt package

    The returned byte string is encoded with utf-8.

    Returns:
        A salted, hashed password, which is a byte string.

    is_valid(hashed_password: bytes, password: str) -> bool

    Validates that the provided password matches the hashed password.

    The method is using the bcrypt package

    Returns:
        True if the password matches, False otherwise.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ function hash_password
    Returns a salted, hashed password, which is a byte string.

    Args:
        password (str): password to hash

    Returns:
        bytes: salted, hashed password
    """
    # convert password to a byte string
    password_bytes = password.encode('utf-8')

    # generate salt
    salt = bcrypt.gensalt()

    # hash the password
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    # return the hashed password
    return hashed_password

def is_valid(hashed_password: bytes, password: str) -> bool:
    """ function is_valid
    Validates that the provided password matches the hashed password.

    Args:
        hashed_password (bytes): hashed password
        password (str): password to validate

    Returns:
        bool: True if the password matches, False otherwise.
    """
    # convert the password string to bytes
    password_bytes = password.encode('utf-8')
    
    #  check if provided password
    # matches the hashed password
    return bcrypt.checkpw(password_bytes, hashed_password)
