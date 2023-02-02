#!/usr/bin/env python3

""" Complex types - string and int/float to tuple """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:

    """

    Parameters

    ----------

    k: str

    v: mixed List of integers and floats

    Return: tuple (k, square of the int/float v)

    """

    return (k, v ** 2)
