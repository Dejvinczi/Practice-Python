"""
Create a program that asks the user for a number and then prints out a list of
all the divisors of that number. (If you don’t know what a divisor is, it is a
number that divides evenly into another number. For example, 13 is a divisor
of 26 because 26/13 has no remainder.)
"""


def number_divisors(number: int):
    """Print information about number divisors."""
    if not isinstance(number, int):
        raise ValueError('Must be a number.')
    possible_positive_integer_divisors = range(1, number + 1)
    correct_divisors = [divisor
                        for divisor in possible_positive_integer_divisors
                        if not number % divisor]
    print(f'Number {number} divisors are: {correct_divisors}')


number_divisors(2)
number_divisors(124)
number_divisors('fail_value')
