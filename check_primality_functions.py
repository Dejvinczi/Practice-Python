"""
Ask the user for a number and determine whether the number is prime or not.
Take this opportunity to practice using functions, described below.
"""


def is_prime_number(number):
    """Return that number is prime or not."""
    possible_divisors = range(1, number + 1)
    divisors_count = len(
        [divisor for divisor in possible_divisors if not number % divisor]
    )
    return divisors_count == 2


while True:
    input_number = int(input('Provide positive integer number: '))
    is_prime = is_prime_number(input_number)
    if is_prime:
        print(f'{input_number} is prime number.')
    else:
        print(f'{input_number} is not prime number.')
