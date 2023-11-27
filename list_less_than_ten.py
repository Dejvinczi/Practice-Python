"""
Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements
of the list that are less than 5.
"""


def less_than_5(number):
    return number < 5


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
filtered_a = list(filter(less_than_5, a))
print(f'Elements from the list that are less than 5: {filtered_a}')
