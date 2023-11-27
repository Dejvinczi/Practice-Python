"""
Time for some fake graphics! Let’s say we want to draw game boards
that look like this:

 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---

This one is 3x3 (like in tic tac toe). Obviously, they come in many
other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them
to the screen using Python’s print statement.

Remember that in Python 3, printing to the screen is accomplished by
print("Thing to show on screen")
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


while True:
    size = input('Provide size of game board (example: 3x3, 3x6 etc..): ')
    splitted_size_arr = size.split('x')
    if not splitted_size_arr or len(splitted_size_arr) != 2:
        print('Invalid provided size value. Try again!')
        continue

    x = int(splitted_size_arr[0])
    y = int(splitted_size_arr[1])

    game_board(x, y)
