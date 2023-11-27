"""
Create the tic tac toe game and check who's win.
"""


def tic_tac_toe(game_board):
    """Return a number of player who's win the tic tac toe (1 or 2).
    If not winner return None"""
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


WINNER_IS_2 = [
    [2, 2, 0],
    [2, 1, 0],
    [2, 1, 1],
]

WINNER_IS_1 = [
    [1, 2, 0],
    [2, 1, 0],
    [2, 1, 1],
]

WINNER_IS_ALSO_1 = [
    [0, 1, 0],
    [2, 1, 0],
    [2, 1, 1],
]

NO_WINNER = [
    [1, 2, 0],
    [2, 1, 0],
    [2, 1, 2],
]

ALSO_NO_WINNER = [
    [1, 2, 0],
    [2, 1, 0],
    [2, 1, 0],
]


list_of_game_boards = [
    WINNER_IS_2,
    WINNER_IS_1,
    WINNER_IS_ALSO_1,
    NO_WINNER,
    ALSO_NO_WINNER
]


for game_board in list_of_game_boards:
    winner = tic_tac_toe(game_board)
    print('Game board:')
    for row in game_board:
        print(row)
    match winner:
        case 1:
            print('Winner: 1')
        case 2:
            print('Winner: 2')
        case _:
            print('There is no winner.')

    print('\n')
