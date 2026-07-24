'''
Cement Calculator
This program calculates the amount of cement needed for concrete slabs
given thickness, width, and length measurements in inches.
Converts cubic inches to cubic yards.
'''

import math

# Return cement amount in yards using cubic inches given thickness (t),
# width (w), and length (l), in inches.
def calc_yards_cement(t, w, l):
    cubic_inches = math.pow(t, 1) * math.pow(w, 1) * math.pow(l, 1)
    cubic_yards = cubic_inches / math.pow(36, 3)
    return round(cubic_yards, 2)

# Output (print) results of calculating yards given
# thickness (t), width (w), and length (l) in inches
def print_results(t, w, l):
    yards = calc_yards_cement(t, w, l)
    print(f"A cement slab {t}\" thick, {w}\" wide, and {l}\" long requires {yards} cubic yards of cement")

# Test the functions with the two cement slabs
# Slab 1: 4" thick, 4' by 12' (converted to inches: 4" thick, 48" wide, 144" long)
print_results(4, 48, 144)

# Slab 2: 4" thick, 15' by 20' (converted to inches: 4" thick, 180" wide, 240" long)
print_results(4, 180, 240)

'''
References:
https://www.concretenetwork.com/concrete/howmuch/calculator.htm
https://www.todayshomeowner.com/cubic-yard-calculator/
'''
