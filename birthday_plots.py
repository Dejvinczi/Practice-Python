"""
In the previous exercise we counted how many birthdays there are in each
month in our dictionary of birthdays.

In this exercise, use the bokeh Python library to plot a histogram of
which months the scientists have birthdays in! Because it would take a
long time for you to input the months of various scientists, you can use
my scientist birthday JSON file. Just parse out the months (if you don’t
know how, I suggest looking at the previous exercise or its solution) and
draw your histogram.

If you are using a purely web-based interface for coding, this exercise
won’t work for you, since it requires installing the bokeh Python package.
Now might be a good time to install Python on your own computer.
"""
import json
import math
import calendar
from datetime import datetime
from collections import Counter

from bokeh.plotting import figure, show, output_file

from birthday_json import main as birthday_json_main
from birthday_months import __count_months


output_file("uploads/plot.html")


def main():
    """Main program func."""
    stop = False
    while not stop:
        print()
        print("============ MENU ============")
        print("=> 1.Manage birthday json.    ")
        print("=> 2.Generate months plot. ")
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
                months, counts = list(zip(*months_counter.items()))

                categories = calendar.month_name[1:]
                p = figure(
                    x_range=categories,
                    title='Birthday Months')
                p.xaxis.major_label_orientation = math.pi / 4
                p.vbar(x=months, top=counts)

                show(p)
            case 5:
                print('BYE! Exiting...')
                stop = True
        print("==============================")


if __name__ == '__main__':
    main()
