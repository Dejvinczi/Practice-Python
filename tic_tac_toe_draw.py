"""
Create the tic tac toe game and check who's win.
"""


def tic_tac_toe(game_board):
    """Return a number of player who's win the tic tac toe (1 or 2).
    If not winner return 0"""
    for row in range(0, 3):
        row_check = set([
            game_board[row][0],
            game_board[row][1],
            game_board[row][2],
        ])
        if len(row_check) == 1 and game_board[row][0]:
            return game_board[row][0]

    for column in range(0, 3):
        column_check = set([
            game_board[0][column],
            game_board[1][column],
            game_board[2][column],
        ])
        if len(column_check) == 1 and game_board[0][column]:
            return game_board[0][column]

    diagonals_check_1 = set([
        game_board[0][0],
        game_board[1][1],
        game_board[2][2],
    ])
    diagonals_check_2 = set([
        game_board[0][2],
        game_board[1][1],
        game_board[2][0],
    ])

    if len(diagonals_check_1) == 1 or \
            len(diagonals_check_2) == 1 and game_board[1][1]:
        return game_board[1][1]

    return 0


def get_coordinates(move_str):
    """Parse and validate player move. Return move coordinates."""
    move_arr = move_str.split(',')
    if len(move_arr) != 2:
        raise ValueError('Invalid movement value.')

    x = int(move_arr[0].strip()) - 1
    y = int(move_arr[1].strip()) - 1

    return x, y


def print_game_board(game_board):
    """Print the current game board"""
    for row in game_board:
        print(row)


game_board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

game_round = 1
while True:
    print('\nCurrent game board:')
    print_game_board(game_board)

    player = 'X' if game_round % 2 else 'O'
    try:
        x, y = get_coordinates(input(f'Player {player} move: '))
    except ValueError as err:
        print(err)
        continue
    if game_board[x][y]:
        print('There is already value, try again.')
        continue

    game_board[x][y] = player
    winner = tic_tac_toe(game_board)
    if winner:
        print(f'The game is end - WINNER Player {winner}')
        break
    if game_round == 9:
        print('The game is end - DRAW!')
        break

    game_round += 1
