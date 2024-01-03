#!/usr/bin/env python3
"""
6. Complex types - mixed list

Write a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and floats
and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ Function sum_mixed_list takes a list of integers and floats
    and sums them as a float.

    Args:
        mxd_list (List[int, float]): list of integers and floats

    Returns:
        float: sum of integers and floats
    """
    return sum(mxd_list)
