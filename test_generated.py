from sample_code import *

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-2, 3) == 1
    assert add_numbers(-1, -1) == -2

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(4) == True
    assert is_even(-2) == True

def test_add_numbers_edge_cases():
    assert add_numbers(0, 0) == 0
    assert add_numbers(-0, 0) == 0
    assert add_numbers(0, -0) == 0

def test_is_even_edge_cases():
    assert is_even(0) == True
    assert is_even(-0) == True
    assert is_even(float('nan')) == False  # nan is not even or odd

def test_add_numbers_negative_numbers():
    assert add_numbers(-2, -3) == -5
    assert add_numbers(-1, -2) == -3

def test_add_numbers_with_large_numbers():
    assert add_numbers(1000000000, 2000000000) == 3000000000

def test_is_even_with_large_numbers():
    assert is_even(2000000000) == True
    assert is_even(-2000000000) == True