#!/usr/bin/env python3
"""
8. Complex types - functions

Write a type-annotated function make_multiplier
that takes a float multiplier as argument
and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that multiplies a float by multiplier.

    Args:
        multiplier (float): multiplier to multiply by

    Returns:
        Callable[[float], float]: callable function
        that multiplies a float by multiplier
    """
    def multiplier_function(number: float) -> float:
        """
        Function that multiplies the function argument by
        multiplier argument from the parent function.

        Args:
            number (float): number to multiply by multiplier

        Returns:
            float: number from this function (* by)
                multiplier of parent function
        """
        return number * multiplier
    return multiplier_function
