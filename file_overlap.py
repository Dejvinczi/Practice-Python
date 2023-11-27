"""
Given two .txt files that have lists of numbers in them, find the numbers that
are overlapping. One .txt file has a list of all prime numbers under 1000, and
the other .txt file has a list of happy numbers up to 1000.
"""
import os
import requests
from requests import HTTPError

url_1 = 'https://www.practicepython.org/assets/primenumbers.txt'
url_2 = 'https://www.practicepython.org/assets/happynumbers.txt'
file_1_name = os.path.basename(url_1)
file_2_name = os.path.basename(url_2)

try:
    res = requests.get(url_1, stream=True)
    with open(f'uploads/{file_1_name}', 'wb') as file_1:
        for chunk in res.iter_content(chunk_size=128):
            file_1.write(chunk)
        file_1.close()
except HTTPError as err:
    print(err.response.text)
    raise err
except Exception as e:
    print(e)
    raise e

try:
    res = requests.get(url_2, stream=True)
    with open(f'uploads/{file_2_name}', 'wb') as file_2:
        for chunk in res.iter_content(chunk_size=128):
            file_2.write(chunk)
        file_2.close()
except HTTPError as err:
    print(err.response.text)
    raise err
except Exception as e:
    print(e)
    raise e

list_1 = []
with open(f'uploads/{file_1_name}') as file_1:
    line = file_1.readline().rstrip('\n')
    while line:
        list_1.append(int(line))
        line = file_1.readline().rstrip('\n')
    file_1.close()

list_2 = []
with open(f'uploads/{file_2_name}') as file_2:
    line = file_2.readline().rstrip('\n')
    while line:
        list_2.append(int(line))
        line = file_2.readline().rstrip('\n')
    file_2.close()

set_1 = set(list_1)
set_2 = set(list_2)
print(f'Common elements files {file_1_name} and {file_2_name} are:')
print(list(set_1.intersection(set_2)))
