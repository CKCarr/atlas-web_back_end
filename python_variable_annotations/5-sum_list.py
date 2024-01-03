#!/usr/bin/env python3
"""
5. Complex types - list of floats

Write a type-annotated function sum_list
which takes a list input_list of floats as argument
and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    :Function sum_list: sums a list of floats

    :param input_list: list of floats
    :Return: sum of list of floats
    """
    return sum(input_list)
