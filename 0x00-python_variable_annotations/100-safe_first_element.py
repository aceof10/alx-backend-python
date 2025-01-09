#!/usr/bin/env python3
"""type-annotated function safe_first_element"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns first element of a sequence"""
    if lst:
        return lst[0]
    else:
        return None
