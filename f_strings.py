"""
Implement the same exercise as Exercise 1 (Create a program that asks the
user to enter their name and their age. Print out a message addressed to
them that tells them the year that they will turn 100 years old), except
use f-strings instead of the + operator to print the resulting output message.
"""
from datetime import date

print('Hello dude!')
print('Provide next information and I will let you know when you are 100 old:')
name = input('What"s your name?: ')
age = int(input('Provide your age: '))

current_year = date.today().year
year_when_one_hundred = current_year + (100 - age)


print(f'{name}, you will be 100 years old in {year_when_one_hundred}.')
