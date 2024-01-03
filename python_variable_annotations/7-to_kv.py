#!/usr/bin/env python3
"""
7. Complex types - string and int/float to tuple

Write a type-annotated function to_kv
that takes a string k and an int OR float v as arguments
and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float v
and should be annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function to_kv creates a key/value tuple

    Args:
        k (str): String key
        v (Union[int, float]): int or float that will be squared

    Returns:
        Tuple[str, float]: Tuple with key:k and value:v**2
    """
    return (k, v**2)
