"""
Write a function that takes an ordered list of numbers (a list where the
elements are in order from smallest to largest) and another number. The
function decides whether or not the given number is inside the list and
returns (then prints) an appropriate boolean.
"""
import random


def binary_search(target, arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        middle_element = arr[mid]
        if middle_element == target:
            return middle_element

        if middle_element > target:
            high = mid - 1
        else:
            low = mid + 1

    return None


ordered_list = [el for el in range(0, 21)]
print(f'Your ordered list: {ordered_list}')
while True:
    input_number = int(input('Provide any number: '))
    idx = binary_search(input_number, ordered_list)
    if idx is None:
        print(f'Element {input_number} is not in the list.')
    else:
        print(f'Element {input_number} is at index {idx}')
