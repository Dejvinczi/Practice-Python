"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they
guessed too low, too high, or exactly right
"""
import random

random_number = random.randint(1, 9)

while True:
    provided_number = int(input('Provide integer number from 1 to 9: '))
    if provided_number == random_number:
        print(f'Congratulations! This number is {provided_number}')
        break
    else:
        too_value = 'high' if provided_number > random_number else 'low'
        print(f'Too {too_value}.')
