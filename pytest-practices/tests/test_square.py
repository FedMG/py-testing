import sys
sys.path.append('/workspace/pytest-practices/')

import pytest
import source.shapes as shapes

def test_multiple_square_araes(side_length, expected_area):
    assert shapes.Shape(side_length).area() == expected_area