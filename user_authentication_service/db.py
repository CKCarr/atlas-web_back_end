#!/usr/bin/env python3
"""DB module
"""
import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session


# Set SQLAlchemy log level: only show error messages and above
logging.getLogger('sqlalchemy').setLevel(logging.ERROR)


from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Method that saves an user to the database
        adding new user to the session,
        saves it to the database
        """
        # Create a new user object
        new_user = User(email=email,
                        hashed_password=hashed_password)
        # Add the user to the session object
        self._session.add(new_user)
        # Save the user to the database
        self._session.commit()
        #  Return newly created user object
        return new_user
