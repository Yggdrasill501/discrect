# -*- coding: utf-8 -*-
"""Module with the greatest common divisor function ."""


def gcd(a: int,
        b: int) -> int:
    """Function that calculates greatest common divider of two numbers.

    :param a: int.
    :param b: int.
    :returns: Greatest common divider.
    :rtype: int.
    """
    while a != b:
        if a > b:
            a = a - b
            return a
        b = b - a
        return b
