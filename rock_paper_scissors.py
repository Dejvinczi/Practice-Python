"""
Make a two-player Rock-Paper-Scissors game.
"""
import random

# Possible variants of game figures
POSSIBLE_VARIANTS = ('ROCK', 'PAPER', 'SCISSORS')


def random_variant():
    return random.choice(POSSIBLE_VARIANTS)


while True:
    second_player_variant = random_variant()
    first_player_varian = input(
        f'Provide one of choices ({POSSIBLE_VARIANTS}): ')
    input_str_upp = first_player_varian.upper()

    if input_str_upp not in POSSIBLE_VARIANTS:
        print(f'"{first_player_varian}" is not a option. Try again!')
        continue

    win = False
    match input_str_upp:
        case 'ROCK':
            win = (second_player_variant == 'SCISSORS')
        case 'PAPER':
            win = (second_player_variant == 'ROCK')
        case 'SCISSORS':
            win = (second_player_variant == 'PAPER')

    if win:
        print(
            f'Congratulations! {input_str_upp} beat {second_player_variant}.')
        break
    else:
        print(f'Sorry! {second_player_variant} beat {input_str_upp}.')
