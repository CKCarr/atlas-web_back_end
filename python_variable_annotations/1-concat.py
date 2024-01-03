#!/usr/bin/env python3

"""
Task 1. Basic annotations - concat

Write a type-annotated function concat
that takes a string str1 and a string str2 as arguments
and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """ concat function
    concatenates two strings and returns the result

    Args:
        str1 (str): String 1
        str2 (str): String 2

    Returns:
        str: result String from concatenation
    """
    return str1 + str2
