"""File to count Fermat's little theorem"""
import dispy.core.fermats_little_theorem.fermat_little_theorem
import logging

MODULE_LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def test_fermat_little_theorem():
    """Test for Fermat's little theorem."""
    number = dispy.core.fermats_little_theorem.fermat_little_theorem.FermatLittleTheorem(5, 2)
    assert number.calculate() is True


def test_fermat_little_theorem_with_logger():
    """Test for Fermat's little theorem."""
    MODULE_LOGGER.info(f"Test for Fermat's little theorem, for numbers {1024,11}.")
    number = dispy.core.fermats_little_theorem.fermat_little_theorem.FermatLittleTheorem(1024, 11)
    result = number.calculate()
    MODULE_LOGGER.info(f"Result: {result}")
    assert number.calculate() is True
