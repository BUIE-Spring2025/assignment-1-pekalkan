import pytest
from main import int_to_roman

# Test for numbers out of the valid range (should return None)
def test_int_to_roman_out_of_range():
    assert int_to_roman(0) is None
    assert int_to_roman(-1) is None
    assert int_to_roman(4000) is None
    assert int_to_roman(9999) is None