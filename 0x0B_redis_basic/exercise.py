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
import functools
from typing import Union, Callable, Optional, Any


def decode_utf8(data: bytes) -> str:
    """ decode_utf8 function that returns a string
    Args:
        data: bytes to decode
    Returns:
        str: the decoded string
    """
    return data.decode("utf-8")


def count_calls(method: Callable) -> Callable:
    """ count_calls decorator that counts how many times a method is called
    Args:
        method: the method to decorate
    Returns:
        Callable: the decorated method
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function that wraps the input method
        Args:
            self: the Cache instance
            *args: the input arguments
            **kwargs: the input keyword arguments
        Returns:
            Any: the result of the input method
        """
        # get the method name
        method_name_keys = f"{method.__qualname__}"
        # increment the method call count
        self._redis.incr(method_name_keys)
        # return the result of the input method
        return method(self, *args, **kwargs)
    # return the wrapper function
    return wrapper


def call_history(method: Callable) -> Callable:
    """ call_history decorator that stores the history of inputs and outputs
    Args:
        method: the method to decorate
    Returns:
        Callable: the decorated method
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function that wraps the input method
        Args:
            self: the Cache instance
            *args: the input arguments
            **kwargs: the input keyword arguments
        Returns:
            Any: the result of the input method
        """
        # generate the method name key for the input method
        input_key = f"{method.__qualname__}:inputs"

        # generate the method name key for the output method
        output_key = f"{method.__qualname__}:outputs"

        # store the input arguments in the input key
        self._redis.rpush(input_key, str(args))

        # execute the wrap function and store the output
        output = method(self, *args, **kwargs)

        # store the output in redis
        self._redis.rpush(output_key, str(output))

        # return the output of the original method
        return output
    # return the wrapper function
    return wrapper


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
        retrieve: return the list value of the input key
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

    @call_history
    @count_calls
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
