#!/usr/bin/env python3
""" Module Create a Cache class.
    store an instance of the Redis client as a private variable
    0. Writing strings to Redis
    1. Reading from Redis and recovering original type
    2. Incrementing values
    3. Storing lists
    4. Retrieving lists
"""

import redis
import uuid
from typing import Union, Callable, Optional, Any


def decode_utf8(data: bytes) -> str:
    """ decode_utf8 function that returns a string
    Args:
        data: bytes to decode
    Returns:
        str: the decoded string
    """
    return data.decode("utf-8")


class Cache:
    """ Cache class created an instance of the Redis client

    Args:
        None
    Methods:
        store: store the input data in Redis using the input key
        get: return the value of the input key
        get_str: return the string value of the input key
        get_int: return the int value of the input key
        get_list: return the list value of the input key
        append: append the value to the list stored at the input key
        retrive: return the list value of the input key
    """
    # store an instance of the Redis client as a private variable
    # class variable, typing annotation
    _redis: redis.Redis

    def __init__(self) -> None:
        """ Initialize the Cache instance
        Args:
            self: the Cache instance
        Returns:
            None
        """
        # store an instance of the Redis client as a private variable
        self._redis = redis.Redis()
        # Flush the existing Redis instance
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store the input data in Redis using the input key
        Args:
            date: the input data to store in Redis
        Returns:
            str: the key of the stored data
        """
        # generate a unique key with uuid
        generated_key = str(uuid.uuid4())
        # store the data in redis using the generated key
        self._redis.set(generated_key, data)
        # return the generated key
        return generated_key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """ return the value of the input key
        Args:
            key: the input key to retrieve the value
            fn: the function to recover the original type
        Returns:
            Any: the value of the input key
        """
        # get the value of the input key
        value = self._redis.get(key)
        # if the value is not None and the function is not None
        if value is not None and fn is not None:
            # return the value after applying the function
            return fn(value)
        # return the value if it is not None
        return value

    def get_str(self, key: str) -> Optional[str]:
        """ method returns the string value of the input key
        Args:
            key: the input key to retrieve the value
        Returns:
            str: the string value of the input key
        """
        # validate the input key
        if key is None:
            return None
        # get the value of the input key
        value = self.get(key)
        # if value is not None, return the string value
        if value is not None:
            value = decode_utf8(value)
        # return the value if it is not None
        return value

    def get_int(self, key: str) -> Optional[int]:
        """ method returns the int value of the input key
        Args:
            key: the input key to retrieve the value
        Returns:
            int: the int value of the input key
        """
        # validate the input key
        if key is None:
            return None
        # get the value of the input key
        value = self.get(key)
        # if value is not None, return the int value
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                return None
        # return the value if it is not None
        return value
