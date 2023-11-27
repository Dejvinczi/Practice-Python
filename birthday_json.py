"""
In this exercise, modify your program from Part 1 to load the birthday
dictionary from a JSON file on disk, rather than having the dictionary
defined in the program.

Bonus: Ask the user for another scientist’s name and birthday to add to
the dictionary, and update the JSON file you have on disk with the scientist’s
name. If you run the program multiple times and keep adding new names, your
JSON file should keep getting bigger and bigger.
"""
import os
import json
from datetime import datetime


def __get_json_data():
    """Load/create "uploads/birthdays.json" and return data."""
    if not os.path.exists('uploads/birthdays.json'):
        default_data = {
            'User One': '10/10/1010',
            'User Two': '11/11/1111',
            'User Three': '12/12/1212',
        }
        with open('uploads/birthdays.json', 'w', encoding='utf-8') as file:
            json.dump(default_data, file)
            file.seek(0)
            file.close()

    with open('uploads/birthdays.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        file.close()

    return data


def __update_json_data(data):
    """Update content in "uploads/birthdays.json"""
    with open('uploads/birthdays.json', 'w+', encoding='UTF-8') as file:
        file.write(json.dumps(data))
        file.seek(0)
        file.close()


def __validate_name(name):
    """Validate a prompted name."""
    name_splitted = name.split(' ')
    if len(name_splitted) != 2:
        raise ValueError({'name': 'Invalid format. ("Firstname Surname")'})

    firstname = name_splitted[0].capitalize()
    surname = name_splitted[1].capitalize()

    return f'{firstname} {surname}'


def __validate_birthday(birthday):
    """Validate a prompted birthday."""
    try:
        datetime.strptime(birthday, "%d/%m/%Y").date()
    except ValueError as v_err:
        raise ValueError({'birthday': 'Invalid format. (dd/mm/yyyy)'})

    return birthday


def __get_birthdays(name: str = None):
    data = __get_json_data()
    if name:
        try:
            name = __validate_name(name)
        except ValueError as v_err:
            print(v_err)
            return

        birthday = data.get(name)
        if birthday:
            return {name: birthday}
        else:
            print(f'{name} not found.')
            return None

    return data


def __set_birthday(name: str, birthday: str):
    errs = {}
    if not name:
        errs.update({'name': 'Required field.'})
    if not birthday:
        errs.update({'birthday': 'Required field.'})
    if errs:
        for k, v in errs.items():
            print(f'{k.capitalize()}: {v}')
        return

    try:
        name = __validate_name(name)
        birthday = __validate_birthday(birthday)
    except ValueError as v_err:
        print(v_err)
        return

    updated_data = __get_json_data()
    updated_data.update({name: birthday})
    __update_json_data(updated_data)

    print('UPDATED!')


def __remove_birthday(name: str):
    errs = {}
    if not name:
        errs.update({'name': 'Required field.'})
    if errs:
        for k, v in errs.items():
            print(f'{k.capitalize()}: {v}')
        return

    try:
        name = __validate_name(name)
    except ValueError as v_err:
        print(v_err)
        return

    updated_data = __get_json_data()
    if name in updated_data:
        del updated_data[name]
        __update_json_data(updated_data)
        print('DELETED!')
    else:
        print(f'{name} not found.')


def print_data(data):
    """"Print data."""
    if len(data) > 1:
        counter = 0
        for k, v in data.items():
            print(f'{counter}. {k} - {v}')
            counter += 1
    else:
        print(data)


def main():
    """Main program func."""
    birthday_data = __get_birthdays()

    print('Welcome to the birthday dictionary. We know the birthdays of: ')
    print_data(birthday_data)

    stop = False
    while not stop:
        print()
        print("============ MENU ============")
        print("=> 1.Get birthdays.           ")
        print("=> 2.Get birthday.            ")
        print("=> 3.Set birthday.            ")
        print("=> 4.Remove birthday.         ")
        print("=> 5.Exit.                    ")
        print("========== CHOOSE ============")
        try:
            option = int(input('Provide option (1-4): '))
            if option not in list(range(1, 6)):
                raise ValueError
        except ValueError:
            print('Provided value is not a valid option. Try again.')
            continue

        match option:
            case 1:
                data = __get_birthdays()
                print_data(data)
            case 2:
                name = input('Fullname: ')
                name_data = __get_birthdays(name)
                if not name_data:
                    continue
                print_data(name_data)
            case 3:
                name = input('Fullname: ')
                birthday = input('Birthday ("dd/mm/yyyy"): ')
                __set_birthday(name, birthday)
            case 4:
                name = input('Fullname: ')
                __remove_birthday(name)
            case 5:
                print('BYE! Exiting...')
                stop = True
        print("==============================")


if __name__ == '__main__':
    main()
