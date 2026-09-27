import pytest
from impulse_momentum_math import momentum, impulse

def test_momentum():
    """test accuracy of momentum calculations"""
    m = momentum(2, 3)
    assert m == 6

def test_negative_mass():
    """affirm function raises ValueError when negative mass is input"""
    with pytest.raises(ValueError):
        momentum(2, -2)


def test_impulse():
    """test accuracy of impulse calculations"""
    i = impulse(9)
    assert i == 9

def test_zero_velocity():
    """verify function properly handles cases where v=0"""
    m = momentum (0, 3)
    assert m == 0

def test_zero_mass():
    """verify function properly handles cases where m=0"""
    m = momentum(3, 0)
    assert m == 0


def test_negative_velocity():
    """verify an input of a negative velocity results in a negative momentum"""
    m = momentum(-2, 5)
    assert m == -10