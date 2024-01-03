#!/usr/bin/env python3
"""
3. Basic annotations - to string

Write a type-annotated function to_str
that takes a float n as argument
and returns the string representation of the float.
"""


def to_str(n: float) -> str:
    """to_str function takes a float and returns the string representation.

    Args:
        n (float): the given float to be converted to string

    Returns:
        str: the string representation of the float
    """
    return str(n)
