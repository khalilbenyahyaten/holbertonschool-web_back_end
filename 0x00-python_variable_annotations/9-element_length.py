#!/usr/bin/env python3
""" parameters """
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ types """
    return [(i, len(i)) for i in lst]
