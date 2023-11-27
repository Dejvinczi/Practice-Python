"""
Implement the same exercise as Exercise 1 (Create a program that asks the
user to enter their name and their age. Print out a message addressed to
them that tells them the year that they will turn 100 years old), except
don’t explicitly write out the year. Use the built-in Python datetime library
to make the code you write work during every year, not just the one we are
currently in.
"""
from datetime import date

print('Hello dude!')
print('Provide next information and I will let you know when you are 100 old:')
name = input('What"s your name?: ')
age = int(input('Provide your age: '))

current_year = date.today().year
year_when_one_hundred = current_year + (100 - age)


print(f'{name}, you will be 100 years old in {year_when_one_hundred}.')
