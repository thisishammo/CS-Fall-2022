#

# Question 3

#

print()

print("Question 3")

print("------------------------------------------")

# Calculate total distance walked per week given a pivot radius of 90 feet,

# five pivots, two inspections per day, and working five days a week. Round

# all results to two decimal places. Use 3.1416 for the

# circumference equation calculation.

# Initialize variables

pi = 3.1416
radius = 90  # feet
num_pivots = 5
inspections_per_day = 2
work_days_per_week = 5

# Calculate the circumference of one pivot

circumference = 2 * pi * radius

# Calculate and display total distance walked (feet and miles)

distance_per_day = circumference * num_pivots * inspections_per_day
distance_per_week_feet = distance_per_day * work_days_per_week
feet_per_mile = 5280
weekly_distance = distance_per_week_feet / feet_per_mile

print(f"Circumference of one pivot: {circumference:.2f} feet")
print(f"Distance walked per week: {distance_per_week_feet:.2f} feet")
print(f"Distance walked per week: {weekly_distance:.2f} miles")