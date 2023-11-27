"""
Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string, except
with the words in backwards order. For example, say I type the string:

For:
    >>My name is Michele
Then I would see the string:
    >>Michele is name My
"""


def reverse_word_order(input_str):
    """Return a reversed  multiple word string."""
    input_str_arr = input_str.split(' ')
    input_str_arr = reversed(input_str_arr)

    return ' '.join(input_str_arr)


while True:
    input_str = input('Provide some multiple word string: ')
    if not input_str:
        print('String cannot be empty! Try again.')

    reversed_input_str = reverse_word_order(input_str)
    print(f'Reversed: {reversed_input_str}')
