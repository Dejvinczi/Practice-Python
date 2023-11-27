"""
One area of confusion for new coders is the concept of functions (which
have been addressed on this blog in exercise 11 for example). So in this
exercise, we will be stretching our functions muscle by refactoring an
existing code snippet into using functions.

Here is the code snippet to refactor (taken from a correct but very
repeated solution to exercise 24 on this website):

print(" --- --- ---")
print("|   |   |   |")
print(" --- --- ---")
print("|   |   |   |")
print(" --- --- ---")
print("|   |   |   |")
print(" --- --- ---")
"""


MIN_LEN_OF_GAME_BOARD = 1


def game_board(size_x, size_y):
    """Print a game board (size_x x size_y) size."""
    if not size_x or not size_y:
        return

    start_x_sequence = '|   |'
    x_sequence = start_x_sequence + '    |' * (size_y - 1)
    y_sequence = ' --- ' * size_y

    print(y_sequence)
    for _ in range(size_x):
        print(x_sequence)
        print(y_sequence)


def main():
    """Main program func."""
    while True:
        size = input('Provide size of game board (example: 3x3, 3x6 etc..): ')
        splitted_size_arr = size.split('x')
        if not splitted_size_arr or len(splitted_size_arr) != 2:
            print('Invalid provided size value. Try again!')
            continue

        x = int(splitted_size_arr[0])
        y = int(splitted_size_arr[1])

        game_board(x, y)


if __name__ == '__main__':
    main()
