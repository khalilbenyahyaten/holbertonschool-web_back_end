#!/usr/bin/env python3
""" make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ make multiplier """
    def multiply(x):
        return x * multiplier
    return multiply
