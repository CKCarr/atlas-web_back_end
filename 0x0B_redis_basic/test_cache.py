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
from parameterized import parameterized_class
from exercise import Cache


@parameterized_class(('value', 'fn'), [
    (b"foo", None),
    (123, int),
    ("bar", lambda d: d.decode("utf-8"))
])
class TestCache(unittest.TestCase):
    """ TestCache class to test the
        Cache class functionality.
    """
    def setUp(self):
        """ Set up the Cache instance
        """
        self.cache = Cache()

    def test_store_and_get(self):
        """Test storing and retrieving data."""
        key = self.cache.store(self.value)
        self.assertEqual(self.cache.get(key, fn=self.fn), self.value)


    def test_get_str(self):
        """Test retrieving data as a string."""
        key = self.cache.store(self.value)
        expected_str = self.value.decode('utf-8') if isinstance(self.value, bytes) else str(self.value)
        self.assertEqual(self.cache.get_str(key), expected_str)

    def test_get_int(self):
        """Test retrieving data as an integer."""
        key = self.cache.store(self.value)
        try:
            int_value = int(self.value)
        except ValueError:
            with self.assertRaises(ValueError):
                self.cache.get_int(key)
        else:
            self.assertEqual(self.cache.get_int(key), int_value)


if __name__ == '__main__':
    unittest.main()
