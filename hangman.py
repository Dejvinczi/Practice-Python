"""
In Part 1, we loaded a random word list and picked a word from it. In
Part 2, we wrote the logic for guessing the letter and displaying that
information to the user. In this exercise, we have to put it all together
and add logic for handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point.
Now add the following features:
-Only let the user guess 6 times, and tell the user how many guesses they
have left.
-Keep track of the letters the user guessed. If the user guesses a
letter they already guessed, don’t penalize them - let them guess again.

Optional additions:
-When the player wins or loses, let them start a new game.
-Rather than telling the user "You have 4 incorrect guesses left", display
some picture art for the Hangman. This is challenging - do the
other parts of the exercise first!
"""
import os
import random
import string
import requests

URL = 'https://norvig.com/ngrams/sowpods.txt'
FILENAME = os.path.basename(URL)
WORDS = 'NOT_SET'
SELECTED_WORD = 'NOT_SET'
HANGMAN = ('o', 'O', '<-', '->', '/', ' \\')
DEFAULT_HANGMAN = (' ', ' ', '  ', ' ', ' ', ' ')

guessed_letters = []
wrong_letter_counter = 0
wrong_letters = set()
current_hangman = []


def __get_words():
    """Download words from the file and return the tuple of words."""
    try:
        response = requests.get(URL)
    except requests.HTTPError as http_err:
        print(f'Some HTTP problems.. {str(htp_err)}')
    except Exception as err:
        print(f'Some Python problems.. {str(err)}')

    with open(f'uploads/{FILENAME}', 'w+') as words_file:
        words_file.write(response.text)
        words_file.seek(0)
        word = words_file.readline().strip('\n')
        words = []
        while word:
            words.append(word)
            word = words_file.readline().strip('\n')

    return tuple(words)


def __pick_word():
    """Return random word from the WORDS."""
    random_word = random.choice(WORDS)
    print(random_word)
    return random_word


def __initial():
    """Initial new game."""
    global WORDS
    global SELECTED_WORD
    global HANGMAN
    global guessed_letters
    global wrong_letter_counter
    global wrong_letters
    global current_hangman
    if WORDS == 'NOT_SET':
        WORDS = __get_words()

    SELECTED_WORD = __pick_word()
    current_hangman = list(DEFAULT_HANGMAN)
    wrong_letter_counter = 0
    wrong_letters = set()
    guessed_letters = [
        '_' for _ in range(0, len(SELECTED_WORD))
    ]


def __guess(letter: str):
    """Return that player guess letter or not.
        If not - check that again for the letter."""
    global WORDS
    global SELECTED_WORD
    global HANGMAN
    global guessed_letters
    global wrong_letter_counter
    global wrong_letters
    global current_hangman
    if letter in SELECTED_WORD:
        for idx, word_letter in enumerate(SELECTED_WORD):
            if letter == word_letter:
                guessed_letters[idx] = word_letter
        return True, None

    if letter in wrong_letters:
        return True, True

    wrong_letters.add(letter)
    current_hangman[wrong_letter_counter] = HANGMAN[wrong_letter_counter]
    wrong_letter_counter += 1

    return False, False


def __print_game_board():
    """Print on the screen current game board."""
    print('\n=============')
    print('  ||        |')
    print(f'  ||        {current_hangman[0]}')
    print(
        f'  ||      {current_hangman[2]}{current_hangman[1]}{current_hangman[3]}')
    print(f'  ||       {current_hangman[4]}{current_hangman[5]}')
    print('  ||')
    print('  ||')
    print('======')
    print()
    print(f'WORD: {" ".join(guessed_letters)}\n')


def __game():
    """Game logic function."""
    global guessed_letters
    global SELECTED_WORD
    global current_hangman
    global current_hangman
    global HANGMAN
    __print_game_board()
    letter = input('Provide letter (A-Z): ')

    if letter not in string.ascii_letters:
        print(f'Provided "{letter}" is not a choice.')
        print(f'Choices: {string.ascii_letters}')
        return 1

    guessed, miss_again = __guess(letter.upper())
    if guessed:
        print('CORRECT!')
    elif not miss_again:
        print('MISSED! Again... be careful!')
    else:
        print('MISSED!')

    play = wrong_letter_counter != 6 and guessed_letters.count('_')
    if play:
        return 1

    __print_game_board()
    print(f'\nTHE GAME IS END! "{SELECTED_WORD}" is the whole word.')
    msg = "YOU WON!" if guessed else "YOU LOSE!"
    print(f'{msg}')

    return 0


def main():
    """Main program function."""
    print('========================================================')
    print('Welcome in the Hangman game!')
    name = input("Enter your name: ")
    print('========================================================')
    program = True

    while program:
        print('\n========================================================')
        print(f"Hello {name}! Let's start the game!\n")
        __initial()

        play = True
        while play:
            play = __game()

        again = input('\nRestart? Type "yes" if you want play again: ')
        if again.lower() in ['y', 'yes']:
            program = True
        else:
            print('Goodbye!')
            program = False


if __name__ == '__main__':
    main()
