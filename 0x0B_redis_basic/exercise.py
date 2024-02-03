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
