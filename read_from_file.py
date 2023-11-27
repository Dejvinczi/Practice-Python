"""
Given a .txt file that has a list of a bunch of names, count how many of each
name there are in the file, and print out the results to the screen. I have a
.txt file for you:
https://www.practicepython.org/assets/nameslist.txt

Extra:

Instead of using the .txt file from above (or instead of, if you want
the challenge), take this .txt file, and count how many of each “category”
of each image there are. This text file is actually a list of files
corresponding to the SUN database scene recognition database, and lists
the file directory hierarchy for the images. Once you take a look at the
first line or two of the file, it will be clear which part represents the
scene category. To do this, you’re going to have to remember a bit about
string parsing in Python 3. I talked a little bit about it in this post.
"""
import os
import requests
from requests import HTTPError

url = 'https://www.practicepython.org/assets/nameslist.txt'
file_name = os.path.basename(url)
names_dict = {}

# Get names from the url file
try:
    res = requests.get(url)
except HTTPError as err:
    print(err.response.text)
    raise err

# Write it into my local file
with open(f'uploads/{file_name}', 'w') as w_file:
    file_text = res.text
    w_file.write(file_text)
    w_file.close()

# Read current created file
with open(f'uploads/{file_name}', 'r') as r_file:
    name = r_file.readline().rstrip('\n')
    while name:
        if name in names_dict:
            names_dict[name] += 1
        else:
            names_dict[name] = 1
        name = r_file.readline().rstrip('\n')

print('There is some information about name count in file:')
for name, count in names_dict.items():
    print(f'{name}: {count}')
