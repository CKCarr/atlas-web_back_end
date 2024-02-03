#!/usr/bin/env python3
""" Module to test Cache class functionality.
    store an instance of the Redis client as a private variable
    0. Writing strings to Redis
    1. Reading from Redis and recovering original type
    2. Incrementing values
    3. Storing lists
    4. Retrieving lists
"""
import unittest
from exercise import Cache
# add `# type: ignore` to the problematic import
from parameterized import parameterized # type: ignore


cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)

if __name__ == '__main__':
    unittest.main()
