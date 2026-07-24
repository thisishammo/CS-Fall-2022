'''
Pythagorean Theorem Calculator
This program calculates missing sides of a right-angled triangle
using the Pythagorean Theorem (a² + b² = c²)
'''

import math

# Calculate the missing side c of a right-angled triangle
def calc_side_c(a, b):
    return round(math.sqrt(pow(a, 2) + pow(b, 2)), 2)

# Calculate the missing side a or b of the same kind of triangle
def calc_side_ab(ab, c):
    return round(math.sqrt(pow(c, 2) - pow(ab, 2)), 2)

# Test the functions
print("Testing Pythagorean Theorem Calculator")
print("-" * 40)

# Test calc_side_c with values 5 and 10
print("c = " + str(calc_side_c(5, 10)))

# Test calc_side_ab with values 4 as side a or b, and 8 as hypotenuse c
print("a = " + str(calc_side_ab(4, 8)))

'''
References:
https://www.rapidtables.com/calc/math/pythagorean-calculator.html
https://en.wikipedia.org/wiki/Pythagorean_theorem
https://docs.python.org/3/library/math.html
'''
