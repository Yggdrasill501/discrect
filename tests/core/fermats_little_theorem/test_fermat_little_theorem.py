"""File to count Fermat's little theorem"""
import dispy.core.fermats_little_theorem.fermat_little_theorem


def test_fermat_little_theorem():
    """Test for Fermat's little theorem."""
    number = dispy.core.fermats_little_theorem.fermat_little_theorem.FermatLittleTheorem(5, 2)
    assert number.calculate() is True
