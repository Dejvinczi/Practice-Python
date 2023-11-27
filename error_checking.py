"""
Given this solution to Exercise 9, modify it to have one level of user
feedback: if the user does not enter a number between 1 and 9, tell them.
Don’t count this guess against the user when counting the number of
guesses they used.
"""
import random

random_number = random.randint(1, 9)

attempt = 1
while True:
    input_number = int(
        input(F'Attempt {attempt} - Provide positive integer from 0 to 100: ')
    )
    if input_number == random_number:
        print(f'Congratulations! Guessed at {attempt} attempt.')
        break
    elif input_number > random_number:
        print("Too high, try again!")
    else:
        print('Too low, try again!')
