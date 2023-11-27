"""
Let’s say I give you a list saved in a variable:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Write one line of Python that takes this list a and makes a new list that has
only the even elements of this list in it.
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_a = [element for element in a if not element % 2]
print(f'List A: {a}')
print(f'Even elements of List A: {even_a}')
