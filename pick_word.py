"""
In this exercise, the task is to write a function that picks a random word from
a list of words from the SOWPODS dictionary(https://norvig.com/ngrams/sowpods.txt).
Download this file and save it in the same directory as your Python code.
This file is Peter Norvig’s compilation of the dictionary of words used in
professional Scrabble tournaments. Each line in the file contains a single word.
"""
import os
import random
import requests

url = 'https://norvig.com/ngrams/sowpods.txt'
filename = os.path.basename(url)
try:
    res = requests.get(url)
except requests.HTTPError as err:
    print(err)
    raise err

file = f'uploads/{filename}'
word_list = []
with open(file, 'w') as w_file:
    file_text = res.text
    w_file.write(file_text)
    w_file.close()

with open(file, 'r') as r_file:
    line = r_file.readline().strip('\n')
    while line:
        word_list.append(line)
        line = r_file.readline().strip('\n')
    r_file.close()

random_word = random.choice(word_list)
print(f'The random word from the word list is: {random_word}')
