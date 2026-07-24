'''
Test cases for Question 5 - Cement Calculator
'''

import math

def calc_yards_cement(t, w, l):
    cubic_inches = math.pow(t, 1) * math.pow(w, 1) * math.pow(l, 1)
    cubic_yards = cubic_inches / math.pow(36, 3)
    return round(cubic_yards, 2)

def test_cement_case():
    """Test cubic_yards_cement(3, 15, 100)"""
    result = calc_yards_cement(3, 15, 100)
    # Calculate expected value
    cubic_inches = 3 * 15 * 100
    cubic_yards_expected = cubic_inches / (36 * 36 * 36)
    expected = round(cubic_yards_expected, 2)
    
    assert result == expected, f"Expected cubic_yards_cement(3, 15, 100) = {expected}, got {result}"
    print(f"cubic_yards_cement(3, 15, 100) = {result} cubic yards ✓")

if __name__ == "__main__":
    test_cement_case()
    print("All test cases for Question 5 passed!")
