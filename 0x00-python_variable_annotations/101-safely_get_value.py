#!/usr/bin/env python3

""" More involved type annotations """

from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')


def safely_get_value(

        dct: Mapping,

        key: Any,

        default: Union[T, None] = None) -> Union[Any, T]:

    """

    Parameters

    ----------

    dct: Mapping

    key: Any

    default: T or None

    Return: the key in dct or default

    """

    if key in dct:

        return dct[key]

    else:

        return default
