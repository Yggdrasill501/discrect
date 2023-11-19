# -*- coding: utf-8 -*-
"""File to count Fermat's little theorem"""
import dispy.core.types


class FermatLittleTheorem:

    def __init__(self, p: dispy.core.types.PrimeNumber, a: dispy.core.types.PositiveInteger) -> None:
        """Fermat's little theorem: a^(p-1) = 1 (mod p)

        :param p: prime number from types dispy.core.types.PrimeNumber.
        :param a: integer number.
        """
        if not self._rule(p, a):
            raise ValueError(f"The number {a} is divisible by {p}.")
        self.a = a
        self.p = p

    def calculate(self):
        """Calculate Fermat's little theorem: a^(p-1) = 1 (mod p)"""
        return pow(self.a.__int__(), self.p.__int__() - 1, self.p.__int__()) == 1

    @staticmethod
    def _rule(p, a: dispy.core.types.PositiveInteger) -> bool:
        """Rule: a is positive number that is not divisible by p"""
        return a % p != 0
