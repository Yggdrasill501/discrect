# -*- coding: utf-8 -*-


def gcd(a: int,
         b: int) -> int:
    """Return the greatest common divisor of a and b."""
    while a != b:
        if a > b:
            a = a - b
            return a
        else:
            b = b - a
            return b

