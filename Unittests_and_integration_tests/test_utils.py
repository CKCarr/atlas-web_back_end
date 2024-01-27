#!/usr/bin/env python3
"""
Generic utilities for github org client.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap class

    Args:
        unittest (unittest.TestCase): Unit testing for utils.py
    """
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access_nested_map method for utils.py
        check if the method returns the expected result
        """
        # call the function with nested_map and path
        result = access_nested_map(nested_map, path)
        # assert that it returns as expected
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
