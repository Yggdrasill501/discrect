# -*- coding: utf-8 -*-
"""Factory to read and write numbers in different numeral systems."""


class ChangeNumrealSystem:
    """Class read change numeral systems."""

    def __int__(self, numeral_system_from: int, number: int, numeral_system_to: int):
        """Initialize class.

        :param numeral_system_from: Numeral system from.
        :param number: Number.
        :param numeral_system_to: Numeral system to.
        """
        self.numeral_system_from = numeral_system_from
        self.number = number
        self.numeral_system_to = numeral_system_to

    def read_numeral_system(self) -> int:
        """Read numeral system.

        :return: Number in decimal numeral system.
        :rtype: int.
        """
        if self.numeral_system_from == 10:
            pass
        elif self.numeral_system_from == 2:
            pass
        elif self.numeral_system_from == 3:
            pass
        elif self.numeral_system_from == 4:
            pass
        elif self.numeral_system_from == 5:
            pass
        elif self.numeral_system_from == 6:
            pass
        elif self.numeral_system_from == 7:
            pass
        elif self.numeral_system_from == 8:
            pass
        elif self.numeral_system_from == 9:
            pass
        elif self.numeral_system_from == 16:
            pass

    def change_numeral_system(self) -> int:
        """Change numeral system.

        :return: Number in new numeral system.
        :rtype: int.
        """
