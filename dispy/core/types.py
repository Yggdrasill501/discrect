"""Extension to the dispy.core.types module."""


class PrimeNumber:
    def __init__(self, number) -> None:
        """Constructor prime number."""
        if not self._is_prime_number(number):
            raise ValueError(f"The number {number} is not prime number.")
        self.number = number

    @staticmethod
    def _is_prime_number(number) -> bool:
        """Returns True if the number is prime, False otherwise."""
        if number < 2:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    def __str__(self) -> str:
        """Returns the string representation of the number."""
        return str(self.number)

    def __repr__(self) -> str:
        """Returns the representation of the number."""
        return f"PrimeNumber({self.number})"

    def __int__(self):
        """Returns the integer value of the number."""
        return int(self.number)


class PositiveInteger:
    def __init__(self, number) -> None:
        """Constructor positive integer number."""
        if not self._is_positive_integer(number):
            raise ValueError(f"The number {number} is not positive integer.")
        self.number = number

    @staticmethod
    def _is_positive_integer(number) -> bool:
        """Returns True if the number is positive integer, False otherwise."""
        if number < 1:
            return False
        if not isinstance(number, int):
            return False
        return True

    def __str__(self) -> str:
        """Returns the string representation of the number."""
        return str(self.number)

    def __repr__(self) -> str:
        """Returns the representation of the number."""
        return f"PositiveInteger({self.number})"

    def __mod__(self, other):
        """Returns the remainder of the division of the number by other."""
        return self.number % other

    def __int__(self) -> int:
        """Returns the integer value of the number."""
        return int(self.number)
