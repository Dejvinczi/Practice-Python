"""
You, the user, will have in your head a number between 0 and 100.
The program will guess a number, and you, the user, will say whether it is
too high, too low, or your number.

At the end of this exchange, your program should print out how
many guesses it took to get your number.
"""
import random

random_number = random.randint(1, 9)

attempt = 1
while True:
    try:
        input_number = int(
            input(F'Attempt {attempt} - Provide positive integer from 1 to 9: '))
        if input_number not in list(range(1, 10)):
            print('Value not in property range. Try again..')
            continue
    except ValueError:
        print('Invalid value! Try again..')
        continue

    if input_number == random_number:
        print(f'Congratulations! Guessed at {attempt} attempt.')
        break
    elif input_number > random_number:
        print("Too high, try again!")
    else:
        print('Too low, try again!')
