#!/usr/bin/env python3

"""contains some shit"""


from typing import Union, List

mxd_lst = List[Union[int, float]]

def sum_mixed_list(mxd_lst: mxd_lst) -> float:

    """returns sum of the floats contained in the mxd_lst"""

    return sum(mxd_lst)
