"""
In this exercise, load that JSON file from disk, extract the months of all
the birthdays, and count how many scientists have a birthday in each month.

Your program should output something like:

{
	"May": 3,
	"November": 2,
	"December": 1
}
"""
import json
from datetime import datetime
from collections import Counter

from birthday_json import (
    __get_json_data,
    main as birthday_json_main,
)


def __count_months():
    """Count and return information about months in birthday json."""
    data = __get_json_data()
    months = []

    for birthday_str in data.values():
        birthday = datetime.strptime(birthday_str, "%d/%m/%Y")
        month = birthday.strftime("%B")
        months.append(month)

    months_counter = Counter(months)

    return months_counter


def main():
    """Main program func."""
    stop = False
    while not stop:
        print()
        print("============ MENU ============")
        print("=> 1.Manage birthday json.    ")
        print("=> 2.Count months. ")
        print("=> 3.Exit.                    ")
        print("========== CHOOSE ============")
        try:
            option = int(input('Provide option (1-3): '))
            if option not in list(range(1, 4)):
                raise ValueError
        except ValueError:
            print('Provided value is not a valid option. Try again.')
            continue

        match option:
            case 1:
                birthday_json_main()
            case 2:
                months_counter = __count_months()
                for month, count in months_counter.items():
                    print(f'{month} - {count}')
            case 5:
                print('BYE! Exiting...')
                stop = True
        print("==============================")


if __name__ == '__main__':
    main()
