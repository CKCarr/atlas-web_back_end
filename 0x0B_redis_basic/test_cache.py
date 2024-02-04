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

class TestCacheWithString(unittest.TestCase):
    """ TestCacheWithString class to test Cache class functionality. """
    def setUp(self):
        self.cache = Cache()
        self.value = b"foo"

    def test_store_and_get(self):
        """ Test store and get methods. """
        key = self.cache.store(self.value)
        self.assertEqual(self.cache.get(key), self.value)

    def test_get_str(self):
        """ Test get_str method. """
        key = self.cache.store(self.value)
        self.assertEqual(self.cache.get_str(key), "foo")

    def test_get_int(self):
        """ Test get_int method. """
        key = self.cache.store(self.value)
        with self.assertRaises(ValueError):
            self.cache.get_int(key)

class TestCacheWithInt(unittest.TestCase):
    """ TestCacheWithInt class to test Cache class functionality. """
    def setUp(self):
        self.cache = Cache()
        self.value = 123

    def test_store_and_get(self):
        """ Test store and get methods. """
        key = self.cache.store(self.value)
        # convert to int before comparing
        self.assertEqual(int(self.cache.get(key)), self.value)

    def test_get_str(self):
        """ Test get_str method. """
        key = self.cache.store(self.value)
        self.assertEqual(self.cache.get_str(key), "123")

    def test_get_int(self):
        """ Test get_int method. """
        key = self.cache.store(self.value)
        self.assertEqual(self.cache.get_int(key), 123)

class TestCacheWithStringFunction(unittest.TestCase):
    """ TestCacheWithStringFunction class to test Cache class functionality. """
    def setUp(self):
        self.cache = Cache()
        self.value = "bar"
        self.fn = lambda d: d.decode("utf-8")

    def test_store_and_get(self):
        """ Test store and get methods. """
        key = self.cache.store(self.value)
        self.assertEqual(self.cache.get(key, fn=self.fn), self.value)

    def test_get_str(self):
        """ Test get_str method. """
        key = self.cache.store(self.value)
        self.assertEqual(self.cache.get_str(key), "bar")

    def test_get_int(self):
        """ Test get_int method. """
        key = self.cache.store(self.value)
        with self.assertRaises(ValueError):
            self.cache.get_int(key)


if __name__ == '__main__':
    unittest.main()
