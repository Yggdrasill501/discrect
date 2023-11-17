"""Extension to the dispy.core.types module."""


class PrimeNumber:
    def __init__(self, number) -> None:
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
        return str(self.number)

    def __repr__(self) -> str:
        return f"PrimeNumber({self.number})"


class PositiveInteger:
    def __init__(self, number) -> None:
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
        return str(self.number)

    def __repr__(self) -> str:
        return f"PositiveInteger({self.number})"

    def __mod__(self, other):
        return self.number % other
