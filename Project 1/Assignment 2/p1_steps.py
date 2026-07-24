#

# Question 2

#

import math

print()

print("Question 2")

print("------------------------------------------")

# Calculate the total number of trips given 100, 500, 1000, or 5000 daily

# steps, 16 steps per floor, and down and back up the stairs as one trip.

# Reuse the step variable. Round the number of trips up to the nearest

# whole integer.

# Recommended variable names: steps_per_floor, target_steps, trips

# Initialize variables

steps_per_floor = 16
floor = 5
steps_per_trip = steps_per_floor * floor * 2

# Calculate 100 steps and display the number of trips

target_steps = 100
trips = math.ceil(target_steps / steps_per_trip)
print(f"For {target_steps} steps: {trips} trip(s)")

# Calculate 500 steps and display the number of trips

target_steps = 500
trips = math.ceil(target_steps / steps_per_trip)
print(f"For {target_steps} steps: {trips} trip(s)")

# Calculate 1000 steps and display the number of trips

target_steps = 1000
trips = math.ceil(target_steps / steps_per_trip)
print(f"For {target_steps} steps: {trips} trip(s)")

# Calculate 5000 steps and display the number of trips

target_steps = 5000
trips = math.ceil(target_steps / steps_per_trip)
print(f"For {target_steps} steps: {trips} trip(s)")
