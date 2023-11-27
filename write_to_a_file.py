"""
Take the code from the How To Decode A Website exercise (if you didn’t do it
or just want to play with some different code, use the code from the solution),
and instead of printing the results to a screen, write the results to a
txt file. In your code, just make up a name for the file you are saving to.
"""


txt = 'Some text that will be write into file.'
file_name = input('Provide name of file: ')

if not file_name:
    raise ValueError('File name cannot be empty string.')

with open(f'uploads/{file_name}.txt', 'w') as o_file:
    o_file.write(txt)
    o_file.close()
