"""
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that
are common between the lists (without duplicates). Make sure your program
works on two lists of different sizes.
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Make elements unique
set_a = set(a)
set_b = set(b)

# Intersection two sets
a_and_b = list(set_a.intersection(set_b))

print(f'List A: {a}')
print(f'List B: {b}')
print(f'Intersection of list a and b: {a_and_b}.')
