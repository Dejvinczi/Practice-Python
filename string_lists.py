"""
Ask the user for a string and print out whether this string is a palindrome
or not. (A palindrome is a string that reads the same forwards and backwards.)
"""


def is_palindrome(input_str: str):
    """Return that the string is a palindrome or not."""
    if not isinstance(input_str, str) or not input_str:
        raise ValueError('Must be a non empty string.')
    input_str = input_str.lower()
    return 'Yes' if input_str == input_str[::-1] else 'No'


example_str = input('Input a string and i will say, it is palindrome or not: ')
print(f'String {example_str} is palindrome? {is_palindrome(example_str)}')
