#!/usr/bin/env python3
""" tuple """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ tuple """
    return (k, v ** 2)
