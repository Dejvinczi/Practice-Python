"""
Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.
"""


def remove_duplicates(input_list):
    """Return list without duplicates."""
    return list(set(input_list))


a = [1, 1, 2, 3, 4, 4]  # [1, 2, 3, 4]
b = [100, 100, 100, 1]  # [1, 100]

print(f'List A: {a}')
print(f'List A without duplicates: {remove_duplicates(a)}')
print(f'List B: {b}')
print(f'List B without duplicates: {remove_duplicates(b)}')
