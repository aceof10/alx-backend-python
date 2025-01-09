#!/usr/bin/env python3
"""
   takes a float multiplier as argument
   and returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        multiplies a float
    """
    def multiplier(n: float) -> float:
        """
            returns the multiplies of a float
        """
        return n * multiplier

    return make_multiplier
