'''
Test cases for Question 2 - Stair Trips Calculator
'''

import math

def calc_trips(steps_per_floor, floors, target_steps):
    """Helper function to calculate trips"""
    steps_per_trip = steps_per_floor * floors * 2
    return math.ceil(target_steps / steps_per_trip)

def test_steps_case_1():
    """Test case 1: steps_per_floor=16, floors=5"""
    steps_per_floor = 16
    floors = 5
    
    trips_100 = calc_trips(steps_per_floor, floors, 100)
    assert trips_100 == 1, f"Expected trips for 100 steps: 1, got {trips_100}"
    
    trips_500 = calc_trips(steps_per_floor, floors, 500)
    assert trips_500 == 4, f"Expected trips for 500 steps: 4, got {trips_500}"
    
    trips_1000 = calc_trips(steps_per_floor, floors, 1000)
    assert trips_1000 == 7, f"Expected trips for 1000 steps: 7, got {trips_1000}"
    
    trips_5000 = calc_trips(steps_per_floor, floors, 5000)
    assert trips_5000 == 32, f"Expected trips for 5000 steps: 32, got {trips_5000}"
    
    print("Test case 1 passed!")
    print(f"Trips for 100 steps: {trips_100}")
    print(f"Trips for 500 steps: {trips_500}")
    print(f"Trips for 1000 steps: {trips_1000}")
    print(f"Trips for 5000 steps: {trips_5000}")

def test_steps_case_2():
    """Test case 2: steps_per_floor=13, floors=7"""
    steps_per_floor = 13
    floors = 7
    
    trips_100 = calc_trips(steps_per_floor, floors, 100)
    assert trips_100 == 1, f"Expected trips for 100 steps: 1, got {trips_100}"
    
    trips_500 = calc_trips(steps_per_floor, floors, 500)
    assert trips_500 == 3, f"Expected trips for 500 steps: 3, got {trips_500}"
    
    trips_1000 = calc_trips(steps_per_floor, floors, 1000)
    assert trips_1000 == 6, f"Expected trips for 1000 steps: 6, got {trips_1000}"
    
    trips_5000 = calc_trips(steps_per_floor, floors, 5000)
    assert trips_5000 == 28, f"Expected trips for 5000 steps: 28, got {trips_5000}"
    
    print("Test case 2 passed!")
    print(f"Trips for 100 steps: {trips_100}")
    print(f"Trips for 500 steps: {trips_500}")
    print(f"Trips for 1000 steps: {trips_1000}")
    print(f"Trips for 5000 steps: {trips_5000}")

if __name__ == "__main__":
    test_steps_case_1()
    test_steps_case_2()
    print("All test cases for Question 2 passed!")
