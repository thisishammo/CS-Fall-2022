'''
Test cases for Question 4 - Pythagorean Theorem Calculator
'''

import math

def calc_side_c(a, b):
    return round(math.sqrt(pow(a, 2) + pow(b, 2)), 2)

def calc_side_ab(ab, c):
    return round(math.sqrt(pow(c, 2) - pow(ab, 2)), 2)

def test_pythagorean_c():
    """Test calc_side_c(3, 4) - should return 5"""
    result = calc_side_c(3, 4)
    assert result == 5.0, f"Expected calc_side_c(3, 4) = 5.0, got {result}"
    print(f"calc_side_c(3, 4) = {result} ✓")

def test_pythagorean_ab():
    """Test calc_side_ab(9, 16) - should return 13.23"""
    result = calc_side_ab(9, 16)
    expected = 13.23
    assert result == expected, f"Expected calc_side_ab(9, 16) = {expected}, got {result}"
    print(f"calc_side_ab(9, 16) = {result} ✓")

if __name__ == "__main__":
    test_pythagorean_c()
    test_pythagorean_ab()
    print("All test cases for Question 4 passed!")
