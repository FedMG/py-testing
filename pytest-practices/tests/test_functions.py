import sys
sys.path.append('/workspace/pytest-practices')

import pytest
import source.functions as functions
import time

def test_add():
    result = functions.add(1, 4)
    assert result == 5


def test_divide():
    result = functions.divide(10, 5)
    assert result == 2


def test_divide_by_zero():
    # ERROR
    # result = functions.divide(10, 0)
    # assert True

    # with pytest.raises(ZeroDivisionError):
    #     functions.divide(10, 0)

    with pytest.raises(ValueError):
        functions.divide(10, 0)


def test_add_strings():
    result = functions.add('I like', 'programming')
    assert 'I like programming'


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = functions.divide(10, 5)
    assert result == 2


@pytest.mark.skip(reason='This feature is currently broken')
def test_add():
    assert functions.add(1, 2) == 3


@pytest.mark.xfail(reason='we cannot divide by zero')
def test_divide_by_zero_broken():
    functions.divide(4, 0)
