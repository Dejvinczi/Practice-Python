"""
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user.
"""


def odd_or_even(number: int):
    """Return that number is even or odd."""
    if not isinstance(number, int):
        raise ValueError('Must be a number.')
    return 'odd' if number % 2 else 'even'


print(odd_or_even(1))  # odd
print(odd_or_even(2))  # even
print(odd_or_even(3))  # odd
print(odd_or_even(4))  # even
print(odd_or_even('fail_arg'))  # even
