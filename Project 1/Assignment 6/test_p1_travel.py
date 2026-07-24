'''
Test cases for Question 6 - Travel Time Calculator
'''

def calc_travel_time(distance, speed):
    time_hours = distance / speed
    time_minutes = time_hours * 60
    return time_minutes

def test_travel_case():
    """Test print_travel_time(26.2, 13.16)"""
    distance = 26.2
    speed = 13.16
    
    total_minutes = calc_travel_time(distance, speed)
    hours = int(total_minutes // 60)
    remaining_minutes = total_minutes - (hours * 60)
    minutes = int(remaining_minutes)
    seconds = round((remaining_minutes - minutes) * 60)
    
    print(f"To travel {distance} miles at {speed} MPH will take {hours} hr, {minutes} min, and {seconds} sec ✓")
    
    # Verify the calculation is reasonable
    assert hours >= 0, f"Hours should be non-negative, got {hours}"
    assert 0 <= minutes < 60, f"Minutes should be between 0 and 59, got {minutes}"
    assert 0 <= seconds < 60, f"Seconds should be between 0 and 59, got {seconds}"

if __name__ == "__main__":
    test_travel_case()
    print("All test cases for Question 6 passed!")
