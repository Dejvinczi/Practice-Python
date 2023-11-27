"""
Take two lists, say for example these two:
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that
are common between the lists (without duplicates). Make sure your program
works on two lists of different sizes. Write this in using at least
one list comprehension.
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a_and_b = list(set((el for el in a if el in b)))

print(f'List A: {a}')
print(f'List B: {b}')
print(f'Common of List A and B: {a_and_b}')
