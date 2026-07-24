# CS 122 Fall 2020 Assignment 1
# Author: Hammond
# Credit: 
# Description: Introduction to programming problem set uses Python numeric data types and operations to solve a variety of small problems.

import math

print("Question 1")
print("------------------------------------------")

# Initialize variables with values
children = 120
adults = 130
slices_per_child = 3
slices_per_adult = 2
slices_per_watermelon = 15
extra = 0.2

# Calculate the total number of watermelon slices and display the number of slices
total_slices = (children * slices_per_child) + (adults * slices_per_adult)
print("Total slices:", total_slices)

# Add extra amount and display number of slices
total_slices = total_slices + (total_slices * extra)
print("Total slices (including extra):", total_slices)

# Calculate the number of watermelons and display the number of watermelons
watermelons = total_slices / slices_per_watermelon
print("Total watermelons:", watermelons)

# Round the number of watermelons up and display the number of watermelons
watermelons = math.ceil(watermelons)
print("Total watermelons (rounded up):", watermelons)
