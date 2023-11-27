"""
Write a program that asks the user how many Fibonnaci numbers to generate and
then generates them. Take this opportunity to think about how you can
use functions. Make sure to ask the user to enter the number of numbers in
the sequence to generate.
"""


def fibonacci(n):
    """Return Fibonacci sequence."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = fibonacci(n - 1)
    sequence.append(sequence[-1] + sequence[-2])

    return sequence


while True:
    n = int(input('Provide a positive integer: '))
    if n <= 0:
        print('Number must be a positive integer. Try again.')
        continue
    fib_seq = fibonacci(n)
    print(f'Fibonnaci sequence for {n} is: {fib_seq}')
