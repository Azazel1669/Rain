import pytest
from yandex_testing_lesson import is_under_queen_attack


def test_one_step():
    assert is_under_queen_attack('e2', 'e2') is True


def test_false_step():
    assert is_under_queen_attack('f3', 'h2') is False


def test_right_step():
    assert is_under_queen_attack('f3', 'e2') is True


def test_right_step2():
    assert is_under_queen_attack('f3', 'd3') is True


def test_right_step3():
    assert is_under_queen_attack('f3', 'f4') is True


def test_wrong_first():
    with pytest.raises(TypeError):
        is_under_queen_attack(10, 'a2')


def test_wrong_second():
    with pytest.raises(ValueError):
        is_under_queen_attack('j5', 'a2')


def test_wrong_third():
    with pytest.raises(ValueError):
        is_under_queen_attack('a2b', 'a2')


def test_wrong_forth():
    with pytest.raises(ValueError):
        is_under_queen_attack('abc', 'a2')


def test_wrong_first1():
    with pytest.raises(TypeError):
        is_under_queen_attack('a2', 42)


def test_wrong_second1():
    with pytest.raises(ValueError):
        is_under_queen_attack('a2', 'j5')


def test_wrong_second2():
    with pytest.raises(ValueError):
        is_under_queen_attack('a2', 'a2b')


def test_wrong_third1():
    with pytest.raises(ValueError):
        is_under_queen_attack('a2', 'abc')