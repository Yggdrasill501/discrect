# -*- coding: utf-8 -*-
"""File for unit test for gcd."""
import pytest
import dispy.core.gcd


def test_gcd():
    """Test for gcd."""
    number = dispy.core.gcd.gcd(8, 4)
    assert number == 4