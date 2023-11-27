"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""


def first_and_last_element(input_list):
    """Return first and last element of list."""
    if len(input_list) > 1:
        return [input_list[0], input_list[-1]]

    return input_list


a = [5, 10, 15, 20, 25]
first_and_last = first_and_last_element(a)
print(f'List of numbers: {a}')
print(f'First and last element of this list: {first_and_last}')
