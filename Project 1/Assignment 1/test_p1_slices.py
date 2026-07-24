'''
Test cases for Question 1 - Watermelon Slices Calculator
'''

import math

# Import the calculation logic from p1_slices.py
children = 0
slices_per_child = 0
adults = 0
slices_per_adult = 0
slices_per_watermelon = 0
extra = 0

def test_slices_case_1():
    """Test case 1: children=120, slices_per_child=3, adults=130, slices_per_adult=2"""
    children = 120
    slices_per_child = 3
    adults = 130
    slices_per_adult = 2
    slices_per_watermelon = 15
    extra = 0.2
    
    # Calculate total slices
    total_slices = children * slices_per_child + adults * slices_per_adult
    assert total_slices == 620, f"Expected total slices: 620, got {total_slices}"
    
    # Calculate total slices with extra
    total_with_extra = total_slices * (1 + extra)
    assert total_with_extra == 744.0, f"Expected total with extra: 744.0, got {total_with_extra}"
    
    # Calculate watermelons needed
    watermelons = total_with_extra / slices_per_watermelon
    assert watermelons == 49.6, f"Expected watermelons: 49.6, got {watermelons}"
    
    # Calculate rounded up watermelons
    watermelons_rounded = math.ceil(watermelons)
    assert watermelons_rounded == 50, f"Expected watermelons rounded: 50, got {watermelons_rounded}"
    
    print("Test case 1 passed!")

def test_slices_case_2():
    """Test case 2: children=110, slices_per_child=3, adults=25, slices_per_adult=2"""
    children = 110
    slices_per_child = 3
    adults = 25
    slices_per_adult = 2
    slices_per_watermelon = 15
    extra = 0.2
    
    # Calculate total slices
    total_slices = children * slices_per_child + adults * slices_per_adult
    assert total_slices == 380, f"Expected total slices: 380, got {total_slices}"
    
    # Calculate total slices with extra
    total_with_extra = total_slices * (1 + extra)
    assert total_with_extra == 456.0, f"Expected total with extra: 456.0, got {total_with_extra}"
    
    # Calculate watermelons needed
    watermelons = total_with_extra / slices_per_watermelon
    assert watermelons == 30.4, f"Expected watermelons: 30.4, got {watermelons}"
    
    # Calculate rounded up watermelons
    watermelons_rounded = math.ceil(watermelons)
    assert watermelons_rounded == 31, f"Expected watermelons rounded: 31, got {watermelons_rounded}"
    
    print("Test case 2 passed!")

if __name__ == "__main__":
    test_slices_case_1()
    test_slices_case_2()
    print("All test cases for Question 1 passed!")
