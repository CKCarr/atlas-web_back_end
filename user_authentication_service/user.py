#!/usr/bin/env python3
""" 0. User model
    In this task you will create a SQLAlchemy model named User
    for a database table named users
    (by using the mapping declaration of SQLAlchemy).

    The model will have the following attributes:

            id (int), the integer primary key
            email (str), a non-nullable string
            hashed_password (str), a non-nullable string
            session_id (str), a nullable string
            reset_token (str), a nullable string
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """ User class for db table users """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(self, *args, **kwargs):
        """ Initialize user Instance

        Args:
            args ([type]): not used
            kwargs ([type]): multiple key/value arguments to send
        """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', None)
        self.hashed_password = kwargs.get('hashed_password', None)
        self.session_id = kwargs.get('session_id', None)
        self.reset_token = kwargs.get('reset_token', None)
