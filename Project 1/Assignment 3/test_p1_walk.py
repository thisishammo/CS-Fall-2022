'''
Test cases for Question 3 - Pivot Irrigation Distance Calculator
'''

def calc_weekly_distance(pi, radius, num_pivots, inspects_per_day, workdays):
    """Helper function to calculate weekly distance"""
    circumference = 2 * pi * radius
    distance_per_day = circumference * num_pivots * inspects_per_day
    distance_per_week_feet = distance_per_day * workdays
    feet_per_mile = 5280
    weekly_distance_miles = distance_per_week_feet / feet_per_mile
    return distance_per_week_feet, weekly_distance_miles

def test_walk_case_1():
    """Test case 1: radius=90, num_pivots=5, inspects_per_day=2, workdays=5"""
    pi = 3.1416
    radius = 90
    num_pivots = 5
    inspects_per_day = 2
    workdays = 5
    
    distance_feet, distance_miles = calc_weekly_distance(pi, radius, num_pivots, inspects_per_day, workdays)
    
    # Round to 2 decimal places for comparison
    distance_feet_rounded = round(distance_feet, 2)
    distance_miles_rounded = round(distance_miles, 2)
    
    # Use approximate equality for floating point comparison
    assert abs(distance_feet_rounded - 28274.40) < 0.1, f"Expected distance (feet): ~28274.40, got {distance_feet_rounded}"
    assert abs(distance_miles_rounded - 5.35) < 0.01, f"Expected distance (miles): ~5.35, got {distance_miles_rounded}"
    
    print("Test case 1 passed!")
    print(f"Weekly distance (feet): {distance_feet_rounded}")
    print(f"Weekly distance (miles): {distance_miles_rounded}")

def test_walk_case_2():
    """Test case 2: radius=40, num_pivots=3, inspects_per_day=4, workdays=6"""
    pi = 3.1416
    radius = 40
    num_pivots = 3
    inspects_per_day = 4
    workdays = 6
    
    distance_feet, distance_miles = calc_weekly_distance(pi, radius, num_pivots, inspects_per_day, workdays)
    
    # Round to 2 decimal places for comparison
    distance_feet_rounded = round(distance_feet, 2)
    distance_miles_rounded = round(distance_miles, 2)
    
    # Use approximate equality for floating point comparison
    assert abs(distance_feet_rounded - 18095.57) < 0.1, f"Expected distance (feet): ~18095.57, got {distance_feet_rounded}"
    assert abs(distance_miles_rounded - 3.43) < 0.01, f"Expected distance (miles): ~3.43, got {distance_miles_rounded}"
    
    print("Test case 2 passed!")
    print(f"Weekly distance (feet): {distance_feet_rounded}")
    print(f"Weekly distance (miles): {distance_miles_rounded}")

if __name__ == "__main__":
    test_walk_case_1()
    test_walk_case_2()
    print("All test cases for Question 3 passed!")
