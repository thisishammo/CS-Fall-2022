'''
Travel Time Calculator
This program calculates travel time given distance and speed,
and displays the results in hours, minutes, and seconds.
'''

# Calculate travel time in minutes given the distance in miles and the speed in mph
def calc_travel_time(distance, speed):
    return round((distance / speed) * 60, 2)

# Output the travel time hours, minutes, seconds, given distance, and speed
def print_travel_time(distance, speed):
    total_minutes = calc_travel_time(distance, speed)
    total_seconds = int(total_minutes * 60)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    print(f"To travel {distance} miles at {speed} MPH will take {hours} hr, {minutes} min, and {seconds} sec")

# Test the functions
# Highway trip: 120 miles at 55 mph vs 70 mph
print_travel_time(120, 55)
print_travel_time(120, 70)

# Around-town trip: 5 miles at 25 mph vs 35 mph
print_travel_time(5, 25)
print_travel_time(5, 35)

'''
References:
https://www.calculatorsoup.com/calculators/math/speed-distance-time-calculator.php
'''
