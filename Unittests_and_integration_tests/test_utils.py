#!/usr/bin/env python3
"""
Generic utilities for github org client.
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
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

    @parameterized.expand([
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b'))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test access_method_nested_map method for utils.py
        check if the method raises the correct exception
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ TestGetJson class for utils.py
    Args:
        unittest (unittest.TestCase): Unit testing for utils.py
    """
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test get_json method for utils.py
        check if the method returns the result as expected
        """
        # mock the get_json function
        mock = Mock()
        # set the return value of the mock
        mock.json.return_value = test_payload
        # patch the requests.get to return the mock response object
        with patch('requests.get') as mock_get:
            # set the return value of the mock
            mock_get.return_value = mock
            # call the function using the test_url
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            # assert that the mock was called once with the test_url
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """  TestMemoize class for utils.py
    Args:
        unittest (unittest.TestCase): Unit testing for utils.py
    """

    def test_memoize(self):
        """ Test memoize method for utils.py
        check if the method returns the result as expected
        """
        # create a mock class
        class TestClass:
            """ TestClass class
            Args:
                unittest (unittest.TestCase): Unit testing for utils.py
                memoize method
            """
            def __init__(self):
                """ __init__ method
                Args:
                    self (TestClass): the class itself
                """
                self.call_count = 0

            def a_method(self):
                """ a_method method
                Args:
                    self (TestClass): the class itself
                """
                self.call_count += 1
                return 42

            @memoize
            def a_property(self):
                """ a_property method
                Args:
                    self (TestClass): the class itself
                """
                return self.a_method()

        # create a mock object from the mock class
        with patch.object(
                TestClass, 'a_method', return_value=42) as mocked_method:
            test_instance = TestClass()
            # call the a_property method twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Check if the return values are as expected
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Check if the a_method method was called only once
            mocked_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
