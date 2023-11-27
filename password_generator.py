"""
Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of lowercase letters, uppercase
letters, numbers, and symbols. The passwords should be random, generating
a new password every time the user asks for a new password. Include your
run-time code in a main method.
"""
import random
import string


def pass_gen(
        size=10, characters=string.ascii_letters + string.digits + string.punctuation):
    """Random password generator."""
    return ''.join(random.choice(characters) for _ in range(size))


print(pass_gen(size=(int(input('Provide length of password: ')))))
