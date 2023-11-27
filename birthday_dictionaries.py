"""
For this exercise, we will keep track of when our friend’s birthdays are, and
be able to find that information based on their name. Create a dictionary
(in your file) of names and birthdays. When you run your program it should
ask the user to enter a name, and return the birthday of that person back to
them. The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.

Happy coding!
"""
BIRTHDAY_DICT = {
    'Dawid': '01/01/1111',
    'Tomek': '02/02/2222',
    'Daniel': '03/03/3333',
    'Sandra': '04/04/4444',
    'Monika': '05/05/5555',
}


def __get_birthdate(name):
    """Return birthdate of person."""
    return BIRTHDAY_DICT.get(name)


def main():
    """Main program func."""
    print('Welcome to the birthday dictionary. We know the birthdays of: ')
    for el in BIRTHDAY_DICT:
        print(el)

    stop = False
    while not stop:
        input_name = input("\nWho's birthday do you want to look up: ")
        name = input_name.capitalize()
        birthday = __get_birthdate(name)
        if birthday:
            print(f"{name}'s birthday is {birthday}")
        else:
            print('I have no information about {input_name} person.')

        again = input('\nAgain? Provide yes/y: ')
        stop = again.lower() not in ['yes', 'y']


if __name__ == '__main__':
    main()
