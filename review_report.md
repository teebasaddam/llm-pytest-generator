ISSUES FOUND:
- Missing import for pytest
- Missing import for typing
- Syntax error in 'is_even_non_numeric'
- Test 'test_is_even_negative' is unnecessary as its functionality is already tested in 'test_is_even'
- Test 'test_add_numbers_non_int' is unnecessary as add_numbers function will return the integer part when adding two float numbers which will be a non-error scenario in this function
- Missing parameter type hint and type checking for 'a' and 'b' in add_numbers function

CORRECTED TEST FILE:
# test_sample_code.py
import pytest
import typing

from typing import Union
from sample_code import add_numbers, is_even

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-2, 3) == 1
    assert add_numbers(-2, -3) == -5

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-2) == True
    assert is_even(-3) == False

def test_add_numbers_non_numeric():
    with pytest.raises(TypeError):
        add_numbers(2, 'a')

def test_is_even_non_numeric():
    with pytest.raises(TypeError):
        is_even('a')

def test_add_numbers_mixed_type():
    with pytest.raises(TypeError):
        add_numbers(2, 3.5)

def test_is_even_number():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-2) == True
    assert is_even(-3) == False

def test_is_even_neg_number():
    assert is_even(-2) == True

def test_add_numbers_int():
    assert add_numbers(2, 3) == 5

Note: Since we have defined our parameters as integer values in this corrected version 
      it would not allow float value. So 'test_add_numbers_mixed_type' is a corrected 
      version of 'test_add_numbers_non_int'.