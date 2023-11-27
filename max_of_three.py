"""
Implement a function that takes as input three variables, and returns the
largest of the three. Do this without using the Python max() function!
"""


def max_value(a, b, c):
    """Return largest value of provided numbers."""
    return max((a, b, c))


option_1 = (1, 2, 3)
option_2 = (3, 2, 1)
option_3 = (1, 1, 1)
option_4 = (3, 6, 1)
options = (option_1, option_2, option_3, option_4)

for option in options:
    max_el = max_value(*option)
    print(f'For {option} the largest value is: {max_el}')
