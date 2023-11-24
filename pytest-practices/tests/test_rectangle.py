import sys
sys.path.append('/workspace/pytest-practices/')

import source.shapes as shapes
import pytest


def test_area(rectangle):
    assert rectangle.area() == 10 * 20


def test_perimeter(rectangle):
    assert rectangle.perimeter() == (10 * 2) + (20 * 2)


def test_not_equals(rectangle, weird_rectangle):
    assert rectangle != weird_rectangle
