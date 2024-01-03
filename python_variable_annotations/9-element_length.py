#!/usr/bin/env python3
"""
9. Let's duck type an iterable object

Annotate the below function’s parameters
and return values with the appropriate types

def element_length(lst):
    return [(i, len(i)) for i in lst]
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    each containing a sequence from the iterable
    and the length of that sequence.

    Args:
        lst (Iterable[Sequence]): An iterable where each element
        is a sequence supporting len() function.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples,
        each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
