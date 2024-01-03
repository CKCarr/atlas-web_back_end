#!/usr/bin/env python3
import math

"""
2. Basic annotations - floor

Write a type-annotated function floor
which takes a float n as argument
and returns the floor of the float.
"""


def floor(n: float) -> int:
    """ float function which returns the floor of the float

    Args:
        n (float): the given float to be floored

    Returns:
        int: result of the floor operation
    """
    return math.floor(n)
