import pytest
from fractions import Fraction
from points import Proj


def test_scaling_gives_equal_points():
    assert Proj(1, 2, -3) == Proj(2, 4, -6)


def test_different_points_differ():
    assert Proj(1, 2, -3) != Proj(1, 2, 3)


def test_zero_vector_rejected():
    with pytest.raises(ValueError):
        Proj(0, 0, 0)


def test_fractional_input():
    assert Proj("1/2", 0, 1) == Proj(1, 0, 2)


def test_hashable():
    assert Proj(1, 2, -3) in {Proj(2, 4, -6)}


def test_data_is_normalized():
    assert Proj(2, 4, -6).data == (Fraction(1), Fraction(2), Fraction(-3))


def test_repr():
    assert repr(Proj(2, 4, -6)) == "[1 : 2 : -3]"